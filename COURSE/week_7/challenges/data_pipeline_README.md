# Challenge 4: Soccer Data Processing Pipeline

**Difficulty: ⭐⭐⭐⭐☆**

## Challenge Overview

In this challenge, you'll build a complete data processing pipeline for soccer analytics. This pipeline will handle the end-to-end flow of soccer data from collection through transformation to final analysis, implementing Extract-Transform-Load (ETL) principles in a modular, extensible way.

## Learning Objectives

- Design modular, extensible data processing architecture
- Implement Extract-Transform-Load (ETL) workflows
- Create reusable components for data processing
- Handle multiple data sources and formats
- Implement caching and optimization strategies
- Apply object-oriented design to data processing

## Real-World Context

NCAA soccer programs need automated data pipelines that can regularly collect, process, and analyze player and team statistics. These pipelines must be robust, efficient, and able to handle various data sources and formats. In production environments, such pipelines run on schedules, process large volumes of data, and feed dashboards and analytics tools that coaches and analysts use daily. Building efficient, maintainable data pipelines is a critical skill for sports analytics professionals who need to provide timely, accurate insights to their organizations.

## Challenge Details

### The Task

Your task is to create a complete data processing pipeline that:

1. Extracts data from various sources (CSV files, JSON, APIs, databases)
2. Transforms the data through cleaning, feature engineering, and aggregation
3. Loads the processed data to destinations for analysis and visualization
4. Implements caching for performance optimization
5. Provides a modular, extensible framework for future enhancements

### Pipeline Architecture

```
                    +---------------------+
                    |   Pipeline Manager  |
                    +---------------------+
                              |
      +---------------------+---------------------+
      |                     |                     |
+------------+     +----------------+     +------------+
|   Sources  |     |  Transformers  |     |  Loaders   |
+------------+     +----------------+     +------------+
| CSV Source |     | Cleaner        |     | CSV Loader |
| JSON Source|     | Feature Eng.   |     | DB Loader  |
| API Source |     | Aggregator     |     | JSON Loader|
| DB Source  |     | Normalizer     |     |            |
+------------+     +----------------+     +------------+
      |                     |                     |
      |                     v                     |
      |         +---------------------+           |
      +-------->|    Cache Manager    |<----------+
                +---------------------+
```

## Tips and Hints

### Data Source Implementation

Creating a flexible data source system:

```python
class DataSource:
    """Base class for all data sources."""
    def __init__(self, name):
        self.name = name
    
    def extract(self):
        """Extract data from source."""
        raise NotImplementedError("Subclasses must implement extract()")

class CSVDataSource(DataSource):
    """Data source for CSV files."""
    def __init__(self, name, file_path, **kwargs):
        super().__init__(name)
        self.file_path = file_path
        self.kwargs = kwargs
    
    def extract(self):
        """Extract data from CSV file."""
        try:
            logging.info(f"Loading data from {self.file_path}")
            return pd.read_csv(self.file_path, **self.kwargs)
        except Exception as e:
            logging.error(f"Error loading {self.file_path}: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error
```

### Transformer Implementation

Creating data transformers:

```python
class Transformer:
    """Base class for all data transformers."""
    def __init__(self, name):
        self.name = name
    
    def transform(self, data):
        """Transform the input data."""
        raise NotImplementedError("Subclasses must implement transform()")

class CleaningTransformer(Transformer):
    """Transformer for cleaning data."""
    def __init__(self, name, columns_to_clean=None):
        super().__init__(name)
        self.columns_to_clean = columns_to_clean
    
    def transform(self, data):
        """Clean the input data."""
        logging.info(f"Cleaning data with {self.name}")
        df = data.copy()
        
        # If no columns specified, clean all columns
        columns = self.columns_to_clean if self.columns_to_clean else df.columns
        
        for col in columns:
            if col not in df.columns:
                continue
                
            # Handle missing values based on column type
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(0)
            else:
                df[col] = df[col].fillna('')
            
            # Remove or fix invalid values
            if pd.api.types.is_numeric_dtype(df[col]):
                # Replace negative values with 0 for certain metrics
                if col in ['goals', 'assists', 'shots', 'passes']:
                    df.loc[df[col] < 0, col] = 0
        
        return df
```

### Caching for Performance

Implementing efficient caching:

```python
class Cache:
    """Cache for storing intermediate results in the pipeline."""
    def __init__(self, cache_dir='.cache'):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_key(self, data, step_name):
        """Generate a cache key based on data content and step name."""
        # Create a hash of the data and step name
        data_hash = hashlib.md5(pd.util.hash_pandas_object(data).values).hexdigest()
        step_hash = hashlib.md5(step_name.encode()).hexdigest()
        return f"{step_hash}_{data_hash}.pkl"
    
    def get(self, data, step_name):
        """Retrieve data from the cache."""
        cache_key = self._get_cache_key(data, step_name)
        cache_path = os.path.join(self.cache_dir, cache_key)
        
        if os.path.exists(cache_path):
            try:
                with open(cache_path, 'rb') as f:
                    cached_data = pickle.load(f)
                logging.info(f"Cache hit for {step_name}")
                return cached_data
            except Exception as e:
                logging.warning(f"Error reading cache: {e}")
        
        logging.info(f"Cache miss for {step_name}")
        return None
    
    def set(self, input_data, output_data, step_name):
        """Store data in the cache."""
        cache_key = self._get_cache_key(input_data, step_name)
        cache_path = os.path.join(self.cache_dir, cache_key)
        
        try:
            with open(cache_path, 'wb') as f:
                pickle.dump(output_data, f)
            logging.info(f"Cached result for {step_name}")
        except Exception as e:
            logging.warning(f"Error writing cache: {e}")
```

### Pipeline Implementation

Creating a flexible pipeline:

```python
class Pipeline:
    """Data processing pipeline for soccer analytics."""
    def __init__(self, name, use_cache=True):
        self.name = name
        self.steps = []
        self.use_cache = use_cache
        self.cache = Cache() if use_cache else None
    
    def add_source(self, source):
        """Add a data source to the pipeline."""
        self.steps.append(('source', source))
        return self
    
    def add_transformer(self, transformer):
        """Add a transformer to the pipeline."""
        self.steps.append(('transformer', transformer))
        return self
    
    def add_loader(self, loader):
        """Add a loader to the pipeline."""
        self.steps.append(('loader', loader))
        return self
    
    def run(self):
        """Run the pipeline."""
        logging.info(f"Running pipeline: {self.name}")
        data = None
        result = None
        
        for step_type, step in self.steps:
            try:
                if step_type == 'source':
                    logging.info(f"Extracting data from {step}")
                    data = step.extract()
                
                elif step_type == 'transformer' and data is not None:
                    logging.info(f"Applying transformer: {step}")
                    
                    # Try to get from cache
                    cached_result = None
                    if self.use_cache:
                        cached_result = self.cache.get(data, step.name)
                    
                    if cached_result is not None:
                        data = cached_result
                    else:
                        # Apply transformation
                        transformed_data = step.transform(data)
                        
                        # Cache the result
                        if self.use_cache:
                            self.cache.set(data, transformed_data, step.name)
                        
                        data = transformed_data
                
                elif step_type == 'loader' and data is not None:
                    logging.info(f"Loading data with: {step}")
                    result = step.load(data)
            
            except Exception as e:
                logging.error(f"Error in step {step}: {e}")
                raise
        
        return result
```

## Testing Your Solution

Your solution should:

1. Successfully extract data from various sources
2. Apply appropriate transformations to the data
3. Load the processed data to the correct destinations
4. Use caching to optimize performance on repeated runs
5. Handle errors gracefully with proper logging
6. Be modular and extensible for future enhancements

Test your pipeline with:
- Different data sources (CSV, JSON, etc.)
- Various transformations (cleaning, feature engineering, aggregation)
- Different destinations (files, databases)
- Large datasets to verify performance
- Repeated runs to verify caching benefits

## Application to Capstone

The data pipeline you build in this challenge will form the backbone of your capstone project's data processing system, enabling you to:

1. Regularly collect new NCAA soccer data from various sources
2. Process and clean the data in a consistent, repeatable way
3. Transform raw statistics into meaningful metrics and insights
4. Store processed data in formats suitable for your dashboard and analysis
5. Ensure your system is modular and maintainable

A well-designed data pipeline will make your capstone project more robust, efficient, and scalable, allowing you to focus on analysis and insights rather than data wrangling.

## Resources

- [ETL Pipeline Best Practices](https://www.alooma.com/blog/etl-pipeline-best-practices)
- [Data Pipeline Architecture Patterns](https://databricks.com/blog/2019/08/14/productionizing-machine-learning-from-deployment-to-drift-detection.html)
- [Python Design Patterns](https://python-patterns.guide/)
- [Caching in Python](https://realpython.com/python-caching/)
- [Logging in Python](https://realpython.com/python-logging/)
- [Error Handling Best Practices](https://docs.python-guide.org/writing/structure/#error-handling)