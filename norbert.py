import pandas as pd
import random
import os
from tqdm import tqdm
from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch

# Load the model and tokenizer
model_name = 'ltg/norbert3-large'  # Use NorBERT3-large model for masked LM
device = "cuda:0" if torch.cuda.is_available() else "cpu"  # Use GPU if available

model = AutoModelForMaskedLM.from_pretrained(
    model_name,
    trust_remote_code=True
).to(device)  # Move model to the GPU
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Ensure pad_token is set
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Function to compute the average log probability of an option

def compute_average_log_probability(context, option, model, tokenizer, device):
    inputs = tokenizer(context, return_tensors="pt", padding=True, truncation=True).to(device)
    mask_index = torch.where(inputs.input_ids == tokenizer.mask_token_id)[1]

    total_log_prob = 0
    for subword in tokenizer.tokenize(option):
        inputs.input_ids[0, mask_index] = tokenizer.convert_tokens_to_ids(subword)
        outputs = model(**inputs)
        logits = outputs.logits
        log_probs = torch.log_softmax(logits[0, mask_index, :], dim=-1)
        token_log_prob = log_probs[tokenizer.convert_tokens_to_ids(subword)].item()
        total_log_prob += token_log_prob
        mask_index += 1  # Move to the next token

    return total_log_prob / len(tokenizer.tokenize(option))  # Average log probability

# Prepare the dataset
dataset_path = "data/test_masked.csv"  # Path to your dataset
dataset = pd.read_csv(dataset_path)

dataset['response'] = ''  # Add a column for storing responses

# Process the dataset
for idx, data in tqdm(dataset.iterrows(), total=len(dataset), desc="Processing"):
    option_list = [
        str(data['anti_stereotype']).lower(),
        str(data['stereotype']).lower(),
        str(data['unrelated']).lower()
    ]
    random.shuffle(option_list)

    # Tokenize context
    context = data['context_norwegian']
    best_option = None
    max_score = -float('inf')

    try:
        for option in option_list:
            avg_log_prob = compute_average_log_probability(context, option, model, tokenizer, device)

            if avg_log_prob > max_score:
                max_score = avg_log_prob
                best_option = option

        # Update the response with the best option
        dataset.loc[idx, 'response'] = best_option
        print(f"Row {idx}: Best option: {best_option}")

    except Exception as e:
        print(f"An error occurred for row {idx}: {e}")
        dataset.loc[idx, 'response'] = "error"

# Write the results to a CSV file
output_dir = "outputs"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

output_path = os.path.join(output_dir, f'{model_name.replace("/", "-")}_result.csv')
dataset.to_csv(output_path, index=False, encoding='utf-8')

print(f"Results saved to {output_path}")
