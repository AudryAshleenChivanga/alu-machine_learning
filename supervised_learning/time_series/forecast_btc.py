#!/usr/bin/env bash
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

# Load CSVs
coinbase = pd.read_csv("coinbase.csv")
bitstamp = pd.read_csv("bitstamp.csv")

# Merge or choose one
df = coinbase.copy()

# Convert time column
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df.set_index('timestamp', inplace=True)

# Resample to hourly
df_hourly = df['close'].resample('H').last().dropna()

# Scaling
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df_hourly.values.reshape(-1, 1))

# Create sequences
X, y = [], []
seq_len = 24
for i in range(len(scaled) - seq_len):
    X.append(scaled[i:i+seq_len])
    y.append(scaled[i+seq_len])
X, y = np.array(X), np.array(y)

# Save
np.savez("btc_preprocessed.npz", X=X, y=y)
joblib.dump(scaler, "scaler.pkl")
