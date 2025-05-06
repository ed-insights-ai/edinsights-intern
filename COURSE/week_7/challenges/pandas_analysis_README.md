# Challenge 1: Soccer Data Analysis with Pandas

**Difficulty: ⭐⭐⭐☆☆**

## Challenge Overview

In this challenge, you'll use Pandas to analyze soccer player and team data. You'll clean, transform, and analyze the data to extract meaningful insights that could be valuable for coaches, scouts, and analysts working with NCAA soccer programs.

## Learning Objectives

- Master data cleaning and preprocessing techniques for sports statistics
- Implement data transformation operations for soccer analytics
- Create aggregations and calculations for performance metrics
- Merge and join different datasets for comprehensive analysis
- Extract actionable insights from soccer data

## Real-World Context

Soccer analysts at NCAA programs need to process large amounts of raw data from various sources to identify patterns, evaluate player performance, and inform strategic decisions. Pandas provides the tools to efficiently manipulate this data, calculate metrics that aren't directly available in the raw statistics, and present insights in a format that coaches and scouts can use to make decisions about recruitment, training focus, and game tactics.

## Challenge Details

### The Task

You'll work with several soccer datasets including player statistics, team performance, and match results. Your tasks include:

1. Loading and cleaning messy soccer data
2. Transforming and aggregating player statistics
3. Joining multiple datasets for comprehensive analysis
4. Calculating player performance metrics
5. Analyzing team and player trends

### Data Analysis Workflow

```
+--------------------+
| Load Player Data   |
+--------------------+
         |
         v
+--------------------+
| Clean Player Data  |
+--------------------+
         |
         v
+--------------------+
| Calculate Metrics  |
+--------------------+
         |
         v
+--------------------+    +--------------------+
| Load Team Data     |--->| Merge Data        |
+--------------------+    +--------------------+
                                   |
                                   v
                          +--------------------+
                          | Aggregate Stats    |
                          +--------------------+
                                   |
                                   v
                          +--------------------+
                          | Analyze Performance|
                          +--------------------+
                                   |
                                   v
                          +--------------------+
                          | Generate Report    |
                          +--------------------+
```

## Tips and Hints

### Data Cleaning

When cleaning soccer data, focus on:

```python
# Handle missing values appropriately based on the column
df['goals'] = df['goals'].fillna(0)  # Missing goals likely means 0
df['assists'] = df['assists'].fillna(0)  # Missing assists likely means 0

# Fix data types
df['minutes_played'] = df['minutes_played'].astype(int)
df['jersey_number'] = df['jersey_number'].astype('Int64')  # Int64 allows for NaN values

# Handle outliers
# For example, replace negative values with NaN or reasonable values
df['age'] = df['age'].apply(lambda x: x if 15 <= x <= 40 else np.nan)

# Remove duplicates
df = df.drop_duplicates(subset=['player_id', 'match_id'])
```

### Calculating Performance Metrics

Common soccer performance metrics include:

```python
# Goals per 90 minutes
df['goals_per_90'] = df['goals'] * 90 / df['minutes_played']

# Shot conversion rate
df['shot_conversion'] = df['goals'] / df['shots']

# Expected goals difference (actual goals vs. expected)
df['xg_difference'] = df['goals'] - df['expected_goals']

# Passes per minute
df['passes_per_minute'] = df['total_passes'] / df['minutes_played']

# Tackle success rate
df['tackle_success_rate'] = df['successful_tackles'] / df['tackle_attempts']
```

### Merging Data

When working with multiple soccer datasets:

```python
# Merge player and team data
merged_df = pd.merge(
    player_df,
    team_df,
    on='team_id',
    how='left'
)

# Add match data for more context
player_match_df = pd.merge(
    player_stats_df,
    match_df,
    on='match_id',
    how='left'
)
```

### Aggregation

Aggregating soccer data helps identify patterns:

```python
# Aggregate player stats by position
position_stats = player_df.groupby('position').agg({
    'goals': 'sum',
    'assists': 'sum',
    'minutes_played': 'sum',
    'shots': 'sum',
    'goals_per_90': 'mean',
    'shot_conversion': 'mean'
}).reset_index()

# Aggregate team performance by season
team_season_stats = match_df.groupby(['team_id', 'season']).agg({
    'goals_for': 'sum',
    'goals_against': 'sum',
    'wins': 'sum',
    'losses': 'sum',
    'draws': 'sum'
}).reset_index()

# Calculate points based on wins, draws, losses
team_season_stats['points'] = team_season_stats['wins'] * 3 + team_season_stats['draws']
```

### Identifying Top Performers

Finding top performers based on various metrics:

```python
# Top goal scorers
top_scorers = player_df.sort_values('goals', ascending=False).head(10)

# Players with best shot conversion
top_converters = player_df[player_df['shots'] >= 10].sort_values('shot_conversion', ascending=False).head(10)

# Most efficient passers
top_passers = player_df[player_df['minutes_played'] >= 500].sort_values('pass_completion_rate', ascending=False).head(10)
```

## Testing Your Solution

Your solution should:

1. Successfully load and clean the provided data
2. Calculate meaningful performance metrics
3. Merge different datasets correctly
4. Perform insightful aggregations
5. Identify patterns and top performers
6. Generate a comprehensive summary report

Test your code with different scenarios:
- How does it handle missing data?
- Does it identify outliers correctly?
- Are the calculated metrics correct?
- Do the aggregations provide meaningful insights?
- Is the final report clear and informative?

## Application to Capstone

The data analysis techniques you develop in this challenge will be directly applicable to your capstone project, where you'll need to:

1. Process raw NCAA soccer data collected by your scraper
2. Calculate advanced metrics for player evaluation
3. Compare players within and across positions
4. Identify top performers based on various criteria
5. Generate insights that could inform coaching and recruitment decisions

Your capstone's analytics capabilities will rely heavily on the Pandas skills you develop in this challenge, especially when processing large datasets of player statistics from multiple seasons.

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Tutorial](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html)
- [Handling Missing Data in Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)
- [Pandas Merge, Join, and Concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)
- [Pandas Groupby Operations](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)
- [Soccer Analytics with Python](https://towardsdatascience.com/soccer-analytics-with-python-7cb0a8d3c4fa)
- [Football (Soccer) Analytics Guide](https://github.com/devinpleuler/analytics-handbook)