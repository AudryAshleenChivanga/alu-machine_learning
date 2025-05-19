import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib

# Load data
data = np.load("btc_preprocessed.npz")
X, y = data["X"], data["y"]

# Split
split = int(0.8 * len(X))
X_train, X_val = X[:split], X[split:]
y_train, y_val = y[:split], y[split:]

# tf.data.Dataset
train_ds = tf.data.Dataset.from_tensor_slices((X_train, y_train)).batch(32).shuffle(1000)
val_ds = tf.data.Dataset.from_tensor_slices((X_val, y_val)).batch(32)

# Model
model = Sequential([
    LSTM(64, return_sequences=False, input_shape=(24, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Train
model.fit(train_ds, validation_data=val_ds, epochs=10)

# Save model
model.save("btc_forecast_model.h5")
