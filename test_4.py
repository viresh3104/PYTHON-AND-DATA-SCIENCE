import pandas as pd
from fuzzywuzzy import process, fuzz

# Load the Excel file
df = pd.read_excel('non_matched_values_updated.xlsx')

# Print the column names to identify the correct names
print("Column names in the Excel file:", df.columns.tolist())

# Assuming the columns are named 'ERP' and 'CRM'
column1 = df['ERP'].dropna().tolist()
column2 = df['CRM'].dropna().tolist()

# Define the threshold for fuzzy matching
threshold = 80

# Create lists to store matched and unmatched names
matched = []
unmatched_column1 = []
unmatched_column2 = column2.copy()  # Start with all names in column2

# Iterate through each name in column1 and find the best match in column2
for name1 in column1:
    match, score = process.extractOne(name1, column2, scorer=fuzz.token_set_ratio)
    if score >= threshold:
        matched.append((name1, match))
        if match in unmatched_column2:
            unmatched_column2.remove(match)  # Remove matched name from unmatched list
    else:
        unmatched_column1.append(name1)

# Convert matched lists to DataFrame
matched_df = pd.DataFrame(matched, columns=['ERP', 'CRM'])

# Convert unmatched lists to DataFrame, ensuring equal length by padding with empty strings
max_unmatched_len = max(len(unmatched_column1), len(unmatched_column2))
unmatched_df = pd.DataFrame({
    'Unmatched ERP': unmatched_column1 + [''] * (max_unmatched_len - len(unmatched_column1)),
    'Unmatched CRM': unmatched_column2 + [''] * (max_unmatched_len - len(unmatched_column2))
})

# Save the matched and unmatched DataFrames to new Excel files
matched_df.to_excel('80p.xlsx', index=False)
unmatched_df.to_excel('no_match.xlsx', index=False)
