# Challenge 2: Soccer Metrics Computation with NumPy

**Difficulty: ⭐⭐⭐☆☆**

## Challenge Overview

In this challenge, you'll implement efficient numerical calculations for soccer analytics using NumPy. You'll leverage NumPy's vectorized operations to compute various performance metrics for players and teams, optimizing for both performance and accuracy.

## Learning Objectives

- Implement vectorized operations for efficient computation
- Create mathematical functions for soccer-specific metrics
- Handle special cases and edge conditions in numerical calculations
- Optimize calculations for large datasets
- Apply NumPy's statistical functions to soccer analytics

## Real-World Context

In the realm of soccer analytics, computational efficiency is crucial when processing large datasets containing statistics for hundreds of players across multiple seasons. NCAA soccer programs need to quickly calculate various performance metrics and compare players across different teams and positions. NumPy provides the foundation for these calculations, enabling fast, vectorized operations that can process thousands of data points in milliseconds, allowing coaches and analysts to get quick insights during matches or training sessions.

## Challenge Details

### The Task

Your task is to create a suite of functions that efficiently calculate various soccer performance metrics, including:

1. Basic metrics like goals per minute and shot efficiency
2. Advanced metrics like expected goals (xG) performance 
3. Custom weighted metrics that combine different aspects of performance
4. Team form and performance indicators
5. Player similarity and comparison metrics

### NumPy Computation Workflow

```
+---------------------------+
| Import Player Statistics  |
+---------------------------+
            |
            v
+---------------------------+
| Preprocess & Validate     |
+---------------------------+
            |
            v
+---------------------------+
| Calculate Basic Metrics   |
+---------------------------+
            |
            v
+---------------------------+
| Calculate Advanced Metrics|
+---------------------------+
            |
            v
+---------------------------+
| Normalize & Standardize   |
+---------------------------+
            |
            v
+---------------------------+
| Rank & Compare Players    |
+---------------------------+
            |
            v
+---------------------------+
| Generate Performance Index|
+---------------------------+
```

## Tips and Hints

### Vectorized Operations

Always use NumPy's vectorized operations instead of loops for maximum efficiency:

```python
# Inefficient way (avoid):
goals_per_minute = []
for i in range(len(goals)):
    if minutes[i] > 0:
        goals_per_minute.append(goals[i] / minutes[i])
    else:
        goals_per_minute.append(0)

# Efficient way with NumPy (recommended):
goals_per_minute = np.zeros_like(goals, dtype=float)
mask = minutes > 0
goals_per_minute[mask] = goals[mask] / minutes[mask]
```

### Handling Edge Cases

Always handle division by zero and other edge cases:

```python
def shot_efficiency(goals, shots):
    """Calculate shot efficiency (goals / shots)."""
    # Create output array filled with zeros
    efficiency = np.zeros_like(goals, dtype=float)
    
    # Only calculate for players with shots > 0
    mask = shots > 0
    efficiency[mask] = goals[mask] / shots[mask]
    
    return efficiency
```

### Player Similarity

Use vector operations to calculate player similarity:

```python
def cosine_similarity(player_metrics, reference_player):
    """Calculate cosine similarity between players."""
    # Normalize vectors for better comparison
    norms = np.sqrt(np.sum(player_metrics ** 2, axis=1))
    normalized_metrics = player_metrics / norms[:, np.newaxis]
    
    # Normalize the reference player
    ref_norm = np.sqrt(np.sum(reference_player ** 2))
    normalized_ref = reference_player / ref_norm
    
    # Calculate cosine similarity
    similarity = np.dot(normalized_metrics, normalized_ref)
    
    return similarity
```

### Weighted Metrics

Create weighted performance metrics to emphasize different aspects:

```python
def weighted_contribution(goals, assists, minutes, weights):
    """Calculate weighted contribution per 90 minutes."""
    # Apply weights to each statistic
    weighted_sum = weights['goals'] * goals + weights['assists'] * assists
    
    # Calculate per 90 minutes
    minutes_mask = minutes > 0
    contribution = np.zeros_like(goals, dtype=float)
    contribution[minutes_mask] = weighted_sum[minutes_mask] * 90 / minutes[minutes_mask]
    
    return contribution
```

### Moving Window Calculations

For calculating form or trends over time:

```python
def calculate_form(results, window_size=5):
    """Calculate form based on recent results (1=win, 0=draw, -1=loss)."""
    # Initialize output array
    form = np.zeros(len(results) - window_size + 1)
    
    # Calculate moving average
    for i in range(len(form)):
        # More weight to recent matches
        weights = np.linspace(0.5, 1.0, window_size)
        weighted_results = results[i:i+window_size] * weights
        form[i] = np.sum(weighted_results) / np.sum(weights)
    
    return form
```

### Z-Score Normalization

Normalize metrics for fair comparison:

```python
def z_score_normalize(metrics):
    """Normalize metrics using z-scores."""
    mean = np.mean(metrics)
    std = np.std(metrics)
    
    # Avoid division by zero
    if std == 0:
        return np.zeros_like(metrics)
    
    return (metrics - mean) / std
```

## Testing Your Solution

Your solution should:

1. Correctly calculate all required metrics
2. Handle edge cases (e.g., division by zero) gracefully
3. Use vectorized operations for efficiency
4. Produce consistent results for identical inputs
5. Scale well with large datasets

Test your functions with:
- Edge cases (zeros, extremely large values)
- Realistic player data
- Large arrays (thousands of players)
- Different combinations of weights

## Application to Capstone

The numerical computation techniques you develop in this challenge will serve as the foundation for your capstone project's analytics engine. Your capstone will need to:

1. Process large volumes of NCAA soccer data efficiently
2. Calculate performance metrics in real-time for interactive dashboards
3. Compare players across different teams and positions
4. Identify players with similar playing styles
5. Generate comprehensive performance indices

The NumPy skills you develop here will ensure your capstone can handle these requirements efficiently, providing coaches and analysts with quick, accurate insights from the data.

## Resources

- [NumPy Documentation](https://numpy.org/doc/stable/)
- [NumPy for Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Vectorization in NumPy](https://realpython.com/numpy-array-programming/)
- [Statistical Functions in NumPy](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [Football Analytics with NumPy](https://medium.com/@ryanswanstrom/a-guide-to-numpy-and-sports-analytics-5a5acbb8e5f3)
- [Scientific Computing with NumPy](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html)