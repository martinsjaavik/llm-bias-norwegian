import pandas as pd

# Load the dataset
file_path = 'dataset_ableism.csv'  # Replace with the correct path to your CSV file
df = pd.read_csv(file_path)

# Add a new 'context' column with 'NA' values
df['context'] = 'NA'

# Move 'context_norwegian' to the last column
context_norwegian = df.pop('context_norwegian')
df['context_norwegian'] = context_norwegian

# Save the modified dataset to a new CSV file
output_path = 'modified_dataset.csv'  # Path to save the modified CSV file
df.to_csv(output_path, index=False)

print(f"CSV file has been modified and saved to {output_path}")
