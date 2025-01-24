import pandas as pd
import torch

import pandas as pd

def filter_response_dataframe(df):
    """
    Filters and updates a DataFrame by ensuring that the 'response' column contains valid options.
    If the 'response' contains any value from the 'stereotype', 'anti_stereotype', or 'unrelated' columns,
    it is updated to the exact text in the matching column. Rows without valid matches are removed.

    Args:
        df (pd.DataFrame): The input DataFrame with the required columns.

    Returns:
        pd.DataFrame: The updated and filtered DataFrame.
    """
    # Ensure the necessary columns exist
    required_columns = {"response", "stereotype", "anti_stereotype", "unrelated", "context_norwegian"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"The DataFrame must contain the columns: {required_columns}")

    updated_responses = []
    removed_rows = []

    # Iterate over rows to validate and update responses
    for _, row in df.iterrows():
        response = row["response"]
        # Check if response matches or contains any of the valid options
        if row["stereotype"] in response:
            updated_responses.append(row["stereotype"])
        elif row["anti_stereotype"] in response:
            updated_responses.append(row["anti_stereotype"])
        elif row["unrelated"] in response:
            updated_responses.append(row["unrelated"])
        else:
            # Collect rows that don't match any valid option
            removed_rows.append(row)

    # Filter out invalid rows
    filtered_df = df[df.index.isin(row.name for row in removed_rows) == False]

    # Update the response column for the valid rows
    filtered_df.loc[:, "response"] = updated_responses

    # Print details of removed rows
    print(f"\nRows removed: {len(removed_rows)}")
    if removed_rows:
        print("Details of removed rows:")
        for row in removed_rows:
            print(f"Context (Norwegian): {row['context_norwegian']}")
            print(f"Response: {row['response']}")
            print(f"  Stereotype: {row['stereotype']}")
            print(f"  Anti-stereotype: {row['anti_stereotype']}")
            print(f"  Unrelated: {row['unrelated']}")
            print("-" * 40)
    print(f"\nRows removed: {len(removed_rows)}")

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

