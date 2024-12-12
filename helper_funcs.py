import pandas as pd
import torch

def filter_response_dataframe(df):
    """
    Filters a DataFrame to keep rows where the 'response' column matches one of the values
    in the 'stereotype', 'anti_stereotype', or 'unrelated' columns.

    Args:
        df (pd.DataFrame): The input DataFrame with the required columns.

    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    # Ensure the necessary columns exist
    required_columns = {"response", "stereotype", "anti_stereotype", "unrelated", "context_norwegian"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"The DataFrame must contain the columns: {required_columns}")
    
    # Create a list of valid values from the 'stereotype', 'anti_stereotype', and 'unrelated' columns
    valid_responses = df["stereotype"].tolist() + df["anti_stereotype"].tolist() + df["unrelated"].tolist()

    # Filter rows where 'response' matches any of the valid values
    filtered_df = df[df["response"].isin(valid_responses)]

    # Identify rows that were removed
    removed_rows = df[~df["response"].isin(valid_responses)]

    # Print the number of rows removed and details for each
    print(f"\nRows removed: {len(removed_rows)}")
    if not removed_rows.empty:
        print("Details of removed rows:")
        for _, row in removed_rows.iterrows():
            print(f"Context (Norwegian): {row['context_norwegian']}")
            print(f"Response: {row['response']}")
            print(f"  Stereotype: {row['stereotype']}")
            print(f"  Anti-stereotype: {row['anti_stereotype']}")
            print(f"  Unrelated: {row['unrelated']}")
            print("-" * 40)

    return filtered_df

def compute_average_log_probability(context, option, model, tokenizer, device):
    inputs = tokenizer(context, return_tensors="pt", padding=True, truncation=True).to(device)
    mask_index = torch.where(inputs.input_ids == tokenizer.mask_token_id)[1]
    total_log_prob = 0

    for subword in tokenizer.tokenize(option):
        inputs.input_ids[0, mask_index] = tokenizer.convert_tokens_to_ids(subword)
        outputs = model(**inputs)
        logits = outputs.logits
        log_probs = torch.log_softmax(logits[0, mask_index, :], dim=-1)
        token_log_prob = log_probs[0, tokenizer.convert_tokens_to_ids(subword)].item()
        total_log_prob += token_log_prob
        mask_index += 1  # Move to the next token

    return total_log_prob / len(tokenizer.tokenize(option))  # Average log probability

