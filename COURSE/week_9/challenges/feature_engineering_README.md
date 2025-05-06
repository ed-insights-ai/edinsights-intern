# Feature Engineering Challenge

## Overview
Welcome to the Feature Engineering Challenge! In this assignment, you'll develop advanced features for soccer analytics and evaluate their importance. Feature engineering is the process of creating new variables from existing data that better represent the underlying patterns and improve model performance. In soccer analytics, thoughtfully engineered features can reveal player qualities and game dynamics that raw statistics might miss.

## Learning Objectives
- Create meaningful features from basic soccer statistics
- Apply various feature transformation techniques
- Develop domain-specific soccer analytics metrics
- Implement and compare feature selection methods
- Visualize feature importance and relationships
- Evaluate the impact of engineered features on model performance

## NCAA Soccer Application
Feature engineering is crucial for effective NCAA Division II soccer analysis:
- Create standardized metrics that account for differences in playing time
- Develop position-specific performance indicators for fair player comparison
- Engineer composite metrics that capture overall contribution across statistics
- Derive efficiency metrics to identify undervalued skills
- Create features that reflect tactical concepts and game context
- Build predictive features that estimate future performance potential

## Conceptual Background

### Feature Engineering Fundamentals
Feature engineering involves several key approaches:

1. **Transformation**: Applying mathematical functions to variables
   - Log, square root, polynomial transformations
   - Normalization and standardization
   - Binning and discretization

2. **Interaction**: Creating new features by combining variables
   - Products and ratios between features
   - Conditional combinations based on domain knowledge
   - Polynomial feature interactions

3. **Extraction**: Deriving new information
   - Creating categorical features from continuous ones
   - Time-based features from temporal data
   - Aggregated or summary statistics

4. **Domain-Specific**: Applying field expertise
   - Soccer-specific performance metrics
   - Position-adjusted statistics
   - Game context features

### Feature Selection
Not all features contribute equally to a model. Feature selection methods include:

1. **Filter Methods**: Statistical approaches
   - Correlation analysis
   - Mutual information
   - ANOVA tests

2. **Wrapper Methods**: Model-based selection
   - Recursive Feature Elimination (RFE)
   - Forward/backward selection
   - Exhaustive search

3. **Embedded Methods**: Selection during model training
   - Lasso regression
   - Random Forest importance
   - Gradient Boosting importance

### Dimensionality Reduction
For high-dimensional data, reducing dimensions can improve model performance:
- Principal Component Analysis (PCA)
- Feature Agglomeration
- Matrix Factorization

## Challenge Tasks

### Task 1: Basic Feature Engineering
Implement fundamental feature engineering techniques:

```python
# Example: Creating basic engineered features
# Create DataFrame for new features
df_basic = pd.DataFrame(index=df.index)

# 1. Interaction features
df_basic['speed_dribbling'] = df['speed'] * df['dribbling']
df_basic['shooting_physicality'] = df['shooting'] * df['physicality']
df_basic['passing_vision'] = df['passing'] * df.get('vision', 1)  # If vision exists

# 2. Ratio features
df_basic['shooting_efficiency'] = df['goals'] / df['shots'].replace(0, 1)
df_basic['dribble_pass_ratio'] = df['dribbling'] / df['passing'].replace(0, 1)
df_basic['defense_attack_ratio'] = df['defending'] / df['shooting'].replace(0, 1)

# 3. Transformed features
df_basic['log_minutes'] = np.log1p(df['minutes'])  # log(1+x) to handle zeros
df_basic['sqrt_goals'] = np.sqrt(df['goals'])
df_basic['exp_defending'] = np.exp(df['defending'] / 100)  # Scaled to avoid overflow

# 4. Binary features
df_basic['is_forward'] = (df['position'] == 'F').astype(int)
df_basic['is_midfielder'] = (df['position'] == 'MF').astype(int)
df_basic['is_defender'] = (df['position'] == 'D').astype(int)
df_basic['is_goalkeeper'] = (df['position'] == 'GK').astype(int)
df_basic['is_experienced'] = (df['age'] >= 28).astype(int)
df_basic['is_young_talent'] = (df['age'] <= 23).astype(int)

# 5. Categorical encodings
position_dummies = pd.get_dummies(df['position'], prefix='pos')
team_dummies = pd.get_dummies(df['team'], prefix='team')

# Combine all basic features
df_basic = pd.concat([df_basic, position_dummies, team_dummies], axis=1)

# Visualize some of the new features
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(df['shooting'], df['goals'], alpha=0.7)
plt.xlabel('Shooting Rating')
plt.ylabel('Goals')
plt.title('Shooting Rating vs. Goals')

plt.subplot(1, 2, 2)
plt.scatter(df_basic['shooting_efficiency'], df['goals'], alpha=0.7)
plt.xlabel('Shooting Efficiency')
plt.ylabel('Goals')
plt.title('Shooting Efficiency vs. Goals')

plt.tight_layout()
plt.savefig('plots/basic_feature_engineering.png', dpi=300)
plt.close()
```

### Task 2: Soccer-specific Features
Create domain-specific features for soccer analytics:

```python
# Example: Creating soccer-specific features
# Create DataFrame for soccer features
df_soccer = pd.DataFrame(index=df.index)

# 1. Per 90 minutes metrics (standard in soccer analytics)
minutes_90 = df['minutes'] / 90
df_soccer['goals_per_90'] = df['goals'] / minutes_90.replace(0, np.nan)
df_soccer['assists_per_90'] = df['assists'] / minutes_90.replace(0, np.nan)
df_soccer['tackles_per_90'] = df['tackles'] / minutes_90.replace(0, np.nan)
df_soccer['interceptions_per_90'] = df['interceptions'] / minutes_90.replace(0, np.nan)

# 2. Contribution metrics
df_soccer['goal_contribution'] = df['goals'] + df['assists']
df_soccer['goal_contribution_per_90'] = df_soccer['goal_contribution'] / minutes_90.replace(0, np.nan)

# 3. Efficiency metrics
df_soccer['shot_conversion'] = df['goals'] / df['shots'].replace(0, 1)
df_soccer['passing_accuracy'] = df.get('completed_passes', df['passing'] * 0.85) / df.get('total_passes', df['passing']).replace(0, 1)

# 4. Position-specific performance indicators
# For forwards
df_soccer['forward_rating'] = (
    3 * df['goals_per_90'].fillna(0) + 
    2 * df['assists_per_90'].fillna(0) + 
    1 * df_soccer['shot_conversion']
) * (df['position'] == 'F')

# For midfielders
df_soccer['midfielder_rating'] = (
    1 * df['goals_per_90'].fillna(0) + 
    3 * df['assists_per_90'].fillna(0) + 
    2 * df_soccer['passing_accuracy'] + 
    1 * df_soccer['tackles_per_90'].fillna(0)
) * (df['position'] == 'MF')

# For defenders
df_soccer['defender_rating'] = (
    3 * df_soccer['tackles_per_90'].fillna(0) + 
    3 * df_soccer['interceptions_per_90'].fillna(0) + 
    1 * df_soccer['passing_accuracy'] +
    0.5 * df['assists_per_90'].fillna(0)
) * (df['position'] == 'D')

# 5. Overall performance index
df_soccer['performance_index'] = (
    df_soccer['forward_rating'] + 
    df_soccer['midfielder_rating'] + 
    df_soccer['defender_rating']
)

# Visualize position-specific ratings
plt.figure(figsize=(12, 6))

positions = ['F', 'MF', 'D']
ratings = ['forward_rating', 'midfielder_rating', 'defender_rating']

for i, (pos, rating) in enumerate(zip(positions, ratings)):
    plt.subplot(1, 3, i+1)
    pos_data = df[df['position'] == pos]
    pos_rating = df_soccer.loc[pos_data.index, rating]
    plt.hist(pos_rating[pos_rating > 0], bins=10)
    plt.xlabel(f'{pos} Rating')
    plt.ylabel('Count')
    plt.title(f'{pos} Position Rating Distribution')

plt.tight_layout()
plt.savefig('plots/position_ratings.png', dpi=300)
plt.close()
```

### Task 3: Advanced Feature Engineering
Implement more sophisticated feature engineering techniques:

```python
# Example: Advanced feature engineering
# Create DataFrame for advanced features
df_advanced = pd.DataFrame(index=df.index)

# 1. Polynomial features
numeric_features = ['age', 'goals_per_90', 'assists_per_90', 'shot_conversion']
numeric_df = df_soccer[numeric_features].fillna(0)

poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(numeric_df)
poly_feature_names = [f"{numeric_features[i]}_{numeric_features[j]}" 
                     for i in range(len(numeric_features)) 
                     for j in range(i, len(numeric_features))]

df_poly = pd.DataFrame(poly_features[:, len(numeric_features):], 
                      columns=poly_feature_names, 
                      index=df.index)
df_advanced = pd.concat([df_advanced, df_poly], axis=1)

# 2. Binning for age groups
age_bins = [15, 20, 25, 30, 35, 40]
age_labels = ['U20', '20-24', '25-29', '30-34', '35+']
df_advanced['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
age_dummies = pd.get_dummies(df_advanced['age_group'], prefix='age')
df_advanced = pd.concat([df_advanced, age_dummies], axis=1)

# 3. Peak performance indicators
# Players typically peak around age 27-29
df_advanced['years_to_peak'] = 28 - df['age']
df_advanced['years_from_peak'] = np.abs(df_advanced['years_to_peak'])
df_advanced['in_peak_years'] = ((df['age'] >= 26) & (df['age'] <= 30)).astype(int)

# 4. Create team strength indicators
team_avg_performance = df.groupby('team')['performance_rating'].mean().reset_index()
team_strength_map = dict(zip(team_avg_performance['team'], team_avg_performance['performance_rating']))
df_advanced['team_strength'] = df['team'].map(team_strength_map)
df_advanced['relative_to_team'] = df['performance_rating'] / df_advanced['team_strength'].replace(0, 1)

# 5. Physical attribute interactions
if 'height' in df.columns and 'weight' in df.columns:
    df_advanced['bmi'] = df['weight'] / ((df['height']/100) ** 2)
    df_advanced['height_to_position'] = df['height'] * (
        1.1 * (df['position'] == 'GK') + 
        1.05 * (df['position'] == 'D') + 
        0.95 * (df['position'] == 'MF') + 
        1.0 * (df['position'] == 'F')
    )

# Visualize some advanced features
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
for age_group in age_labels:
    group_data = df_advanced[df_advanced['age_group'] == age_group]
    plt.scatter(group_data['years_from_peak'], 
               df.loc[group_data.index, 'performance_rating'],
               alpha=0.7, label=age_group)
plt.xlabel('Years from Peak Age')
plt.ylabel('Performance Rating')
plt.title('Performance vs. Distance from Peak Age')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(df_advanced['relative_to_team'], df['goals'],
           alpha=0.7, c=df['position'].astype('category').cat.codes, cmap='viridis')
plt.xlabel('Performance Relative to Team')
plt.ylabel('Goals')
plt.title('Goals vs. Relative Team Performance')
plt.colorbar(label='Position')

plt.tight_layout()
plt.savefig('plots/advanced_features.png', dpi=300)
plt.close()
```

### Task 4: Statistical Feature Selection
Apply statistical methods to select the most relevant features:

```python
# Example: Statistical feature selection
# Select numerical columns for analysis
numeric_cols = df_features.select_dtypes(include=[np.number]).columns.tolist()
numeric_cols = [col for col in numeric_cols if col != target]

# Prepare X and y
X = df_features[numeric_cols]
y = df_features[target]

# 1. Correlation analysis
# Pearson correlation (linear relationships)
pearson_correlations = {}
for col in numeric_cols:
    if col != target:
        corr, p_value = pearsonr(X[col].fillna(0), y)
        pearson_correlations[col] = {'correlation': corr, 'p_value': p_value}

# Convert to DataFrame for easier analysis
pearson_df = pd.DataFrame.from_dict(pearson_correlations, orient='index')
pearson_df = pearson_df.sort_values('correlation', key=abs, ascending=False)

# Visualize top correlations
plt.figure(figsize=(12, 8))
top_features = pearson_df.head(15).index.tolist()
corr_matrix = X[top_features].corrwith(y).abs().sort_values(ascending=False)

plt.barh(range(len(corr_matrix)), corr_matrix.values, align='center')
plt.yticks(range(len(corr_matrix)), corr_matrix.index)
plt.xlabel('Absolute Correlation with ' + target)
plt.title('Top 15 Features by Correlation with ' + target)
plt.tight_layout()
plt.savefig('plots/pearson_correlations.png', dpi=300)
plt.close()

# 2. Mutual Information (works for non-linear relationships)
mi_selector = SelectKBest(mutual_info_regression, k=15)
mi_selector.fit(X.fillna(0), y)
mi_scores = pd.DataFrame(
    {'feature': X.columns, 'mi_score': mi_selector.scores_}
).sort_values('mi_score', ascending=False)

# Visualize mutual information
plt.figure(figsize=(12, 8))
plt.barh(range(15), mi_scores.head(15)['mi_score'], align='center')
plt.yticks(range(15), mi_scores.head(15)['feature'])
plt.xlabel('Mutual Information Score')
plt.title('Top 15 Features by Mutual Information with ' + target)
plt.tight_layout()
plt.savefig('plots/mutual_information.png', dpi=300)
plt.close()

# 3. Compare both methods
comparison = pd.DataFrame({
    'feature': pearson_df.index,
    'pearson': pearson_df['correlation'].abs(),
    'p_value': pearson_df['p_value']
})
comparison = comparison.merge(
    mi_scores, on='feature', how='left'
).sort_values('pearson', ascending=False)

# Save results
comparison.to_csv('models/statistical_feature_selection.csv', index=False)

# Return results for further analysis
statistical_results = {
    'pearson': pearson_df,
    'mutual_info': mi_scores,
    'comparison': comparison,
    'top_pearson': pearson_df.head(15).index.tolist(),
    'top_mi': mi_scores.head(15)['feature'].tolist()
}
```

### Task 5: Model-based Feature Selection
Use machine learning models to select important features:

```python
# Example: Model-based feature selection
# 1. Lasso Regression for feature selection
from sklearn.linear_model import LassoCV

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X.fillna(0))

# Fit Lasso with cross-validation to find optimal alpha
lasso_cv = LassoCV(cv=5, random_state=42, max_iter=10000)
lasso_cv.fit(X_scaled, y)

# Get selected features and their coefficients
lasso_coef = pd.DataFrame({
    'feature': X.columns,
    'coefficient': lasso_cv.coef_
})
lasso_selected = lasso_coef[lasso_coef['coefficient'] != 0].sort_values(
    'coefficient', key=abs, ascending=False
)

# Plot Lasso coefficients
plt.figure(figsize=(12, 8))
plt.barh(
    range(len(lasso_selected)), 
    lasso_selected['coefficient'].values, 
    align='center'
)
plt.yticks(range(len(lasso_selected)), lasso_selected['feature'])
plt.xlabel('Lasso Coefficient')
plt.title(f'Features Selected by Lasso (alpha={lasso_cv.alpha_:.4f})')
plt.tight_layout()
plt.savefig('plots/lasso_coefficients.png', dpi=300)
plt.close()

# 2. Random Forest feature importance
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X.fillna(0), y)

# Get feature importance
rf_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

# Plot Random Forest importance
plt.figure(figsize=(12, 8))
plt.barh(
    range(15), 
    rf_importance.head(15)['importance'].values, 
    align='center'
)
plt.yticks(range(15), rf_importance.head(15)['feature'])
plt.xlabel('Random Forest Importance')
plt.title('Top 15 Features by Random Forest Importance')
plt.tight_layout()
plt.savefig('plots/random_forest_importance.png', dpi=300)
plt.close()

# 3. Recursive Feature Elimination (RFE)
lr = LinearRegression()
rfe = RFE(estimator=lr, n_features_to_select=15, step=1)
rfe.fit(X.fillna(0), y)

# Get selected features
rfe_selected = pd.DataFrame({
    'feature': X.columns,
    'selected': rfe.support_,
    'rank': rfe.ranking_
}).sort_values('rank')

# Plot RFE results
plt.figure(figsize=(12, 8))
selected_features = rfe_selected[rfe_selected['selected']]['feature'].tolist()
plt.barh(range(len(selected_features)), [1] * len(selected_features), align='center')
plt.yticks(range(len(selected_features)), selected_features)
plt.xlabel('Selected (1=Yes)')
plt.title('Features Selected by RFE')
plt.tight_layout()
plt.savefig('plots/rfe_selected.png', dpi=300)
plt.close()

# 4. Compare all methods
model_comparison = pd.DataFrame({'feature': X.columns})
model_comparison['lasso'] = model_comparison['feature'].isin(lasso_selected['feature'])
model_comparison['rf_top15'] = model_comparison['feature'].isin(rf_importance.head(15)['feature'])
model_comparison['rfe'] = model_comparison['feature'].isin(selected_features)
model_comparison['selection_count'] = model_comparison[['lasso', 'rf_top15', 'rfe']].sum(axis=1)
model_comparison = model_comparison.sort_values('selection_count', ascending=False)

# Save results
model_comparison.to_csv('models/model_based_feature_selection.csv', index=False)

# Return results for further analysis
model_results = {
    'lasso': lasso_selected,
    'random_forest': rf_importance,
    'rfe': rfe_selected,
    'comparison': model_comparison,
    'consensus_features': model_comparison[model_comparison['selection_count'] > 1]['feature'].tolist()
}
```

### Task 6: Dimensionality Reduction
Apply dimensionality reduction for feature creation:

```python
# Example: Dimensionality reduction with PCA
# 1. Implement PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X.fillna(0))

pca = PCA()
pca.fit(X_scaled)

# Calculate explained variance
explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

# Plot explained variance
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(range(1, len(explained_variance) + 1), explained_variance)
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance by Component')

plt.subplot(1, 2, 2)
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, 'o-')
plt.axhline(y=0.8, color='r', linestyle='--')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Cumulative Explained Variance')
plt.tight_layout()
plt.savefig('plots/pca_explained_variance.png', dpi=300)
plt.close()

# 2. Create PCA features
n_components = np.argmax(cumulative_variance >= 0.8) + 1
print(f"Number of components to explain 80% variance: {n_components}")

pca_reduced = PCA(n_components=n_components)
principal_components = pca_reduced.fit_transform(X_scaled)

# Create PCA feature DataFrame
pca_cols = [f'PC{i+1}' for i in range(n_components)]
pca_df = pd.DataFrame(principal_components, columns=pca_cols, index=X.index)

# 3. Visualize first two principal components
plt.figure(figsize=(10, 8))
positions = df['position'].values
position_colors = {'F': 'red', 'MF': 'blue', 'D': 'green', 'GK': 'purple'}
colors = [position_colors.get(pos, 'gray') for pos in positions]

scatter = plt.scatter(pca_df['PC1'], pca_df['PC2'], c=colors, alpha=0.7)
plt.xlabel(f'PC1 ({explained_variance[0]:.2%} variance)')
plt.ylabel(f'PC2 ({explained_variance[1]:.2%} variance)')
plt.title('PCA: First Two Principal Components')

# Add position legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=v, label=k, markersize=8) 
           for k, v in position_colors.items()]
plt.legend(handles=handles, title='Position')
plt.savefig('plots/pca_visualization.png', dpi=300)
plt.close()

# 4. Interpret components
component_df = pd.DataFrame(
    pca_reduced.components_,
    columns=X.columns,
    index=pca_cols
)

# Visualize component loadings for PC1 and PC2
plt.figure(figsize=(12, 10))
loadings = component_df.iloc[:2]  # PC1 and PC2

# Get top contributing features
n_top = 10
top_features = {}
for i, pc in enumerate(loadings.index):
    sorted_loadings = loadings.iloc[i].abs().sort_values(ascending=False)
    top_features[pc] = sorted_loadings.index[:n_top].tolist()

# Plot PC1 loadings
plt.subplot(2, 1, 1)
pc1_loadings = loadings.iloc[0].sort_values()
plt.barh(range(len(pc1_loadings[-n_top:])), pc1_loadings[-n_top:].values)
plt.yticks(range(len(pc1_loadings[-n_top:])), pc1_loadings[-n_top:].index)
plt.xlabel('Loading Value')
plt.title('PC1 Top Feature Loadings')

# Plot PC2 loadings
plt.subplot(2, 1, 2)
pc2_loadings = loadings.iloc[1].sort_values()
plt.barh(range(len(pc2_loadings[-n_top:])), pc2_loadings[-n_top:].values)
plt.yticks(range(len(pc2_loadings[-n_top:])), pc2_loadings[-n_top:].index)
plt.xlabel('Loading Value')
plt.title('PC2 Top Feature Loadings')

plt.tight_layout()
plt.savefig('plots/pca_component_loadings.png', dpi=300)
plt.close()

# Return results
dim_reduction_results = {
    'pca': pca,
    'explained_variance': explained_variance,
    'cumulative_variance': cumulative_variance,
    'n_components': n_components,
    'pca_features': pca_df,
    'component_loadings': component_df,
    'top_features': top_features
}
```

### Task 7: Feature Importance Visualization
Create comprehensive visualizations of feature importance:

```python
# Example: Feature importance visualization across methods
# Collect feature importance from different methods
feature_importance = pd.DataFrame({'feature': X.columns})

# Add importance from different methods
feature_importance['pearson'] = feature_importance['feature'].map(
    dict(zip(pearson_df.index, pearson_df['correlation'].abs()))
).fillna(0)

feature_importance['mutual_info'] = feature_importance['feature'].map(
    dict(zip(mi_scores['feature'], mi_scores['mi_score']))
).fillna(0)

feature_importance['lasso'] = feature_importance['feature'].map(
    dict(zip(lasso_coef['feature'], lasso_coef['coefficient'].abs()))
).fillna(0)

feature_importance['random_forest'] = feature_importance['feature'].map(
    dict(zip(rf_importance['feature'], rf_importance['importance']))
).fillna(0)

# Normalize each method's scores to 0-1 scale
for method in ['pearson', 'mutual_info', 'lasso', 'random_forest']:
    max_value = feature_importance[method].max()
    if max_value > 0:
        feature_importance[method] = feature_importance[method] / max_value

# Calculate average importance across methods
feature_importance['avg_importance'] = feature_importance[
    ['pearson', 'mutual_info', 'lasso', 'random_forest']
].mean(axis=1)

# Sort by average importance
feature_importance = feature_importance.sort_values('avg_importance', ascending=False)

# Create heatmap of top features
top_n = 20
top_features = feature_importance.head(top_n)['feature'].tolist()
importance_heatmap = feature_importance[
    feature_importance['feature'].isin(top_features)
].set_index('feature')[['pearson', 'mutual_info', 'lasso', 'random_forest']]

plt.figure(figsize=(12, 10))
sns.heatmap(importance_heatmap, cmap='viridis', annot=True, fmt='.2f')
plt.title(f'Feature Importance Across Methods (Top {top_n} Features)')
plt.savefig('plots/feature_importance_heatmap.png', dpi=300)
plt.close()

# Create bar chart of average importance
plt.figure(figsize=(12, 10))
plt.barh(
    range(top_n),
    feature_importance.head(top_n)['avg_importance'].values,
    align='center'
)
plt.yticks(range(top_n), feature_importance.head(top_n)['feature'])
plt.xlabel('Average Importance')
plt.title(f'Top {top_n} Features by Average Importance')
plt.tight_layout()
plt.savefig('plots/average_feature_importance.png', dpi=300)
plt.close()

# Create correlation matrix of top features
top_feature_corr = X[top_features].corr()

plt.figure(figsize=(12, 10))
mask = np.triu(np.ones_like(top_feature_corr, dtype=bool))
sns.heatmap(
    top_feature_corr, 
    mask=mask, 
    cmap='coolwarm', 
    annot=True, 
    fmt='.2f',
    square=True
)
plt.title('Correlation Matrix of Top Features')
plt.tight_layout()
plt.savefig('plots/top_feature_correlation.png', dpi=300)
plt.close()

# Return visualization results
visualization_results = {
    'feature_importance': feature_importance,
    'top_features': top_features,
    'importance_heatmap': importance_heatmap,
    'top_feature_correlation': top_feature_corr
}
```

### Task 8: Soccer Analytics Feature Evaluation
Evaluate the impact of engineered features on soccer analytics models:

```python
# Example: Evaluate feature sets for soccer analytics models
# Create feature sets to compare
feature_sets = {
    'original': [col for col in df.columns if col != target and df[col].dtype != 'object'],
    'basic': list(df_basic.columns),
    'soccer': list(df_soccer.columns),
    'advanced': list(df_advanced.columns),
    'statistical_top': statistical_results['top_pearson'][:15],
    'model_based_top': model_results['consensus_features'][:15],
    'pca': list(pca_df.columns)
}

# Add an "all features" set
all_features = []
for feature_set in ['original', 'basic', 'soccer', 'advanced']:
    all_features.extend(feature_sets[feature_set])
feature_sets['all'] = list(set(all_features))  # Remove duplicates

# Create model evaluation function
def evaluate_feature_set(features, target_col):
    # Prepare data
    X = df_features[features].fillna(0)
    y = df_features[target_col]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train and evaluate models
    models = {
        'linear': LinearRegression(),
        'lasso': Lasso(alpha=0.01),
        'random_forest': RandomForestRegressor(n_estimators=100, random_state=42)
    }
    
    results = {}
    for name, model in models.items():
        # Train model
        model.fit(X_train, y_train)
        
        # Evaluate
        train_pred = model.predict(X_train)
        test_pred = model.predict(X_test)
        
        train_r2 = r2_score(y_train, train_pred)
        test_r2 = r2_score(y_test, test_pred)
        test_mse = mean_squared_error(y_test, test_pred)
        
        # Store results
        results[name] = {
            'train_r2': train_r2,
            'test_r2': test_r2,
            'test_mse': test_mse
        }
    
    return results

# Evaluate each feature set
evaluation_results = {}
for set_name, features in feature_sets.items():
    print(f"Evaluating feature set: {set_name} ({len(features)} features)")
    evaluation_results[set_name] = evaluate_feature_set(features, target)

# Create comparison DataFrame
comparison_rows = []
for set_name, set_results in evaluation_results.items():
    for model_name, metrics in set_results.items():
        comparison_rows.append({
            'Feature Set': set_name,
            'Model': model_name,
            'Train R²': metrics['train_r2'],
            'Test R²': metrics['test_r2'],
            'Test MSE': metrics['test_mse']
        })

comparison_df = pd.DataFrame(comparison_rows)

# Plot comparison
plt.figure(figsize=(14, 8))

# Plot test R² by feature set and model
sns.barplot(
    x='Feature Set', 
    y='Test R²', 
    hue='Model', 
    data=comparison_df,
    palette='viridis'
)
plt.title('Model Performance Comparison Across Feature Sets')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig('plots/feature_set_comparison.png', dpi=300)
plt.close()

# Identify best feature sets for each model
best_sets = comparison_df.loc[
    comparison_df.groupby('Model')['Test R²'].idxmax()
][['Model', 'Feature Set', 'Test R²']]

print("Best feature sets by model:")
print(best_sets)

# Return evaluation results
model_evaluation = {
    'feature_sets': feature_sets,
    'evaluation_results': evaluation_results,
    'comparison': comparison_df,
    'best_sets': best_sets
}
```

## Hints and Tips

1. **Domain Knowledge**:
   - Leverage soccer-specific knowledge when creating features
   - Consider position context (forwards, midfielders, defenders have different roles)
   - Account for minutes played in all metrics (per-90 is standard in soccer)
   - Create composite metrics that reflect overall contribution

2. **Feature Engineering Best Practices**:
   - Start with simple transformations before complex ones
   - Create features that have interpretable meaning
   - Watch out for multicollinearity in engineered features
   - Create visualization-ready features (normalize where appropriate)

3. **Feature Selection Guidelines**:
   - Use multiple methods to identify important features
   - Consider both statistical and model-based approaches
   - Look for consensus across different methods
   - Remember that different models may benefit from different features

4. **Practical Considerations**:
   - Handle missing values appropriately for each feature
   - Scale features when working with distance-based algorithms
   - Document your engineered features for transparency
   - Consider the computational cost of complex feature engineering

5. **Soccer Analytics Context**:
   - Performance metrics should account for position
   - Efficiency is often more important than raw counts
   - Consider the team context when evaluating individual performance
   - Age is a key factor in player development and valuation

## Extension Opportunities

1. **Time-based Features**: Analyze player performance trends over a season

2. **Text Analysis**: Extract features from player descriptions or scouting reports

3. **Physical Attributes**: Develop complex features that model physical performance

4. **Expected Goals (xG)**: Create an expected goals model using shot characteristics

5. **Player Similarity**: Engineer features that help identify similar players

6. **Tactical Compatibility**: Create features that measure how well players might work together

7. **Automated Feature Engineering**: Implement automated feature generation and selection

## Resources

- [Feature Engineering for Machine Learning](https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/)
- [Scikit-learn Feature Selection Documentation](https://scikit-learn.org/stable/modules/feature_selection.html)
- [Soccer Analytics Metrics Guide](https://fbref.com/en/expected-goals-model-explained/)
- [Advanced Soccer Metrics](https://statsbomb.com/articles/soccer/statsbomb-data-our-metrics/)
- [PCA Explanation](https://setosa.io/ev/principal-component-analysis/)
- [Feature Selection Techniques](https://towardsdatascience.com/feature-selection-techniques-in-machine-learning-with-python-f24e7da3f36e)
- [Soccer Performance Analysis](https://www.statsperform.com/resource/football-player-performance-analysis/)

## Submission

Complete the implementation of the functions in `feature_engineering.py`. When you run the script, it should execute all feature engineering tasks and generate visualization files in the 'plots' directory.