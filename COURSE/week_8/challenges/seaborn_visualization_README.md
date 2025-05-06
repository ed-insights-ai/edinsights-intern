# Challenge 2: Seaborn Statistical Visualization for Soccer Analytics

**Difficulty: ⭐⭐⭐☆☆**

## Challenge Overview

In this challenge, you'll use Seaborn to create statistical visualizations that reveal patterns and relationships in soccer player and team data. Seaborn's statistical plotting capabilities will help you uncover insights about performance distributions, relationships between metrics, and group comparisons that are essential for advanced soccer analytics.

## Learning Objectives

- Create distribution visualizations to understand the spread of soccer metrics
- Build categorical plots to compare performance across positions and teams
- Implement relationship plots to identify correlations between performance metrics
- Design matrix plots to visualize complex relationships and clustering
- Apply advanced styling techniques to create polished visualizations
- Develop multi-panel statistical dashboards for comprehensive analysis

## Real-World Context

NCAA soccer analysts need to understand the statistical properties of player and team performance metrics to identify strengths, weaknesses, and patterns. Distributions reveal the range and frequency of performance levels, while relationship plots help identify which metrics are predictive of success. Statistical visualizations allow coaches and scouts to make data-driven decisions about player development, tactical approaches, and recruitment by providing a solid statistical foundation for their analysis.

## Challenge Details

### The Task

Work through the tasks in `seaborn_visualization.py` to create statistical visualizations using the provided soccer player data. You'll implement the following:

1. Distribution plots to visualize the spread of performance metrics
2. Categorical plots to compare metrics across positions and teams
3. Relationship plots to identify correlations between metrics
4. Matrix and grid plots for multi-dimensional analysis
5. Advanced styling techniques to create professional visualizations
6. Complex figures combining multiple visualization types
7. Statistical analysis visualizations showing significance and confidence intervals
8. Soccer-specific visualizations tailored to performance analysis

### Visualization Workflow

```
+-------------------------+
| Define Analysis Question|
+-------------------------+
           |
           v
+-------------------------+
| Choose Visualization    |
| Type Based on Question  |
+-------------------------+
           |
           v
+-------------------------+
| Prepare and Transform   |
| Data as Needed          |
+-------------------------+
           |
           v
+-------------------------+
| Create Basic Plot       |
+-------------------------+
           |
           v
+-------------------------+
| Add Statistical Elements|
| (CI, Regression, etc.)  |
+-------------------------+
           |
           v
+-------------------------+
| Apply Styling and Theme |
+-------------------------+
           |
           v
+-------------------------+
| Add Context and Labels  |
+-------------------------+
           |
           v
+-------------------------+
| Save Visualization      |
+-------------------------+
```

## Tips and Hints

### Distribution Plots

Visualize the distribution of performance metrics with various plot types:

```python
# Histogram with KDE curve
plt.figure(figsize=(10, 6))
sns.histplot(df['goals_per_90'].dropna(), kde=True, color='navy')
plt.title('Distribution of Goals per 90 Minutes')
plt.xlabel('Goals per 90 Minutes')
plt.ylabel('Number of Players')
plt.savefig('plots/goals_per_90_dist.png', dpi=300)

# Box plot by position
plt.figure(figsize=(12, 6))
sns.boxplot(x='position', y='goals_per_90', data=df, palette='Set2')
plt.title('Goals per 90 Minutes by Position')
plt.xlabel('Position')
plt.ylabel('Goals per 90 Minutes')
plt.savefig('plots/goals_per_90_by_position.png', dpi=300)

# Violin plot for more detailed distribution
plt.figure(figsize=(12, 6))
sns.violinplot(x='position', y='performance_rating', data=df, palette='Set3', inner='quartile')
plt.title('Performance Rating Distribution by Position')
plt.xlabel('Position')
plt.ylabel('Performance Rating')
plt.savefig('plots/performance_by_position_violin.png', dpi=300)

# Strip plot with jittered points
plt.figure(figsize=(12, 6))
sns.stripplot(x='position', y='goals_per_90', data=df, jitter=True, palette='deep')
plt.title('Individual Player Goals per 90 Minutes by Position')
plt.xlabel('Position')
plt.ylabel('Goals per 90 Minutes')
plt.savefig('plots/individual_goals_by_position.png', dpi=300)
```

### Categorical Plots

Compare metrics across categories like position and team:

```python
# Bar plot showing mean statistic by position
plt.figure(figsize=(12, 6))
sns.barplot(x='position', y='pass_accuracy', data=df, palette='viridis')
plt.title('Average Pass Accuracy by Position')
plt.xlabel('Position')
plt.ylabel('Pass Accuracy')
plt.savefig('plots/pass_accuracy_by_position.png', dpi=300)

# Count plot showing the number of players in each position
plt.figure(figsize=(10, 6))
sns.countplot(x='position', data=df, palette='Set1')
plt.title('Number of Players by Position')
plt.xlabel('Position')
plt.ylabel('Count')
plt.savefig('plots/player_count_by_position.png', dpi=300)

# Box plot with multiple categories (position and team)
plt.figure(figsize=(14, 8))
sns.boxplot(x='position', y='goals_per_90', hue='team', data=df, palette='pastel')
plt.title('Goals per 90 Minutes by Position and Team')
plt.xlabel('Position')
plt.ylabel('Goals per 90 Minutes')
plt.legend(title='Team')
plt.savefig('plots/goals_per_90_by_position_team.png', dpi=300)

# Point plot with error bars
plt.figure(figsize=(12, 6))
sns.pointplot(x='position', y='performance_rating', hue='team', data=df, palette='dark', markers=['o', 's', 'D', '^', '*'])
plt.title('Average Performance Rating by Position and Team')
plt.xlabel('Position')
plt.ylabel('Performance Rating')
plt.legend(title='Team')
plt.savefig('plots/performance_by_position_team.png', dpi=300)
```

### Relationship Plots

Identify correlations and relationships between performance metrics:

```python
# Scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='shots', y='goals', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relationship Between Shots and Goals')
plt.xlabel('Total Shots')
plt.ylabel('Total Goals')
plt.savefig('plots/shots_goals_regression.png', dpi=300)

# Joint plot showing marginal distributions
joint_plot = sns.jointplot(x='shots', y='goals', data=df, kind='reg', height=8, ratio=5, 
                          marginal_kws={'color': 'navy'}, scatter_kws={'alpha': 0.6})
joint_plot.fig.suptitle('Joint Distribution of Shots and Goals', y=1.05, fontsize=16)
joint_plot.savefig('plots/shots_goals_joint.png', dpi=300)

# Pair plot to visualize relationships between multiple variables
metrics = ['goals', 'assists', 'shots', 'pass_accuracy', 'performance_rating']
pair_plot = sns.pairplot(df[metrics + ['position']], hue='position', palette='Set2', 
                       height=2.5, plot_kws={'alpha': 0.6})
pair_plot.fig.suptitle('Relationships Between Key Performance Metrics', y=1.02, fontsize=16)
pair_plot.savefig('plots/performance_metrics_pairplot.png', dpi=300)

# Residual plot to check regression assumptions
plt.figure(figsize=(10, 6))
sns.residplot(x='shots', y='goals', data=df, lowess=True, color='navy')
plt.title('Residual Plot for Shots vs. Goals')
plt.xlabel('Shots')
plt.ylabel('Residuals')
plt.savefig('plots/shots_goals_residuals.png', dpi=300)
```

### Matrix and Grid Plots

Create complex visualizations for multi-dimensional analysis:

```python
# Correlation heatmap
plt.figure(figsize=(12, 10))
metrics = ['goals', 'assists', 'shots', 'shots_on_goal', 'pass_accuracy', 
           'tackles', 'interceptions', 'yellow_cards', 'performance_rating']
corr = df[metrics].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))  # Mask for upper triangle
sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt='.2f', square=True, 
           linewidths=0.5, cbar_kws={'shrink': 0.8})
plt.title('Correlation Matrix of Performance Metrics')
plt.tight_layout()
plt.savefig('plots/correlation_heatmap.png', dpi=300)

# Clustermap for hierarchical clustering
plt.figure(figsize=(12, 10))
cluster = sns.clustermap(df[metrics].corr(), cmap='viridis', annot=True, fmt='.2f',
                       linewidths=0.5, figsize=(12, 12))
plt.title('Hierarchical Clustering of Performance Metrics')
plt.savefig('plots/metrics_clustermap.png', dpi=300)

# Facet grid to show relationships conditional on categories
g = sns.FacetGrid(df, col='position', height=4, aspect=1.2)
g.map_dataframe(sns.scatterplot, x='shots', y='goals')
g.add_legend()
g.set_axis_labels('Shots', 'Goals')
g.set_titles('{col_name}')
g.fig.suptitle('Shots vs. Goals by Position', y=1.05, fontsize=16)
plt.savefig('plots/shots_goals_by_position.png', dpi=300)

# Pair grid with custom plot types
g = sns.PairGrid(df, vars=metrics[:4], hue='position', palette='Set2', height=2.5)
g.map_diag(sns.kdeplot)
g.map_upper(sns.scatterplot, alpha=0.6)
g.map_lower(sns.regplot, scatter_kws={'alpha': 0.6})
g.add_legend()
g.fig.suptitle('Custom Pair Grid of Performance Metrics', y=1.02, fontsize=16)
plt.savefig('plots/custom_pair_grid.png', dpi=300)
```

### Statistical Visualization

Create visualizations that incorporate statistical analysis:

```python
# Plot showing confidence intervals
plt.figure(figsize=(12, 6))
sns.barplot(x='position', y='performance_rating', data=df, capsize=0.2, errorbar=('ci', 95), palette='Blues_d')
plt.title('Average Performance Rating by Position (with 95% CI)')
plt.xlabel('Position')
plt.ylabel('Performance Rating')
plt.savefig('plots/performance_ci_by_position.png', dpi=300)

# Plot for group comparison with statistical significance
# For simplicity, we'll create two groups for comparison
forwards = df[df['position'] == 'F']['goals_per_90'].dropna()
midfielders = df[df['position'] == 'MF']['goals_per_90'].dropna()

plt.figure(figsize=(10, 6))
# Plot distributions
sns.histplot(forwards, color='red', alpha=0.5, label='Forwards', kde=True)
sns.histplot(midfielders, color='blue', alpha=0.5, label='Midfielders', kde=True)

# Perform t-test and add result annotation
from scipy import stats
t_stat, p_val = stats.ttest_ind(forwards, midfielders, equal_var=False)
sig_text = f"T-test: t={t_stat:.2f}, p={p_val:.4f}" + ("*" if p_val < 0.05 else "")
plt.text(0.95, 0.95, sig_text, transform=plt.gca().transAxes, 
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.title('Goals per 90 Minutes: Forwards vs. Midfielders')
plt.xlabel('Goals per 90 Minutes')
plt.ylabel('Count')
plt.legend()
plt.savefig('plots/forwards_vs_midfielders_goals.png', dpi=300)
```

## Testing Your Solution

Your solution should:

1. Create all the required plots for each task
2. Apply appropriate statistical visualizations based on the data type
3. Include proper styling, themes, and color palettes
4. Correctly handle categorical and numerical variables
5. Incorporate statistical elements like confidence intervals where appropriate
6. Save all visualizations to the 'plots' directory

Consider these questions:
- Do your visualizations clearly show the distributions of key metrics?
- Are relationships between metrics effectively illustrated?
- Do your plots allow for easy comparison between different groups?
- Are your visualizations appropriately styled and labeled?
- Do the statistical elements add meaningful context to the data?

## Application to Capstone

The Seaborn visualization skills you develop in this challenge will be valuable for your capstone project in several ways:

1. Creating statistically rigorous visualizations to support analytical findings
2. Comparing performance distributions across positions, teams, and other categories
3. Identifying correlations between metrics that could inform player evaluation
4. Building statistical dashboards that communicate complex relationships clearly
5. Developing a visual style that makes your analytics dashboard informative and professional

These statistical visualization techniques will help you move beyond basic descriptive statistics to more sophisticated analytical insights in your NCAA soccer analytics capstone project.

## Resources

- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Statistical Data Visualization](https://seaborn.pydata.org/tutorial/statistical_visualization.html)
- [Categorical Data Visualization](https://seaborn.pydata.org/tutorial/categorical.html)
- [Visualizing Regression Models](https://seaborn.pydata.org/tutorial/regression.html)
- [The Python Graph Gallery](https://python-graph-gallery.com/)