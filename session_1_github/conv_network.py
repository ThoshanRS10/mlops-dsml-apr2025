import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Generate dummy data
def generate_dummy_data(num_samples=1000, img_size=(28, 28), num_classes=10):
    x_data = np.random.rand(num_samples, img_size[0], img_size[1], 1).astype('float32')  # Random grayscale images
    y_data = np.random.randint(0, num_classes, num_samples)  # Random labels
    y_data = tf.keras.utils.to_categorical(y_data, num_classes)  # One-hot encode labels
    return x_data, y_data

# Create dummy training and testing data
x_train, y_train = generate_dummy_data(num_samples=1000)
x_test, y_test = generate_dummy_data(num_samples=200)

# Define a simple CNN model
def create_cnn_model(input_shape, num_classes):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

# Create the model
input_shape = (28, 28, 1)  # Grayscale images of size 28x28
num_classes = 10
model = create_cnn_model(input_shape, num_classes)

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Test accuracy: {test_acc}")