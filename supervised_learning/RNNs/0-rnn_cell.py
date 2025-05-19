import numpy as np

class RNNCell:
    def __init__(self, i, h, o):
        """
        Initialize the RNN cell
        i: input data dimension
        h: hidden state dimension
        o: output dimension
        """
        # Weight for hidden state and input concatenated
        self.Wh = np.random.randn(i + h, h)
        self.bh = np.zeros((1, h))

        # Weight and bias for output
        self.Wy = np.random.randn(h, o)
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        Perform forward propagation for one time step
        h_prev: shape (m, h), previous hidden state
        x_t: shape (m, i), input data at time t
        Returns: h_next, y
        """
        # Concatenate previous hidden state and current input
        concat = np.concatenate((h_prev, x_t), axis=1)  # shape (m, h+i)

        # Compute next hidden state using tanh activation
        h_next = np.tanh(np.dot(concat, self.Wh) + self.bh)  # shape (m, h)

        # Compute output using softmax activation
        y_linear = np.dot(h_next, self.Wy) + self.by  # shape (m, o)
        y = self.softmax(y_linear)  # shape (m, o)

        return h_next, y

    @staticmethod
    def softmax(x):
        """Compute softmax activation"""
        e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return e_x / np.sum(e_x, axis=1, keepdims=True)
