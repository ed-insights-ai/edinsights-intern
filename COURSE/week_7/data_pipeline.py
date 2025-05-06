"""
Data Pipeline Development
---------------------
Create a data processing pipeline for soccer statistics.
This exercise focuses on building a robust, multi-stage data processing system.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import logging
import time
import json
import pickle
from datetime import datetime
from functools import wraps

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("data_pipeline.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Create directories if they don't exist
os.makedirs('data', exist_ok=True)
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)
os.makedirs('data/outputs', exist_ok=True)
os.makedirs('cache', exist_ok=True)

def timer_decorator(func):
    """
    Decorator to measure the execution time of a function.
    
    Args:
        func: The function to be decorated
        
    Returns:
        wrapper: The wrapped function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Function {func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

def cache_result(cache_path):
    """
    Decorator to cache function results to a file.
    
    Args:
        cache_path (str): Path to save the cache
        
    Returns:
        decorator: The decorator function
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create a cache key based on function name, args, and kwargs
            cache_key = f"{func.__name__}_{str(args)}_{str(kwargs)}"
            cache_file = os.path.join(cache_path, f"{hash(cache_key)}.pkl")
            
            # Check if cache exists and is recent (less than 1 day old)
            if os.path.exists(cache_file):
                file_age = time.time() - os.path.getmtime(cache_file)
                if file_age < 86400:  # 24 hours in seconds
                    logger.info(f"Loading cached result for {func.__name__}")
                    with open(cache_file, 'rb') as f:
                        return pickle.load(f)
            
            # Execute the function and cache the result
            result = func(*args, **kwargs)
            with open(cache_file, 'wb') as f:
                pickle.dump(result, f)
            logger.info(f"Cached result for {func.__name__}")
            return result
        return wrapper
    return decorator

class DataSource:
    """
    Base class for data sources in the pipeline.
    
    Attributes:
        name (str): Name of the data source
        description (str): Description of the data source
    """
    
    def __init__(self, name, description=""):
        """
        Initialize a data source.
        
        Args:
            name (str): Name of the data source
            description (str, optional): Description of the data source. Defaults to "".
        """
        self.name = name
        self.description = description
    
    def get_data(self):
        """
        Get data from the source.
        
        Returns:
            pandas.DataFrame: DataFrame containing the data
        """
        raise NotImplementedError("Subclasses must implement get_data method")
    
    def __str__(self):
        """String representation of the data source."""
        return f"DataSource({self.name})"

class CSVDataSource(DataSource):
    """
    Data source that reads from a CSV file.
    
    Attributes:
        name (str): Name of the data source
        file_path (str): Path to the CSV file
        description (str): Description of the data source
    """
    
    def __init__(self, name, file_path, description=""):
        """
        Initialize a CSV data source.
        
        Args:
            name (str): Name of the data source
            file_path (str): Path to the CSV file
            description (str, optional): Description of the data source. Defaults to "".
        """
        super().__init__(name, description)
        self.file_path = file_path
    
    @timer_decorator
    def get_data(self):
        """
        Get data from the CSV file.
        
        Returns:
            pandas.DataFrame: DataFrame containing the data from the CSV file
        """
        # YOUR CODE HERE
        # 1. Check if the file exists
        # 2. Read the CSV file into a pandas DataFrame
        # 3. Return the DataFrame
        pass

class SQLDataSource(DataSource):
    """
    Data source that reads from a SQL database.
    
    Attributes:
        name (str): Name of the data source
        connection_string (str): Database connection string
        query (str): SQL query to execute
        description (str): Description of the data source
    """
    
    def __init__(self, name, connection_string, query, description=""):
        """
        Initialize a SQL data source.
        
        Args:
            name (str): Name of the data source
            connection_string (str): Database connection string
            query (str): SQL query to execute
            description (str, optional): Description of the data source. Defaults to "".
        """
        super().__init__(name, description)
        self.connection_string = connection_string
        self.query = query
    
    @timer_decorator
    def get_data(self):
        """
        Get data from the SQL database.
        
        Returns:
            pandas.DataFrame: DataFrame containing the results of the SQL query
        """
        # YOUR CODE HERE
        # 1. Connect to the database
        # 2. Execute the query and fetch the results
        # 3. Return the results as a DataFrame
        # Note: For this exercise, you can simulate this by returning dummy data
        pass

class APIDataSource(DataSource):
    """
    Data source that reads from an API.
    
    Attributes:
        name (str): Name of the data source
        api_url (str): URL of the API
        params (dict): Parameters for the API request
        description (str): Description of the data source
    """
    
    def __init__(self, name, api_url, params=None, description=""):
        """
        Initialize an API data source.
        
        Args:
            name (str): Name of the data source
            api_url (str): URL of the API
            params (dict, optional): Parameters for the API request. Defaults to None.
            description (str, optional): Description of the data source. Defaults to "".
        """
        super().__init__(name, description)
        self.api_url = api_url
        self.params = params or {}
    
    @timer_decorator
    def get_data(self):
        """
        Get data from the API.
        
        Returns:
            pandas.DataFrame: DataFrame containing the data from the API
        """
        # YOUR CODE HERE
        # 1. Make a request to the API
        # 2. Parse the response
        # 3. Return the data as a DataFrame
        # Note: For this exercise, you can simulate this by returning dummy data
        pass

class DataTransformer:
    """
    Base class for data transformers in the pipeline.
    
    Attributes:
        name (str): Name of the transformer
        description (str): Description of the transformer
    """
    
    def __init__(self, name, description=""):
        """
        Initialize a data transformer.
        
        Args:
            name (str): Name of the transformer
            description (str, optional): Description of the transformer. Defaults to "".
        """
        self.name = name
        self.description = description
    
    def transform(self, df):
        """
        Transform the data.
        
        Args:
            df (pandas.DataFrame): DataFrame to transform
            
        Returns:
            pandas.DataFrame: Transformed DataFrame
        """
        raise NotImplementedError("Subclasses must implement transform method")
    
    def __str__(self):
        """String representation of the transformer."""
        return f"DataTransformer({self.name})"

class CleaningTransformer(DataTransformer):
    """
    Transformer for data cleaning operations.
    
    Attributes:
        name (str): Name of the transformer
        columns_to_drop (list): Columns to drop
        columns_to_fill (dict): Columns to fill with specified values
        description (str): Description of the transformer
    """
    
    def __init__(self, name, columns_to_drop=None, columns_to_fill=None, description=""):
        """
        Initialize a cleaning transformer.
        
        Args:
            name (str): Name of the transformer
            columns_to_drop (list, optional): Columns to drop. Defaults to None.
            columns_to_fill (dict, optional): Columns to fill with specified values. Defaults to None.
            description (str, optional): Description of the transformer. Defaults to "".
        """
        super().__init__(name, description)
        self.columns_to_drop = columns_to_drop or []
        self.columns_to_fill = columns_to_fill or {}
    
    @timer_decorator
    def transform(self, df):
        """
        Clean the data by dropping columns and filling missing values.
        
        Args:
            df (pandas.DataFrame): DataFrame to clean
            
        Returns:
            pandas.DataFrame: Cleaned DataFrame
        """
        # YOUR CODE HERE
        # 1. Create a copy of the DataFrame to avoid modifying the original
        # 2. Drop the specified columns
        # 3. Fill missing values in the specified columns
        # 4. Return the cleaned DataFrame
        pass

class FeatureEngineeringTransformer(DataTransformer):
    """
    Transformer for feature engineering operations.
    
    Attributes:
        name (str): Name of the transformer
        feature_definitions (dict): Definitions of features to create
        description (str): Description of the transformer
    """
    
    def __init__(self, name, feature_definitions=None, description=""):
        """
        Initialize a feature engineering transformer.
        
        Args:
            name (str): Name of the transformer
            feature_definitions (dict, optional): Definitions of features to create. Defaults to None.
            description (str, optional): Description of the transformer. Defaults to "".
        """
        super().__init__(name, description)
        self.feature_definitions = feature_definitions or {}
    
    @timer_decorator
    def transform(self, df):
        """
        Create new features based on the feature definitions.
        
        Args:
            df (pandas.DataFrame): DataFrame to transform
            
        Returns:
            pandas.DataFrame: DataFrame with new features
        """
        # YOUR CODE HERE
        # 1. Create a copy of the DataFrame to avoid modifying the original
        # 2. Create new features based on the feature definitions
        # 3. Return the DataFrame with new features
        pass

class AggregationTransformer(DataTransformer):
    """
    Transformer for data aggregation operations.
    
    Attributes:
        name (str): Name of the transformer
        group_by_columns (list): Columns to group by
        aggregations (dict): Aggregation functions to apply
        description (str): Description of the transformer
    """
    
    def __init__(self, name, group_by_columns, aggregations, description=""):
        """
        Initialize an aggregation transformer.
        
        Args:
            name (str): Name of the transformer
            group_by_columns (list): Columns to group by
            aggregations (dict): Aggregation functions to apply
            description (str, optional): Description of the transformer. Defaults to "".
        """
        super().__init__(name, description)
        self.group_by_columns = group_by_columns
        self.aggregations = aggregations
    
    @timer_decorator
    def transform(self, df):
        """
        Aggregate the data.
        
        Args:
            df (pandas.DataFrame): DataFrame to aggregate
            
        Returns:
            pandas.DataFrame: Aggregated DataFrame
        """
        # YOUR CODE HERE
        # 1. Group the DataFrame by the specified columns
        # 2. Apply the specified aggregation functions
        # 3. Reset the index to get the groupby columns back
        # 4. Return the aggregated DataFrame
        pass

class DataSink:
    """
    Base class for data sinks in the pipeline.
    
    Attributes:
        name (str): Name of the data sink
        description (str): Description of the data sink
    """
    
    def __init__(self, name, description=""):
        """
        Initialize a data sink.
        
        Args:
            name (str): Name of the data sink
            description (str, optional): Description of the data sink. Defaults to "".
        """
        self.name = name
        self.description = description
    
    def save_data(self, df):
        """
        Save the data.
        
        Args:
            df (pandas.DataFrame): DataFrame to save
            
        Returns:
            bool: True if the data was saved successfully
        """
        raise NotImplementedError("Subclasses must implement save_data method")
    
    def __str__(self):
        """String representation of the data sink."""
        return f"DataSink({self.name})"

class CSVDataSink(DataSink):
    """
    Data sink that writes to a CSV file.
    
    Attributes:
        name (str): Name of the data sink
        file_path (str): Path to the CSV file
        description (str): Description of the data sink
    """
    
    def __init__(self, name, file_path, description=""):
        """
        Initialize a CSV data sink.
        
        Args:
            name (str): Name of the data sink
            file_path (str): Path to the CSV file
            description (str, optional): Description of the data sink. Defaults to "".
        """
        super().__init__(name, description)
        self.file_path = file_path
    
    @timer_decorator
    def save_data(self, df):
        """
        Save the data to a CSV file.
        
        Args:
            df (pandas.DataFrame): DataFrame to save
            
        Returns:
            bool: True if the data was saved successfully
        """
        # YOUR CODE HERE
        # 1. Create the directory if it doesn't exist
        # 2. Save the DataFrame to the CSV file
        # 3. Return True if successful
        pass

class DatabaseDataSink(DataSink):
    """
    Data sink that writes to a database.
    
    Attributes:
        name (str): Name of the data sink
        connection_string (str): Database connection string
        table_name (str): Name of the table to write to
        description (str): Description of the data sink
    """
    
    def __init__(self, name, connection_string, table_name, description=""):
        """
        Initialize a database data sink.
        
        Args:
            name (str): Name of the data sink
            connection_string (str): Database connection string
            table_name (str): Name of the table to write to
            description (str, optional): Description of the data sink. Defaults to "".
        """
        super().__init__(name, description)
        self.connection_string = connection_string
        self.table_name = table_name
    
    @timer_decorator
    def save_data(self, df):
        """
        Save the data to a database table.
        
        Args:
            df (pandas.DataFrame): DataFrame to save
            
        Returns:
            bool: True if the data was saved successfully
        """
        # YOUR CODE HERE
        # 1. Connect to the database
        # 2. Write the DataFrame to the table
        # 3. Return True if successful
        # Note: For this exercise, you can simulate this by logging the action
        pass

class JSONDataSink(DataSink):
    """
    Data sink that writes to a JSON file.
    
    Attributes:
        name (str): Name of the data sink
        file_path (str): Path to the JSON file
        description (str): Description of the data sink
    """
    
    def __init__(self, name, file_path, description=""):
        """
        Initialize a JSON data sink.
        
        Args:
            name (str): Name of the data sink
            file_path (str): Path to the JSON file
            description (str, optional): Description of the data sink. Defaults to "".
        """
        super().__init__(name, description)
        self.file_path = file_path
    
    @timer_decorator
    def save_data(self, df):
        """
        Save the data to a JSON file.
        
        Args:
            df (pandas.DataFrame): DataFrame to save
            
        Returns:
            bool: True if the data was saved successfully
        """
        # YOUR CODE HERE
        # 1. Create the directory if it doesn't exist
        # 2. Convert the DataFrame to JSON
        # 3. Save the JSON to the file
        # 4. Return True if successful
        pass

class Pipeline:
    """
    Data processing pipeline.
    
    Attributes:
        name (str): Name of the pipeline
        description (str): Description of the pipeline
        sources (list): List of data sources
        transformers (list): List of data transformers
        sinks (list): List of data sinks
    """
    
    def __init__(self, name, description=""):
        """
        Initialize a pipeline.
        
        Args:
            name (str): Name of the pipeline
            description (str, optional): Description of the pipeline. Defaults to "".
        """
        self.name = name
        self.description = description
        self.sources = []
        self.transformers = []
        self.sinks = []
    
    def add_source(self, source):
        """
        Add a data source to the pipeline.
        
        Args:
            source (DataSource): Data source to add
            
        Returns:
            Pipeline: Self for method chaining
        """
        self.sources.append(source)
        return self
    
    def add_transformer(self, transformer):
        """
        Add a data transformer to the pipeline.
        
        Args:
            transformer (DataTransformer): Data transformer to add
            
        Returns:
            Pipeline: Self for method chaining
        """
        self.transformers.append(transformer)
        return self
    
    def add_sink(self, sink):
        """
        Add a data sink to the pipeline.
        
        Args:
            sink (DataSink): Data sink to add
            
        Returns:
            Pipeline: Self for method chaining
        """
        self.sinks.append(sink)
        return self
    
    @timer_decorator
    def run(self):
        """
        Run the pipeline.
        
        Returns:
            dict: Dictionary containing the results of the pipeline run
        """
        results = {
            'start_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'pipeline_name': self.name,
            'sources': [],
            'transformers': [],
            'sinks': [],
            'end_time': None,
            'success': False
        }
        
        try:
            # Process each data source
            all_data = []
            for source in self.sources:
                logger.info(f"Getting data from source: {source.name}")
                df = source.get_data()
                all_data.append(df)
                results['sources'].append({
                    'name': source.name,
                    'records': len(df),
                    'columns': df.columns.tolist()
                })
            
            # Combine data from all sources
            if len(all_data) == 1:
                df = all_data[0]
            else:
                # YOUR CODE HERE
                # Implement logic to combine multiple DataFrames
                # For example, you could concatenate them, merge them, etc.
                pass
            
            # Apply transformers in sequence
            for transformer in self.transformers:
                logger.info(f"Applying transformer: {transformer.name}")
                df = transformer.transform(df)
                results['transformers'].append({
                    'name': transformer.name,
                    'records_after': len(df),
                    'columns_after': df.columns.tolist()
                })
            
            # Save to all sinks
            for sink in self.sinks:
                logger.info(f"Saving data to sink: {sink.name}")
                success = sink.save_data(df)
                results['sinks'].append({
                    'name': sink.name,
                    'success': success
                })
            
            results['success'] = True
            logger.info("Pipeline run completed successfully")
        
        except Exception as e:
            logger.error(f"Pipeline run failed: {str(e)}")
            results['error'] = str(e)
        
        results['end_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return results

def create_sample_pipeline():
    """
    Create a sample data pipeline for soccer statistics.
    
    Returns:
        Pipeline: The sample pipeline
    """
    # Create the pipeline
    pipeline = Pipeline(
        name="Soccer Statistics Pipeline",
        description="Pipeline for processing and analyzing soccer player statistics"
    )
    
    # Add data sources
    # For this example, we'll use the sample player data from pandas_analysis.py
    pipeline.add_source(
        CSVDataSource(
            name="Player Data",
            file_path="data/player_data.csv",
            description="Sample player statistics data"
        )
    )
    
    # Add transformers
    # 1. Cleaning transformer to handle missing values and drop unnecessary columns
    pipeline.add_transformer(
        CleaningTransformer(
            name="Data Cleaning",
            columns_to_drop=[],  # No columns to drop in this example
            columns_to_fill={
                'goals': 0,
                'assists': 0,
                'shots': 0,
                'shots_on_goal': 0
            }
        )
    )
    
    # 2. Feature engineering transformer to create derived metrics
    pipeline.add_transformer(
        FeatureEngineeringTransformer(
            name="Feature Engineering",
            feature_definitions={
                'goals_per_90': 'goals * 90 / minutes',
                'assists_per_90': 'assists * 90 / minutes',
                'shots_per_90': 'shots * 90 / minutes',
                'shot_accuracy': 'shots_on_goal / shots',
                'goal_conversion': 'goals / shots',
                'efficiency_score': '(goals * 3 + assists * 2) / games_played'
            }
        )
    )
    
    # 3. Aggregation transformer to create team-level statistics
    pipeline.add_transformer(
        AggregationTransformer(
            name="Team Aggregation",
            group_by_columns=['team'],
            aggregations={
                'goals': ['sum', 'mean'],
                'assists': ['sum', 'mean'],
                'goals_per_90': 'mean',
                'assists_per_90': 'mean',
                'efficiency_score': 'mean',
                'games_played': 'sum'
            }
        )
    )
    
    # Add data sinks
    pipeline.add_sink(
        CSVDataSink(
            name="Team Stats CSV",
            file_path="data/outputs/team_stats.csv"
        )
    )
    
    pipeline.add_sink(
        JSONDataSink(
            name="Team Stats JSON",
            file_path="data/outputs/team_stats.json"
        )
    )
    
    return pipeline

def main():
    """Run the data pipeline."""
    print("Data Pipeline Development")
    
    # Check if sample data exists, if not, suggest running pandas_analysis.py first
    if not os.path.exists('data/player_data.csv'):
        print("Sample data not found. Please run pandas_analysis.py first to generate the sample data.")
        return
    
    # Create and run the pipeline
    print("\nCreating and running the sample pipeline...")
    pipeline = create_sample_pipeline()
    results = pipeline.run()
    
    # Save the pipeline results
    results_file = "data/outputs/pipeline_results.json"
    os.makedirs(os.path.dirname(results_file), exist_ok=True)
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print a summary of the results
    print("\nPipeline run summary:")
    print(f"Pipeline: {results['pipeline_name']}")
    print(f"Start time: {results['start_time']}")
    print(f"End time: {results['end_time']}")
    print(f"Success: {results['success']}")
    
    print("\nSources processed:")
    for source in results['sources']:
        print(f"- {source['name']}: {source['records']} records, {len(source['columns'])} columns")
    
    print("\nTransformers applied:")
    for transformer in results['transformers']:
        print(f"- {transformer['name']}: {transformer['records_after']} records after transformation")
    
    print("\nData saved to sinks:")
    for sink in results['sinks']:
        status = "Success" if sink['success'] else "Failed"
        print(f"- {sink['name']}: {status}")
    
    print(f"\nDetailed results saved to {results_file}")

if __name__ == "__main__":
    main()