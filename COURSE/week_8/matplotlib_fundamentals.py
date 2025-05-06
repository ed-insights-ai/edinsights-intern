"""
Matplotlib Fundamentals
-------------------
Complete visualization tasks using Matplotlib.
This exercise focuses on creating and customizing different types of plots.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import logging
from matplotlib.ticker import MultipleLocator
from matplotlib import cm
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("matplotlib_fundamentals.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Create directories if they don't exist
os.makedirs('data', exist_ok=True)
os.makedirs('plots', exist_ok=True)

def load_or_generate_data():
    """
    Load the sample player data or generate synthetic data if it doesn't exist.
    
    Returns:
        pandas.DataFrame: DataFrame containing player data
    """
    # Try to load the player data created in previous exercises
    if os.path.exists('data/player_data.csv'):
        logger.info("Loading existing player data")
        return pd.read_csv('data/player_data.csv')
    
    # If the file doesn't exist, generate synthetic data
    logger.info("Generating synthetic data")
    
    # Generate synthetic data for demonstration
    np.random.seed(42)
    
    # Generate player data
    n_players = 100
    positions = ['F', 'MF', 'D', 'GK']
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    
    data = {
        'player_id': [f'P{i:03d}' for i in range(1, n_players + 1)],
        'name': [f'Player {i}' for i in range(1, n_players + 1)],
        'position': np.random.choice(positions, size=n_players),
        'team': np.random.choice(teams, size=n_players),
        'age': np.random.randint(18, 35, size=n_players),
        'games_played': np.random.randint(1, 30, size=n_players),
        'minutes': np.random.randint(0, 2700, size=n_players),
        'goals': np.random.randint(0, 20, size=n_players),
        'assists': np.random.randint(0, 15, size=n_players),
        'shots': np.random.randint(0, 100, size=n_players),
        'shots_on_goal': np.random.randint(0, 60, size=n_players),
        'pass_accuracy': np.random.uniform(0.6, 0.95, size=n_players),
        'tackles': np.random.randint(0, 150, size=n_players),
        'interceptions': np.random.randint(0, 150, size=n_players),
        'fouls_committed': np.random.randint(0, 50, size=n_players),
        'yellow_cards': np.random.randint(0, 8, size=n_players),
        'red_cards': np.random.randint(0, 2, size=n_players),
    }
    
    df = pd.DataFrame(data)
    
    # Add some derived metrics
    df['goals_per_90'] = df['goals'] * 90 / df['minutes'].replace(0, np.nan)
    df['assists_per_90'] = df['assists'] * 90 / df['minutes'].replace(0, np.nan)
    df['shot_accuracy'] = df['shots_on_goal'] / df['shots'].replace(0, np.nan)
    
    # Save the generated data
    df.to_csv('data/player_data.csv', index=False)
    
    return df

def task_1_basic_plots(df):
    """
    Task 1: Create basic plot types with Matplotlib.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a line plot
    # 2. Create a bar chart
    # 3. Create a scatter plot
    # 4. Create a histogram
    # 5. Save the plots to the 'plots' directory
    pass

def task_2_customized_visualizations(df):
    """
    Task 2: Create customized visualizations with styling and formatting.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a customized bar chart with labels, title, and grid
    # 2. Create a styled scatter plot with custom markers and colors
    # 3. Create a customized histogram with specified bins and density curve
    # 4. Save the plots to the 'plots' directory
    pass

def task_3_multi_panel_figures(df):
    """
    Task 3: Create multi-panel figures with subplots.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a 2x2 grid of subplots with different plot types
    # 2. Create a figure with a main plot and smaller inset plot
    # 3. Create a figure with subplots of different sizes (using GridSpec)
    # 4. Save the plots to the 'plots' directory
    pass

def task_4_statistical_plots(df):
    """
    Task 4: Create statistical plots.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a box plot to compare distributions
    # 2. Create a violin plot to show distribution density
    # 3. Create an error bar plot with confidence intervals
    # 4. Save the plots to the 'plots' directory
    pass

def task_5_plot_customization(df):
    """
    Task 5: Advanced plot customization.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a plot with custom fonts, colors, and styles
    # 2. Add annotations and text to highlight specific data points
    # 3. Use custom line styles, markers, and colormaps
    # 4. Save the plots to the 'plots' directory
    pass

def task_6_time_series_visualization():
    """
    Task 6: Create time series visualizations.
    
    Returns:
        None
    """
    # Generate synthetic time series data for player performance
    # Start date: 2023-01-01
    start_date = datetime(2023, 1, 1)
    
    # Generate dates for 30 games
    dates = [start_date + timedelta(days=3*i) for i in range(30)]
    
    # Generate performance metrics for 3 players
    np.random.seed(42)
    
    player1_goals = np.random.randint(0, 3, size=30)
    player1_assists = np.random.randint(0, 2, size=30)
    
    player2_goals = np.random.randint(0, 2, size=30)
    player2_assists = np.random.randint(0, 3, size=30)
    
    player3_goals = np.random.randint(0, 1, size=30)
    player3_assists = np.random.randint(0, 1, size=30)
    
    # Create DataFrame
    time_series_data = pd.DataFrame({
        'Date': dates,
        'Player1_Goals': player1_goals,
        'Player1_Assists': player1_assists,
        'Player2_Goals': player2_goals,
        'Player2_Assists': player2_assists,
        'Player3_Goals': player3_goals,
        'Player3_Assists': player3_assists
    })
    
    # Calculate cumulative stats
    time_series_data['Player1_Cumulative_Goals'] = time_series_data['Player1_Goals'].cumsum()
    time_series_data['Player2_Cumulative_Goals'] = time_series_data['Player2_Goals'].cumsum()
    time_series_data['Player3_Cumulative_Goals'] = time_series_data['Player3_Goals'].cumsum()
    
    # YOUR CODE HERE
    # 1. Create a line plot of cumulative goals over time
    # 2. Create a plot with proper date formatting on the x-axis
    # 3. Create a plot with annotations for important dates
    # 4. Save the plots to the 'plots' directory
    pass

def task_7_3d_plots():
    """
    Task 7: Create 3D plots.
    
    Returns:
        None
    """
    # Generate synthetic 3D data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    # YOUR CODE HERE
    # 1. Create a 3D surface plot
    # 2. Create a 3D wireframe plot
    # 3. Create a 3D scatter plot
    # 4. Save the plots to the 'plots' directory
    pass

def task_8_soccer_specific_plots(df):
    """
    Task 8: Create soccer-specific visualizations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a plot comparing goals and assists for top players
    # 2. Create a plot showing the distribution of statistics by position
    # 3. Create a plot showing the relationship between shots and goals
    # 4. Save the plots to the 'plots' directory
    pass

def main():
    """Run all Matplotlib visualization tasks."""
    print("Matplotlib Fundamentals")
    
    # Load or generate data
    df = load_or_generate_data()
    
    print("\nTask 1: Basic Plots")
    task_1_basic_plots(df)
    
    print("\nTask 2: Customized Visualizations")
    task_2_customized_visualizations(df)
    
    print("\nTask 3: Multi-Panel Figures")
    task_3_multi_panel_figures(df)
    
    print("\nTask 4: Statistical Plots")
    task_4_statistical_plots(df)
    
    print("\nTask 5: Plot Customization")
    task_5_plot_customization(df)
    
    print("\nTask 6: Time Series Visualization")
    task_6_time_series_visualization()
    
    print("\nTask 7: 3D Plots")
    task_7_3d_plots()
    
    print("\nTask 8: Soccer-Specific Plots")
    task_8_soccer_specific_plots(df)
    
    print("\nAll visualizations have been saved to the 'plots' directory.")

if __name__ == "__main__":
    main()