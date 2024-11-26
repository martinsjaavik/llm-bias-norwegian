import pandas as pd
import random
import os
from tqdm import tqdm
from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM

# Load NorBERT3-large model and tokenizer
model_name = "ltg/norbert3-large"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForMaskedLM.from_pretrained(model_name, trust_remote_code=True)

# Ensure the `[MASK]` token is set
if tokenizer.mask_token is None:
    tokenizer.mask_token = "[MASK]"

# Initialize the pipeline
pipe = pipeline("fill-mask", model=model, tokenizer=tokenizer, trust_remote_code=True, device=0)  # Use GPU if available

# Define the dataset path
dataset_path = "data/test_masked.csv"
dataset = pd.read_csv(dataset_path)

# Create an empty list to store the responses
responses = []

# Process the dataset
for idx, data in tqdm(dataset.iterrows(), total=len(dataset), desc="Processing"):
    # Shuffle options
    option_list = [str(data['anti_stereotype']).lower(), str(data['stereotype']).lower(), str(data['unrelated']).lower()]
    random.shuffle(option_list)

    # Construct the query
    context = data['context_norwegian']
    query = f"{context} {tokenizer.mask_token}"  # Add the mask token to the query

    try:
        # Get predictions
        predictions = pipe(query)

        # Filter the predictions to include only options from `option_list`
        valid_predictions = [pred for pred in predictions if pred['token_str'] in option_list]

        if valid_predictions:
            # Select the highest-scoring prediction from `valid_predictions`
            response = max(valid_predictions, key=lambda x: x['score'])['token_str']
        else:
            # If no valid predictions, default to error
            response = "error"

        # Append the response to the list
        responses.append(response.lower())
    except Exception as e:
        print("An error occurred:", e)
        responses.append("error")

# Add the responses to a new dataframe column (keeping the original dataset unchanged)
dataset['response'] = responses

# Save the results
try:
    # Create output directory if it doesn't exist
    if 'outputs' not in os.listdir():
        os.mkdir('outputs')

    output_path = f'outputs/{model_name.replace("/", "-")}_result.csv'
    dataset.to_csv(output_path, index=False, encoding='utf-8')

    print(f"Results saved to {output_path}")
except Exception as e:
    print("An error occurred while saving results:", e)
