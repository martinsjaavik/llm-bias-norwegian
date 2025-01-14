import pandas as pd
import random
import os
from tqdm import tqdm
from generate_reports import write_report
from transformers import AutoModelForMaskedLM, AutoTokenizer
from helper_funcs import filter_response_dataframe
import torch

# Load the model and tokenizer
model_name = 'NbAiLab/nb-bert-large'  # Use NorBERT3-large model for masked LM
device = "cuda:0"  # Use GPU if available

model = AutoModelForMaskedLM.from_pretrained(
    model_name,
    trust_remote_code=True
).to(device)  # Move model to the GPU
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Ensure pad_token is set
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Prepare the dataset
dataset_path = "data/dataset_masked.csv"
dataset = pd.read_csv(dataset_path)

def prepare_masked_context(context, option, tokenizer):
    """
    Prepare context by inserting the correct number of mask tokens for the option.
    """
    # Tokenize the option to know how many masks we need
    option_tokens = tokenizer(option, add_special_tokens=False)['input_ids']
    num_masks = len(option_tokens)
    
    # Replace [MASK] with the correct number of mask tokens
    masked_context = context.replace("[MASK]", " ".join([tokenizer.mask_token] * num_masks))
    return masked_context, num_masks

def score_masked_option(model, tokenizer, context, option, device):
    """
    Score how well a multi-token option fits in a masked context.
    """
    # Prepare context with correct number of masks
    masked_context, num_masks = prepare_masked_context(context, option, tokenizer)
    
    # Tokenize the full context
    inputs = tokenizer(masked_context, return_tensors="pt", padding=True, truncation=True)
    input_ids = inputs['input_ids'].to(device)
    
    # Find positions of all mask tokens
    mask_token_indices = torch.where(input_ids == tokenizer.mask_token_id)[1]
    
    if len(mask_token_indices) != num_masks:
        raise ValueError(f"Number of mask tokens ({len(mask_token_indices)}) doesn't match option tokens ({num_masks})")
    
    # Tokenize the option
    option_tokens = tokenizer(option, add_special_tokens=False)['input_ids']
    
    # Calculate score for each mask position
    scores = []
    with torch.no_grad():
        outputs = model(input_ids=input_ids)
        logits = outputs.logits
        
        # Score each position
        for idx, (mask_idx, target_token) in enumerate(zip(mask_token_indices, option_tokens)):
            mask_logits = logits[0, mask_idx, :]
            token_score = mask_logits[target_token].item()
            scores.append(token_score)
    
    # Return average score across all positions
    return sum(scores) / len(scores)

# In the main loop:
for col, data in tqdm(dataset.iterrows(), total=len(dataset), desc="Processing"):
    context = data['context_norwegian']
    option_list = [str(data['anti_stereotype']).lower(),
                  str(data['stereotype']).lower(),
                  str(data['unrelated']).lower()]
    
    try:
        best_option = None
        max_score = -float('inf')
        
        for option in option_list:
            score = score_masked_option(model, tokenizer, context, option, device)
            if score > max_score:
                max_score = score
                best_option = option
        
        dataset.loc[col, 'response'] = best_option
        # Optionally store the score
        dataset.loc[col, 'score'] = max_score
        
    except Exception as e:
        print(f"An error occurred: {e}")
        dataset.loc[col, 'response'] = "error"
        dataset.loc[col, 'score'] = None

# Write the results to a CSV file and generate reports
try:
    if 'outputs' not in os.listdir():
        os.mkdir('outputs')

    df_result = pd.DataFrame(dataset)
    df_result = filter_response_dataframe(df_result)
    output_path = f'outputs/{model_name.replace("/", "-")}_result.csv'
    df_result.to_csv(output_path, index=False, encoding='utf-8')

    # Generate the report using the model name
    report = write_report(model_name)

    output_path_md = f'reports/{model_name.replace("/", "-")}_result.md'
    output_path_txt = f'reports/{model_name.replace("/", "-")}_result.txt'

    with open(output_path_md, "w") as file:
        file.write(report)

    with open(output_path_txt, "w") as file:
        file.write(report)

except Exception as e:
    print(f"An error occurred: {e}")
    print(f"The result is still stored at {output_path}")
    exit(1)
