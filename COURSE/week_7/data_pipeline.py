"""
CHALLENGE: Soccer Data Processing Pipeline

Your task is to create a data processing pipeline for soccer analytics.
This pipeline will handle the end-to-end flow of soccer data from collection to analysis.

The challenge includes:
1. Building a modular data processing pipeline
2. Implementing data extraction, transformation, and loading (ETL)
3. Handling different data sources and formats
4. Creating efficient data transformations
5. Implementing caching and optimization

REQUIREMENTS:
- Create a modular, extensible pipeline architecture
- Handle multiple data sources and formats
- Implement proper error handling and logging
- Optimize for performance with large datasets
- Document your pipeline design and implementation
"""

import pandas as pd
import numpy as np
import os
import json
import logging
import time
import hashlib
import pickle
from typing import List, Dict, Tuple, Optional, Union, Callable, Any


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DataSource:
    """
    Base class for data sources in the pipeline.
    
    This abstract class defines the interface for all data sources.
    Subclasses should implement the extract method.
    """
    
    def __init__(self, name: str):
        """
        Initialize the data source.
        
        Args:
            name: Name of the data source
        """
        self.name = name
        
    def extract(self) -> pd.DataFrame:
        """
        Extract data from the source.
        
        Returns:
            A pandas DataFrame containing the extracted data
        """
        raise NotImplementedError("Subclasses must implement extract()")
    
    def __str__(self) -> str:
        return f"DataSource({self.name})"


class CSVDataSource(DataSource):
    """
    Data source for CSV files.
    """
    
    def __init__(self, name: str, file_path: str, **kwargs):
        """
        Initialize the CSV data source.
        
        Args:
            name: Name of the data source
            file_path: Path to the CSV file
            **kwargs: Additional arguments for pd.read_csv()
        """
        super().__init__(name)
        self.file_path = file_path
        self.kwargs = kwargs
        
    def extract(self) -> pd.DataFrame:
        """
        Extract data from the CSV file.
        
        Returns:
            A pandas DataFrame containing the data from the CSV file
        """
        # TODO: Implement this method to extract data from a CSV file
        # Make sure to handle errors appropriately
        pass


class JSONDataSource(DataSource):
    """
    Data source for JSON files.
    """
    
    def __init__(self, name: str, file_path: str, **kwargs):
        """
        Initialize the JSON data source.
        
        Args:
            name: Name of the data source
            file_path: Path to the JSON file
            **kwargs: Additional arguments for pd.read_json()
        """
        super().__init__(name)
        self.file_path = file_path
        self.kwargs = kwargs
        
    def extract(self) -> pd.DataFrame:
        """
        Extract data from the JSON file.
        
        Returns:
            A pandas DataFrame containing the data from the JSON file
        """
        # TODO: Implement this method to extract data from a JSON file
        # Make sure to handle errors appropriately
        pass


class APIDataSource(DataSource):
    """
    Data source for API endpoints.
    """
    
    def __init__(self, name: str, url: str, params: Dict[str, Any] = None):
        """
        Initialize the API data source.
        
        Args:
            name: Name of the data source
            url: URL of the API endpoint
            params: Parameters for the API request
        """
        super().__init__(name)
        self.url = url
        self.params = params or {}
        
    def extract(self) -> pd.DataFrame:
        """
        Extract data from the API endpoint.
        
        Returns:
            A pandas DataFrame containing the data from the API
        """
        # TODO: Implement this method to extract data from an API
        # Make sure to handle errors appropriately
        pass


class DatabaseDataSource(DataSource):
    """
    Data source for database connections.
    """
    
    def __init__(self, name: str, connection_string: str, query: str):
        """
        Initialize the database data source.
        
        Args:
            name: Name of the data source
            connection_string: Connection string for the database
            query: SQL query to execute
        """
        super().__init__(name)
        self.connection_string = connection_string
        self.query = query
        
    def extract(self) -> pd.DataFrame:
        """
        Extract data from the database.
        
        Returns:
            A pandas DataFrame containing the data from the database
        """
        # TODO: Implement this method to extract data from a database
        # Make sure to handle errors appropriately
        pass


class Transformer:
    """
    Base class for data transformers in the pipeline.
    
    This abstract class defines the interface for all data transformers.
    Subclasses should implement the transform method.
    """
    
    def __init__(self, name: str):
        """
        Initialize the transformer.
        
        Args:
            name: Name of the transformer
        """
        self.name = name
        
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Transform the input data.
        
        Args:
            data: Input data to transform
            
        Returns:
            Transformed data
        """
        raise NotImplementedError("Subclasses must implement transform()")
    
    def __str__(self) -> str:
        return f"Transformer({self.name})"


class CleaningTransformer(Transformer):
    """
    Transformer for cleaning data.
    """
    
    def __init__(self, name: str, columns_to_clean: List[str] = None):
        """
        Initialize the cleaning transformer.
        
        Args:
            name: Name of the transformer
            columns_to_clean: List of columns to clean (if None, clean all columns)
        """
        super().__init__(name)
        self.columns_to_clean = columns_to_clean
        
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the input data.
        
        Args:
            data: Input data to clean
            
        Returns:
            Cleaned data
        """
        # TODO: Implement this method to clean the data
        # Handle missing values, data type conversion, etc.
        pass


class FeatureEngineeringTransformer(Transformer):
    """
    Transformer for feature engineering.
    """
    
    def __init__(self, name: str, feature_definitions: Dict[str, Callable]):
        """
        Initialize the feature engineering transformer.
        
        Args:
            name: Name of the transformer
            feature_definitions: Dictionary mapping feature names to functions that create them
        """
        super().__init__(name)
        self.feature_definitions = feature_definitions
        
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Add engineered features to the input data.
        
        Args:
            data: Input data to transform
            
        Returns:
            Data with engineered features
        """
        # TODO: Implement this method to add engineered features
        # Apply each feature definition function to the data
        pass


class AggregationTransformer(Transformer):
    """
    Transformer for data aggregation.
    """
    
    def __init__(self, name: str, group_by: List[str], aggregations: Dict[str, List[str]]):
        """
        Initialize the aggregation transformer.
        
        Args:
            name: Name of the transformer
            group_by: Columns to group by
            aggregations: Dictionary mapping columns to aggregation methods
        """
        super().__init__(name)
        self.group_by = group_by
        self.aggregations = aggregations
        
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Aggregate the input data.
        
        Args:
            data: Input data to aggregate
            
        Returns:
            Aggregated data
        """
        # TODO: Implement this method to aggregate the data
        # Group by specified columns and apply aggregations
        pass


class Loader:
    """
    Base class for data loaders in the pipeline.
    
    This abstract class defines the interface for all data loaders.
    Subclasses should implement the load method.
    """
    
    def __init__(self, name: str):
        """
        Initialize the loader.
        
        Args:
            name: Name of the loader
        """
        self.name = name
        
    def load(self, data: pd.DataFrame) -> Any:
        """
        Load data to the destination.
        
        Args:
            data: Data to load
            
        Returns:
            Result of the loading operation
        """
        raise NotImplementedError("Subclasses must implement load()")
    
    def __str__(self) -> str:
        return f"Loader({self.name})"


class CSVLoader(Loader):
    """
    Loader for CSV files.
    """
    
    def __init__(self, name: str, file_path: str, **kwargs):
        """
        Initialize the CSV loader.
        
        Args:
            name: Name of the loader
            file_path: Path to the CSV file
            **kwargs: Additional arguments for pd.to_csv()
        """
        super().__init__(name)
        self.file_path = file_path
        self.kwargs = kwargs
        
    def load(self, data: pd.DataFrame) -> str:
        """
        Load data to a CSV file.
        
        Args:
            data: Data to load
            
        Returns:
            Path to the saved CSV file
        """
        # TODO: Implement this method to save data to a CSV file
        # Make sure to handle errors appropriately
        pass


class DatabaseLoader(Loader):
    """
    Loader for databases.
    """
    
    def __init__(self, name: str, connection_string: str, table_name: str, if_exists: str = 'replace'):
        """
        Initialize the database loader.
        
        Args:
            name: Name of the loader
            connection_string: Connection string for the database
            table_name: Name of the table to load data into
            if_exists: Action to take if the table already exists ('replace', 'append', or 'fail')
        """
        super().__init__(name)
        self.connection_string = connection_string
        self.table_name = table_name
        self.if_exists = if_exists
        
    def load(self, data: pd.DataFrame) -> bool:
        """
        Load data to a database table.
        
        Args:
            data: Data to load
            
        Returns:
            True if the loading was successful, False otherwise
        """
        # TODO: Implement this method to save data to a database
        # Make sure to handle errors appropriately
        pass


class Cache:
    """
    Cache for storing intermediate results in the pipeline.
    """
    
    def __init__(self, cache_dir: str = '.cache'):
        """
        Initialize the cache.
        
        Args:
            cache_dir: Directory to store cache files
        """
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        
    def _get_cache_key(self, data: pd.DataFrame, step_name: str) -> str:
        """
        Generate a cache key based on the data and step name.
        
        Args:
            data: Input data
            step_name: Name of the processing step
            
        Returns:
            Cache key
        """
        # TODO: Implement this method to generate a unique cache key
        # Consider using a hash of the data and step name
        pass
    
    def get(self, data: pd.DataFrame, step_name: str) -> Optional[pd.DataFrame]:
        """
        Retrieve data from the cache.
        
        Args:
            data: Input data
            step_name: Name of the processing step
            
        Returns:
            Cached data or None if not found
        """
        # TODO: Implement this method to retrieve data from the cache
        # Return None if the data is not in the cache
        pass
    
    def set(self, input_data: pd.DataFrame, output_data: pd.DataFrame, step_name: str) -> None:
        """
        Store data in the cache.
        
        Args:
            input_data: Input data
            output_data: Output data to cache
            step_name: Name of the processing step
        """
        # TODO: Implement this method to store data in the cache
        pass


class Pipeline:
    """
    Data processing pipeline for soccer analytics.
    """
    
    def __init__(self, name: str, use_cache: bool = True):
        """
        Initialize the pipeline.
        
        Args:
            name: Name of the pipeline
            use_cache: Whether to use caching
        """
        self.name = name
        self.steps = []
        self.use_cache = use_cache
        self.cache = Cache() if use_cache else None
        
    def add_source(self, source: DataSource) -> 'Pipeline':
        """
        Add a data source to the pipeline.
        
        Args:
            source: The data source to add
            
        Returns:
            The pipeline instance for method chaining
        """
        self.steps.append(('source', source))
        return self
    
    def add_transformer(self, transformer: Transformer) -> 'Pipeline':
        """
        Add a transformer to the pipeline.
        
        Args:
            transformer: The transformer to add
            
        Returns:
            The pipeline instance for method chaining
        """
        self.steps.append(('transformer', transformer))
        return self
    
    def add_loader(self, loader: Loader) -> 'Pipeline':
        """
        Add a loader to the pipeline.
        
        Args:
            loader: The loader to add
            
        Returns:
            The pipeline instance for method chaining
        """
        self.steps.append(('loader', loader))
        return self
    
    def run(self) -> Any:
        """
        Run the pipeline.
        
        Returns:
            Result of the pipeline execution
        """
        # TODO: Implement this method to run the pipeline
        # Extract data from the source, apply transformations, and load the result
        # Use caching if enabled
        pass


def create_player_stats_pipeline(csv_file_path: str, output_file_path: str) -> Pipeline:
    """
    Create a pipeline for processing player statistics.
    
    Args:
        csv_file_path: Path to the CSV file with player data
        output_file_path: Path to save the processed data
        
    Returns:
        A configured pipeline instance
    """
    # TODO: Implement this function to create a player stats pipeline
    # Create appropriate data sources, transformers, and loaders
    pass


def create_team_stats_pipeline(csv_file_path: str, output_file_path: str) -> Pipeline:
    """
    Create a pipeline for processing team statistics.
    
    Args:
        csv_file_path: Path to the CSV file with team data
        output_file_path: Path to save the processed data
        
    Returns:
        A configured pipeline instance
    """
    # TODO: Implement this function to create a team stats pipeline
    # Create appropriate data sources, transformers, and loaders
    pass


def create_match_stats_pipeline(csv_file_path: str, output_file_path: str) -> Pipeline:
    """
    Create a pipeline for processing match statistics.
    
    Args:
        csv_file_path: Path to the CSV file with match data
        output_file_path: Path to save the processed data
        
    Returns:
        A configured pipeline instance
    """
    # TODO: Implement this function to create a match stats pipeline
    # Create appropriate data sources, transformers, and loaders
    pass


def main():
    """
    Main function to demonstrate pipeline capabilities.
    """
    # Example file paths (replace with actual paths in a real scenario)
    player_data_path = "data/player_stats.csv"  # Placeholder path
    team_data_path = "data/team_stats.csv"      # Placeholder path
    match_data_path = "data/match_stats.csv"    # Placeholder path
    
    output_dir = "processed_data"
    os.makedirs(output_dir, exist_ok=True)
    
    player_output_path = os.path.join(output_dir, "processed_player_stats.csv")
    team_output_path = os.path.join(output_dir, "processed_team_stats.csv")
    match_output_path = os.path.join(output_dir, "processed_match_stats.csv")
    
    # Create example data if the files don't exist
    if not os.path.exists(player_data_path):
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(player_data_path), exist_ok=True)
        
        # Create example player data
        player_data = pd.DataFrame({
            'player_id': range(1, 51),
            'first_name': [f'Player{i}' for i in range(1, 51)],
            'last_name': [f'Lastname{i}' for i in range(1, 51)],
            'position': np.random.choice(['Forward', 'Midfielder', 'Defender', 'Goalkeeper'], 50),
            'team_id': np.random.randint(1, 11, 50),
            'age': np.random.randint(18, 35, 50),
            'goals': np.random.randint(0, 20, 50),
            'assists': np.random.randint(0, 15, 50),
            'minutes_played': np.random.randint(0, 3000, 50)
        })
        
        # Introduce some missing values and errors for cleaning
        player_data.loc[np.random.choice(player_data.index, 5), 'goals'] = np.nan
        player_data.loc[np.random.choice(player_data.index, 5), 'assists'] = np.nan
        player_data.loc[np.random.choice(player_data.index, 3), 'age'] = -1  # Invalid age
        
        # Save to CSV
        player_data.to_csv(player_data_path, index=False)
    
    # Create example team data if the file doesn't exist
    if not os.path.exists(team_data_path):
        os.makedirs(os.path.dirname(team_data_path), exist_ok=True)
        
        team_data = pd.DataFrame({
            'team_id': range(1, 11),
            'team_name': [f'Team{i}' for i in range(1, 11)],
            'wins': np.random.randint(5, 25, 10),
            'losses': np.random.randint(5, 20, 10),
            'draws': np.random.randint(0, 10, 10)
        })
        
        # Introduce some errors for cleaning
        team_data.loc[np.random.choice(team_data.index, 2), 'wins'] = -1  # Invalid wins
        
        # Save to CSV
        team_data.to_csv(team_data_path, index=False)
    
    # Create example match data if the file doesn't exist
    if not os.path.exists(match_data_path):
        os.makedirs(os.path.dirname(match_data_path), exist_ok=True)
        
        match_data = pd.DataFrame({
            'match_id': range(1, 101),
            'home_team_id': np.random.randint(1, 11, 100),
            'away_team_id': np.random.randint(1, 11, 100),
            'home_score': np.random.randint(0, 5, 100),
            'away_score': np.random.randint(0, 5, 100),
            'date': pd.date_range(start='2023-01-01', periods=100)
        })
        
        # Introduce some missing values and errors for cleaning
        match_data.loc[np.random.choice(match_data.index, 5), 'home_score'] = np.nan
        match_data.loc[np.random.choice(match_data.index, 5), 'away_score'] = np.nan
        
        # Save to CSV
        match_data.to_csv(match_data_path, index=False)
    
    # TODO: Implement pipeline execution
    # 1. Create player stats pipeline and run it
    # 2. Create team stats pipeline and run it
    # 3. Create match stats pipeline and run it
    
    print("Data pipeline processing completed!")


if __name__ == "__main__":
    main()