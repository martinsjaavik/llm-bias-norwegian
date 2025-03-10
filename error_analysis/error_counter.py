import json
from collections import Counter

def count_issues(json_file_path):
    """
    Counts the possible issues of JSON objects in a file.
    If an object has more than one possible issue, only the first one is counted.
    
    Args:
        json_file_path (str): Path to the JSON file
        
    Returns:
        Counter: A counter object with issue types and their counts
    """
    try:
        # Open and read the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Counter to store the counts of each issue
        issue_counter = Counter()
        
        # If the data is a dictionary, convert it to a list
        if isinstance(data, dict):
            data = [data]
        
        # Iterate through each object in the JSON data
        for obj in data:
            # Check if the object has an analysis field with possible_issues
            if 'analysis' in obj and 'possible_issues' in obj['analysis']:
                possible_issues = obj['analysis']['possible_issues']
                
                # If there are issues, count the first one
                if possible_issues and len(possible_issues) > 0:
                    first_issue = possible_issues[0]
                    issue_counter[first_issue] += 1
        
        return issue_counter
    
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
        return Counter()
    except json.JSONDecodeError:
        print(f"Error: '{json_file_path}' is not a valid JSON file.")
        return Counter()
    except Exception as e:
        print(f"Error: {str(e)}")
        return Counter()

def main():
    # Change this to your JSON file path
    json_file_path = 'error_analysis/gpt-0-shot.json'
    
    # Count the issues
    issue_counts = count_issues(json_file_path)
    
    # Print the results
    print("Issue Counts:")
    if not issue_counts:
        print("No issues found or error occurred.")
    else:
        for issue, count in issue_counts.items():
            print(f"  {issue}: {count}")
        print(f"Total objects with issues: {sum(issue_counts.values())}")

if __name__ == "__main__":
    main()