# testing.md
This file stores neural network training test data to keep a log of past experiments so they are not repeated.

## Colab Training
Link to the Colab file for this project, used to train the neural network.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1XtMGtiI1XkhwrfcPSUsHYUje7PvZdNGc)

### Changing the Neural Network
The neural network can be edited in an attempt to optimize it and to increase its accuracy.

```python
model = keras.Sequential([
  layers.Dense(10, activation=tf.nn.relu, input_shape=[5]), # Hidden and Input Layers
  layers.Dense(10, activation=tf.nn.relu), # Hidden Layer
  layers.Dense(10, activation=tf.nn.relu), # Hidden Layer
  layers.Dense(10, activation=tf.nn.relu), # Hidden Layer
  layers.Dense(2) # Output Layer
])
```

This is an example of one neural network. The layers fall into three categories: **Input**, **Hidden** and **Output**. The **Input** layer is represented by `input_shape=[5]` which represents the 5 inputs that the neural network uses (in this case: rotation and the four LIDAR distances). Changing this value would allow for different data to be fed into the neural network to train, for example rotation and three LIDARs.

For example:

```python
# Five inputs
layers.Dense(10, activation=tf.nn.relu, input_shape=[5])
```

```python
# Four inputs
layers.Dense(10, activation=tf.nn.relu, input_shape=[4])
```

This neural network contains 4 **Hidden** layers, these do the majority of the processing of the neural network. In this case, each of the hidden layers contains 10 neurons. More layers can be added into the list by simply adding an additional `layers.Dense()`. Another editable value is the activation type, represented by `activation=tf.nn.relu`. This representing the `relu` activaiton type. More activation types exist, however this project only uses `relu`. Changing the first value in the parenthesis allows for a different number of neurons in a given layer.

For example:

```python
# Ten neurons in this layer
layers.Dense(10, activation=tf.nn.relu)
```

```python
# Five neurons in this layer
layers.Dense(5, activation=tf.nn.relu)
```

Finally the network combines the previous layer into the **Output** layer, which dictates the number of outputs that the neural network is generating. This project looks to produce two values X and Y, so it has an output layer of two. This is changed by editing the value in the final layer.

For example:

```python
# Two outputs
layers.Dense(2)
```

```python
# Three outputs
layers.Dense(3)
```

The data and some code needs to be edited to allow for a different input or output shape, as the neural network would not match the data it is given. However, for this project the data will stay the same and so only the **Hidden** layers need to be edited.

A neural network which takes in 3 inputs, contains 2 hidden layers with 5 neurons each and outputs 1 value is written like so:

```python
model = keras.Sequential([
  layers.Dense(5, activation=tf.nn.relu, input_shape=[3]), # First Hidden and Input Layer
  layers.Dense(5, activation=tf.nn.relu), # Hidden Layer
  layers.Dense(1) # Output Layer
])
```

There are two other major factors which can effect the performance of the neural network: the **Optimizer** and the number of **Epochs**.

The **Optimizer** is shown here:

```python
optimizer = tf.keras.optimizers.Adam(0.002)
```

The value in the parenthesis is the Learning Rate. The Learning Rate determines how quickly the neural network learns. However, faster is not always better as the network may overshoot and never be very accurate. If the Learning Rate is too slow, the network may never converge or may take extremely long to train. In this case the `Adam` optimizer is used, several different optimizers exist, however for the current value of Learning Rate Adam is the best optimizer.

The differences between the optimizers can be seen on [this website](https://medium.com/octavian-ai/which-optimizer-and-learning-rate-should-i-use-for-deep-learning-5acb418f9b2).

**Citation:**
Mack, David. “How to Pick the Best Learning Rate for Your Machine Learning Project.” *Medium*, Octavian, 9 Apr. 2018, https://medium.com/octavian-ai/which-optimizer-and-learning-rate-should-i-use-for-deep-learning-5acb418f9b2.

## Neural Network Trials
In this section several different neural network structures will be tested and recorded. The purpose of this section is to stop unnecessary repetition of tests and to optimize the neural network to maximize accuracy.

![test1](tests/1.png = 250x)
