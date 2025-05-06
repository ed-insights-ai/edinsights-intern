"""
CSV Data Processing
----------------
Complete the following functions according to their docstrings.
This exercise focuses on working with CSV files in Python, both using
standard library and pandas.
"""

import csv
import pandas as pd


def read_csv_standard(filepath, has_header=True):
    """
    Read a CSV file using the standard csv module.
    
    Args:
        filepath (str): Path to the CSV file
        has_header (bool, optional): Whether the CSV has a header row. Defaults to True.
        
    Returns:
        tuple: (headers, data) where headers is a list of column names
               and data is a list of rows (each row is a list of values)
               If has_header is False, headers will be None
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    # YOUR CODE HERE
    pass

def write_csv_standard(filepath, data, headers=None):
    """
    Write data to a CSV file using the standard csv module.
    
    Args:
        filepath (str): Path to the CSV file
        data (list): List of rows (each row is a list of values)
        headers (list, optional): List of column names. Defaults to None.
        
    Returns:
        bool: True if write was successful
        
    Raises:
        IOError: If writing to the file fails
    """
    # YOUR CODE HERE
    pass

def filter_csv_rows(filepath, filter_func, output_filepath=None):
    """
    Filter rows in a CSV file based on a filter function.
    
    Args:
        filepath (str): Path to the input CSV file
        filter_func (function): Function that takes a row (dict) and returns a boolean
        output_filepath (str, optional): Path to the output CSV file. 
                                         If None, return filtered rows without writing. 
                                         Defaults to None.
        
    Returns:
        list: Filtered rows (each row is a dict with column names as keys)
              Empty if output_filepath is provided
        
    Raises:
        FileNotFoundError: If the input file doesn't exist
    """
    # YOUR CODE HERE
    pass

def read_csv_pandas(filepath):
    """
    Read a CSV file using pandas.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pandas.DataFrame: DataFrame containing the CSV data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    # YOUR CODE HERE
    pass

def write_csv_pandas(filepath, dataframe):
    """
    Write a pandas DataFrame to a CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        dataframe (pandas.DataFrame): DataFrame to write
        
    Returns:
        bool: True if write was successful
        
    Raises:
        IOError: If writing to the file fails
    """
    # YOUR CODE HERE
    pass

def filter_csv_pandas(filepath, filter_func, output_filepath=None):
    """
    Filter rows in a CSV file using pandas based on a filter function.
    
    Args:
        filepath (str): Path to the input CSV file
        filter_func (function): Function that takes a row (pandas.Series) and returns a boolean
        output_filepath (str, optional): Path to the output CSV file. 
                                         If None, return filtered DataFrame without writing. 
                                         Defaults to None.
        
    Returns:
        pandas.DataFrame: Filtered DataFrame
                          Empty if output_filepath is provided
        
    Raises:
        FileNotFoundError: If the input file doesn't exist
    """
    # YOUR CODE HERE
    pass

def aggregate_csv_data(filepath, group_by, agg_functions):
    """
    Aggregate CSV data using pandas.
    
    Args:
        filepath (str): Path to the CSV file
        group_by (str or list): Column(s) to group by
        agg_functions (dict): Dictionary mapping column names to aggregation functions
                              Example: {'column1': 'sum', 'column2': 'mean'}
        
    Returns:
        pandas.DataFrame: Aggregated DataFrame
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    # YOUR CODE HERE
    pass

def merge_csv_files(filepath1, filepath2, merge_on, how='inner'):
    """
    Merge two CSV files based on a common column using pandas.
    
    Args:
        filepath1 (str): Path to the first CSV file
        filepath2 (str): Path to the second CSV file
        merge_on (str or list): Column(s) to merge on
        how (str, optional): Type of merge to perform.
                             One of 'inner', 'outer', 'left', 'right'. 
                             Defaults to 'inner'.
        
    Returns:
        pandas.DataFrame: Merged DataFrame
        
    Raises:
        FileNotFoundError: If either file doesn't exist
    """
    # YOUR CODE HERE
    pass

def main():
    """Run examples to test your functions."""
    # Create a sample CSV file
    sample_data = [
        ['id', 'name', 'age', 'city'],
        ['1', 'John', '30', 'New York'],
        ['2', 'Jane', '25', 'Los Angeles'],
        ['3', 'Bob', '35', 'Chicago'],
        ['4', 'Alice', '28', 'New York']
    ]
    sample_file = "sample.csv"
    with open(sample_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)
    print(f"Created sample CSV file: {sample_file}")
    
    # Read CSV using standard library
    print("\nReading CSV using standard library:")
    headers, data = read_csv_standard(sample_file)
    print(f"Headers: {headers}")
    print(f"Data (first 2 rows): {data[:2]}")
    
    # Filter CSV rows
    print("\nFiltering CSV rows (age > 28):")
    def age_filter(row):
        return int(row['age']) > 28
    filtered_rows = filter_csv_rows(sample_file, age_filter)
    print(f"Filtered rows: {filtered_rows}")
    
    # Read CSV using pandas
    print("\nReading CSV using pandas:")
    df = read_csv_pandas(sample_file)
    print(df.head())
    
    # Aggregate data
    print("\nAggregating data by city:")
    agg_df = aggregate_csv_data(sample_file, 'city', {'age': 'mean'})
    print(agg_df)
    
    # Clean up
    import os
    os.remove(sample_file)
    print(f"\nCleaned up sample file: {sample_file}")

if __name__ == "__main__":
    main()