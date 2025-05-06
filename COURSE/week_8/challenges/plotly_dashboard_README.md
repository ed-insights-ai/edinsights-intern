# Interactive Plotly Dashboards Challenge

## Overview
Welcome to the Interactive Plotly Dashboards challenge! In this assignment, you'll learn how to create interactive, web-based visualizations using Plotly, one of the most powerful data visualization libraries for Python. Unlike static plots created with Matplotlib or Seaborn, Plotly visualizations allow users to interact with the data through hovering, zooming, panning, and filtering, making them ideal for exploratory data analysis and building dashboards.

## Learning Objectives
- Create interactive web-based visualizations with Plotly
- Build multi-panel dashboards for comprehensive data analysis
- Implement user controls like dropdowns, sliders, and buttons
- Design animated visualizations to show changes over time
- Develop statistical visualizations for soccer analytics
- Create specialized plots for soccer data exploration
- Build a comprehensive soccer analytics dashboard

## NCAA Soccer Application
Interactive visualizations are essential for modern sports analytics platforms. In NCAA Division II soccer analysis:
- Coaches can explore player performance metrics interactively to make tactical decisions
- Scouts can filter and compare players across multiple dimensions
- Analysts can spot trends and patterns that might not be visible in static visualizations
- Teams can build comprehensive dashboards to monitor performance over a season
- Fans can engage with interactive content that lets them explore the data themselves

## Conceptual Background

### Plotly Basics
Plotly has two main interfaces in Python:
1. **Plotly Express (px)**: High-level API for creating common visualizations with minimal code
2. **Plotly Graph Objects (go)**: Lower-level API for building highly customized visualizations

The basic workflow for creating Plotly visualizations:
1. Prepare your data (typically in a Pandas DataFrame)
2. Create a figure using Plotly Express or Graph Objects
3. Customize the figure with layout options, hover information, etc.
4. Save or display the figure (as HTML for web display)

### Interactive Features
Plotly visualizations have built-in interactive features:
- **Hover information**: Display detailed data when hovering over elements
- **Zooming and panning**: Focus on specific areas of interest
- **Selection tools**: Select specific data points
- **Export options**: Download the visualization as PNG
- **Legends**: Toggle visibility of data series

### User Controls
You can enhance interactivity by adding controls:
- **Dropdowns**: Select different metrics or categories
- **Sliders**: Filter data by continuous variables
- **Buttons**: Toggle between different views
- **Range selectors**: Filter by a range of values

### Animations
Plotly can create animated visualizations to show:
- Performance changes over a season
- Evolution of team rankings
- Progressive accumulation of statistics
- Changes in player positions and roles

## Challenge Tasks

### Task 1: Basic Interactive Plots
Create fundamental interactive plots using Plotly Express:
- Interactive scatter plots with hover information
- Bar charts with interactive tooltips
- Line plots with zooming capabilities
- Histograms with selectable bins

```python
# Example: Interactive scatter plot of goals vs. assists
fig = px.scatter(
    df, 
    x='goals', 
    y='assists',
    color='position',
    size='games_played',
    hover_name='name',
    hover_data=['team', 'age', 'performance_rating'],
    title='Goals vs. Assists by Position',
    labels={'goals': 'Goals Scored', 'assists': 'Assists'},
    color_discrete_sequence=px.colors.qualitative.G10
)

fig.update_layout(
    xaxis_title='Goals Scored',
    yaxis_title='Assists',
    legend_title='Position',
    width=900,
    height=600
)

# Save as interactive HTML
fig.write_html('plots/goals_vs_assists_interactive.html')
```

### Task 2: Advanced Interactive Plots
Create more sophisticated visualizations using Plotly Graph Objects:
- Customized scatter plots with templates
- Bubble charts with size and color encoding
- Bar charts with advanced styling
- Polar charts for player attributes

```python
# Example: Polar chart for player attributes
# Select a player for demonstration
player = df.iloc[0]

# Create data for radar chart
categories = ['Goals', 'Assists', 'Pass Accuracy', 'Tackles', 'Interceptions']
values = [
    player['goals_per_90'] / df['goals_per_90'].max(),
    player['assists_per_90'] / df['assists_per_90'].max(),
    player['pass_accuracy'] / df['pass_accuracy'].max(),
    player['tackles'] / df['tackles'].max(),
    player['interceptions'] / df['interceptions'].max()
]
# Close the loop for the radar chart
categories = categories + [categories[0]]
values = values + [values[0]]

# Create the radar chart
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values,
    theta=categories,
    fill='toself',
    name=player['name'],
    line_color='crimson'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 1]
        )
    ),
    title=f"Player Attribute Radar: {player['name']} ({player['position']})",
    width=700,
    height=700
)

fig.write_html('plots/player_radar.html')
```

### Task 3: Plots with Dropdowns and Sliders
Enhance visualizations with interactive controls:
- Dropdowns to select different metrics
- Sliders to filter by age or other numeric values
- Buttons to toggle between different views
- Multiple interactive controls on a single visualization

```python
# Example: Scatter plot with dropdown for different metrics
metrics = {
    'Goals per 90': 'goals_per_90',
    'Assists per 90': 'assists_per_90',
    'Shot Accuracy': 'shot_accuracy',
    'Pass Accuracy': 'pass_accuracy'
}

fig = px.scatter(
    df,
    x='age',
    y='goals_per_90',
    color='position',
    size='games_played',
    hover_name='name',
    hover_data=['team'],
    title='Player Metrics by Age',
    labels={'age': 'Age', 'goals_per_90': 'Goals per 90 Minutes'},
)

# Create dropdown buttons for different y-axis metrics
buttons = []
for metric_name, metric_col in metrics.items():
    button = dict(
        method='update',
        label=metric_name,
        args=[
            {'y': [df[metric_col]]},
            {'yaxis.title.text': metric_name}
        ]
    )
    buttons.append(button)

fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=buttons,
            direction='down',
            showactive=True,
            x=0.1,
            y=1.15,
            xanchor='left',
            yanchor='top'
        )
    ]
)

fig.write_html('plots/metrics_by_age_interactive.html')
```

### Task 4: Animated Visualizations
Create animations to show changes over time:
- Animated scatter plots of performance evolution
- Animated bar charts for cumulative statistics
- Animated line charts for performance trends
- Animated bubble charts for multi-dimensional comparison

```python
# Example: Animated bar chart of cumulative goals
fig = px.bar(
    cum_df, 
    x='player_name', 
    y='cum_goals',
    color='player_name',
    animation_frame='game',
    animation_group='player_name',
    title='Cumulative Goals by Game',
    labels={'cum_goals': 'Total Goals', 'player_name': 'Player'},
    range_y=[0, cum_df['cum_goals'].max() * 1.1]
)

fig.update_layout(
    showlegend=False,
    xaxis_title='Player',
    yaxis_title='Cumulative Goals',
    width=800,
    height=500
)

fig.write_html('plots/cumulative_goals_animated.html')
```

### Task 5: Multi-Panel Dashboards
Create comprehensive dashboards with multiple visualizations:
- 2x2 grid of different visualizations
- Subplots of different sizes
- Mix of different plot types
- Synchronized axes for related visualizations

```python
# Example: Dashboard with multiple visualizations
# Create a 2x2 subplot figure
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Goals by Position', 
        'Performance Rating Distribution',
        'Goals vs. Assists', 
        'Age Distribution by Position'
    ),
    specs=[
        [{"type": "bar"}, {"type": "box"}],
        [{"type": "scatter"}, {"type": "histogram"}]
    ]
)

# 1. Bar chart of average goals by position
pos_goals = df.groupby('position')['goals'].mean().reset_index()
fig.add_trace(
    go.Bar(
        x=pos_goals['position'], 
        y=pos_goals['goals'],
        marker_color='royalblue'
    ),
    row=1, col=1
)

# 2. Box plot of performance ratings
fig.add_trace(
    go.Box(
        y=df['performance_rating'],
        x=df['position'],
        marker_color='indianred'
    ),
    row=1, col=2
)

# 3. Scatter plot of goals vs. assists
fig.add_trace(
    go.Scatter(
        x=df['goals'],
        y=df['assists'],
        mode='markers',
        marker=dict(
            size=10,
            color=df['performance_rating'],
            colorscale='Viridis',
            showscale=True
        ),
        text=df['name'],
        hoverinfo='text+x+y'
    ),
    row=2, col=1
)

# 4. Histogram of age by position
for position in df['position'].unique():
    fig.add_trace(
        go.Histogram(
            x=df[df['position'] == position]['age'],
            name=position,
            opacity=0.7,
            nbinsx=15
        ),
        row=2, col=2
    )

# Update layout
fig.update_layout(
    height=800,
    width=1000,
    title_text='Soccer Player Dashboard',
    showlegend=False
)

fig.write_html('plots/player_dashboard.html')
```

### Task 6: Statistical Visualizations
Create interactive statistical visualizations:
- Box plots for comparing distributions
- Violin plots for distribution shapes
- Density plots for multiple distributions
- Correlation plots with regression lines

### Task 7: Specialized Visualizations
Create specialized plot types:
- Heatmaps for correlation matrices
- 3D visualizations for multi-dimensional analysis
- Radar/spider charts for player comparison
- Sunburst or treemap charts for hierarchical data

### Task 8: Soccer Dashboard
Create a comprehensive soccer analytics dashboard:
- Player performance by position
- Team comparison dashboard
- Player comparison tool
- Match analysis dashboard

## Hints and Tips

1. **Start Simple**: Begin with basic interactive plots before moving to more complex visualizations.

2. **Use Templates**: Plotly provides templates to quickly style your visualizations:
   ```python
   fig.update_layout(template='plotly_dark')  # Other options: 'plotly', 'plotly_white', 'ggplot2', etc.
   ```

3. **Custom Hover Information**: Customize what appears when users hover over data points:
   ```python
   fig.update_traces(
       hovertemplate='<b>%{hovertext}</b><br>Goals: %{x}<br>Assists: %{y}<br>Team: %{customdata[0]}<extra></extra>',
       hovertext=df['name'],
       customdata=df[['team']]
   )
   ```

4. **Layout Optimization**: Ensure your visualizations are properly sized and labeled:
   ```python
   fig.update_layout(
       title={'text': 'My Title', 'x': 0.5, 'xanchor': 'center'},
       margin=dict(l=40, r=40, t=50, b=40)
   )
   ```

5. **Color Scales**: Choose appropriate color scales for your data:
   ```python
   # Sequential for continuous data
   fig.update_traces(marker_colorscale='Viridis')
   
   # Diverging for data with a meaningful midpoint
   fig.update_traces(marker_colorscale='RdBu')
   
   # Qualitative for categorical data
   fig.update_traces(marker_color=px.colors.qualitative.Plotly)
   ```

6. **Responsiveness**: Make dashboards responsive for different screen sizes:
   ```python
   fig.update_layout(
       autosize=True,
       width=None,
       height=None
   )
   ```

7. **Animation Controls**: Customize animation settings:
   ```python
   fig.update_layout(
       updatemenus=[{
           'type': 'buttons',
           'buttons': [
               dict(label='Play', method='animate', args=[None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}]),
               dict(label='Pause', method='animate', args=[[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate'}])
           ]
       }]
   )
   ```

8. **Performance**: For large datasets, consider using WebGL rendering:
   ```python
   fig = px.scatter(df, x='x', y='y', render_mode='webgl')
   ```

## Extension Opportunities

1. **Dashboard Integration**: Integrate your Plotly visualizations into the Flask dashboard in the PROJECT directory.

2. **Custom Controls**: Create custom control panels for filtering and comparing players.

3. **Match Timeline**: Create an animated timeline of match events.

4. **Player Comparison Tool**: Build an interactive tool for comparing multiple players across various metrics.

5. **Team Formation Visualization**: Visualize team formations and player positions on a soccer pitch.

## Resources

- [Plotly Python Documentation](https://plotly.com/python/)
- [Plotly Express Walkthrough](https://plotly.com/python/plotly-express/)
- [Plotly Graph Objects Reference](https://plotly.com/python/graph-objects/)
- [Interactive Controls Tutorial](https://plotly.com/python/dropdowns/)
- [Animation Tutorial](https://plotly.com/python/animations/)
- [Subplot Guide](https://plotly.com/python/subplots/)
- [Soccer Analytics with Plotly](https://towardsdatascience.com/advanced-sports-visualization-with-plotly-93e412510c48)

## Submission

Complete the implementation of the functions in `plotly_dashboard.py`. When you run the script, it should generate a series of interactive HTML visualizations in the 'plots' directory.