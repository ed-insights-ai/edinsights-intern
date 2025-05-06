# Challenge 1: Matplotlib Fundamentals for Soccer Analytics

**Difficulty: ⭐⭐☆☆☆**

## Challenge Overview

In this challenge, you'll use Matplotlib to create static visualizations of soccer player and team data. You'll learn how to create, customize, and style different types of plots to effectively communicate insights from your soccer analytics data.

## Learning Objectives

- Create basic plot types with Matplotlib (line, bar, scatter, histogram)
- Customize visualizations with labels, titles, colors, and styles
- Design multi-panel figures using subplots
- Implement statistical visualizations for soccer data
- Apply advanced styling and annotation techniques

## Real-World Context

NCAA soccer analysts often need to create clear, informative visualizations to communicate insights to coaches, players, and administrators. Static visualizations in reports and presentations need to be informative, professional, and easy to understand. The ability to create custom, publication-quality plots is essential for translating complex soccer statistics into actionable insights for improving team performance and player development.

## Challenge Details

### The Task

Work through the tasks in `matplotlib_fundamentals.py` to create and customize various types of plots using the provided soccer player data. You'll implement the following:

1. Basic plot types (line, bar, scatter, histogram)
2. Customized visualizations with advanced styling
3. Multi-panel figures with subplots
4. Statistical plots for analyzing distributions
5. Time series visualizations for performance trends
6. 3D plots for multi-dimensional analysis
7. Soccer-specific visualizations for player comparison

### Visualization Workflow

```
+------------------------+
| Load/Generate Data     |
+------------------------+
          |
          v
+--------------------------+
| Explore Data Structure   |
+--------------------------+
          |
          v
+------------------------+
| Choose Plot Type       |
+------------------------+
          |
          v
+------------------------+
| Create Basic Plot      |
+------------------------+
          |
          v
+------------------------+
| Customize Appearance   |
+------------------------+
          |
          v
+------------------------+
| Add Labels & Annotation|
+------------------------+
          |
          v
+------------------------+
| Save Visualization     |
+------------------------+
```

## Tips and Hints

### Basic Plots

Start with the fundamental plot types to visualize different aspects of soccer data:

```python
# Line plot for time series or cumulative statistics
plt.figure(figsize=(10, 6))
plt.plot(games, cumulative_goals, marker='o', linestyle='-', color='blue', linewidth=2)
plt.title('Cumulative Goals Over Time')
plt.xlabel('Games Played')
plt.ylabel('Total Goals')
plt.grid(True)
plt.savefig('plots/cumulative_goals.png', dpi=300, bbox_inches='tight')

# Bar chart for comparing discrete values
plt.figure(figsize=(12, 6))
plt.bar(player_names, goals, color='crimson')
plt.title('Goals by Player')
plt.xlabel('Player')
plt.ylabel('Goals Scored')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('plots/player_goals_bar.png', dpi=300)

# Scatter plot for relationships between variables
plt.figure(figsize=(10, 6))
plt.scatter(shots, goals, alpha=0.7, c=shot_accuracy, cmap='viridis')
plt.colorbar(label='Shot Accuracy')
plt.title('Goals vs. Shots')
plt.xlabel('Total Shots')
plt.ylabel('Total Goals')
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('plots/goals_vs_shots.png', dpi=300)

# Histogram for distributions
plt.figure(figsize=(10, 6))
plt.hist(goals_per_90, bins=15, alpha=0.7, color='navy', edgecolor='black')
plt.title('Distribution of Goals per 90 Minutes')
plt.xlabel('Goals per 90 Minutes')
plt.ylabel('Number of Players')
plt.grid(True, axis='y', alpha=0.3)
plt.savefig('plots/goals_per_90_hist.png', dpi=300)
```

### Multi-Panel Figures

Create more complex visualizations with multiple subplots:

```python
# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# First subplot: Goals distribution
axs[0, 0].hist(df['goals'], bins=10, color='navy', alpha=0.7)
axs[0, 0].set_title('Goals Distribution')
axs[0, 0].set_xlabel('Goals')
axs[0, 0].set_ylabel('Number of Players')

# Second subplot: Assists distribution
axs[0, 1].hist(df['assists'], bins=10, color='crimson', alpha=0.7)
axs[0, 1].set_title('Assists Distribution')
axs[0, 1].set_xlabel('Assists')
axs[0, 1].set_ylabel('Number of Players')

# Third subplot: Goals vs. Assists scatter plot
axs[1, 0].scatter(df['goals'], df['assists'], alpha=0.7, c=df['minutes'], cmap='viridis')
axs[1, 0].set_title('Goals vs. Assists')
axs[1, 0].set_xlabel('Goals')
axs[1, 0].set_ylabel('Assists')

# Fourth subplot: Goals per 90 minutes by position
positions = df['position'].unique()
goals_by_pos = [df[df['position'] == pos]['goals_per_90'].mean() for pos in positions]
axs[1, 1].bar(positions, goals_by_pos, color='green', alpha=0.7)
axs[1, 1].set_title('Avg. Goals per 90 by Position')
axs[1, 1].set_xlabel('Position')
axs[1, 1].set_ylabel('Goals per 90')

# Add a main title to the figure
fig.suptitle('Soccer Player Statistics Overview', fontsize=16)

# Adjust layout and save
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust for the main title
plt.savefig('plots/player_stats_overview.png', dpi=300, bbox_inches='tight')
```

### Statistical Visualization

Implement statistical plots to analyze distributions and comparisons:

```python
# Box plot for comparing distributions by position
plt.figure(figsize=(12, 6))
positions = df['position'].unique()
data = [df[df['position'] == pos]['goals_per_90'].dropna() for pos in positions]
bp = plt.boxplot(data, patch_artist=True, labels=positions)

# Customize box colors
colors = ['lightblue', 'lightgreen', 'salmon', 'khaki']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Goals per 90 Minutes by Position')
plt.ylabel('Goals per 90 Minutes')
plt.xlabel('Position')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.savefig('plots/goals_per_90_by_position_boxplot.png', dpi=300)
```

### Time Series Visualization

Create visualizations for time-based data:

```python
# Line plot with proper date formatting
plt.figure(figsize=(12, 6))
plt.plot(time_series_data['Date'], time_series_data['Player1_Cumulative_Goals'], 
         marker='o', linestyle='-', label='Player 1')
plt.plot(time_series_data['Date'], time_series_data['Player2_Cumulative_Goals'], 
         marker='s', linestyle='--', label='Player 2')
plt.plot(time_series_data['Date'], time_series_data['Player3_Cumulative_Goals'], 
         marker='^', linestyle='-.', label='Player 3')

# Format the date axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
plt.gcf().autofmt_xdate()  # Rotate date labels

plt.title('Cumulative Goals by Player')
plt.xlabel('Match Date')
plt.ylabel('Total Goals')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/cumulative_goals_time_series.png', dpi=300)
```

### Soccer-Specific Plots

Create visualizations tailored to soccer analytics:

```python
# Comparing goals and assists for top players
top_players = df.nlargest(10, 'goals')

plt.figure(figsize=(12, 6))
x = np.arange(len(top_players))
width = 0.35

plt.bar(x - width/2, top_players['goals'], width, label='Goals', color='#1f77b4')
plt.bar(x + width/2, top_players['assists'], width, label='Assists', color='#ff7f0e')

plt.title('Goals and Assists for Top Goal Scorers')
plt.xlabel('Player')
plt.ylabel('Count')
plt.xticks(x, top_players['name'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.savefig('plots/top_scorers_goals_assists.png', dpi=300)
```

## Testing Your Solution

Your solution should:

1. Create all the required plot types
2. Apply proper styling and customization
3. Include clear labels, titles, and annotations
4. Use appropriate color schemes and visual elements
5. Save all visualizations to the 'plots' directory

Try to think about:
- Is each visualization clear and informative?
- Are the plot types appropriate for the data being visualized?
- Do the visualizations effectively communicate patterns and insights?
- Are the plots visually appealing and professional?

## Application to Capstone

The Matplotlib skills you develop in this challenge will be directly applicable to your capstone project in several ways:

1. Creating static visualizations for reports and presentations about NCAA soccer performance
2. Developing custom visualizations tailored to specific soccer metrics and statistics
3. Producing publication-quality figures for documentation and analysis
4. Building the foundation for more complex interactive visualizations in your dashboard

These visualization skills will help you effectively communicate your soccer analytics insights to coaches, players, and other stakeholders, making your capstone project more impactful and user-friendly.

## Resources

- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Customizing Matplotlib](https://matplotlib.org/stable/tutorials/introductory/customizing.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Python for Data Visualization](https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html)
- [Soccer Analytics Visualization Examples](https://www.fcpython.com/blog/introduction-to-visualising-data-football-in-python)
- [Color Maps in Matplotlib](https://matplotlib.org/stable/tutorials/colors/colormaps.html)