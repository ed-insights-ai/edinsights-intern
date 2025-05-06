"""
Soccer Analytics Visualization
--------------------------
Create soccer-specific visualizations for player and team analysis.
This exercise focuses on implementing informative visualizations for soccer analytics.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import os
import logging
from mplsoccer import Pitch, VerticalPitch, FontManager

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("soccer_visualization.log"), logging.StreamHandler()]
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

def generate_match_data():
    """
    Generate synthetic match data for visualization.
    
    Returns:
        dict: Dictionary containing synthetic match data
    """
    np.random.seed(42)
    
    # Generate synthetic shot data
    n_shots = 20
    
    # Shot coordinates (x: 0 to 120, y: 0 to 80, with (0,0) at bottom-left corner)
    shot_x = np.random.uniform(80, 118, n_shots)  # Most shots from the attacking third
    shot_y = np.random.uniform(10, 70, n_shots)
    
    # Shot outcomes (1 for goal, 0 for miss/save)
    shot_outcome = np.random.choice([0, 1], size=n_shots, p=[0.8, 0.2])  # 20% success rate
    
    # Shot xG (expected goals - probability of scoring)
    # Higher when closer to goal and central
    distance_to_goal = np.sqrt((120 - shot_x) ** 2 + (40 - shot_y) ** 2)
    angle = np.abs(np.arctan2(shot_y - 40, 120 - shot_x))
    shot_xg = np.exp(-0.1 * distance_to_goal - 0.5 * angle)
    shot_xg = np.clip(shot_xg, 0.01, 0.99)
    
    # Player who took the shot
    shot_player = np.random.choice([f'Player {i}' for i in range(1, 12)], size=n_shots)
    
    # Team (all shots by Team A in this simple example)
    shot_team = ['Team A'] * n_shots
    
    # Generate synthetic pass data
    n_passes = 100
    
    # Pass start coordinates
    pass_start_x = np.random.uniform(0, 120, n_passes)
    pass_start_y = np.random.uniform(0, 80, n_passes)
    
    # Pass end coordinates
    pass_length = np.random.uniform(5, 30, n_passes)
    pass_angle = np.random.uniform(0, 2 * np.pi, n_passes)
    pass_end_x = np.clip(pass_start_x + pass_length * np.cos(pass_angle), 0, 120)
    pass_end_y = np.clip(pass_start_y + pass_length * np.sin(pass_angle), 0, 80)
    
    # Pass outcome (1 for complete, 0 for incomplete)
    pass_outcome = np.random.choice([0, 1], size=n_passes, p=[0.2, 0.8])  # 80% completion rate
    
    # Player who made the pass
    pass_player = np.random.choice([f'Player {i}' for i in range(1, 12)], size=n_passes)
    
    # Team (all passes by Team A in this simple example)
    pass_team = ['Team A'] * n_passes
    
    # Create match data dictionary
    match_data = {
        'shots': {
            'x': shot_x,
            'y': shot_y,
            'outcome': shot_outcome,
            'xG': shot_xg,
            'player': shot_player,
            'team': shot_team
        },
        'passes': {
            'start_x': pass_start_x,
            'start_y': pass_start_y,
            'end_x': pass_end_x,
            'end_y': pass_end_y,
            'outcome': pass_outcome,
            'player': pass_player,
            'team': pass_team
        }
    }
    
    return match_data

def task_1_player_performance_radar(df):
    """
    Task 1: Create radar/spider charts for player performance comparison.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a radar chart comparing multiple players on key metrics
    # 2. Create a radar chart for different position groups with position-specific metrics
    # 3. Create an interactive radar chart with plotly
    # 4. Save the plots to the 'plots' directory
    pass

def task_2_shot_map(match_data):
    """
    Task 2: Create a shot map visualization.
    
    Args:
        match_data (dict): Dictionary containing match data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a basic shot map showing shot locations and outcomes
    # 2. Create a shot map with expected goals (xG) representation
    # 3. Create an interactive shot map with plotly
    # 4. Save the plots to the 'plots' directory
    pass

def task_3_pass_map_and_network(match_data):
    """
    Task 3: Create pass maps and pass networks.
    
    Args:
        match_data (dict): Dictionary containing match data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create a basic pass map showing successful and unsuccessful passes
    # 2. Create a pass network showing connections between players
    # 3. Create a heatmap of pass origins or destinations
    # 4. Save the plots to the 'plots' directory
    pass

def task_4_player_comparison_dashboard(df):
    """
    Task 4: Create a comprehensive player comparison dashboard.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Select 3-4 players for comparison
    # 2. Create a multi-panel dashboard comparing various performance metrics
    # 3. Include appropriate visualizations for different metric types
    # 4. Save the dashboard to the 'plots' directory
    pass

def task_5_team_performance_visualization(df):
    """
    Task 5: Create team performance visualizations.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # Aggregate player data to team level
    team_data = df.groupby('team').agg({
        'goals': 'sum',
        'assists': 'sum',
        'shots': 'sum',
        'shots_on_goal': 'sum',
        'pass_accuracy': 'mean',
        'tackles': 'sum',
        'interceptions': 'sum',
        'yellow_cards': 'sum',
        'red_cards': 'sum',
        'fouls_committed': 'sum',
        'performance_rating': 'mean'
    }).reset_index()
    
    # YOUR CODE HERE
    # 1. Create a team performance overview dashboard
    # 2. Create visualizations comparing teams across key metrics
    # 3. Create a visualization showing team strengths and weaknesses
    # 4. Save the plots to the 'plots' directory
    pass

def task_6_performance_trends_visualization(df):
    """
    Task 6: Create visualizations showing player performance trends.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # Generate synthetic time series data for demonstration
    np.random.seed(42)
    
    # Select 5 players for demonstration
    players = df.iloc[:5]
    
    # Generate performance data for 10 games
    games = 10
    metrics = ['goals', 'assists', 'shots', 'shots_on_goal', 'pass_accuracy', 'tackles']
    
    # Create an empty DataFrame to store the time series data
    columns = ['player_id', 'player_name', 'game'] + metrics
    trend_data = pd.DataFrame(columns=columns)
    
    # Generate random performance data for each player and game
    for _, player in players.iterrows():
        for game in range(1, games + 1):
            # Generate random performance metrics
            game_data = {
                'player_id': player['player_id'],
                'player_name': player['name'],
                'game': game,
                'goals': np.random.randint(0, 3),
                'assists': np.random.randint(0, 2),
                'shots': np.random.randint(1, 6),
                'shots_on_goal': np.random.randint(0, 4),
                'pass_accuracy': np.random.uniform(0.6, 0.95),
                'tackles': np.random.randint(0, 8)
            }
            
            # Append to the DataFrame
            trend_data = pd.concat([trend_data, pd.DataFrame([game_data])], ignore_index=True)
    
    # YOUR CODE HERE
    # 1. Create a line chart showing performance trends over games
    # 2. Create a visualization showing cumulative statistics
    # 3. Create a visualization highlighting performance improvements or declines
    # 4. Save the plots to the 'plots' directory
    pass

def task_7_performance_distribution_by_position(df):
    """
    Task 7: Create visualizations showing performance distributions by position.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # YOUR CODE HERE
    # 1. Create box plots or violin plots showing metric distributions by position
    # 2. Create a visualization comparing position-specific performance metrics
    # 3. Create a visualization identifying top performers in each position
    # 4. Save the plots to the 'plots' directory
    pass

def task_8_comprehensive_player_profile(df):
    """
    Task 8: Create a comprehensive player profile visualization.
    
    Args:
        df (pandas.DataFrame): DataFrame containing player data
        
    Returns:
        None
    """
    # Select a player for the profile
    # Choose the player with the highest performance rating
    player_idx = df['performance_rating'].idxmax()
    player = df.iloc[player_idx]
    
    # YOUR CODE HERE
    # 1. Create a multi-panel dashboard showing all aspects of the player's performance
    # 2. Include appropriate charts for different metric types
    # 3. Include comparison to position averages
    # 4. Save the profile to the 'plots' directory
    pass

def main():
    """Run all soccer visualization tasks."""
    print("Soccer Analytics Visualization")
    
    # Set plotting styles
    plt.style.use('fivethirtyeight')
    sns.set_theme(style="whitegrid")
    
    # Load or generate player data
    df = load_or_generate_data()
    
    # Generate synthetic match data
    match_data = generate_match_data()
    
    print("\nTask 1: Player Performance Radar")
    task_1_player_performance_radar(df)
    
    print("\nTask 2: Shot Map")
    task_2_shot_map(match_data)
    
    print("\nTask 3: Pass Map and Network")
    task_3_pass_map_and_network(match_data)
    
    print("\nTask 4: Player Comparison Dashboard")
    task_4_player_comparison_dashboard(df)
    
    print("\nTask 5: Team Performance Visualization")
    task_5_team_performance_visualization(df)
    
    print("\nTask 6: Performance Trends Visualization")
    task_6_performance_trends_visualization(df)
    
    print("\nTask 7: Performance Distribution by Position")
    task_7_performance_distribution_by_position(df)
    
    print("\nTask 8: Comprehensive Player Profile")
    task_8_comprehensive_player_profile(df)
    
    print("\nAll visualizations have been saved to the 'plots' directory.")

if __name__ == "__main__":
    main()