import tensorflow as tf
from tensorflow.keras import layers, models

def create_neural_network(input_shape, num_classes):
    model = models.Sequential([
        layers.InputLayer(input_shape=input_shape),
        layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

# Example usage
if __name__ == "__main__":
    input_shape = (28, 28, 1)  # Example for MNIST dataset
    num_classes = 10  # Number of classes in MNIST
    model = create_neural_network(input_shape, num_classes)
    model.summary()