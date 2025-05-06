"""
NCAA Soccer Player Analysis Dashboard

A Flask web application for visualizing player statistics and analysis results.
"""

from flask import Flask, render_template, request, jsonify
import pandas as pd
import json
import os
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analysis.player_metrics import compare_players

app = Flask(__name__)

# Sample data loading - in a real app, this would come from a database
def load_sample_data():
    """Load sample player data for demonstration."""
    try:
        # Adjust path as needed
        data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                               'data', 'sample', 'player_stats_sample.csv')
        return pd.read_csv(data_path)
    except Exception as e:
        print(f"Error loading sample data: {e}")
        # Return empty DataFrame if file not found
        return pd.DataFrame()

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('index.html')

@app.route('/players')
def get_players():
    """API endpoint to get the list of players."""
    player_data = load_sample_data()
    players = player_data[['player_id', 'first_name', 'last_name', 'team', 'position']].to_dict('records')
    return jsonify(players)

@app.route('/player/<player_id>')
def get_player(player_id):
    """API endpoint to get details for a specific player."""
    player_data = load_sample_data()
    player = player_data[player_data['player_id'] == player_id]
    
    if player.empty:
        return jsonify({'error': 'Player not found'}), 404
    
    # Calculate metrics for this player
    metrics = compare_players(player)
    
    # Combine basic data with metrics
    result = player.to_dict('records')[0]
    for col in metrics.columns:
        result[col] = metrics[col].iloc[0]
    
    return jsonify(result)

@app.route('/metrics')
def get_metrics():
    """API endpoint to get calculated metrics for all players."""
    player_data = load_sample_data()
    
    # Get requested metrics or use defaults
    requested_metrics = request.args.get('metrics')
    if requested_metrics:
        metrics_list = requested_metrics.split(',')
    else:
        metrics_list = ['goals_per_90', 'assists_per_90', 'shot_accuracy', 'efficiency_score']
    
    # Calculate metrics
    metrics = compare_players(player_data, metrics_list)
    
    # Combine with player identifiers
    result = pd.concat([
        player_data[['player_id', 'first_name', 'last_name', 'team', 'position']],
        metrics
    ], axis=1)
    
    return jsonify(result.to_dict('records'))

@app.route('/teams')
def get_teams():
    """API endpoint to get the list of teams."""
    player_data = load_sample_data()
    teams = player_data['team'].unique().tolist()
    return jsonify(teams)

@app.route('/team/<team_name>')
def get_team_players(team_name):
    """API endpoint to get players from a specific team."""
    player_data = load_sample_data()
    team_players = player_data[player_data['team'] == team_name]
    
    if team_players.empty:
        return jsonify({'error': 'Team not found'}), 404
    
    return jsonify(team_players.to_dict('records'))

@app.route('/positions')
def get_positions():
    """API endpoint to get the list of positions."""
    player_data = load_sample_data()
    positions = player_data['position'].unique().tolist()
    return jsonify(positions)

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs(os.path.join(os.path.dirname(__file__), 'templates'), exist_ok=True)
    
    # Create a simple index.html if it doesn't exist
    index_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    if not os.path.exists(index_path):
        with open(index_path, 'w') as f:
            f.write("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>NCAA Soccer Player Analysis</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
                    h1 { color: #2c3e50; }
                    .container { max-width: 1200px; margin: 0 auto; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>NCAA Soccer Player Analysis Dashboard</h1>
                    <p>This is a placeholder for the interactive dashboard. API endpoints are available.</p>
                    <h2>Available API Endpoints:</h2>
                    <ul>
                        <li><a href="/players">/players</a> - List all players</li>
                        <li><a href="/metrics">/metrics</a> - Get performance metrics</li>
                        <li><a href="/teams">/teams</a> - List all teams</li>
                        <li><a href="/positions">/positions</a> - List all positions</li>
                    </ul>
                </div>
            </body>
            </html>
            """)
    
    # Run the app
    app.run(debug=True, port=5000)