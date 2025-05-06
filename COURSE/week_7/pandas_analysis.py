"""
Pandas Data Analysis
-----------------
Complete data analysis tasks using pandas for data manipulation and exploration.
This exercise focuses on processing, cleaning, and transforming complex datasets.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("pandas_analysis.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

def generate_sample_data():
    """
    Generate sample soccer player data for analysis.
    
    Returns:
        pandas.DataFrame: DataFrame containing sample player data
    """
    # Generate some sample data for the exercises
    np.random.seed(42)
    
    positions = ['F', 'MF', 'D', 'GK']
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    
    n_players = 200
    
    data = {
        'player_id': [f'P{i:03d}' for i in range(1, n_players + 1)],
        'first_name': [f'FirstName{i}' for i in range(1, n_players + 1)],
        'last_name': [f'LastName{i}' for i in range(1, n_players + 1)],
        'position': np.random.choice(positions, size=n_players),
        'team': np.random.choice(teams, size=n_players),
        'age': np.random.randint(18, 35, size=n_players),
        'height': np.random.normal(180, 10, size=n_players).round(1),  # in cm
        'weight': np.random.normal(75, 8, size=n_players).round(1),    # in kg
        'games_played': np.random.randint(1, 30, size=n_players),
        'minutes': np.random.randint(0, 2700, size=n_players),
        'goals': np.zeros(n_players),
        'assists': np.zeros(n_players),
        'shots': np.zeros(n_players),
        'shots_on_goal': np.zeros(n_players),
        'passes': np.random.randint(20, 1000, size=n_players),
        'pass_accuracy': np.random.uniform(0.6, 0.95, size=n_players).round(3),
        'tackles': np.zeros(n_players),
        'interceptions': np.zeros(n_players),
        'saves': np.zeros(n_players),
        'fouls_committed': np.random.randint(0, 50, size=n_players),
        'fouls_suffered': np.random.randint(0, 50, size=n_players),
        'yellow_cards': np.random.randint(0, 8, size=n_players),
        'red_cards': np.random.randint(0, 2, size=n_players),
    }
    
    # Adjust stats based on position to be more realistic
    for i in range(n_players):
        if data['position'][i] == 'F':  # Forward
            data['goals'][i] = np.random.randint(0, 20)
            data['assists'][i] = np.random.randint(0, 15)
            data['shots'][i] = np.random.randint(10, 100)
            data['shots_on_goal'][i] = np.random.randint(5, int(data['shots'][i] * 0.7))
            data['tackles'][i] = np.random.randint(0, 30)
            data['interceptions'][i] = np.random.randint(0, 30)
        elif data['position'][i] == 'MF':  # Midfielder
            data['goals'][i] = np.random.randint(0, 10)
            data['assists'][i] = np.random.randint(0, 20)
            data['shots'][i] = np.random.randint(5, 60)
            data['shots_on_goal'][i] = np.random.randint(3, int(data['shots'][i] * 0.6))
            data['tackles'][i] = np.random.randint(10, 80)
            data['interceptions'][i] = np.random.randint(10, 80)
        elif data['position'][i] == 'D':  # Defender
            data['goals'][i] = np.random.randint(0, 5)
            data['assists'][i] = np.random.randint(0, 8)
            data['shots'][i] = np.random.randint(0, 20)
            data['shots_on_goal'][i] = np.random.randint(0, int(data['shots'][i] * 0.5))
            data['tackles'][i] = np.random.randint(30, 150)
            data['interceptions'][i] = np.random.randint(30, 150)
        elif data['position'][i] == 'GK':  # Goalkeeper
            data['goals'][i] = np.random.randint(0, 2)
            data['assists'][i] = np.random.randint(0, 3)
            data['shots'][i] = np.random.randint(0, 5)
            data['shots_on_goal'][i] = np.random.randint(0, int(data['shots'][i] * 0.3))
            data['tackles'][i] = np.random.randint(0, 10)
            data['interceptions'][i] = np.random.randint(0, 20)
            data['saves'] = np.random.randint(20, 150)
    
    # Create a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Save the data to a CSV file
    df.to_csv('data/player_data.csv', index=False)
    
    return df

def task_1_data_loading_and_inspection(file_path='data/player_data.csv'):
    """
    Task 1: Load data from CSV and perform basic inspection.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        dict: Dictionary containing results of the inspection
    """
    # YOUR CODE HERE
    # 1. Load the data from the CSV file
    # 2. Display basic information about the DataFrame (shape, dtypes, etc.)
    # 3. Check for missing values
    # 4. Generate descriptive statistics
    # 5. Return a dictionary with the results
    pass

def task_2_data_cleaning(df):
    """
    Task 2: Clean and preprocess the data.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        pandas.DataFrame: Cleaned DataFrame
    """
    # YOUR CODE HERE
    # 1. Handle any missing values
    # 2. Remove any duplicates
    # 3. Fix data types if needed
    # 4. Handle outliers
    # 5. Add any derived features
    # 6. Return the cleaned DataFrame
    pass

def task_3_exploratory_analysis(df):
    """
    Task 3: Perform exploratory data analysis.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        dict: Dictionary containing results of the analysis
    """
    # YOUR CODE HERE
    # 1. Analyze distributions of key variables
    # 2. Calculate correlations between variables
    # 3. Identify patterns and relationships
    # 4. Generate summary statistics by position
    # 5. Return a dictionary with the results
    pass

def task_4_aggregation_and_grouping(df):
    """
    Task 4: Perform aggregation and grouping operations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        dict: Dictionary containing DataFrames of aggregated data
    """
    # YOUR CODE HERE
    # 1. Group data by position and calculate statistics
    # 2. Group data by team and calculate statistics
    # 3. Calculate aggregate statistics for different age groups
    # 4. Return a dictionary with the aggregated DataFrames
    pass

def task_5_merging_and_joining(df):
    """
    Task 5: Demonstrate merging and joining operations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        dict: Dictionary containing results of merge operations
    """
    # Generate some additional data for joining
    team_data = pd.DataFrame({
        'team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'founded': [2000, 1995, 2005, 1990, 2010],
        'stadium_capacity': [40000, 35000, 42000, 38000, 41000]
    })
    
    coach_data = pd.DataFrame({
        'team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E', 'Team F'],
        'coach': ['Coach A', 'Coach B', 'Coach C', 'Coach D', 'Coach E', 'Coach F'],
        'experience_years': [10, 15, 8, 20, 5, 12]
    })
    
    # YOUR CODE HERE
    # 1. Perform different types of joins (inner, left, right, outer)
    # 2. Merge player data with team data
    # 3. Merge player data with coach data
    # 4. Return a dictionary with the merged DataFrames
    pass

def task_6_advanced_aggregation(df):
    """
    Task 6: Perform advanced aggregation operations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        dict: Dictionary containing results of advanced aggregation
    """
    # YOUR CODE HERE
    # 1. Use groupby with multiple columns
    # 2. Apply multiple aggregation functions to different columns
    # 3. Create pivot tables and crosstabs
    # 4. Use custom aggregation functions
    # 5. Return a dictionary with the results
    pass

def task_7_advanced_selection(df):
    """
    Task 7: Demonstrate advanced selection and filtering techniques.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        dict: Dictionary containing filtered DataFrames
    """
    # YOUR CODE HERE
    # 1. Use boolean indexing for complex conditions
    # 2. Use query() method for filtering
    # 3. Use .loc and .iloc for advanced selection
    # 4. Filter data using multiple conditions
    # 5. Return a dictionary with the filtered DataFrames
    pass

def task_8_data_transformation(df):
    """
    Task 8: Perform data transformation operations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        dict: Dictionary containing transformed DataFrames
    """
    # YOUR CODE HERE
    # 1. Apply normalization or standardization to numeric columns
    # 2. Perform binning operations
    # 3. Create categorical variables from continuous data
    # 4. Apply mathematical transformations (log, square root, etc.)
    # 5. Return a dictionary with the transformed DataFrames
    pass

def visualize_results(df, analysis_results):
    """
    Create visualizations for the analysis results.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        analysis_results (dict): Dictionary containing analysis results
        
    Returns:
        None
    """
    # Create a directory for plots if it doesn't exist
    os.makedirs('plots', exist_ok=True)
    
    # YOUR CODE HERE (OPTIONAL)
    # Create relevant plots based on the analysis results
    # Save the plots to the 'plots' directory
    pass

def main():
    """Run all pandas analysis tasks."""
    print("Pandas Data Analysis")
    
    # Check if sample data exists, if not, generate it
    if not os.path.exists('data/player_data.csv'):
        print("Generating sample data...")
        df = generate_sample_data()
    else:
        print("Loading existing data...")
        df = pd.read_csv('data/player_data.csv')
    
    print("\nTask 1: Data Loading and Inspection")
    inspection_results = task_1_data_loading_and_inspection()
    
    print("\nTask 2: Data Cleaning")
    cleaned_df = task_2_data_cleaning(df)
    
    print("\nTask 3: Exploratory Analysis")
    analysis_results = task_3_exploratory_analysis(cleaned_df)
    
    print("\nTask 4: Aggregation and Grouping")
    aggregation_results = task_4_aggregation_and_grouping(cleaned_df)
    
    print("\nTask 5: Merging and Joining")
    merge_results = task_5_merging_and_joining(cleaned_df)
    
    print("\nTask 6: Advanced Aggregation")
    adv_aggregation_results = task_6_advanced_aggregation(cleaned_df)
    
    print("\nTask 7: Advanced Selection")
    selection_results = task_7_advanced_selection(cleaned_df)
    
    print("\nTask 8: Data Transformation")
    transformation_results = task_8_data_transformation(cleaned_df)
    
    print("\nCreating visualizations...")
    visualize_results(cleaned_df, analysis_results)
    
    print("\nAnalysis complete! Review the outputs above and check the 'plots' directory for visualizations.")

if __name__ == "__main__":
    main()