# Clustering and Classification Challenge

## Overview
Welcome to the Clustering and Classification Challenge! In this assignment, you'll apply unsupervised learning techniques to identify natural groupings and patterns in soccer player data. Clustering helps reveal hidden structures and relationships that might not be immediately obvious from raw statistics. For soccer analytics, clustering can identify player archetypes, tactical patterns, and similarity between players with different statistical profiles.

## Learning Objectives
- Apply various clustering algorithms to soccer player data
- Determine optimal clustering parameters and evaluate results
- Visualize high-dimensional data for pattern recognition
- Interpret clusters to create meaningful player archetypes
- Compare different clustering approaches for specific analytics tasks
- Apply dimensionality reduction techniques for visualization

## NCAA Soccer Application
Clustering techniques offer several valuable applications for NCAA Division II soccer analysis:
- Identify similar player types for recruitment and scouting
- Group players with similar skill sets for tactical decision-making
- Discover natural position groupings beyond traditional designations
- Find undervalued players with similar profiles to top performers
- Develop position-specific performance benchmarks
- Analyze team playing styles and tactical approaches

## Conceptual Background

### Clustering Fundamentals
Clustering is an unsupervised learning approach that groups similar data points together based on their features. The core algorithms include:

1. **K-means**: Partitions data into k clusters by minimizing within-cluster variance
2. **Hierarchical Clustering**: Builds nested clusters by merging or splitting them successively
3. **DBSCAN**: Density-based clustering that can find arbitrarily shaped clusters and identify outliers
4. **Gaussian Mixture Models**: Probabilistic model assuming data points are generated from a mixture of Gaussian distributions

### Clustering Evaluation
Without ground truth labels, clustering quality is evaluated through intrinsic metrics:
- **Silhouette Score**: Measures how similar points are to their own cluster compared to other clusters
- **Calinski-Harabasz Index**: Ratio of between-cluster to within-cluster dispersion
- **Davies-Bouldin Index**: Average similarity between clusters (lower is better)

### Dimensionality Reduction
High-dimensional data can be difficult to visualize and analyze. Techniques to reduce dimensionality include:
- **Principal Component Analysis (PCA)**: Linear transformation that maximizes variance
- **t-SNE**: Non-linear technique that preserves local relationships
- **UMAP**: Manifold learning technique that preserves both local and global structure

## Challenge Tasks

### Task 1: K-means Clustering
Implement K-means clustering and determine the optimal number of clusters:

```python
# Example: K-means clustering with elbow method
# Determine optimal number of clusters
inertia = []
silhouette_scores = []
k_range = range(2, 10)

for k in k_range:
    # Create and fit K-means model
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    
    # Get cluster assignments
    labels = kmeans.labels_
    
    # Calculate metrics
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, labels))

# Plot elbow method
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(k_range, inertia, 'o-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia (Within-Cluster Sum of Squares)')
plt.title('Elbow Method for Optimal k')

plt.subplot(1, 2, 2)
plt.plot(k_range, silhouette_scores, 'o-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score for Optimal k')
plt.tight_layout()
plt.savefig('plots/kmeans_elbow_method.png', dpi=300)
plt.close()

# Use the optimal k (let's say k=4 from analysis)
optimal_k = 4
optimal_kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
optimal_kmeans.fit(X_scaled)
labels = optimal_kmeans.labels_

# Reduce dimensions for visualization using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot clusters
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', 
                     alpha=0.8, s=100, edgecolors='k')
plt.xlabel(f'Principal Component 1 ({pca.explained_variance_ratio_[0]:.2%} variance)')
plt.ylabel(f'Principal Component 2 ({pca.explained_variance_ratio_[1]:.2%} variance)')
plt.title(f'K-means Clustering (k={optimal_k})')
plt.colorbar(scatter, label='Cluster')
plt.savefig('plots/kmeans_clusters_pca.png', dpi=300)
plt.close()
```

### Task 2: Hierarchical Clustering
Implement hierarchical clustering and explore different linkage methods:

```python
# Example: Hierarchical clustering with dendrogram
# Create linkage matrix
Z = linkage(X_scaled, method='ward')

# Plot dendrogram
plt.figure(figsize=(12, 8))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Player Index')
plt.ylabel('Distance')
dendrogram(
    Z,
    truncate_mode='lastp',  # Show only the last p merged clusters
    p=10,  # Show only the last p merged clusters
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,  # Show contracted nodes as a triangle
)
plt.axhline(y=6, color='r', linestyle='--')  # Draw a horizontal line where to cut
plt.savefig('plots/hierarchical_dendrogram.png', dpi=300)
plt.close()

# Implement Agglomerative Clustering with different linkages
linkage_methods = ['ward', 'complete', 'average', 'single']
silhouette_scores = []

for method in linkage_methods:
    # Create and fit the model
    model = AgglomerativeClustering(n_clusters=4, linkage=method)
    labels = model.fit_predict(X_scaled)
    
    # Calculate silhouette score
    score = silhouette_score(X_scaled, labels)
    silhouette_scores.append(score)
    
    # Plot clusters
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', 
                         alpha=0.8, s=100, edgecolors='k')
    plt.xlabel(f'Principal Component 1')
    plt.ylabel(f'Principal Component 2')
    plt.title(f'Hierarchical Clustering (Linkage: {method})')
    plt.colorbar(scatter, label='Cluster')
    plt.savefig(f'plots/hierarchical_clusters_{method}.png', dpi=300)
    plt.close()

# Compare linkage methods
plt.figure(figsize=(10, 6))
plt.bar(linkage_methods, silhouette_scores)
plt.xlabel('Linkage Method')
plt.ylabel('Silhouette Score')
plt.title('Hierarchical Clustering: Linkage Method Comparison')
plt.savefig('plots/hierarchical_linkage_comparison.png', dpi=300)
plt.close()
```

### Task 3: DBSCAN Clustering
Implement DBSCAN clustering to identify dense regions and potential outliers:

```python
# Example: DBSCAN clustering
# Determine appropriate epsilon with k-distance graph
from sklearn.neighbors import NearestNeighbors

# Calculate distances
neighbors = NearestNeighbors(n_neighbors=5)
neighbors_fit = neighbors.fit(X_scaled)
distances, indices = neighbors_fit.kneighbors(X_scaled)

# Sort distances
distances = np.sort(distances[:, 4])  # Get the distance to the 5th nearest neighbor

# Plot k-distance graph
plt.figure(figsize=(10, 6))
plt.plot(distances)
plt.xlabel('Points (sorted)')
plt.ylabel('Distance to 5th Nearest Neighbor')
plt.title('K-Distance Graph for DBSCAN Epsilon Selection')
plt.axhline(y=0.5, color='r', linestyle='--')  # Example threshold
plt.savefig('plots/dbscan_kdistance.png', dpi=300)
plt.close()

# Implement DBSCAN with selected parameters
epsilon = 0.5  # Example value based on k-distance graph
min_samples = 5

dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
dbscan_labels = dbscan.fit_predict(X_scaled)

# Identify number of clusters and noise points
n_clusters = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
n_noise = list(dbscan_labels).count(-1)

print(f'DBSCAN found {n_clusters} clusters and {n_noise} noise points')

# Plot the clusters
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=dbscan_labels, cmap='viridis', 
                     alpha=0.8, s=100, edgecolors='k')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title(f'DBSCAN Clustering (eps={epsilon}, min_samples={min_samples})')
plt.colorbar(scatter, label='Cluster')

# Highlight noise points
noise_mask = dbscan_labels == -1
plt.scatter(X_pca[noise_mask, 0], X_pca[noise_mask, 1], 
           s=150, linewidths=2, c='red', marker='x', label='Outliers')
plt.legend()
plt.savefig('plots/dbscan_clusters.png', dpi=300)
plt.close()
```

### Task 4: Gaussian Mixture Models
Implement Gaussian Mixture Models for soft clustering:

```python
# Example: Gaussian Mixture Models
# Determine optimal number of components using BIC
n_components_range = range(1, 10)
bic_scores = []
aic_scores = []

for n_components in n_components_range:
    # Fit GMM
    gmm = GaussianMixture(n_components=n_components, random_state=42, 
                         covariance_type='full', n_init=5)
    gmm.fit(X_scaled)
    
    # Calculate metrics
    bic_scores.append(gmm.bic(X_scaled))
    aic_scores.append(gmm.aic(X_scaled))

# Plot BIC and AIC
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(n_components_range, bic_scores, 'o-')
plt.xlabel('Number of Components')
plt.ylabel('BIC Score')
plt.title('BIC for Optimal Components')

plt.subplot(1, 2, 2)
plt.plot(n_components_range, aic_scores, 'o-')
plt.xlabel('Number of Components')
plt.ylabel('AIC Score')
plt.title('AIC for Optimal Components')
plt.tight_layout()
plt.savefig('plots/gmm_bic_aic.png', dpi=300)
plt.close()

# Use the optimal number of components (e.g., 4)
optimal_n = 4
gmm = GaussianMixture(n_components=optimal_n, random_state=42, 
                      covariance_type='full', n_init=5)
gmm.fit(X_scaled)

# Get cluster assignments and probabilities
gmm_labels = gmm.predict(X_scaled)
gmm_probs = gmm.predict_proba(X_scaled)

# Plot clusters
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=gmm_labels, cmap='viridis', 
                     alpha=0.8, s=100, edgecolors='k')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title(f'Gaussian Mixture Model (n_components={optimal_n})')
plt.colorbar(scatter, label='Cluster')
plt.savefig('plots/gmm_clusters.png', dpi=300)
plt.close()

# Visualize probability distributions for a player
example_player_idx = 0
plt.figure(figsize=(8, 6))
plt.bar(range(optimal_n), gmm_probs[example_player_idx])
plt.xlabel('Component')
plt.ylabel('Probability')
plt.title(f'GMM Component Probabilities for Player {example_player_idx}')
plt.savefig('plots/gmm_player_probabilities.png', dpi=300)
plt.close()
```

### Task 5: Cluster Comparison
Compare the results of different clustering algorithms:

```python
# Example: Comparing clustering algorithms
# Create a function to generate silhouette plots for visual comparison
def plot_silhouette(X, labels, algorithm_name):
    silhouette_avg = silhouette_score(X, labels)
    sample_silhouette_values = silhouette_samples(X, labels)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    
    plt.figure(figsize=(10, 8))
    y_lower = 10
    
    for i in range(n_clusters):
        # Aggregate silhouette scores for samples in cluster i
        ith_cluster_values = sample_silhouette_values[labels == i]
        ith_cluster_values.sort()
        
        size_cluster_i = ith_cluster_values.shape[0]
        y_upper = y_lower + size_cluster_i
        
        plt.fill_betweenx(np.arange(y_lower, y_upper),
                         0, ith_cluster_values,
                         alpha=0.7)
        
        # Label the silhouette plots with cluster numbers
        plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        
        # Compute the new y_lower for next plot
        y_lower = y_upper + 10
    
    plt.xlabel("Silhouette coefficient values")
    plt.ylabel("Cluster label")
    plt.axvline(x=silhouette_avg, color="red", linestyle="--")
    plt.title(f"Silhouette Plot for {algorithm_name}\nAverage Silhouette Score: {silhouette_avg:.3f}")
    plt.savefig(f'plots/silhouette_{algorithm_name}.png', dpi=300)
    plt.close()

# Create comparison table
comparison_data = {
    'Algorithm': ['K-means', 'Hierarchical', 'DBSCAN', 'GMM'],
    'Silhouette': [
        silhouette_score(X_scaled, kmeans_labels),
        silhouette_score(X_scaled, hierarchical_labels),
        silhouette_score(X_scaled, dbscan_labels[dbscan_labels != -1], 
                        X_scaled[dbscan_labels != -1]),  # Excluding noise
        silhouette_score(X_scaled, gmm_labels)
    ],
    'Calinski-Harabasz': [
        calinski_harabasz_score(X_scaled, kmeans_labels),
        calinski_harabasz_score(X_scaled, hierarchical_labels),
        calinski_harabasz_score(X_scaled[dbscan_labels != -1], 
                               dbscan_labels[dbscan_labels != -1]),  # Excluding noise
        calinski_harabasz_score(X_scaled, gmm_labels)
    ],
    'Davies-Bouldin': [
        davies_bouldin_score(X_scaled, kmeans_labels),
        davies_bouldin_score(X_scaled, hierarchical_labels),
        davies_bouldin_score(X_scaled[dbscan_labels != -1], 
                            dbscan_labels[dbscan_labels != -1]),  # Excluding noise
        davies_bouldin_score(X_scaled, gmm_labels)
    ],
    'Num Clusters': [
        len(set(kmeans_labels)),
        len(set(hierarchical_labels)),
        len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0),
        len(set(gmm_labels))
    ]
}

comparison_df = pd.DataFrame(comparison_data)

# Plot comparison metrics
metrics = ['Silhouette', 'Calinski-Harabasz', 'Davies-Bouldin']
plt.figure(figsize=(15, 5))

for i, metric in enumerate(metrics):
    plt.subplot(1, 3, i+1)
    bars = plt.bar(comparison_df['Algorithm'], comparison_df[metric])
    plt.title(metric)
    plt.xticks(rotation=45)
    
    # For Davies-Bouldin, lower is better
    if metric == 'Davies-Bouldin':
        best_idx = comparison_df[metric].values.argmin()
    else:
        best_idx = comparison_df[metric].values.argmax()
    
    # Highlight the best algorithm
    bars[best_idx].set_color('green')

plt.tight_layout()
plt.savefig('plots/clustering_comparison.png', dpi=300)
plt.close()
```

### Task 6: Cluster Interpretation
Interpret clusters and create player archetypes:

```python
# Example: Interpreting clusters from K-means
# Add cluster labels to original data
df_clustered = df.copy()
df_clustered['cluster'] = kmeans_labels

# Calculate summary statistics for each cluster
cluster_stats = df_clustered.groupby('cluster').agg({
    'speed': 'mean',
    'dribbling': 'mean',
    'shooting': 'mean',
    'passing': 'mean',
    'defending': 'mean',
    'physicality': 'mean',
    'goals_per_90': 'mean',
    'assists_per_90': 'mean',
    'height': 'mean',
    'weight': 'mean',
    'position': lambda x: x.value_counts().index[0]  # Most common position
}).round(2)

# Create radar charts for each cluster
categories = ['Speed', 'Dribbling', 'Shooting', 'Passing', 'Defending', 'Physicality']
min_vals = df[['speed', 'dribbling', 'shooting', 'passing', 'defending', 'physicality']].min()
max_vals = df[['speed', 'dribbling', 'shooting', 'passing', 'defending', 'physicality']].max()

# Normalize values for radar chart
def normalize_row(row):
    return [(val - min_vals[i]) / (max_vals[i] - min_vals[i]) 
            for i, val in enumerate(row)]

plt.figure(figsize=(15, 10))
for i, cluster in enumerate(cluster_stats.index):
    values = cluster_stats.iloc[i][['speed', 'dribbling', 'shooting', 'passing', 
                                   'defending', 'physicality']].values
    
    # Normalize values
    normalized_values = normalize_row(values)
    
    # Create angles for radar chart
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    
    # Complete the loop
    normalized_values = np.concatenate((normalized_values, [normalized_values[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    categories_plot = categories + [categories[0]]
    
    # Create subplot
    ax = plt.subplot(2, 2, i+1, polar=True)
    ax.plot(angles, normalized_values, 'o-', linewidth=2)
    ax.fill(angles, normalized_values, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)
    most_common_pos = cluster_stats.iloc[i]['position']
    n_players = (df_clustered['cluster'] == cluster).sum()
    ax.set_title(f'Cluster {cluster} Profile\n'
                f'Most Common Position: {most_common_pos}\n'
                f'Number of Players: {n_players}')

plt.tight_layout()
plt.savefig('plots/cluster_radar_profiles.png', dpi=300)
plt.close()

# Create player archetype descriptions based on profiles
archetypes = {
    0: "Speed Dribblers: High speed and dribbling, average shooting and passing",
    1: "Target Forwards: Excellent shooting and physicality, lower passing",
    2: "Playmakers: Superior passing and good dribbling, average defending",
    3: "Defensive Specialists: Strong defending and physicality, lower attacking stats"
}

for cluster, description in archetypes.items():
    print(f"Cluster {cluster}: {description}")
```

### Task 7: Dimensionality Reduction
Implement dimensionality reduction techniques for visualization:

```python
# Example: PCA for dimensionality reduction and component interpretation
# Implement PCA
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

# Plot explained variance
plt.figure(figsize=(10, 6))
explained_variance = pca.explained_variance_ratio_
plt.bar(range(len(explained_variance)), explained_variance)
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('PCA Explained Variance')
plt.xticks(range(len(explained_variance)))
plt.savefig('plots/pca_explained_variance.png', dpi=300)
plt.close()

# Plot 2D projection
plt.figure(figsize=(12, 10))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans_labels, 
                     cmap='viridis', alpha=0.8, s=100, edgecolors='k')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%} variance)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%} variance)')
plt.title('PCA 2D Projection of Player Data with Cluster Labels')
plt.colorbar(scatter, label='Cluster')

# Add annotations for some points
for i in range(0, len(X_pca), 20):  # Annotate every 20th point
    plt.annotate(
        df.iloc[i]['name'],
        (X_pca[i, 0], X_pca[i, 1]),
        xytext=(5, 5),
        textcoords='offset points'
    )

plt.savefig('plots/pca_2d_projection.png', dpi=300)
plt.close()

# Create 3D projection with Plotly
fig = px.scatter_3d(
    x=X_pca[:, 0], y=X_pca[:, 1], z=X_pca[:, 2],
    color=kmeans_labels,
    labels={
        'x': f'PC1 ({pca.explained_variance_ratio_[0]:.2%})',
        'y': f'PC2 ({pca.explained_variance_ratio_[1]:.2%})',
        'z': f'PC3 ({pca.explained_variance_ratio_[2]:.2%})'
    },
    title='PCA 3D Projection of Player Data'
)
fig.update_traces(marker=dict(size=5))
fig.write_html('plots/pca_3d_projection.html')

# Interpret principal components
component_df = pd.DataFrame(
    pca.components_,
    columns=feature_names
)

# Visualize component loadings
plt.figure(figsize=(12, 8))
sns.heatmap(component_df, annot=True, cmap='coolwarm', fmt='.2f')
plt.xlabel('Feature')
plt.ylabel('Principal Component')
plt.title('PCA Component Loadings')
plt.savefig('plots/pca_component_loadings.png', dpi=300)
plt.close()
```

### Task 8: Position-based Clustering
Implement position-specific clustering:

```python
# Example: Position-specific clustering
positions = df['position'].unique()
position_clusters = {}

plt.figure(figsize=(15, 15))
plot_idx = 1

for position in positions:
    # Filter data for this position
    pos_df = df[df['position'] == position]
    
    # Skip if not enough players
    if len(pos_df) < 10:
        continue
    
    # Select features for clustering
    X_pos = pos_df[['speed', 'dribbling', 'shooting', 'passing', 
                    'defending', 'physicality']].values
    
    # Scale the data
    scaler = StandardScaler()
    X_pos_scaled = scaler.fit_transform(X_pos)
    
    # Determine optimal k (simplified approach)
    max_k = min(5, len(pos_df) // 2)
    k_values = range(2, max_k + 1)
    inertias = []
    
    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_pos_scaled)
        inertias.append(kmeans.inertia_)
    
    # Choose k based on elbow method (here simplified)
    optimal_k = 2  # Default if only 2 k values
    if len(k_values) > 2:
        # Simple heuristic for elbow point
        inertia_diffs = np.diff(inertias)
        optimal_k = k_values[1 + np.argmax(np.diff(inertia_diffs))]
    
    # Perform clustering with optimal k
    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    pos_labels = kmeans.fit_predict(X_pos_scaled)
    
    # Store results
    position_clusters[position] = {
        'labels': pos_labels,
        'centroids': kmeans.cluster_centers_,
        'optimal_k': optimal_k
    }
    
    # Reduce dimensions with PCA for visualization
    pca = PCA(n_components=2)
    X_pos_pca = pca.fit_transform(X_pos_scaled)
    
    # Plot position-specific clusters
    plt.subplot(2, 2, plot_idx)
    scatter = plt.scatter(X_pos_pca[:, 0], X_pos_pca[:, 1], 
                         c=pos_labels, cmap='viridis', alpha=0.8, s=100, edgecolors='k')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title(f'Position: {position} (k={optimal_k})')
    plt.colorbar(scatter, label='Cluster')
    plot_idx += 1

plt.tight_layout()
plt.savefig('plots/position_specific_clusters.png', dpi=300)
plt.close()

# Create position-specific player archetypes
for position, results in position_clusters.items():
    print(f"\nPosition: {position} - {results['optimal_k']} player types identified")
    
    # Create a DataFrame with original position data + cluster labels
    pos_df = df[df['position'] == position].copy()
    pos_df['cluster'] = results['labels']
    
    # Calculate average statistics for each cluster
    cluster_stats = pos_df.groupby('cluster').agg({
        'speed': 'mean',
        'dribbling': 'mean',
        'shooting': 'mean',
        'passing': 'mean',
        'defending': 'mean',
        'physicality': 'mean'
    }).round(1)
    
    print(cluster_stats)
```

## Hints and Tips

1. **Data Preprocessing**:
   - Standardize features before clustering to ensure equal weighting
   - Remove outliers if they significantly affect cluster formation
   - Consider feature correlation and potentially remove highly correlated features
   - Create meaningful derived features when appropriate

2. **Clustering Parameters**:
   - Use appropriate methods to determine optimal parameters (elbow method, silhouette score)
   - For K-means, try different initializations to avoid local minima
   - For DBSCAN, use k-distance plots to select eps parameter
   - For hierarchical clustering, experiment with different linkage methods

3. **Visualization Tips**:
   - Use dimensionality reduction to visualize high-dimensional data
   - Apply consistent color schemes across different visualizations
   - Add meaningful annotations to highlight key data points
   - Create radar charts for multi-dimensional cluster profiles

4. **Cluster Interpretation**:
   - Calculate summary statistics for each cluster
   - Identify distinctive features that characterize each cluster
   - Connect cluster profiles to soccer-specific concepts
   - Validate clusters against domain knowledge

5. **Soccer Context**:
   - Consider position-specific analytics when interpreting clusters
   - Understand that player roles may transcend traditional positions
   - Create archetypes that have tactical meaning for coaches
   - Connect clustering results to recruitment and player development

## Extension Opportunities

1. **Hybrid Clustering**: Combine multiple clustering techniques for improved results

2. **Semi-supervised Clustering**: Use some labeled data to guide the clustering process

3. **Time Series Clustering**: Cluster player performance trajectories over multiple games

4. **Spatial Clustering**: Apply clustering to player movement data on the pitch

5. **Dynamic Clustering**: Develop clustering that adapts to different game contexts

6. **Tactical Clustering**: Apply clustering to team-level metrics to identify playing styles

7. **Interactive Dashboards**: Create interactive visualizations to explore cluster characteristics

## Resources

- [Scikit-learn Clustering Documentation](https://scikit-learn.org/stable/modules/clustering.html)
- [Visualization Techniques for Clustering](https://towardsdatascience.com/10-tips-for-visualizing-high-dimensional-clustering-results-using-python-8ece7c3599d)
- [Soccer Clustering Examples](https://statsbomb.com/articles/soccer/introducing-statsbomb-player-roles/)
- [PCA for Dimensionality Reduction](https://scikit-learn.org/stable/modules/decomposition.html#pca)
- [Silhouette Analysis](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)
- [DBSCAN Parameter Selection](https://towardsdatascience.com/machine-learning-clustering-dbscan-determine-the-optimal-value-for-epsilon-eps-python-example-3100091cfbc)
- [Player Archetype Analysis](https://dtai.cs.kuleuven.be/sports/blog/exploring-passing-archetypes-in-football)

## Submission

Complete the implementation of the functions in `clustering.py`. When you run the script, it should execute all clustering tasks and generate visualization files in the 'plots' directory.