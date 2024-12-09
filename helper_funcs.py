import pandas as pd

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
    required_columns = {"response", "stereotype", "anti_stereotype", "unrelated"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"The DataFrame must contain the columns: {required_columns}")
    
    # Create a list of valid values from the 'stereotype', 'anti_stereotype', and 'unrelated' columns
    valid_responses = df["stereotype"].tolist() + df["anti_stereotype"].tolist() + df["unrelated"].tolist()

    # Filter rows where 'response' matches any of the valid values
    filtered_df = df[df["response"].isin(valid_responses)]

    # Identify rows that were removed
    removed_rows = df[~df["response"].isin(valid_responses)]

    # Print the number of rows removed and their 'response' values
    print(f"Rows removed: {len(removed_rows)}")
    print("Removed responses:")
    print(removed_rows["response"].tolist())

    return filtered_df
