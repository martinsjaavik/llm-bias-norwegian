import pandas as pd
import re
import os
import json
from datetime import datetime

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
        
        text = str(text).lower().strip()
        option = str(option).lower().strip()
        
        # First check: direct equality comparison for single-word responses
        if text == option:
            return True
        
        # Remove common quote characters and clean the text
        text = text.replace('«', '"').replace('»', '"').replace('"', '"').replace('"', '"')
        
        # Create pattern that handles quotes and word boundaries
        pattern = r'(?:^|\W)(?:"|«)?(' + re.escape(option) + r')(?:»|")?\W'
        
        # Find all matches
        matches = re.findall(pattern, text)
        
        # Additional check for when the option appears at the very end of text
        if not matches and text.endswith(option):
            # Make sure it's a whole word match
            if len(text) == len(option) or text[-(len(option)+1)] in " \t\n\"'.,;:!?":
                return True
                
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
    if len(valid_indices) > 0:
        filtered_df.loc[:, "response"] = updated_responses
    
    # Print debugging information
    print(f"\nRows removed: {len(removed_rows)}")
    
    # Save error analysis to disk
    if removed_rows:
        save_error_analysis(removed_rows)
        
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

def save_error_analysis(removed_rows):
    """
    Saves invalid responses to the error_analysis folder for further analysis.
    
    Args:
        removed_rows (list): List of DataFrame rows that were removed
    """
    # Create error_analysis directory if it doesn't exist
    error_dir = "error_analysis"
    os.makedirs(error_dir, exist_ok=True)
    
    # Create a timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Convert each row to a dictionary and save as JSON
    error_data = []
    for i, row in enumerate(removed_rows):
        row_dict = {
            "index": i,
            "context_norwegian": row.get("context_norwegian", ""),
            "model_response": row.get("response", ""),
            "valid_options": {
                "stereotype": row.get("stereotype", ""),
                "anti_stereotype": row.get("anti_stereotype", ""),
                "unrelated": row.get("unrelated", "")
            },
            "analysis": {
                "possible_issues": analyze_mismatch(
                    row.get("response", ""), 
                    [row.get("stereotype", ""), row.get("anti_stereotype", ""), row.get("unrelated", "")]
                )
            }
        }
        error_data.append(row_dict)
    
    # Save as JSON
    json_filename = os.path.join(error_dir, f"invalid_responses_{timestamp}.json")
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(error_data, f, ensure_ascii=False, indent=2)
    
    # Save as CSV for easier spreadsheet analysis
    csv_data = []
    for i, row in enumerate(removed_rows):
        csv_row = {
            "index": i,
            "context_norwegian": row.get("context_norwegian", ""),
            "model_response": row.get("response", ""),
            "stereotype": row.get("stereotype", ""),
            "anti_stereotype": row.get("anti_stereotype", ""),
            "unrelated": row.get("unrelated", ""),
            "possible_issues": ", ".join(analyze_mismatch(
                row.get("response", ""), 
                [row.get("stereotype", ""), row.get("anti_stereotype", ""), row.get("unrelated", "")]
            ))
        }
        csv_data.append(csv_row)
    
    csv_filename = os.path.join(error_dir, f"invalid_responses_{timestamp}.csv")
    pd.DataFrame(csv_data).to_csv(csv_filename, index=False, encoding="utf-8")
    
    print(f"Error analysis saved to:")
    print(f"  - {json_filename}")
    print(f"  - {csv_filename}")

def analyze_mismatch(response, valid_options):
    """
    Analyzes why a response might not have matched any of the valid options.
    
    Args:
        response (str): The model's response
        valid_options (list): List of valid options that should have been matched
        
    Returns:
        list: List of possible issues with the response
    """
    issues = []
    
    if pd.isna(response) or response.strip() == "":
        issues.append("empty_response")
        return issues
    
    response = str(response).lower().strip()
    
    # Add a check for exact matches that somehow weren't caught
    for option in valid_options:
        if pd.notna(option) and str(option).lower().strip() == response:
            issues.append("exact_match_not_detected")
    
    # Check for partial matches (which might indicate spacing or punctuation issues)
    for option in valid_options:
        if pd.isna(option):
            continue
            
        option = str(option).lower()
        
        # If option text exists in response but wasn't matched by regex
        if option in response:
            issues.append("partial_match_without_boundaries")
        
        # Check for close matches (levenshtein distance would be better, but using simple check)
        # This checks if any option word appears in the response
        option_words = set(option.split())
        response_words = set(response.split())
        common_words = option_words.intersection(response_words)
        
        if common_words and len(common_words) >= min(2, len(option_words)):
            issues.append("word_level_partial_match")
    
    # Check for possible reformatting/paraphrasing
    if any([":" in response, "option" in response.lower(), "alternative" in response.lower()]):
        issues.append("possible_reformatting")
    
    # Check for inclusion of multiple options
    option_count = 0
    for option in valid_options:
        if pd.notna(option) and str(option).lower() in response:
            option_count += 1
    
    if option_count > 1:
        issues.append("multiple_options_mentioned")
    
    # If no specific issues found
    if not issues:
        issues.append("unknown_mismatch")
    
    return issues

# Example usage:
# df = pd.read_csv("responses.csv")
# filtered_df = filter_response_dataframe(df)
# filtered_df.to_csv("filtered_responses.csv", index=False)