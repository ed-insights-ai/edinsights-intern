# Predictive Modeling Challenge

## Overview
Welcome to the Predictive Modeling Challenge! In this assignment, you'll build machine learning models to forecast player performance, development trajectories, and market values in soccer. Predictive modeling allows teams to make data-driven decisions about player recruitment, development, and team strategy. By applying these techniques to soccer data, you'll create tools that can identify talent, optimize player development, and maximize team performance.

## Learning Objectives
- Build performance prediction models for soccer players
- Create forecasting models for player development over time
- Develop market value prediction systems
- Implement position-specific predictive models
- Apply ensemble methods for improved predictive power
- Interpret model results to extract actionable insights
- Create player comparison and recommendation systems

## NCAA Soccer Application
Predictive modeling has several valuable applications in NCAA Division II soccer:
- Forecast player performance to aid in recruitment decisions
- Predict player development trajectories to optimize training programs
- Identify undervalued players with high potential
- Create position-specific performance expectations
- Forecast team performance based on player characteristics
- Predict injury risks to prevent player absences
- Compare players across different teams and divisions

## Conceptual Background

### Predictive Modeling Fundamentals
Predictive modeling uses historical data to forecast future outcomes:
1. **Regression Models**: Predict continuous values (goals, assists, etc.)
2. **Classification Models**: Predict categorical outcomes (position suitability, success/failure)
3. **Time Series Models**: Forecast trends over sequential time periods
4. **Ensemble Methods**: Combine multiple models for improved predictions

### Model Evaluation
To assess model performance, several metrics are used:
- **Mean Squared Error (MSE)**: Average squared difference between predictions and actuals
- **Root Mean Squared Error (RMSE)**: Square root of MSE, in same units as target
- **Mean Absolute Error (MAE)**: Average absolute difference between predictions and actuals
- **R² (coefficient of determination)**: Proportion of variance explained by the model
- **Time Series Metrics**: Mean Absolute Percentage Error (MAPE), Forecast Bias

### Model Validation
For reliable model assessment:
- **Train-Test Split**: Dividing data into training and testing sets
- **Cross-Validation**: Multiple iterations of training and testing on different data subsets
- **Time Series Cross-Validation**: Respects temporal order for performance assessment

## Challenge Tasks

### Task 1: Performance Prediction
Build models to predict player performance metrics:

```python
# Example: Build and evaluate performance prediction models
# Prepare features and target
X_columns = ['age', 'height', 'weight', 'speed', 'dribbling', 
             'shooting', 'passing', 'defending', 'physicality']
X = df[X_columns].fillna(0)
y = df['goals']  # Target: goals scored

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create models dictionary
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
}

# Train and evaluate models
results = {}
for name, model in models.items():
    # Train model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    # Calculate metrics
    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    
    # Save results
    results[name] = {
        'model': model,
        'train_mse': train_mse,
        'test_mse': test_mse,
        'test_r2': test_r2
    }

# Compare models
result_df = pd.DataFrame({
    'Model': list(results.keys()),
    'Train MSE': [results[model]['train_mse'] for model in results],
    'Test MSE': [results[model]['test_mse'] for model in results],
    'Test R²': [results[model]['test_r2'] for model in results]
})
result_df = result_df.sort_values('Test R²', ascending=False)

# Plot model comparison
plt.figure(figsize=(10, 6))
plt.barh(result_df['Model'], result_df['Test R²'])
plt.xlabel('R² Score (higher is better)')
plt.title('Model Performance Comparison')
plt.tight_layout()
plt.savefig('plots/model_comparison.png', dpi=300)
plt.close()

# Tune best model (assuming Gradient Boosting was best)
best_model_name = result_df.iloc[0]['Model']
print(f"Tuning {best_model_name}...")

if best_model_name == 'Gradient Boosting':
    param_grid = {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 5, 7]
    }
    
    grid_search = GridSearchCV(
        GradientBoostingRegressor(random_state=42),
        param_grid,
        cv=5,
        scoring='neg_mean_squared_error'
    )
    
    grid_search.fit(X_train, y_train)
    
    # Get best model
    best_params = grid_search.best_params_
    best_model = grid_search.best_estimator_
    
    # Evaluate best model
    best_predictions = best_model.predict(X_test)
    best_mse = mean_squared_error(y_test, best_predictions)
    best_r2 = r2_score(y_test, best_predictions)
    
    print(f"Best parameters: {best_params}")
    print(f"Best model MSE: {best_mse:.4f}")
    print(f"Best model R²: {best_r2:.4f}")
    
    # Update results with tuned model
    results['Tuned Gradient Boosting'] = {
        'model': best_model,
        'params': best_params,
        'train_mse': mean_squared_error(y_train, best_model.predict(X_train)),
        'test_mse': best_mse,
        'test_r2': best_r2
    }
```

### Task 2: Player Development Prediction
Build models to predict player development over time:

```python
# Example: Player development prediction
# Group data by player and season
player_seasons = development_df.groupby(['player_id', 'season'])

# Create features for development prediction
development_features = []

for (player_id, season), group in player_seasons:
    # Skip last season (will be used as target)
    if season < max(development_df['season']):
        # Current season data
        current = group.iloc[0]
        
        # Next season data (target)
        next_season = development_df[(development_df['player_id'] == player_id) & 
                                    (development_df['season'] == season + 1)]
        
        if len(next_season) > 0:
            next_season = next_season.iloc[0]
            
            # Features from current season
            features = {
                'player_id': player_id,
                'season': season,
                'age': current['age'],
                'position': current['position'],
                'speed': current['speed'],
                'dribbling': current['dribbling'],
                'shooting': current['shooting'],
                'passing': current['passing'],
                'defending': current['defending'],
                'physicality': current['physicality'],
                'goals': current['goals'],
                'assists': current['assists'],
                
                # Targets (next season values)
                'next_speed': next_season['speed'],
                'next_dribbling': next_season['dribbling'],
                'next_shooting': next_season['shooting'],
                'next_passing': next_season['passing'],
                'next_defending': next_season['defending'],
                'next_physicality': next_season['physicality'],
                'next_goals': next_season['goals'],
                'next_assists': next_season['assists']
            }
            
            development_features.append(features)

# Create DataFrame
dev_df = pd.DataFrame(development_features)

# Create a model to predict next season's goals
X_dev = dev_df[['age', 'speed', 'dribbling', 'shooting', 
                'passing', 'defending', 'physicality', 'goals']]
y_dev = dev_df['next_goals']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_dev, y_dev, test_size=0.2, random_state=42)

# Train model
dev_model = RandomForestRegressor(n_estimators=100, random_state=42)
dev_model.fit(X_train, y_train)

# Evaluate
y_pred = dev_model.predict(X_test)
dev_mse = mean_squared_error(y_test, y_pred)
dev_r2 = r2_score(y_test, y_pred)

print(f"Development Model MSE: {dev_mse:.4f}")
print(f"Development Model R²: {dev_r2:.4f}")

# Feature importance
feature_importance = pd.DataFrame({
    'Feature': X_dev.columns,
    'Importance': dev_model.feature_importances_
}).sort_values('Importance', ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(feature_importance['Feature'], feature_importance['Importance'])
plt.xlabel('Importance')
plt.title('Feature Importance for Goal Development')
plt.tight_layout()
plt.savefig('plots/development_feature_importance.png', dpi=300)
plt.close()

# Visualize actual vs predicted development
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
plt.xlabel('Actual Goals Next Season')
plt.ylabel('Predicted Goals Next Season')
plt.title('Player Development Prediction: Goals')
plt.tight_layout()
plt.savefig('plots/development_prediction.png', dpi=300)
plt.close()
```

### Task 3: Market Value Prediction
Build models to predict player market value:

```python
# Example: Market value prediction
# Prepare features for market value prediction
X_market = development_df[[
    'age', 'speed', 'dribbling', 'shooting', 'passing', 
    'defending', 'physicality', 'goals', 'assists'
]]
y_market = development_df['market_value']

# Create dummy variables for position
position_dummies = pd.get_dummies(development_df['position'], prefix='pos')
X_market = pd.concat([X_market, position_dummies], axis=1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_market, y_market, test_size=0.2, random_state=42)

# Create pipeline with preprocessing and model
market_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', GradientBoostingRegressor(n_estimators=100, random_state=42))
])

# Train model
market_pipeline.fit(X_train, y_train)

# Evaluate
y_pred = market_pipeline.predict(X_test)
market_mse = mean_squared_error(y_test, y_pred)
market_r2 = r2_score(y_test, y_pred)

print(f"Market Value Model MSE: {market_mse:.4f}")
print(f"Market Value Model R²: {market_r2:.4f}")

# Feature importance (extract from pipeline)
market_model = market_pipeline.named_steps['model']
feature_importance = pd.DataFrame({
    'Feature': X_market.columns,
    'Importance': market_model.feature_importances_
}).sort_values('Importance', ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(feature_importance.head(10)['Feature'], feature_importance.head(10)['Importance'])
plt.xlabel('Importance')
plt.title('Top 10 Features for Market Value Prediction')
plt.tight_layout()
plt.savefig('plots/market_value_feature_importance.png', dpi=300)
plt.close()

# Plot actual vs predicted market values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
plt.xlabel('Actual Market Value')
plt.ylabel('Predicted Market Value')
plt.title('Market Value Prediction')
plt.tight_layout()
plt.savefig('plots/market_value_prediction.png', dpi=300)
plt.close()
```

### Task 4: Position-specific Models
Build position-specific prediction models:

```python
# Example: Position-specific models
positions = development_df['position'].unique()
position_models = {}

# For each position, build a separate model
for position in positions:
    # Filter data for this position
    position_data = development_df[development_df['position'] == position]
    
    # Skip if not enough data
    if len(position_data) < 20:
        print(f"Not enough data for position {position}, skipping")
        continue
    
    print(f"Building model for position: {position} (n={len(position_data)})")
    
    # Prepare features and target
    X_pos = position_data[[
        'age', 'speed', 'dribbling', 'shooting', 
        'passing', 'defending', 'physicality'
    ]]
    y_pos = position_data['goals']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_pos, y_pos, test_size=0.2, random_state=42)
    
    # Train model
    pos_model = RandomForestRegressor(n_estimators=100, random_state=42)
    pos_model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = pos_model.predict(X_test)
    pos_mse = mean_squared_error(y_test, y_pred)
    pos_r2 = r2_score(y_test, y_pred)
    
    # Feature importance
    importance = pd.DataFrame({
        'Feature': X_pos.columns,
        'Importance': pos_model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    # Store results
    position_models[position] = {
        'model': pos_model,
        'mse': pos_mse,
        'r2': pos_r2,
        'feature_importance': importance
    }

# Compare position models
pos_comparison = pd.DataFrame({
    'Position': list(position_models.keys()),
    'MSE': [position_models[p]['mse'] for p in position_models],
    'R²': [position_models[p]['r2'] for p in position_models]
})

plt.figure(figsize=(10, 6))
plt.bar(pos_comparison['Position'], pos_comparison['R²'])
plt.xlabel('Position')
plt.ylabel('R² Score')
plt.title('Model Performance by Position')
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig('plots/position_model_comparison.png', dpi=300)
plt.close()

# Compare top features by position
plt.figure(figsize=(12, 8))
for i, (position, results) in enumerate(position_models.items()):
    plt.subplot(2, 2, i+1)
    importance = results['feature_importance'].head(5)
    plt.barh(importance['Feature'], importance['Importance'])
    plt.xlabel('Importance')
    plt.title(f'Top 5 Features for {position}')

plt.tight_layout()
plt.savefig('plots/position_feature_importance.png', dpi=300)
plt.close()
```

### Task 5: Ensemble Methods
Implement ensemble methods for improved predictions:

```python
# Example: Ensemble methods for performance prediction
# Prepare data
X = df[['age', 'speed', 'dribbling', 'shooting', 'passing', 'defending', 'physicality']]
y = df[target]

# Add position dummies if categorical
if 'position' in df.columns:
    position_dummies = pd.get_dummies(df['position'], prefix='pos')
    X = pd.concat([X, position_dummies], axis=1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Base models
base_models = {
    'Linear Regression': LinearRegression(),
    'Ridge': Ridge(alpha=1.0),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
    'XGBoost': XGBRegressor(n_estimators=100, random_state=42)
}

# Train and evaluate base models
base_results = {}
for name, model in base_models.items():
    # Train model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    test_mse = mean_squared_error(y_test, y_pred)
    test_r2 = r2_score(y_test, y_pred)
    
    # Save results
    base_results[name] = {
        'model': model,
        'test_mse': test_mse,
        'test_r2': test_r2,
        'predictions': y_pred
    }

# 2. Simple averaging ensemble
ensemble_preds = np.zeros(len(y_test))
for name, results in base_results.items():
    ensemble_preds += results['predictions']
ensemble_preds /= len(base_results)

ensemble_mse = mean_squared_error(y_test, ensemble_preds)
ensemble_r2 = r2_score(y_test, ensemble_preds)

print(f"Simple Ensemble MSE: {ensemble_mse:.4f}")
print(f"Simple Ensemble R²: {ensemble_r2:.4f}")

# 3. Weighted ensemble (assign more weight to better models)
weights = {name: 1/results['test_mse'] for name, results in base_results.items()}
total_weight = sum(weights.values())
weights = {name: w/total_weight for name, w in weights.items()}

weighted_preds = np.zeros(len(y_test))
for name, results in base_results.items():
    weighted_preds += weights[name] * results['predictions']

weighted_mse = mean_squared_error(y_test, weighted_preds)
weighted_r2 = r2_score(y_test, weighted_preds)

print(f"Weighted Ensemble MSE: {weighted_mse:.4f}")
print(f"Weighted Ensemble R²: {weighted_r2:.4f}")

# Compare all models
all_results = base_results.copy()
all_results['Simple Ensemble'] = {
    'test_mse': ensemble_mse,
    'test_r2': ensemble_r2
}
all_results['Weighted Ensemble'] = {
    'test_mse': weighted_mse,
    'test_r2': weighted_r2
}

# Create comparison DataFrame
comparison = pd.DataFrame({
    'Model': list(all_results.keys()),
    'MSE': [all_results[model]['test_mse'] for model in all_results],
    'R²': [all_results[model]['test_r2'] for model in all_results]
}).sort_values('R²', ascending=False)

# Plot comparison
plt.figure(figsize=(12, 6))
plt.barh(comparison['Model'], comparison['R²'])
plt.xlabel('R² Score (higher is better)')
plt.title(f'Model Comparison for {target} Prediction')
plt.tight_layout()
plt.savefig('plots/ensemble_comparison.png', dpi=300)
plt.close()
```

### Task 6: Time Series Forecasting
Implement time series forecasting for player development:

```python
# Example: Time series forecasting for player development
# Select a few players for demonstration
player_ids = development_df['player_id'].unique()[:5]

# Create figure for player forecasts
plt.figure(figsize=(15, 10))

for i, player_id in enumerate(player_ids):
    # Get player data
    player_data = development_df[development_df['player_id'] == player_id].sort_values('season')
    
    # Get player name
    player_name = player_data.iloc[0]['name']
    
    # Train on first 3 seasons, predict the next 2
    train_seasons = 3
    
    if len(player_data) <= train_seasons:
        continue
    
    # Features and target
    X_ts = player_data[['age', 'speed', 'dribbling', 'shooting', 
                      'passing', 'defending', 'physicality']]
    y_ts = player_data['goals']
    
    # Train on first n seasons
    X_train = X_ts.iloc[:train_seasons]
    y_train = y_ts.iloc[:train_seasons]
    
    # Test on remaining seasons
    X_test = X_ts.iloc[train_seasons:]
    y_test = y_ts.iloc[train_seasons:]
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Plot results
    plt.subplot(2, 3, i+1)
    plt.plot(player_data['season'].iloc[:train_seasons], y_train, 'b-', label='Training Data')
    plt.plot(player_data['season'].iloc[train_seasons:], y_test, 'g-', label='Actual')
    plt.plot(player_data['season'].iloc[train_seasons:], y_pred, 'r--', label='Predicted')
    plt.xlabel('Season')
    plt.ylabel('Goals')
    plt.title(f"Player: {player_name}")
    plt.legend()

plt.tight_layout()
plt.savefig('plots/player_forecasting.png', dpi=300)
plt.close()

# Create a multi-step forecasting function
def forecast_player(player_data, seasons_ahead=2):
    """Forecast player performance multiple seasons ahead."""
    # Features and target
    X = player_data[['age', 'speed', 'dribbling', 'shooting', 
                   'passing', 'defending', 'physicality']]
    y = player_data['goals']
    
    # Train model on all available data
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Create future features
    last_row = player_data.iloc[-1]
    future_rows = []
    
    for i in range(seasons_ahead):
        # Create next season's features
        next_season = {
            'season': last_row['season'] + i + 1,
            'age': last_row['age'] + i + 1,
        }
        
        # Simple trend continuation for attributes
        for attr in ['speed', 'dribbling', 'shooting', 'passing', 'defending', 'physicality']:
            # Age-based development (declining after age 30)
            if next_season['age'] < 30:
                next_season[attr] = last_row[attr] * 1.01  # 1% improvement
            else:
                next_season[attr] = last_row[attr] * 0.98  # 2% decline
        
        future_rows.append(next_season)
    
    # Convert to DataFrame
    future_df = pd.DataFrame(future_rows)
    
    # Make predictions
    X_future = future_df[['age', 'speed', 'dribbling', 'shooting', 
                        'passing', 'defending', 'physicality']]
    future_df['predicted_goals'] = model.predict(X_future)
    
    return future_df

# Select a player for multi-season forecasting
sample_player_id = player_ids[0]
sample_player_data = development_df[development_df['player_id'] == sample_player_id].sort_values('season')
sample_player_name = sample_player_data.iloc[0]['name']

# Forecast 3 seasons ahead
forecast = forecast_player(sample_player_data, seasons_ahead=3)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(sample_player_data['season'], sample_player_data['goals'], 'b-', label='Historical')
plt.plot(forecast['season'], forecast['predicted_goals'], 'r--', label='Forecast')
plt.xlabel('Season')
plt.ylabel('Goals')
plt.title(f'Multi-season Forecast for {sample_player_name}')
plt.legend()
plt.tight_layout()
plt.savefig('plots/multi_season_forecast.png', dpi=300)
plt.close()
```

### Task 7: Model Interpretation
Interpret the predictive models:

```python
# Example: Model interpretation
# Analyze feature importance from the best model
if 'random_forest' in base_results:
    rf_model = base_results['Random Forest']['model']
    
    # Feature importance
    feature_imp = pd.DataFrame({
        'Feature': X.columns,
        'Importance': rf_model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    # Plot importance
    plt.figure(figsize=(10, 8))
    plt.barh(feature_imp['Feature'], feature_imp['Importance'])
    plt.xlabel('Importance')
    plt.title('Random Forest Feature Importance')
    plt.tight_layout()
    plt.savefig('plots/rf_feature_importance.png', dpi=300)
    plt.close()
    
    # Create partial dependence plots for top features
    top_features = feature_imp.head(4)['Feature'].tolist()
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    for i, feature in enumerate(top_features):
        # Create a range of values for this feature
        feature_idx = list(X.columns).index(feature)
        feature_values = np.linspace(X[feature].min(), X[feature].max(), 100)
        
        # Create samples with only this feature varying
        X_samples = np.tile(X_test.mean(axis=0), (len(feature_values), 1))
        X_samples[:, feature_idx] = feature_values
        
        # Make predictions
        y_samples = rf_model.predict(X_samples)
        
        # Plot
        axes[i].plot(feature_values, y_samples)
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel(f'Predicted {target}')
        axes[i].set_title(f'Partial Dependence: {feature}')
    
    plt.tight_layout()
    plt.savefig('plots/partial_dependence.png', dpi=300)
    plt.close()
    
    # Analyze key predictive relationships
    key_findings = {
        'top_features': top_features,
        'importance_values': feature_imp.head(4)['Importance'].tolist(),
        'interpretation': [
            f"Age has a non-linear relationship with {target}",
            f"Shooting ability is strongly predictive of {target}",
            f"Position is an important factor in {target} prediction",
            f"Speed has a moderate impact on {target}"
        ]
    }
```

### Task 8: Player Comparison and Recommendation
Create a player comparison and recommendation system:

```python
# Example: Player comparison and recommendation system
# Create a function to calculate player similarity
def calculate_similarity(player1, player2, attributes):
    """Calculate similarity between two players."""
    # Calculate Euclidean distance on standardized attributes
    squared_diff = 0
    for attr in attributes:
        # Skip if attribute is missing
        if attr not in player1 or attr not in player2:
            continue
        
        # Get min and max for normalization
        attr_min = df[attr].min()
        attr_max = df[attr].max()
        
        # Skip if min equals max
        if attr_min == attr_max:
            continue
        
        # Normalize values
        p1_norm = (player1[attr] - attr_min) / (attr_max - attr_min)
        p2_norm = (player2[attr] - attr_min) / (attr_max - attr_min)
        
        # Add squared difference
        squared_diff += (p1_norm - p2_norm) ** 2
    
    # Return similarity (1 / (1 + distance))
    distance = np.sqrt(squared_diff)
    return 1 / (1 + distance)

# Create a function to find similar players
def find_similar_players(player_id, df, top_n=5):
    """Find top N similar players to a given player."""
    # Get player data
    player = df[df['player_id'] == player_id].iloc[0]
    
    # Attributes for comparison
    attributes = ['age', 'speed', 'dribbling', 'shooting', 
                 'passing', 'defending', 'physicality']
    
    # Calculate similarity to all other players
    similarities = []
    for _, other_player in df.iterrows():
        # Skip the same player
        if other_player['player_id'] == player_id:
            continue
        
        # Calculate similarity
        sim = calculate_similarity(player, other_player, attributes)
        
        # Add to list
        similarities.append({
            'player_id': other_player['player_id'],
            'name': other_player['name'],
            'position': other_player['position'],
            'similarity': sim
        })
    
    # Sort by similarity and get top N
    similarities.sort(key=lambda x: x['similarity'], reverse=True)
    return similarities[:top_n]

# Create a player recommendation system
def recommend_players(df, target_position, budget=None, top_n=5):
    """Recommend players based on predicted performance and value."""
    # Filter by position
    position_df = df[df['position'] == target_position].copy()
    
    # Prepare features for performance prediction
    X = position_df[['age', 'speed', 'dribbling', 'shooting', 
                   'passing', 'defending', 'physicality']]
    
    # Train performance prediction model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, position_df['goals'])
    
    # Predict performance for all players
    position_df['predicted_performance'] = model.predict(X)
    
    # Calculate value ratio (performance / market_value)
    if 'market_value' in position_df.columns:
        position_df['value_ratio'] = position_df['predicted_performance'] / position_df['market_value'].replace(0, 0.1)
    else:
        # If market value not available, use age as a proxy (younger = better value)
        position_df['value_ratio'] = position_df['predicted_performance'] / (position_df['age'] - 17)
    
    # Filter by budget if provided
    if budget is not None and 'market_value' in position_df.columns:
        position_df = position_df[position_df['market_value'] <= budget]
    
    # Sort by value ratio
    position_df = position_df.sort_values('value_ratio', ascending=False)
    
    # Return top N recommendations
    return position_df.head(top_n)

# Demonstrate player similarity
sample_player_id = df['player_id'].iloc[0]
similar_players = find_similar_players(sample_player_id, df)

print(f"Players similar to {df[df['player_id'] == sample_player_id].iloc[0]['name']}:")
for player in similar_players:
    print(f"{player['name']} (Similarity: {player['similarity']:.2f})")

# Demonstrate player recommendations
forward_recommendations = recommend_players(df, 'F')

print("\nRecommended Forwards:")
for _, player in forward_recommendations.iterrows():
    print(f"{player['name']} (Predicted Goals: {player['predicted_performance']:.1f})")

# Create visualization of player recommendations
plt.figure(figsize=(10, 6))
plt.bar(forward_recommendations['name'], forward_recommendations['predicted_performance'])
plt.xticks(rotation=45, ha='right')
plt.ylabel('Predicted Goals')
plt.title('Top Forward Recommendations')
plt.tight_layout()
plt.savefig('plots/forward_recommendations.png', dpi=300)
plt.close()
```

## Hints and Tips

1. **Data Preparation**:
   - Handle missing values appropriately
   - Scale features for linear models
   - Create appropriate features for soccer analysis
   - Ensure proper train-test splitting to avoid data leakage

2. **Model Selection**:
   - Linear models (Linear Regression, Ridge) work well for interpretability
   - Tree-based models (Random Forest, Gradient Boosting) often perform better
   - Consider ensemble methods for improved predictions
   - Use cross-validation to get robust performance estimates

3. **Time Series Considerations**:
   - Respect temporal ordering in player development data
   - Use appropriate validation approaches for time series
   - Consider players' age curves in your models
   - Implement multi-step forecasting for future seasons

4. **Model Interpretation**:
   - Analyze feature importance to understand key predictors
   - Create partial dependence plots to visualize relationships
   - Connect model insights to soccer-specific knowledge
   - Ensure findings are actionable for coaches and scouts

5. **Soccer Analytics Context**:
   - Consider position-specific models and metrics
   - Account for team context when evaluating players
   - Include age-related factors for development prediction
   - Create metrics that align with soccer expertise

## Extension Opportunities

1. **Advanced Models**: Experiment with deep learning approaches for player forecasting

2. **Injury Prediction**: Create models to predict injury risk based on player characteristics

3. **Team Performance**: Build models that predict team outcomes based on player metrics

4. **Opponent Analysis**: Develop prediction systems that account for opponent strength

5. **Match Outcome Prediction**: Create models for game outcome prediction

6. **Interactive Dashboard**: Build an interactive player scouting dashboard with Plotly Dash

7. **Player Clustering**: Incorporate clustering techniques with predictive modeling

## Resources

- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/en/latest/)
- [Time Series Forecasting with Python](https://machinelearningmastery.com/time-series-forecasting-with-python/)
- [Player Development Models](https://www.researchgate.net/publication/335991737_Modeling_the_Development_of_Elite_Sports_Performance)
- [Football Analytics with Python](https://github.com/devinpleuler/analytics-handbook)
- [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Soccer Analytics GitHub Repositories](https://github.com/topics/soccer-analytics)

## Submission

Complete the implementation of the functions in `predictive_modeling.py`. When you run the script, it should execute all predictive modeling tasks and generate visualization files in the 'plots' directory.