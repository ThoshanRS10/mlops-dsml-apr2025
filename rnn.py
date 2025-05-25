import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Generate dummy sequential data
def generate_dummy_data(timesteps, features, samples):
    X = np.random.random((samples, timesteps, features))
    y = np.random.randint(0, 2, (samples, 1))  # Binary classification
    return X, y

# Parameters
timesteps = 10  # Number of time steps
features = 5    # Number of features per time step
samples = 100   # Number of samples

# Generate data
X, y = generate_dummy_data(timesteps, features, samples)

# Build a simple RNN model
model = Sequential([
    SimpleRNN(32, activation='relu', input_shape=(timesteps, features)),
    Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=5, batch_size=16)

# Evaluate the model
loss, accuracy = model.evaluate(X, y)
print(f"Loss: {loss}, Accuracy: {accuracy}")