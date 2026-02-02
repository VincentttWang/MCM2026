import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def fill_missing_values(df, method='mean', constant=0):
    """
    Fills missing values in a DataFrame.
    method: 'mean', 'median', 'mode', 'ffill', 'bfill', 'constant', 'drop'
    """
    data = df.copy()
    if method == 'mean':
        data = data.fillna(data.mean(numeric_only=True))
    elif method == 'median':
        data = data.fillna(data.median(numeric_only=True))
    elif method == 'mode':
        data = data.fillna(data.mode().iloc[0])
    elif method == 'ffill':
        data = data.fillna(method='ffill')
    elif method == 'bfill':
        data = data.fillna(method='bfill')
    elif method == 'constant':
        data = data.fillna(constant)
    elif method == 'drop':
        data = data.dropna()
    return data

def detect_outliers_zscore(df, threshold=3):
    """
    Detects outliers using Z-score. Returns a boolean mask (True if outlier).
    Only applies to numeric columns.
    """
    data = df.select_dtypes(include=[np.number])
    z_scores = np.abs((data - data.mean()) / data.std())
    return (z_scores > threshold)

def detect_outliers_iqr(df):
    """
    Detects outliers using IQR (Interquartile Range). Returns a boolean mask.
    """
    data = df.select_dtypes(include=[np.number])
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    return ((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR)))

def normalize_minmax(df):
    """
    Scales features to [0, 1].
    """
    scaler = MinMaxScaler()
    data = df.copy()
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    return data, scaler

def normalize_zscore(df):
    """
    Standardizes features by removing the mean and scaling to unit variance.
    """
    scaler = StandardScaler()
    data = df.copy()
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    return data, scaler

if __name__ == "__main__":
    # Test cases
    print("Running data preprocessing tests...")
    
    # Create dummy data
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 100], # 100 is an outlier
        'B': [5, 6, 7, 8, 9],
        'C': ['cat', 'dog', 'cat', 'bird', np.nan]
    })
    
    print("Original DataFrame:\n", df)
    
    # 1. Fill Missing Values
    print("\nFilled Missing (Mean):\n", fill_missing_values(df, method='mean'))
    
    # 2. Outlier Detection
    print("\nOutliers (Z-score > 2):\n", detect_outliers_zscore(df, threshold=2))
    
    # 3. Normalization
    df_filled = fill_missing_values(df, method='mean') # Fill first
    df_norm, _ = normalize_minmax(df_filled)
    print("\nMin-Max Normalized:\n", df_norm)
    
    print("Done.")
