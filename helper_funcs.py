import pandas as pd
import re

def filter_response_dataframe(df):
    """
    Filters and updates a DataFrame by extracting valid options from model responses.
    Uses word boundary checking to ensure exact matches only.
    For example: "umotivert" will not match with "motivert".
    
    Args:
        df (pd.DataFrame): The input DataFrame with columns:
            - response: the model's full text response
            - stereotype: first option
            - anti_stereotype: second option
            - unrelated: third option
            - context_norwegian: the context (for logging)
    Returns:
        pd.DataFrame: The updated DataFrame with cleaned responses
    """
    # Ensure the necessary columns exist
    required_columns = {"response", "stereotype", "anti_stereotype", "unrelated", "context_norwegian"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"The DataFrame must contain the columns: {required_columns}")
    
    valid_indices = []
    updated_responses = []
    removed_rows = []
    
    def find_exact_match(text, option):
        """
        Find exact match of option in text, handling quotes and word boundaries.
        Returns True if exact match is found.
        """
        if pd.isna(text) or pd.isna(option):
            return False
            
        text = str(text).lower()
        option = str(option).lower()
        
        # Remove common quote characters and clean the text
        text = text.replace('«', '"').replace('»', '"').replace('"', '"').replace('"', '"')
        
        # Create pattern that handles quotes and word boundaries
        pattern = r'(?:^|\W)(?:"|«)?(' + re.escape(option) + r')(?:»|")?\W'
        
        # Find all matches
        matches = re.findall(pattern, text)
        return len(matches) > 0
    
    for idx, row in df.iterrows():
        response = str(row["response"]) if pd.notna(row["response"]) else ""
        
        # Get all possible options for this row
        options = [
            (row["stereotype"], "stereotype"),
            (row["anti_stereotype"], "anti_stereotype"),
            (row["unrelated"], "unrelated")
        ]
        
        # Try to find exact match of any option within the response
        found_match = False
        for option_original, option_type in options:
            if find_exact_match(response, option_original):
                valid_indices.append(idx)
                updated_responses.append(option_original)
                found_match = True
                break
        
        if not found_match:
            removed_rows.append(row)
    
    # Create new filtered DataFrame
    filtered_df = df.loc[valid_indices].copy()
    filtered_df.loc[:, "response"] = updated_responses
    
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
    
    return filtered_df