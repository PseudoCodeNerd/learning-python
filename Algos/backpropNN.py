'''Writing a Program for Better Understanding of Back Propagation

@Madhav
Guided by Stephen Lee's Code for the same
'''

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return ( 1 / (1 + np.exp(-1 * x)) )

#layers of neural network
class NNLayer():
    def __init__(self,units,activation=None,learning_rate=None,ifinpLayer=False):
        self.units = units
        self.activation = activation
        self.bias = None
        self.weight = None
        if learning_rate is None:
            learning_rate = 0.3
        self.learning_rate = learning_rate
        self.ifinpLayer = ifinpLayer

        '''
        Parameters of NN:
        units -> number of neural units
        activation -> activation function
        learning_rate -> learning rate for the parameters
        ifinpLayer -> whether it is input layer or not
        '''
        
def initializer(self, back_units):
    self.weight = np.asmatrix(np.random.normal(0,0.5,(self.units,back_units)))
    self.bias = np.asmatrix(np.random.normal(0,0.5,self.units)).T
    if self.activation is None:
        self.activation = sigmoid

def calc_gradient(self):
    if self.activation == sigmoid:
        gradient_mat = np.dot(self.output, (1-self.output).T)
        gradient_activation = np.diag(np.diag(gradient_mat))
    else:
        gradient_activation = 1
    return gradient_activation

def forward_prop(self, x_data):
    self.x_data = x_data
    if self.ifinpLayer:
        #1st layer
        self.wx_plus_a = x_data
        self.output = x_data
        return x_data
    else:
        self.wx_plus_a = np.dot(self.weight, self.x_data) - self.bias
        self.output = self.activation(self.wx_plus_a)
        return self.output

def back_prop(self, gradient):
    gradient_activation = self.calc_gradient()
    gradient = np.asmatrix(gradient.T, gradient_activation)

    self._gradient_weight = np.asmatrix(self.x_data)
    self._gradient_bias = -1
    self._gradient_x = self.weight

    self.gradient_weight = np.dot(gradient.T,gradient_activation)
    self.gradient_bias = gradient * self._gradient_bias
    self.gradient = np.dot(gradient, self._gradient_x)

    self.weight = self.weight - self.learning_rate * self.gradient_weight
    self.bias = self.bias - self.learning_rate * self.gradient_bias.T 

    return self.gradient

#still some confusion in this part of the code; reference from Lee's code
class BPNN():

    def __init__(self):
        self.layers = []
        self.train_mse = []
        self.fig_loss = plt.figure()
        self.ax_loss = self.fig_loss.add_subplot(1,1,1)

    def add_layer(self, layer):
        self.layers.append

    def build(self):
        for i, layer in enumerate(self.layers[:]):
            if i < 1:
                layers.ifinpLayer = True
            else:
                layer.initializer(self.layers[i-1].units)
    
    def summary(self):
        for i, layer in enumerate(self.layers[:]):
            print('-------- layer %d ---------'%i)
            print('weight.shape ',np.shape(layer.weight))
            print('bias.shape ',np.shape(layer.bias))

    def train(self, x_data, y_data, train_round, accuracy):
        self.train_round = train_round
        self.accuracy = accuracy

        self.ax_loss.hlines(self.accuracy, 0, self.train_round * 1.1)

        x_shape = np.shape(x_data)
        for round_i in range(train_round):
            all_loss = 0
            for row in range(x_shape[0]):
                _xdata = np.asmatrix(x_data[row,:]).T
                _ydata = np.asmatrix(y_data[row,:]).T

                for layer in self.layers:
                    _xdata = layer.forward_prop(_xdata)

                loss, gradient = self.calc_loss(_ydata, _xdata)
                all_loss+=loss

                for layer in self.layers[:0:-1]:
                    gradient = layer.back_prop(gradient)

                mse = all_loss/x_shape[0]
                self.train_mse.append(mse)

                self.plot_loss()

                if mse < self.accuracy:
                    print('--- ^^^^^^ ---')
                    return mse

def calc_loss(self, y_data, ydata_):
    self.loss = np.sum(np.power((y_data - ydata_),2))
    self.loss_gradient = 2 * (ydata_ - y_data)
    return self.loss, self.loss_gradient

def plot_loss(self):
    if self.ax_loss.lines:
        self.ax_loss.lines.remove(self.ax_loss.lines[0])
    self.ax_loss.plot(self.train_mse,'r-')
    plt.ion()
    plt.xlabel('step')
    plt.ylabel('loss')
    plt.show()
    plt.pause(0,1)

def example():

    x = np.random.randn(10,10)
    y = np.asarray([[0.8,0.4],[0.4,0.3],[0.34,0.45],[0.67,0.32],
                    [0.88,0.67],[0.78,0.77],[0.55,0.66],[0.55,0.43],[0.54,0.1],
                    [0.1,0.5]])
    
    model = BPNN()
    model.add_layer(NNLayer(10))
    model.add_layer(NNLayer(20))
    model.add_layer(NNLayer(30))
    model.add_layer(NNLayer(2))

    model.build()

    model.summary()

    model.train(x_data=x, y_data=y, train_round=100, accuracy=0.01)

if __name__ == '__main__':
    example()