import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import os

def process_data(df):
    """
    Process raw HTTP request data into features for an anomaly detection model.
    
    Args:
        df (pandas.DataFrame): DataFrame with columns 'url', 'method', 'params'
    
    Returns:
        pandas.DataFrame: DataFrame with extracted numerical features
    """
    # Handle missing values
    df['url'] = df['url'].fillna('')
    df['method'] = df['method'].fillna('UNKNOWN')
    df['params'] = df['params'].fillna('')
    
    # Define suspicious keywords and special characters
    suspicious_keywords = ['sql', 'script', 'union', 'select', 'insert', 'delete', 
                           'drop', 'alert', 'onerror', 'img', 'src']
    special_chars = ['<', '>', "'", '"', ';', '(', ')', '--', '/*', '*/']
    
    # Extract numerical features
    df['url_length'] = df['url'].apply(len)
    df['num_params'] = df['params'].apply(lambda x: len(x.split('&')) if x else 0)
    df['param_length'] = df['params'].apply(len)
    df['suspicious_keywords'] = df['params'].apply(
        lambda x: sum(1 for kw in suspicious_keywords if kw in x.lower())
    )
    df['special_chars'] = df['params'].apply(
        lambda x: sum(x.count(char) for char in special_chars)
    )
    
    # One-hot encode the 'method' column
    encoder = OneHotEncoder(sparse_output=False)  # Fixed line
    method_encoded = encoder.fit_transform(df[['method']])
    method_df = pd.DataFrame(method_encoded, columns=encoder.get_feature_names_out(['method']))
    
    # Combine all features into a single DataFrame
    features_df = pd.concat([
        df[['url_length', 'num_params', 'param_length', 'suspicious_keywords', 'special_chars']],
        method_df
    ], axis=1)
    
    return features_df

if __name__ == "__main__":
    # Define file paths
    raw_data_path = 'raw/http_requests.csv'
    processed_data_path = 'processed/processed_data.csv'
    
    # Create the processed data directory if it doesn’t exist
    os.makedirs('data/processed/', exist_ok=True)
    
    # Load the raw data
    df = pd.read_csv(raw_data_path)
    
    # Process the data
    features_df = process_data(df)
    
    # Save the processed data
    features_df.to_csv(processed_data_path, index=False)
    
    # Print confirmation
    print(f"Processed data saved to {processed_data_path}")
    print(f"Shape of processed data: {features_df.shape}")