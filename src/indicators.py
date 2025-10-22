import pandas as pd
import numpy as np

def lwma(series: pd.Series, period: int) -> pd.Series:
    """Linear Weighted Moving Averages"""
    weights = np.arrange(1, period + 1)
    weights_sum = weights.sum()

    def weighted_avg(x):
        if len(x) < period:
            return np.nan
        return np.dot(x, weights) / weights_sum
    
    return series.rolling(window=period).apply(weighted_avg, raw=True)


def lwma5(close: pd.Series) -> pd.Series:
    """Mahi Malo 5:"""
    return lwma(close, period=5)


def lwma10(close: pd.Series) -> pd.Series:
    """Mahi Malo 10:"""
    return lwma(close, period=10)


def bollinger_bands(data: pd.DataFrame, period: int = 20, mult: float = 2.0) -> pd.DataFrame:
    """Bollinger Bands"""
    close = data['Close']
    middle = close.rolling(window=period).mean()  
    std = close.rolling(window=period).std()
    upper = middle + mult * std
    lower = middle - mult * std
    data['BB_Middle'] = middle 
    data['BB_Upper'] = upper
    data['BB_Lower'] = lower
    return data


def add_mahi_malos(data: pd.DataFrame) -> pd.DataFrame:
    """Add Mahi Malo 5 and 10 to DataFrame."""
    close = data['Close']
    data['Mahi_Malo_5'] = lwma5(close)
    data['Mahi_Malo_10'] = lwma10(close)
    return data