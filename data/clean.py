import yfinance as yf
import pandas as pd
import numpy as np

def make_features(df):
    '''
    Features to implement:
    - % returns over past 1, 5, 10, 20 days (a)
    - Volatility: rolling std over past 10, 20 days (b)
    - Momentum (c)
    - Vol changes: current vol over last 20 day avg vol (d)
    - Crossover momentum (e)
    '''

    # (a) 
    df['ret_1_d'] = df['Close'].pct_change()
    df['ret_5_d'] = df['Close'].pct_change(5)
    df['ret_10_d'] = df['Close'].pct_change(10)
    df['ret_20_d'] = df['Close'].pct_change(20)

    # (b)
    df['vol_10_d'] = df['Close'].rolling(10).std() * np.sqrt(252)
    df['vol_20_d'] = df['Close'].rolling(20).std() * np.sqrt(252)

    # (c)
    df['mom_20_d'] = df['Close'] / df['Close'].shift(20) - 1

    # (d)
    df['volume_20_d'] = df['Volume'] / df['Volume'].rolling(20).mean()

    # (e)
    df['crossover_10_v_50'] = df['Close'].rolling(window=10).mean() - df['Close'].rolling(window=50).mean()

    return df

def make_labels(df):
    # y_t = (close_{t+1} / close_t) - 1
    df['Target'] = df['Close'].pct_change().shift(-1)
    return df

def merge_and_split(df):
    df = make_features(df)
    df = make_labels(df)
    df = df.dropna()
    features = df.drop(columns = 'Target')
    labels = df['Target']
    return features, labels


