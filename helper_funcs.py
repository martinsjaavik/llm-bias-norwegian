import pandas as pd
import re

def filter_response_dataframe(df):
    """
    Filters and updates a DataFrame by extracting valid options from model responses.
    Handles various response formats including numbers, exact words, and None values.
    
    Args:
        df (pd.DataFrame): The input DataFrame with the required columns
    Returns:
        pd.DataFrame: The updated DataFrame with cleaned responses
    """
    # Ensure the necessary columns exist
    required_columns = {"response", "stereotype", "anti_stereotype", "unrelated", "context_norwegian"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"The DataFrame must contain the columns: {required_columns}")
    
    def normalize_text(text):
        """Normalize text for comparison"""
        if pd.isna(text):
            return ""
        return str(text).lower().strip()
    
    def find_match(response, option):
        """
        Find if option matches response, handling various cases:
        - Exact number matches
        - Word boundary matches
        - Quoted text matches
        """
        if pd.isna(response) or pd.isna(option):
            return False
            
        response = normalize_text(response)
        option = normalize_text(option)
        
        # If option is a number, check for exact number match
        if option.isdigit():
            return option in re.findall(r'\b\d+\b', response)
        
        # Clean quotes and check for exact word/phrase match
        response = response.replace('«', '"').replace('»', '"').replace('"', '"').replace('"', '"')
        option_pattern = r'(?:^|\W)(?:"|«)?(' + re.escape(option) + r')(?:»|")?(?:\W|$)'
        return bool(re.search(option_pattern, response))
    
    filtered_rows = []
    removed_rows = []
    
    for idx, row in df.iterrows():
        response = row["response"]
        
        # Get all possible options for this row
        options = [
            (row["stereotype"], "stereotype"),
            (row["anti_stereotype"], "anti_stereotype"),
            (row["unrelated"], "unrelated")
        ]
        
        # Try to find match of any option within the response
        found_match = False
        for option_original, option_type in options:
            if find_match(response, option_original):
                filtered_rows.append({
                    'index': idx,
                    'response': option_original,
                    'matched_type': option_type
                })
                found_match = True
                break
        
        if not found_match:
            removed_rows.append(row)
    
    # Create new filtered DataFrame
    if filtered_rows:
        indices = [row['index'] for row in filtered_rows]
        filtered_df = df.loc[indices].copy()
        filtered_df.loc[:, "response"] = [row['response'] for row in filtered_rows]
    else:
        filtered_df = pd.DataFrame(columns=df.columns)
    
    # Print debugging information
    print(f"\nRows removed: {len(removed_rows)}")
    if removed_rows:
        print("Details of removed rows:")
        for row in removed_rows:
            print(f"Context (Norwegian): {row['context_norwegian']}")
            print(f"Model Response: {row['response']}")
            print(f"Valid options were:")
            print(f"- Stereotype: {row['stereotype']}")
            print(f"- Anti-stereotype: {row['anti_stereotype']}")
            print(f"- Unrelated: {row['unrelated']}")
            print("-" * 40)
    print(f"\nRows removed: {len(removed_rows)}")
    
    return filtered_df