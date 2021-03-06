import os
import tensorflow as tf
from tensorflow import keras

# Load the data

## In case if the dataset is already in your working space
# Get current working directory
current_dir = os.getcwd() 

# Append data/mnist.npz to the previous path to get the full path
data_path = os.path.join(current_dir, "data/mnist.npz") 

# Get dataset
(training_images, training_labels), (test_images, test_labels)= tf.keras.datasets.mnist.load_data(path=data_path)

## In case you need to download the dataset MNIST
# Load the Fashion MNIST dataset
fmnist = tf.keras.datasets.fashion_mnist
# Load the training and test split of the Fashion MNIST dataset
(training_images, training_labels), (test_images, test_labels) = fmnist.load_data()

        
# Normalize pixel values
x_train = x_train / 255.0

data_shape = x_train.shape

print(f"There are {data_shape[0]} examples with shape ({data_shape[1]}, {data_shape[2]})")

class myCallback(tf.keras.callbacks.Callback):
        # Define the correct function signature for on_epoch_end
        def on_epoch_end(self, epoch, logs={}):
            if (logs.get('accuracy') is not None and logs.get('accuracy') > 0.99):
                print("\nReached 99% accuracy so cancelling training!") 
                
                # Stop training once the above condition is met
                self.model.stop_training = True
                
                def train_mnist(x_train, y_train):

# Instantiate the callback class
callbacks = myCallback()

# Define the model, it should have 3 layers:
# - A Flatten layer that receives inputs with the same shape as the images
# - A Dense layer with 512 units and ReLU activation function
# - A Dense layer with 10 units and softmax activation function
model = tf.keras.models.Sequential([ 
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax),
]) 

# Compile the model
model.compile(optimizer='adam', 
            loss='sparse_categorical_crossentropy', 
            metrics=['accuracy']) 

# Fit the model for 10 epochs adding the callbacks
# and save the training history
history = model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])

return history

hist = train_mnist(x_train, y_train)
