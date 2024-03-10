# Import necessary library
import pandas as pd

# Function to read the CSV and compute statistics
def analyze_csv(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Size Statistics
    num_rows, num_cols = df.shape
    size_stats = {'Number of Rows': num_rows, 'Number of Columns': num_cols}
    
    # Summary Statistics for numeric columns
    numeric_summary = df.describe().transpose()  # Using describe() to get summary statistics
    
    # Summary Statistics for categorical columns
    categorical_summary = df.describe(include=['object']).transpose()  # For categorical data
    
    return size_stats, numeric_summary, categorical_summary

size_stats, numeric_summary, categorical_summary = analyze_csv('data/books_data.csv')
print('Size Statistics:', size_stats)
print('Numeric Summary:', numeric_summary)
print('Categorical Summary:', categorical_summary)

# write the numeric summary to a csv file
numeric_summary.to_csv('data/numeric_summary.csv')

# write the categorical summary to a csv file
categorical_summary.to_csv('data/categorical_summary.csv')