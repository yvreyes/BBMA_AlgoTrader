import y.finance as yf
import pandas as pd

def fetch_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Fetch OHLCV data reliability"""
    try:
        data = yf.download(ticker, start=start, end=end)
        if data.empty:
            raise ValueError(f"No data for {ticker}")
        return data[['Open', 'High', 'Low', 'Close', 'Volume']]
    except Exception as e:
        raise RuntimeError(f"Data fetched failed {e}")
    