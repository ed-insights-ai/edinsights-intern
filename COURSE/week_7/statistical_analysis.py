"""
CHALLENGE: Statistical Analysis of Soccer Data

Your task is to perform statistical analysis on soccer player and team data.
You'll apply statistical methods to uncover patterns, test hypotheses, and draw conclusions.

The challenge includes:
1. Calculating descriptive statistics for player and team performance
2. Implementing hypothesis testing to compare groups
3. Analyzing distributions of various soccer metrics
4. Identifying correlations between different performance indicators
5. Drawing statistical conclusions to inform decision making

REQUIREMENTS:
- Use appropriate statistical methods for each analysis
- Implement proper hypothesis testing
- Handle statistical assumptions correctly
- Visualize distributions and relationships
- Document your process and interpretations
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from typing import List, Dict, Tuple, Optional, Union
import seaborn as sns


def calculate_descriptive_stats(data: np.ndarray, metric_name: str) -> Dict[str, float]:
    """
    Calculate descriptive statistics for a given metric.
    
    Args:
        data: NumPy array of values for the metric
        metric_name: Name of the metric being analyzed
        
    Returns:
        Dictionary of descriptive statistics
    """
    # TODO: Implement this function to calculate descriptive statistics
    # Include metrics like:
    # - Mean, median, mode
    # - Standard deviation, variance
    # - Min, max, range
    # - Quartiles, IQR
    # - Skewness, kurtosis
    pass


def plot_distribution(data: np.ndarray, metric_name: str, bins: int = 20) -> None:
    """
    Plot the distribution of a metric with appropriate overlay.
    
    Args:
        data: NumPy array of values for the metric
        metric_name: Name of the metric being plotted
        bins: Number of bins for the histogram
    """
    # TODO: Implement this function to visualize distributions
    # Consider including:
    # - Histogram
    # - Kernel density estimate
    # - Normal distribution overlay (if appropriate)
    # - Key statistics in the plot
    pass


def independent_t_test(group1: np.ndarray, group2: np.ndarray, 
                      metric_name: str) -> Dict[str, float]:
    """
    Perform an independent samples t-test to compare two groups.
    
    Args:
        group1: NumPy array of values for the first group
        group2: NumPy array of values for the second group
        metric_name: Name of the metric being compared
        
    Returns:
        Dictionary with t-statistic, p-value, degrees of freedom, and interpretation
    """
    # TODO: Implement this function to perform an independent t-test
    # Make sure to check assumptions and document the process
    pass


def paired_t_test(pre_values: np.ndarray, post_values: np.ndarray, 
                 metric_name: str) -> Dict[str, float]:
    """
    Perform a paired samples t-test to compare pre and post measurements.
    
    Args:
        pre_values: NumPy array of pre-measurement values
        post_values: NumPy array of post-measurement values
        metric_name: Name of the metric being compared
        
    Returns:
        Dictionary with t-statistic, p-value, degrees of freedom, and interpretation
    """
    # TODO: Implement this function to perform a paired t-test
    # Make sure to check assumptions and document the process
    pass


def anova_test(groups: List[np.ndarray], group_names: List[str], 
              metric_name: str) -> Dict[str, float]:
    """
    Perform a one-way ANOVA to compare multiple groups.
    
    Args:
        groups: List of NumPy arrays for each group
        group_names: List of names for each group
        metric_name: Name of the metric being compared
        
    Returns:
        Dictionary with F-statistic, p-value, and interpretation
    """
    # TODO: Implement this function to perform one-way ANOVA
    # Make sure to check assumptions and document the process
    pass


def correlation_analysis(data: pd.DataFrame, 
                        metrics: List[str]) -> pd.DataFrame:
    """
    Perform correlation analysis between multiple metrics.
    
    Args:
        data: Pandas DataFrame containing the metrics
        metrics: List of metric names to analyze
        
    Returns:
        Pandas DataFrame of correlation coefficients
    """
    # TODO: Implement this function to calculate correlations
    # Use Pearson's correlation coefficient or other appropriate measures
    pass


def plot_correlation_matrix(correlation_matrix: pd.DataFrame) -> None:
    """
    Plot a heatmap of the correlation matrix.
    
    Args:
        correlation_matrix: Pandas DataFrame of correlation coefficients
    """
    # TODO: Implement this function to visualize the correlation matrix
    # Create a clear and interpretable heatmap
    pass


def chi_square_test(observed: np.ndarray, expected: np.ndarray) -> Dict[str, float]:
    """
    Perform a chi-square test to compare observed and expected frequencies.
    
    Args:
        observed: NumPy array of observed frequencies
        expected: NumPy array of expected frequencies
        
    Returns:
        Dictionary with chi-square statistic, p-value, and interpretation
    """
    # TODO: Implement this function to perform a chi-square test
    # Make sure to check assumptions and document the process
    pass


def mann_whitney_test(group1: np.ndarray, group2: np.ndarray, 
                     metric_name: str) -> Dict[str, float]:
    """
    Perform a Mann-Whitney U test for non-parametric comparison of two groups.
    
    Args:
        group1: NumPy array of values for the first group
        group2: NumPy array of values for the second group
        metric_name: Name of the metric being compared
        
    Returns:
        Dictionary with U-statistic, p-value, and interpretation
    """
    # TODO: Implement this function to perform a Mann-Whitney U test
    # Use this for non-parametric comparisons when t-test assumptions are violated
    pass


def regression_analysis(x: np.ndarray, y: np.ndarray, 
                       x_name: str, y_name: str) -> Dict[str, float]:
    """
    Perform simple linear regression analysis.
    
    Args:
        x: NumPy array of independent variable values
        y: NumPy array of dependent variable values
        x_name: Name of the independent variable
        y_name: Name of the dependent variable
        
    Returns:
        Dictionary with regression statistics
    """
    # TODO: Implement this function to perform regression analysis
    # Include slope, intercept, r-squared, p-value, and standard error
    pass


def plot_regression(x: np.ndarray, y: np.ndarray, 
                   x_name: str, y_name: str, stats_dict: Dict[str, float]) -> None:
    """
    Plot the regression line with the data points and confidence interval.
    
    Args:
        x: NumPy array of independent variable values
        y: NumPy array of dependent variable values
        x_name: Name of the independent variable
        y_name: Name of the dependent variable
        stats_dict: Dictionary of regression statistics
    """
    # TODO: Implement this function to visualize the regression analysis
    # Include the scatter plot, regression line, and confidence interval
    pass


def calculate_effect_size(group1: np.ndarray, group2: np.ndarray) -> Dict[str, float]:
    """
    Calculate effect size measures for the difference between two groups.
    
    Args:
        group1: NumPy array of values for the first group
        group2: NumPy array of values for the second group
        
    Returns:
        Dictionary with various effect size measures
    """
    # TODO: Implement this function to calculate effect sizes
    # Include Cohen's d, Hedge's g, and common language effect size
    pass


def bootstrap_confidence_interval(data: np.ndarray, statistic_func: callable, 
                                 confidence: float = 0.95, 
                                 n_iterations: int = 1000) -> Tuple[float, float]:
    """
    Calculate bootstrap confidence interval for a statistic.
    
    Args:
        data: NumPy array of data values
        statistic_func: Function to calculate the desired statistic
        confidence: Confidence level (default: 0.95)
        n_iterations: Number of bootstrap iterations
        
    Returns:
        Tuple of (lower_bound, upper_bound) for the confidence interval
    """
    # TODO: Implement this function to calculate bootstrap confidence intervals
    # Use resampling with replacement to estimate the sampling distribution
    pass


def main():
    """
    Main function to demonstrate statistical analysis capabilities.
    """
    # Generate some sample data for demonstration
    np.random.seed(42)  # For reproducibility
    
    # Player statistics for two teams
    num_players_per_team = 25
    
    # Team A players
    team_a_goals = np.random.poisson(8, num_players_per_team)
    team_a_assists = np.random.poisson(5, num_players_per_team)
    team_a_shots = team_a_goals * np.random.randint(3, 8, num_players_per_team)
    team_a_passes = np.random.normal(300, 50, num_players_per_team).astype(int)
    team_a_minutes = np.random.normal(1800, 300, num_players_per_team).astype(int)
    
    # Team B players
    team_b_goals = np.random.poisson(6, num_players_per_team)
    team_b_assists = np.random.poisson(7, num_players_per_team)
    team_b_shots = team_b_goals * np.random.randint(4, 9, num_players_per_team)
    team_b_passes = np.random.normal(350, 40, num_players_per_team).astype(int)
    team_b_minutes = np.random.normal(1700, 250, num_players_per_team).astype(int)
    
    # Player positions (categorical data)
    positions = ['Forward', 'Midfielder', 'Defender', 'Goalkeeper']
    position_probabilities = [0.2, 0.4, 0.3, 0.1]  # Probability for each position
    
    team_a_positions = np.random.choice(positions, num_players_per_team, p=position_probabilities)
    team_b_positions = np.random.choice(positions, num_players_per_team, p=position_probabilities)
    
    # Create DataFrames for easier analysis
    team_a_df = pd.DataFrame({
        'team': ['Team A'] * num_players_per_team,
        'goals': team_a_goals,
        'assists': team_a_assists,
        'shots': team_a_shots,
        'passes': team_a_passes,
        'minutes': team_a_minutes,
        'position': team_a_positions
    })
    
    team_b_df = pd.DataFrame({
        'team': ['Team B'] * num_players_per_team,
        'goals': team_b_goals,
        'assists': team_b_assists,
        'shots': team_b_shots,
        'passes': team_b_passes,
        'minutes': team_b_minutes,
        'position': team_b_positions
    })
    
    # Combine the DataFrames
    all_players_df = pd.concat([team_a_df, team_b_df], ignore_index=True)
    
    # Add some calculated metrics
    all_players_df['goals_per_90'] = all_players_df['goals'] * 90 / all_players_df['minutes']
    all_players_df['assists_per_90'] = all_players_df['assists'] * 90 / all_players_df['minutes']
    all_players_df['shot_conversion'] = all_players_df['goals'] / all_players_df['shots']
    
    # Pre and post training data (for paired tests)
    pre_training_performance = np.random.normal(0.65, 0.1, 20)
    post_training_performance = pre_training_performance + np.random.normal(0.05, 0.03, 20)
    
    # TODO: Implement your analysis workflow here
    # Use the functions you've implemented to analyze the data
    # Example workflow:
    # 1. Calculate descriptive statistics for key metrics
    # 2. Plot distributions of important variables
    # 3. Compare teams using hypothesis tests
    # 4. Analyze correlations between metrics
    # 5. Perform regression analysis for predictive relationships
    # 6. Calculate confidence intervals for key statistics
    
    print("Statistical analysis completed!")


if __name__ == "__main__":
    main()