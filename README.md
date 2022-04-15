# Neural-network-using-the-MNIST-Dataset
Some notes:

Given the architecture of the net, it should succeed in less than 10 epochs.
When it reaches 99% or greater it should print out the string "Reached 99% accuracy so cancelling training!" and stop training.
If you add any additional variables, make sure you use the same names as the ones used in the class. This is important for the function signatures (the parameters and names) of the callbacks.

Begin by loading the data. A couple of things to notice:

The file mnist.npz is already included in the current workspace under the data directory. By default the load_data from Keras accepts a path relative to ~/.keras/datasets but in this case it is stored somewhere else, as a result of this, you need to specify the full path.

load_data returns the train and test sets in the form of the tuples (x_train, y_train), (x_test, y_test) but in this exercise you will be needing only the train set so you can ignore the second tuple.

There are 60000 examples with shape (28, 28)

If you see the message Reached 99% accuracy so cancelling training! printed out after less than 10 epochs it means your callback worked as expected.
