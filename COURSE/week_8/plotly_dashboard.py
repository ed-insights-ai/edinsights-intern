"""
Interactive Plotly Dashboards
-------------------------
Create interactive visualizations using Plotly.
This exercise focuses on building interactive dashboards with Plotly.
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("plotly_dashboard.log"), logging.StreamHandler()]
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
    
    # Add a performance rating for demonstration
    df['performance_rating'] = (
        df['goals'] * 3 + 
        df['assists'] * 2 + 
        df['shots_on_goal'] * 0.5 + 
        df['tackles'] * 0.3 + 
        df['interceptions'] * 0.3 - 
        df['fouls_committed'] * 0.5 - 
        df['yellow_cards'] * 1 - 
        df['red_cards'] * 3
    ) / df['games_played'].replace(0, 1)
    
    # Save the generated data
    df.to_csv('data/player_data.csv', index=False)
    
    return df

def task_1_basic_interactive_plots(df):
    """
    Task 1: Create basic interactive plots with Plotly Express.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create an interactive scatter plot (with hover information)
    # 2. Create an interactive bar chart
    # 3. Create an interactive line plot
    # 4. Create an interactive histogram
    # 5. Save the plots to the 'plots' directory as HTML files
    pass

def task_2_advanced_interactive_plots(df):
    """
    Task 2: Create advanced interactive plots with Plotly Graph Objects.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a customized scatter plot with advanced hover templates
    # 2. Create a bar chart with custom styling and hover effects
    # 3. Create a bubble chart with size and color encoding
    # 4. Create a polar chart for player attributes
    # 5. Save the plots to the 'plots' directory as HTML files
    pass

def task_3_plots_with_dropdowns_and_sliders(df):
    """
    Task 3: Create plots with interactive controls like dropdowns and sliders.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a plot with a dropdown to select different metrics
    # 2. Create a plot with a slider to filter by age or other numeric values
    # 3. Create a plot with buttons to show/hide different data series
    # 4. Create a plot with multiple interactive controls
    # 5. Save the plots to the 'plots' directory as HTML files
    pass

def task_4_animated_visualizations(df):
    """
    Task 4: Create animated visualizations to show changes over time.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # Generate synthetic time series data for player performance
    # For 5 players over 10 games
    players = df.iloc[:5]
    games = 10
    
    player_ids = players['player_id'].tolist()
    player_names = players['name'].tolist()
    
    # Create an empty list to store the time series data
    time_series_data = []
    
    np.random.seed(42)
    
    for game in range(1, games + 1):
        for i, player_id in enumerate(player_ids):
            # Generate random performance metrics for this game
            goals = np.random.randint(0, 3)
            assists = np.random.randint(0, 2)
            shots = np.random.randint(0, 6)
            shots_on_goal = np.random.randint(0, min(shots + 1, 4))
            
            # Add a row to the time series data
            time_series_data.append({
                'player_id': player_id,
                'player_name': player_names[i],
                'game': game,
                'goals': goals,
                'assists': assists,
                'shots': shots,
                'shots_on_goal': shots_on_goal
            })
    
    # Convert to DataFrame
    time_df = pd.DataFrame(time_series_data)
    
    # Calculate cumulative statistics
    cumulative_data = []
    
    for player_id in player_ids:
        player_data = time_df[time_df['player_id'] == player_id].sort_values('game')
        
        cum_goals = 0
        cum_assists = 0
        
        for _, row in player_data.iterrows():
            cum_goals += row['goals']
            cum_assists += row['assists']
            
            cumulative_data.append({
                'player_id': row['player_id'],
                'player_name': row['player_name'],
                'game': row['game'],
                'goals': row['goals'],
                'assists': row['assists'],
                'cum_goals': cum_goals,
                'cum_assists': cum_assists
            })
    
    cum_df = pd.DataFrame(cumulative_data)
    
    # YOUR CODE HERE
    # 1. Create an animated scatter plot showing changes over games
    # 2. Create an animated bar chart showing cumulative statistics
    # 3. Create an animated line chart showing performance trends
    # 4. Create an animated bubble chart
    # 5. Save the plots to the 'plots' directory as HTML files
    pass

def task_5_multi_panel_dashboards(df):
    """
    Task 5: Create multi-panel dashboards with Plotly subplots.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a dashboard with 2x2 subplots showing different visualizations
    # 2. Create a dashboard with subplots of different sizes
    # 3. Create a dashboard with a mix of plot types
    # 4. Create a dashboard with synchronized axes
    # 5. Save the dashboards to the 'plots' directory as HTML files
    pass

def task_6_statistical_visualizations(df):
    """
    Task 6: Create interactive statistical visualizations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create an interactive box plot
    # 2. Create an interactive violin plot
    # 3. Create a distplot with multiple distributions
    # 4. Create a visualization showing correlation and regression
    # 5. Save the plots to the 'plots' directory as HTML files
    pass

def task_7_specialized_visualizations(df):
    """
    Task 7: Create specialized visualizations with Plotly.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a heatmap visualization
    # 2. Create a 3D visualization
    # 3. Create a radar/spider chart for player comparison
    # 4. Create a sunburst or treemap chart
    # 5. Save the plots to the 'plots' directory as HTML files
    pass

def task_8_soccer_dashboard(df):
    """
    Task 8: Create a comprehensive soccer analytics dashboard.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a dashboard showing player performance by position
    # 2. Create a dashboard for comparing players
    # 3. Create a dashboard showing team statistics
    # 4. Create a dashboard with interactive filters for player selection
    # 5. Save the dashboard to the 'plots' directory as an HTML file
    pass

def main():
    """Run all Plotly visualization tasks."""
    print("Interactive Plotly Dashboards")
    
    # Set default renderer to browser for interactive plots
    pio.renderers.default = "browser"
    
    # Load or generate data
    df = load_or_generate_data()
    
    print("\nTask 1: Basic Interactive Plots")
    task_1_basic_interactive_plots(df)
    
    print("\nTask 2: Advanced Interactive Plots")
    task_2_advanced_interactive_plots(df)
    
    print("\nTask 3: Plots with Dropdowns and Sliders")
    task_3_plots_with_dropdowns_and_sliders(df)
    
    print("\nTask 4: Animated Visualizations")
    task_4_animated_visualizations(df)
    
    print("\nTask 5: Multi-Panel Dashboards")
    task_5_multi_panel_dashboards(df)
    
    print("\nTask 6: Statistical Visualizations")
    task_6_statistical_visualizations(df)
    
    print("\nTask 7: Specialized Visualizations")
    task_7_specialized_visualizations(df)
    
    print("\nTask 8: Soccer Dashboard")
    task_8_soccer_dashboard(df)
    
    print("\nAll visualizations have been saved to the 'plots' directory as HTML files.")
    print("You can open these files in a web browser to interact with the visualizations.")

if __name__ == "__main__":
    main()