"""
Tests for player metrics calculation functions.
"""

import sys
import os
import pandas as pd
import numpy as np
import pytest

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))
from analysis.player_metrics import (
    calculate_goals_per_90, 
    calculate_assists_per_90,
    calculate_goal_contributions,
    calculate_shot_accuracy,
    calculate_conversion_rate,
    calculate_efficiency_score,
    compare_players
)

# Sample data for testing
@pytest.fixture
def sample_player_data():
    return pd.DataFrame({
        'player_id': ['P1', 'P2', 'P3', 'P4'],
        'first_name': ['John', 'Jane', 'Alex', 'Sam'],
        'last_name': ['Smith', 'Doe', 'Johnson', 'Williams'],
        'team': ['Team A', 'Team A', 'Team B', 'Team B'],
        'position': ['F', 'MF', 'D', 'GK'],
        'games_played': [10, 8, 10, 10],
        'minutes': [900, 720, 900, 900],
        'goals': [8, 4, 1, 0],
        'assists': [3, 6, 2, 0],
        'shots': [20, 15, 5, 0],
        'shots_on_goal': [15, 10, 2, 0],
        'yellow_cards': [1, 0, 3, 0],
        'red_cards': [0, 0, 0, 0],
        'fouls_committed': [5, 2, 8, 1],
        'fouls_suffered': [10, 8, 4, 0]
    })

def test_calculate_goals_per_90(sample_player_data):
    """Test goals per 90 minutes calculation."""
    result = calculate_goals_per_90(sample_player_data)
    
    # Expected values: (goals * 90) / minutes
    expected = pd.Series([
        8 * 90 / 900,  # 0.8
        4 * 90 / 720,  # 0.5
        1 * 90 / 900,  # 0.1
        0 * 90 / 900   # 0.0
    ], index=sample_player_data.index)
    
    pd.testing.assert_series_equal(result, expected)

def test_calculate_assists_per_90(sample_player_data):
    """Test assists per 90 minutes calculation."""
    result = calculate_assists_per_90(sample_player_data)
    
    # Expected values: (assists * 90) / minutes
    expected = pd.Series([
        3 * 90 / 900,  # 0.3
        6 * 90 / 720,  # 0.75
        2 * 90 / 900,  # 0.2
        0 * 90 / 900   # 0.0
    ], index=sample_player_data.index)
    
    pd.testing.assert_series_equal(result, expected)

def test_calculate_goal_contributions(sample_player_data):
    """Test goal contributions calculation."""
    result = calculate_goal_contributions(sample_player_data)
    
    # Expected values: goals + assists
    expected = pd.Series([
        8 + 3,  # 11
        4 + 6,  # 10
        1 + 2,  # 3
        0 + 0   # 0
    ], index=sample_player_data.index)
    
    pd.testing.assert_series_equal(result, expected)

def test_calculate_shot_accuracy(sample_player_data):
    """Test shot accuracy calculation."""
    result = calculate_shot_accuracy(sample_player_data)
    
    # Expected values: shots_on_goal / shots
    expected = pd.Series([
        15 / 20,  # 0.75
        10 / 15,  # 0.667
        2 / 5,    # 0.4
        np.nan    # NaN (0/0)
    ], index=sample_player_data.index)
    
    pd.testing.assert_series_equal(result, expected, check_dtype=False)

def test_calculate_conversion_rate(sample_player_data):
    """Test conversion rate calculation."""
    result = calculate_conversion_rate(sample_player_data)
    
    # Expected values: goals / shots
    expected = pd.Series([
        8 / 20,   # 0.4
        4 / 15,   # 0.267
        1 / 5,    # 0.2
        np.nan    # NaN (0/0)
    ], index=sample_player_data.index)
    
    pd.testing.assert_series_equal(result, expected, check_dtype=False)

def test_compare_players(sample_player_data):
    """Test the compare_players function with multiple metrics."""
    metrics = ['goals_per_90', 'assists_per_90', 'shot_accuracy']
    result = compare_players(sample_player_data, metrics)
    
    # Check that the result has the correct columns
    assert list(result.columns) == metrics
    
    # Check that the result has the correct number of rows
    assert len(result) == len(sample_player_data)

def test_handle_zero_division(sample_player_data):
    """Test that functions handle division by zero gracefully."""
    # Create a player with zero minutes
    sample_player_data.loc[4] = ['P5', 'Zero', 'Minutes', 'Team C', 'F', 0, 0, 2, 1, 5, 3, 0, 0, 0, 0]
    
    # Test goals per 90
    goals_per_90 = calculate_goals_per_90(sample_player_data)
    assert np.isnan(goals_per_90.iloc[4])
    
    # Test assists per 90
    assists_per_90 = calculate_assists_per_90(sample_player_data)
    assert np.isnan(assists_per_90.iloc[4])