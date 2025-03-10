import json
import os

def remove_specific_issues(json_file_path, output_file_path=None):
    """
    Removes objects that have 'empty_response' or 'possible_reformatting' as the FIRST issue in their 'possible_issues' array.
    
    Args:
        json_file_path (str): Path to the input JSON file
        output_file_path (str, optional): Path for the output JSON file. If None, will use input filename with '_filtered' suffix.
        
    Returns:
        tuple: (filtered_data, removed_count) - The filtered data and count of removed objects
    """
    try:
        # Open and read the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Determine if data is a list or a single object
        if not isinstance(data, list):
            # If it's a single object, convert to a list for processing
            data = [data]
            was_single_object = True
        else:
            was_single_object = False
        
        original_count = len(data)
        
        # Filter out objects with specified issues
        filtered_data = []
        for obj in data:
            # Check if the object has 'analysis' with 'possible_issues'
            if 'analysis' in obj and 'possible_issues' in obj['analysis']:
                possible_issues = obj['analysis']['possible_issues']
                
                # Skip this object only if the first issue is one of the specified issues
                if possible_issues and (possible_issues[0] == 'empty_response' or possible_issues[0] == 'possible_reformatting'):
                    continue
            
            # If we reach here, the object should be kept
            filtered_data.append(obj)
        
        # Determine how many objects were removed
        removed_count = original_count - len(filtered_data)
        
        # If data was originally a single object and only one remains, convert back to single object
        if was_single_object and len(filtered_data) == 1:
            filtered_data = filtered_data[0]
        
        # If no output file is specified, create one with a '_filtered' suffix
        if output_file_path is None:
            base_name, ext = os.path.splitext(json_file_path)
            output_file_path = f"{base_name}_filtered{ext}"
        
        # Write the filtered data to the output file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(filtered_data, file, indent=2, ensure_ascii=False)
        
        print(f"Successfully filtered JSON data. Removed {removed_count} objects.")
        print(f"Filtered data saved to: {output_file_path}")
        
        return filtered_data, removed_count
    
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
        return None, 0
    except json.JSONDecodeError:
        print(f"Error: '{json_file_path}' is not a valid JSON file.")
        return None, 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, 0

def main():
    # Input JSON file path
    json_file_path = 'error_analysis/norwai_1-shot.json'
    
    # Optional: specify an output file path
    # output_file_path = 'data_filtered.json'
    
    # Remove objects with specified issues
    filtered_data, removed_count = remove_specific_issues(json_file_path)
    
    if filtered_data is not None:
        print(f"Original object count: {removed_count + len(filtered_data) if isinstance(filtered_data, list) else removed_count + 1}")
        print(f"Remaining object count: {len(filtered_data) if isinstance(filtered_data, list) else 1}")

if __name__ == "__main__":
    main()