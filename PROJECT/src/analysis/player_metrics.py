"""
Player Performance Metrics

This module provides functions for calculating various performance metrics
for soccer players based on their statistics.
"""

import pandas as pd
import numpy as np

def calculate_goals_per_90(player_stats):
    """
    Calculate goals per 90 minutes played.
    
    Args:
        player_stats (pd.DataFrame): DataFrame containing player statistics
            with at least 'goals' and 'minutes' columns
    
    Returns:
        pd.Series: Series containing goals per 90 minutes for each player
    """
    # Avoid division by zero
    return player_stats['goals'] * 90 / player_stats['minutes'].replace(0, np.nan)

def calculate_assists_per_90(player_stats):
    """
    Calculate assists per 90 minutes played.
    
    Args:
        player_stats (pd.DataFrame): DataFrame containing player statistics
            with at least 'assists' and 'minutes' columns
    
    Returns:
        pd.Series: Series containing assists per 90 minutes for each player
    """
    return player_stats['assists'] * 90 / player_stats['minutes'].replace(0, np.nan)

def calculate_goal_contributions(player_stats):
    """
    Calculate total goal contributions (goals + assists).
    
    Args:
        player_stats (pd.DataFrame): DataFrame containing player statistics
            with at least 'goals' and 'assists' columns
    
    Returns:
        pd.Series: Series containing total goal contributions for each player
    """
    return player_stats['goals'] + player_stats['assists']

def calculate_shot_accuracy(player_stats):
    """
    Calculate shot accuracy (shots on goal / total shots).
    
    Args:
        player_stats (pd.DataFrame): DataFrame containing player statistics
            with at least 'shots' and 'shots_on_goal' columns
    
    Returns:
        pd.Series: Series containing shot accuracy for each player
    """
    return player_stats['shots_on_goal'] / player_stats['shots'].replace(0, np.nan)

def calculate_conversion_rate(player_stats):
    """
    Calculate conversion rate (goals / shots).
    
    Args:
        player_stats (pd.DataFrame): DataFrame containing player statistics
            with at least 'goals' and 'shots' columns
    
    Returns:
        pd.Series: Series containing conversion rate for each player
    """
    return player_stats['goals'] / player_stats['shots'].replace(0, np.nan)

def calculate_efficiency_score(player_stats):
    """
    Calculate an overall efficiency score based on multiple metrics.
    
    This is a composite score that weighs different aspects of a player's performance.
    
    Args:
        player_stats (pd.DataFrame): DataFrame containing player statistics
            with various performance columns
    
    Returns:
        pd.Series: Series containing efficiency score for each player
    """
    # This is a simple example - actual implementation would be more sophisticated
    goals_per_90 = calculate_goals_per_90(player_stats)
    assists_per_90 = calculate_assists_per_90(player_stats)
    shot_accuracy = calculate_shot_accuracy(player_stats)
    
    # Simple weighted average (weights would be determined by analysis)
    weights = {
        'goals_per_90': 0.5,
        'assists_per_90': 0.3,
        'shot_accuracy': 0.2
    }
    
    # Normalize to 0-100 scale (simplified for example)
    efficiency = (
        goals_per_90 * weights['goals_per_90'] * 25 +
        assists_per_90 * weights['assists_per_90'] * 25 +
        shot_accuracy * weights['shot_accuracy'] * 100
    )
    
    return efficiency

def compare_players(player_stats, metrics=None):
    """
    Compare players across selected metrics.
    
    Args:
        player_stats (pd.DataFrame): DataFrame containing player statistics
        metrics (list): List of metrics to compare (default: standard metrics)
    
    Returns:
        pd.DataFrame: DataFrame with calculated metrics for each player
    """
    if metrics is None:
        metrics = ['goals_per_90', 'assists_per_90', 'shot_accuracy', 'conversion_rate']
    
    results = pd.DataFrame(index=player_stats.index)
    
    # Calculate each metric
    if 'goals_per_90' in metrics:
        results['goals_per_90'] = calculate_goals_per_90(player_stats)
    
    if 'assists_per_90' in metrics:
        results['assists_per_90'] = calculate_assists_per_90(player_stats)
    
    if 'goal_contributions' in metrics:
        results['goal_contributions'] = calculate_goal_contributions(player_stats)
    
    if 'shot_accuracy' in metrics:
        results['shot_accuracy'] = calculate_shot_accuracy(player_stats)
    
    if 'conversion_rate' in metrics:
        results['conversion_rate'] = calculate_conversion_rate(player_stats)
    
    if 'efficiency_score' in metrics:
        results['efficiency_score'] = calculate_efficiency_score(player_stats)
    
    return results

def main():
    """Test function to demonstrate the metrics calculation."""
    try:
        # Try to load sample data
        player_stats = pd.read_csv('../../data/sample/player_stats_sample.csv')
        
        # Calculate metrics
        metrics = ['goals_per_90', 'assists_per_90', 'goal_contributions', 
                  'shot_accuracy', 'conversion_rate', 'efficiency_score']
        
        results = compare_players(player_stats, metrics)
        
        # Print results
        print("Player Performance Metrics:")
        print(results)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()