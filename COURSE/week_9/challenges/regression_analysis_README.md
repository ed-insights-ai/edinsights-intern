# Regression Analysis Challenge

## Overview
Welcome to the Regression Analysis Challenge! In this assignment, you will apply regression modeling techniques to predict soccer player performance metrics. Regression analysis is a fundamental machine learning approach that allows us to understand relationships between variables and make predictions based on those relationships. In soccer analytics, regression models can help teams predict player performance, identify undervalued talent, and optimize tactical decisions.

## Learning Objectives
- Implement various regression models for soccer analytics
- Understand the differences between regression techniques
- Evaluate model performance using appropriate metrics
- Interpret model results to extract actionable insights
- Visualize predictions and model comparisons
- Apply soccer-specific context to statistical modeling

## NCAA Soccer Application
Regression modeling has several applications in NCAA Division II soccer:
- Predict player goals and assists based on historical data and other metrics
- Forecast player development trajectories for recruiting decisions
- Estimate playing time impact on performance for rotation planning
- Identify key performance indicators that most strongly influence outcomes
- Create player valuation models based on predicted contributions
- Develop position-specific performance models to evaluate players in context

## Conceptual Background

### Regression Fundamentals
Regression analysis explores relationships between a dependent variable (target) and one or more independent variables (features). The core approaches include:

1. **Linear Regression**: Models a linear relationship between features and the target
2. **Regularized Regression**: Adds penalties to prevent overfitting (Ridge, Lasso, ElasticNet)
3. **Polynomial Regression**: Captures non-linear relationships through polynomial features
4. **Tree-based Regression**: Uses decision trees to model complex, non-linear patterns

### Model Evaluation
Properly evaluating regression models involves several metrics:
- **Mean Squared Error (MSE)**: Average of squared errors (sensitive to outliers)
- **Root Mean Squared Error (RMSE)**: Square root of MSE, in the same units as target
- **Mean Absolute Error (MAE)**: Average absolute difference between predictions and actuals
- **R² (coefficient of determination)**: Proportion of variance explained by the model

### Feature Selection and Importance
Different regression techniques handle feature selection differently:
- **Linear/Ridge**: Uses all features with varying weights
- **Lasso/ElasticNet**: Can reduce feature coefficients to zero, performing automatic selection
- **Tree-based Methods**: Calculate feature importance based on information gain

## Challenge Tasks

### Task 1: Linear Regression
Implement a basic linear regression model to predict player performance:

```python
# Example: Implementing basic linear regression
# Create and fit the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Analyze feature coefficients
coefficients = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': model.coef_
})
coefficients = coefficients.sort_values('Coefficient', ascending=False)

# Plot feature coefficients
plt.figure(figsize=(10, 6))
plt.barh(coefficients['Feature'], coefficients['Coefficient'])
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.title('Linear Regression Coefficients')
plt.savefig('plots/linear_regression_coefficients.png', dpi=300)
plt.close()
```

### Task 2: Regularized Regression
Compare different regularization approaches (Ridge, Lasso, ElasticNet):

```python
# Example: Implementing regularized regression with hyperparameter tuning
# Ridge Regression with cross-validation
ridge_alphas = np.logspace(-3, 3, 7)
ridge_cv = GridSearchCV(
    Ridge(),
    {'alpha': ridge_alphas},
    cv=5,
    scoring='neg_mean_squared_error'
)
ridge_cv.fit(X_train, y_train)
best_ridge_alpha = ridge_cv.best_params_['alpha']
best_ridge = ridge_cv.best_estimator_

# Lasso Regression with cross-validation
lasso_alphas = np.logspace(-4, 0, 5)
lasso_cv = GridSearchCV(
    Lasso(max_iter=10000),
    {'alpha': lasso_alphas},
    cv=5,
    scoring='neg_mean_squared_error'
)
lasso_cv.fit(X_train, y_train)
best_lasso_alpha = lasso_cv.best_params_['alpha']
best_lasso = lasso_cv.best_estimator_

# Evaluate each model
ridge_pred = best_ridge.predict(X_test)
lasso_pred = best_lasso.predict(X_test)

# Compare feature selection (Lasso can eliminate features)
lasso_coef = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': best_lasso.coef_
})
lasso_selected = lasso_coef[lasso_coef['Coefficient'] != 0]

print(f"Lasso selected {len(lasso_selected)} out of {len(feature_names)} features")
```

### Task 3: Polynomial Regression
Implement polynomial regression to capture non-linear relationships:

```python
# Example: Implementing polynomial regression
degrees = [1, 2, 3]
results = []

for degree in degrees:
    # Create polynomial features
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    # Fit model
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    
    # Evaluate
    train_pred = model.predict(X_train_poly)
    test_pred = model.predict(X_test_poly)
    train_r2 = r2_score(y_train, train_pred)
    test_r2 = r2_score(y_test, test_pred)
    test_mse = mean_squared_error(y_test, test_pred)
    
    results.append({
        'degree': degree,
        'train_r2': train_r2,
        'test_r2': test_r2,
        'test_mse': test_mse
    })

# Visualize results to check for overfitting
plt.figure(figsize=(10, 6))
degrees = [r['degree'] for r in results]
train_r2 = [r['train_r2'] for r in results]
test_r2 = [r['test_r2'] for r in results]

plt.plot(degrees, train_r2, 'o-', label='Training R²')
plt.plot(degrees, test_r2, 'o-', label='Testing R²')
plt.xlabel('Polynomial Degree')
plt.ylabel('R² Score')
plt.title('Polynomial Regression: Training vs Testing Performance')
plt.legend()
plt.savefig('plots/polynomial_regression_comparison.png', dpi=300)
plt.close()
```

### Task 4: Tree-based Regression
Implement and compare tree-based regression models:

```python
# Example: Implementing tree-based regression
# Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_mse = mean_squared_error(y_test, rf_pred)
rf_r2 = r2_score(y_test, rf_pred)

# Gradient Boosting Regressor
gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb_model.fit(X_train, y_train)
gb_pred = gb_model.predict(X_test)
gb_mse = mean_squared_error(y_test, gb_pred)
gb_r2 = r2_score(y_test, gb_pred)

# Analyze feature importance
rf_importance = pd.DataFrame({
    'Feature': feature_names,
    'Importance': rf_model.feature_importances_
}).sort_values('Importance', ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(rf_importance['Feature'][:10], rf_importance['Importance'][:10])
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Top 10 Important Features (Random Forest)')
plt.savefig('plots/rf_feature_importance.png', dpi=300)
plt.close()
```

### Task 5: Model Comparison
Compare all the regression models to identify the best approach:

```python
# Example: Comparing models
models = {
    'Linear Regression': {'mse': linear_mse, 'r2': linear_r2},
    'Ridge Regression': {'mse': ridge_mse, 'r2': ridge_r2},
    'Lasso Regression': {'mse': lasso_mse, 'r2': lasso_r2},
    'Polynomial (Degree 2)': {'mse': poly2_mse, 'r2': poly2_r2},
    'Random Forest': {'mse': rf_mse, 'r2': rf_r2},
    'Gradient Boosting': {'mse': gb_mse, 'r2': gb_r2}
}

# Create comparison DataFrame
comparison_df = pd.DataFrame({
    'Model': list(models.keys()),
    'MSE': [models[model]['mse'] for model in models],
    'R²': [models[model]['r2'] for model in models]
})

# Sort by R² (higher is better)
comparison_df = comparison_df.sort_values('R²', ascending=False)

# Visualize comparison
plt.figure(figsize=(12, 6))
plt.barh(comparison_df['Model'], comparison_df['R²'])
plt.xlabel('R² Score (higher is better)')
plt.ylabel('Model')
plt.title('Model Comparison by R² Score')
plt.xlim(0, 1)
plt.savefig('plots/model_comparison_r2.png', dpi=300)
plt.close()
```

### Task 6: Feature Importance Analysis
Analyze which features most strongly influence the predictions:

```python
# Example: Analyzing feature importance across models
# Extracting feature importance/coefficients from each model
feature_importance = pd.DataFrame({'Feature': feature_names})

# Linear model coefficients (absolute values)
feature_importance['Linear'] = np.abs(linear_model.coef_)

# Ridge coefficients (absolute values)
feature_importance['Ridge'] = np.abs(ridge_model.coef_)

# Lasso coefficients (absolute values)
feature_importance['Lasso'] = np.abs(lasso_model.coef_)

# Random Forest importance
feature_importance['Random Forest'] = rf_model.feature_importances_

# Gradient Boosting importance
feature_importance['Gradient Boosting'] = gb_model.feature_importances_

# Normalize each column to sum to 1 for comparison
for column in feature_importance.columns[1:]:
    feature_importance[column] = feature_importance[column] / feature_importance[column].sum()

# Rank features by average importance
feature_importance['Average Importance'] = feature_importance.iloc[:, 1:].mean(axis=1)
top_features = feature_importance.sort_values('Average Importance', ascending=False).head(10)

# Visualize top features
plt.figure(figsize=(12, 8))
top_features.set_index('Feature').iloc[:, :-1].plot(kind='bar', figsize=(12, 8))
plt.xlabel('Feature')
plt.ylabel('Normalized Importance')
plt.title('Top 10 Feature Importance Across Models')
plt.legend(title='Model')
plt.savefig('plots/feature_importance_comparison.png', dpi=300)
plt.close()
```

### Task 7: Prediction Visualization
Create visualizations of model predictions:

```python
# Example: Visualizing predictions
# Scatter plot of actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, rf_pred, alpha=0.7)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Random Forest: Actual vs. Predicted')
plt.savefig('plots/rf_actual_vs_predicted.png', dpi=300)
plt.close()

# Residual plot
plt.figure(figsize=(10, 6))
residuals = y_test - rf_pred
plt.scatter(rf_pred, residuals, alpha=0.7)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Random Forest: Residual Plot')
plt.savefig('plots/rf_residual_plot.png', dpi=300)
plt.close()

# Error distribution
plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True)
plt.xlabel('Prediction Error')
plt.ylabel('Frequency')
plt.title('Random Forest: Error Distribution')
plt.savefig('plots/rf_error_distribution.png', dpi=300)
plt.close()
```

### Task 8: Soccer-specific Regression
Apply regression analysis to soccer-specific contexts:

```python
# Example: Position-specific regression models
positions = df['position'].unique()
position_models = {}

for position in positions:
    # Filter data for this position
    pos_df = df[df['position'] == position]
    
    # Features and target
    X = pos_df[['age', 'experience', 'previous_goals', 'minutes', 
                'training_score', 'fitness_level']]
    y = pos_df['goals']
    
    # Split data
    if len(pos_df) > 10:  # Only if we have enough samples
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42)
        
        # Train model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        position_models[position] = {
            'model': model,
            'mse': mse,
            'r2': r2,
            'feature_importance': dict(zip(X.columns, model.feature_importances_))
        }

# Compare position models
pos_comparison = pd.DataFrame({
    'Position': list(position_models.keys()),
    'R²': [position_models[pos]['r2'] for pos in position_models]
})

plt.figure(figsize=(10, 6))
plt.bar(pos_comparison['Position'], pos_comparison['R²'])
plt.xlabel('Player Position')
plt.ylabel('Model R² Score')
plt.title('Position-Specific Model Performance')
plt.savefig('plots/position_model_comparison.png', dpi=300)
plt.close()
```

## Hints and Tips

1. **Data Preprocessing**:
   - Handle categorical variables (one-hot encoding for position/team)
   - Scale numerical features when using linear models
   - Check for missing values
   - Consider creating domain-specific features (e.g., goals per minute)

2. **Feature Selection**:
   - Start with domain knowledge (what factors influence player performance?)
   - Use Lasso regression to identify important features
   - Consider the feature importance from tree-based models
   - Remove highly correlated features to reduce multicollinearity

3. **Model Evaluation**:
   - Use cross-validation to get robust estimates of model performance
   - Consider multiple metrics (MSE, MAE, R²) when comparing models
   - Watch for overfitting (large gap between training and testing performance)
   - Consider the interpretability needs when selecting a final model

4. **Soccer Context**:
   - Remember that different positions have different performance expectations
   - Playing time significantly impacts counting statistics
   - Previous performance is often a strong predictor of future performance
   - Age curves are non-linear (players improve, peak, then decline)

5. **Visualization Tips**:
   - Always label axes and include titles
   - Use appropriate colors and styles for clarity
   - Include error bars or uncertainty when possible
   - Create visualizations that would be useful to coaches and analysts

## Extension Opportunities

1. **Advanced Models**: Experiment with more advanced regression techniques like Support Vector Regression or Neural Networks

2. **Time Series Forecasting**: Analyze player performance trends over a season

3. **Multi-output Regression**: Predict multiple performance metrics simultaneously

4. **Bayesian Regression**: Implement Bayesian regression to quantify prediction uncertainty

5. **Custom Loss Functions**: Design soccer-specific loss functions that penalize certain types of errors more heavily

6. **Feature Engineering**: Create advanced soccer-specific features like expected goals (xG) from basic statistics

## Resources

- [Scikit-learn Regression Documentation](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
- [Seaborn Visualization Guide](https://seaborn.pydata.org/tutorial.html)
- [Feature Engineering Techniques](https://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it/)
- [Data Analysis with Python Course](https://www.freecodecamp.org/learn/data-analysis-with-python/)
- [Machine Learning for Soccer Analytics](https://soccermatics.readthedocs.io/en/latest/)
- [Regression Metrics Explained](https://towardsdatascience.com/metrics-to-evaluate-your-regression-model-d89e808b5057)

## Submission

Complete the implementation of the functions in `regression_analysis.py`. When you run the script, it should execute all regression analysis tasks and generate visualization files in the 'plots' directory.