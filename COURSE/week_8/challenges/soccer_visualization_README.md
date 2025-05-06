# Soccer Analytics Visualization Challenge

## Overview
Welcome to the Soccer Analytics Visualization Challenge! In this assignment, you'll create specialized visualizations that are specifically designed for soccer analytics. Modern soccer analysis relies heavily on visual representations to communicate complex patterns, spatial information, and performance metrics. These visualizations help coaches, scouts, and analysts make data-driven decisions about tactics, player selection, and recruitment.

## Learning Objectives
- Create soccer-specific visualizations for player and match analysis
- Implement shot maps and pass networks using spatial data
- Design multi-dimensional player comparison tools
- Visualize performance trends and distributions by position
- Build comprehensive player profiles and team dashboards
- Apply soccer analytics concepts to visual analysis

## NCAA Soccer Application
Soccer-specific visualizations are particularly valuable for NCAA Division II soccer analysis:
- Coaches can visualize shot patterns and passing networks to understand team tactics
- Players can identify strengths and areas for improvement through visual player profiles
- Scouts can compare players across multiple dimensions to identify recruitment targets
- Analysts can communicate insights effectively to non-technical stakeholders
- Teams can track performance trends throughout a season with specialized visualizations

## Conceptual Background

### Soccer Analytics Fundamentals
Soccer analytics involves several key visualization types:

1. **Spatial Visualizations**: Show events on a soccer pitch (shots, passes, defensive actions)
2. **Performance Radars**: Compare players across multiple dimensions
3. **Network Diagrams**: Illustrate passing connections between players
4. **Trend Analysis**: Track performance over time (games, seasons)
5. **Position-Specific Analysis**: Compare players within their position groups

### Soccer Pitch Visualizations
The soccer pitch is the fundamental canvas for many soccer visualizations:
- **Standardized Dimensions**: Full-size pitch is typically 105×68 meters
- **Key Areas**: Penalty area, six-yard box, center circle, etc.
- **Coordinate Systems**: Usually (0,0) at bottom-left or top-left, with x/y in meters
- **Orientation**: Can be horizontal or vertical depending on visualization needs

### Key Metrics in Soccer
Soccer analytics focuses on several types of metrics:
- **Scoring Metrics**: Goals, shots, xG (expected goals)
- **Passing Metrics**: Passes completed, pass accuracy, progressive passes
- **Defensive Metrics**: Tackles, interceptions, blocks, clearances
- **Possession Metrics**: Time on ball, territory control
- **Physical Metrics**: Distance covered, sprints, top speed

## Challenge Tasks

### Task 1: Player Performance Radar
Create radar charts that compare players across multiple performance dimensions:

```python
# Example: Create a basic radar chart for a player
# Select metrics for radar chart
metrics = ['goals_per_90', 'assists_per_90', 'pass_accuracy', 
           'tackles', 'interceptions', 'shot_accuracy']

# Select players to compare
player_indices = [0, 10, 20]  # Sample indices
players = df.iloc[player_indices]

# Create figure and polar axis
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Number of metrics
num_metrics = len(metrics)
angles = np.linspace(0, 2*np.pi, num_metrics, endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# Add labels for each metric around the chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels([m.replace('_', ' ').title() for m in metrics], size=12)

# Plot each player
for i, player in players.iterrows():
    # Calculate normalized values (0-1 scale)
    values = []
    for metric in metrics:
        val = player[metric]
        max_val = df[metric].max()
        norm_val = val / max_val if max_val > 0 else 0
        values.append(norm_val)
    
    # Close the loop
    values += values[:1]
    
    # Plot the player's values
    ax.plot(angles, values, linewidth=2, label=player['name'])
    ax.fill(angles, values, alpha=0.1)

# Add legend and title
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title('Player Comparison Radar Chart', size=15)

# Save the figure
plt.tight_layout()
plt.savefig('plots/player_radar_chart.png', dpi=300)
plt.close()
```

### Task 2: Shot Map
Create visualizations showing shot locations and outcomes on a soccer pitch:

```python
# Example: Create a basic shot map using mplsoccer
# Create a pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white',
              stripe=True, stripe_color='#c2d59d')

# Setup the figure
fig, ax = pitch.draw(figsize=(12, 8))

# Extract shot data
shot_x = match_data['shots']['x']
shot_y = match_data['shots']['y']
shot_outcome = match_data['shots']['outcome']
shot_xg = match_data['shots']['xG']

# Plot the shots
for i in range(len(shot_x)):
    # Size based on xG (expected goals)
    size = 1200 * shot_xg[i]
    
    # Color based on outcome (goal or not)
    color = 'red' if shot_outcome[i] == 1 else 'blue'
    
    # Plot the shot
    ax.scatter(shot_x[i], shot_y[i], s=size, color=color, alpha=0.7, 
               edgecolors='black', linewidths=1)

# Add a legend
goal = plt.scatter([], [], s=100, color='red', alpha=0.7, edgecolors='black', label='Goal')
miss = plt.scatter([], [], s=100, color='blue', alpha=0.7, edgecolors='black', label='Miss/Save')
xg_leg = plt.scatter([], [], s=50, color='white', alpha=0.7, edgecolors='black', label='Size = xG')

# Add the legend
ax.legend(handles=[goal, miss, xg_leg], loc='upper right')

# Add title
ax.set_title('Shot Map', fontsize=20)

# Save the figure
plt.tight_layout()
plt.savefig('plots/shot_map.png', dpi=300)
plt.close()
```

### Task 3: Pass Map and Network
Create visualizations showing passing patterns and connections between players:

```python
# Example: Create a basic pass map
# Create a pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white',
              stripe=True, stripe_color='#c2d59d')

# Setup the figure
fig, ax = pitch.draw(figsize=(12, 8))

# Extract pass data
pass_start_x = match_data['passes']['start_x']
pass_start_y = match_data['passes']['start_y']
pass_end_x = match_data['passes']['end_x']
pass_end_y = match_data['passes']['end_y']
pass_outcome = match_data['passes']['outcome']

# Plot the passes
for i in range(len(pass_start_x)):
    # Only plot successful passes
    if pass_outcome[i] == 1:
        # Draw the pass as an arrow
        ax.arrow(pass_start_x[i], pass_start_y[i], 
                 pass_end_x[i] - pass_start_x[i], 
                 pass_end_y[i] - pass_start_y[i],
                 width=0.5, head_width=3, head_length=3, 
                 color='blue', alpha=0.6)

# Add title
ax.set_title('Successful Passes Map', fontsize=20)

# Save the figure
plt.tight_layout()
plt.savefig('plots/pass_map.png', dpi=300)
plt.close()
```

### Task 4: Player Comparison Dashboard
Create comprehensive dashboards for comparing multiple players:

```python
# Example: Basic player comparison dashboard
# Select players to compare
player_indices = [0, 10, 20]  # Sample indices
players = df.iloc[player_indices]

# Create figure with multiple subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# 1. Bar chart of goals and assists per 90
metrics = ['goals_per_90', 'assists_per_90']
x = np.arange(len(players))
width = 0.35

for i, metric in enumerate(metrics):
    axs[0, 0].bar(x + (i-0.5)*width, players[metric], width, 
                  label=metric.replace('_', ' ').title())

axs[0, 0].set_title('Scoring Contribution per 90 Minutes')
axs[0, 0].set_xticks(x)
axs[0, 0].set_xticklabels(players['name'])
axs[0, 0].legend()

# 2. Horizontal bar chart of defensive actions
metrics = ['tackles', 'interceptions']
y = np.arange(len(players))
height = 0.35

for i, metric in enumerate(metrics):
    axs[0, 1].barh(y + (i-0.5)*height, players[metric], height, 
                   label=metric.title())

axs[0, 1].set_title('Defensive Actions')
axs[0, 1].set_yticks(y)
axs[0, 1].set_yticklabels(players['name'])
axs[0, 1].legend()

# 3. Scatter plot of shot accuracy vs pass accuracy
axs[1, 0].scatter(players['shot_accuracy'], players['pass_accuracy'], 
                 s=100, alpha=0.7)

# Add player names as annotations
for i, player in players.iterrows():
    axs[1, 0].annotate(player['name'], 
                      (player['shot_accuracy'], player['pass_accuracy']),
                      xytext=(5, 5), textcoords='offset points')

axs[1, 0].set_title('Shot Accuracy vs Pass Accuracy')
axs[1, 0].set_xlabel('Shot Accuracy')
axs[1, 0].set_ylabel('Pass Accuracy')

# 4. Bar chart of performance rating
axs[1, 1].bar(players['name'], players['performance_rating'], 
              color=['blue', 'green', 'red'])
axs[1, 1].set_title('Overall Performance Rating')
axs[1, 1].set_xticklabels(players['name'], rotation=45, ha='right')

# Adjust layout and save
plt.tight_layout()
plt.savefig('plots/player_comparison_dashboard.png', dpi=300)
plt.close()
```

### Task 5: Team Performance Visualization
Create visualizations comparing team performance across various metrics:
- Team comparison bar charts
- Team strength/weakness radar charts
- Team performance overview dashboards

### Task 6: Performance Trends Visualization
Create visualizations showing how player performance changes over time:
- Line charts of key metrics over games
- Cumulative statistics visualizations
- Performance improvement/decline analysis

### Task 7: Performance Distribution by Position
Create visualizations showing how metrics are distributed across different positions:
- Box plots of metrics by position
- Violin plots showing distribution shapes
- Position-specific performance indicators

### Task 8: Comprehensive Player Profile
Create a complete visual profile for a single player:
- Multi-panel dashboard of all performance aspects
- Comparison to position averages
- Strengths and weaknesses analysis
- Visual career progression

## Hints and Tips

1. **Pitch Coordinates**: Soccer pitch coordinates typically use one of these systems:
   - StatsBomb: (0,0) at top-left, (120,80) at bottom-right
   - Opta: (0,0) at bottom-left, (100,100) at top-right
   - Metrica: (0,0) at center, (-50,50) at top-left, (50,-50) at bottom-right

2. **Color Usage**: Use appropriate colors for different types of events:
   - Goals: Bright colors like red
   - Shots: Colors based on xG or outcome
   - Passes: Colors based on direction or outcome
   - Defensive actions: Blues or greens

3. **Legend Clarity**: Always include clear legends, especially for shot maps and pass networks:
   ```python
   # Create custom legend elements
   from matplotlib.lines import Line2D
   legend_elements = [
       Line2D([0], [0], marker='o', color='w', markerfacecolor='r', markersize=10, label='Goals'),
       Line2D([0], [0], marker='o', color='w', markerfacecolor='b', markersize=10, label='Shots')
   ]
   ax.legend(handles=legend_elements, loc='upper right')
   ```

4. **Normalization**: When comparing players, normalize metrics appropriately:
   - Per 90 minutes for counting stats (goals, assists, etc.)
   - Percentages for accuracy metrics (pass completion, shot accuracy)
   - Percentiles relative to position for radar charts

5. **Interactive Tools**: Use Plotly for interactive visualizations:
   ```python
   # Create an interactive shot map
   fig = go.Figure()
   
   # Add pitch layout
   # (simplified - you'd need to add lines, etc. for a complete pitch)
   fig.update_layout(
       xaxis_range=[0, 120],
       yaxis_range=[0, 80],
       plot_bgcolor='#6c9c30'  # Green pitch color
   )
   
   # Add shots
   fig.add_trace(go.Scatter(
       x=shot_x,
       y=shot_y,
       mode='markers',
       marker=dict(
           size=shot_xg * 50,  # Size based on xG
           color=['red' if o == 1 else 'blue' for o in shot_outcome],
           line=dict(width=2, color='black')
       ),
       text=[f'xG: {xg:.2f}<br>Outcome: {"Goal" if o==1 else "Miss"}' 
             for xg, o in zip(shot_xg, shot_outcome)],
       hoverinfo='text',
       name='Shots'
   ))
   
   fig.update_layout(title='Interactive Shot Map')
   fig.write_html('plots/interactive_shot_map.html')
   ```

6. **Position-Specific Analysis**: Consider different metrics for different positions:
   - Forwards: Goals, shots, xG
   - Midfielders: Passes, assists, progressive passes
   - Defenders: Interceptions, tackles, clearances
   - Goalkeepers: Saves, save percentage, distribution

7. **Pitch Control Visualization**: For advanced users, visualize pitch control using 2D heatmaps:
   ```python
   # Example of a simple pitch control heatmap
   # (This would be calculated from player positions in real scenarios)
   pitch = Pitch(pitch_type='statsbomb', pitch_color='white', line_color='black')
   fig, ax = pitch.draw(figsize=(12, 8))
   
   # Create a grid of x, y coordinates
   x = np.linspace(0, 120, 50)
   y = np.linspace(0, 80, 50)
   X, Y = np.meshgrid(x, y)
   
   # Simulate team control (this would come from a model in real scenarios)
   # Here we're just creating a simplified example
   Z = np.exp(-0.01 * ((X - 60)**2 + (Y - 40)**2))
   
   # Plot the heatmap
   control = ax.contourf(X, Y, Z, levels=50, cmap='coolwarm', alpha=0.5)
   fig.colorbar(control, ax=ax, label='Team Control')
   
   ax.set_title('Pitch Control Visualization')
   plt.tight_layout()
   plt.savefig('plots/pitch_control.png', dpi=300)
   plt.close()
   ```

## Extension Opportunities

1. **Expected Threat (xT) Maps**: Create visualizations showing the threat value of different pitch areas.

2. **Game State Analysis**: Visualize how player or team performance changes based on game state (winning, losing, drawing).

3. **Pressure Maps**: Create heatmaps showing where a team applies defensive pressure.

4. **Passing Sonars**: Create circular visualizations showing passing directions and distances.

5. **Set Piece Analysis**: Create specialized visualizations for corner kicks, free kicks, and penalties.

6. **Formation Analysis**: Visualize team formations and how they shift throughout a match.

7. **Interactive Player Selector**: Build a Plotly dashboard that allows users to select players for comparison.

## Resources

- [mplsoccer Documentation](https://mplsoccer.readthedocs.io/en/latest/)
- [Football (Soccer) Analytics with Python](https://github.com/Friends-of-Tracking-Data-FoTD/mapping-match-events-in-Python)
- [StatsBomb Open Data](https://github.com/statsbomb/open-data)
- [Soccer Analytics Handbook](https://github.com/devinpleuler/analytics-handbook)
- [FC Python](https://fcpython.com/) - Soccer Analytics Tutorials
- [Metrica Sports Documentation](https://github.com/metrica-sports/sample-data)
- [Football Slices](https://www.footballslices.com/) - Soccer Visualization Examples
- [Soccer Analytics YouTube Channel](https://www.youtube.com/c/McKayJohns)

## Submission

Complete the implementation of the functions in `soccer_visualization.py`. When you run the script, it should generate a series of visualizations in the 'plots' directory.