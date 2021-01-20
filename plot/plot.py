# Functions


def hello_plot():
    """Draws an example matplotlib plot"""
    import numpy as np
    import matplotlib.pyplot as plt
    _plot = plt.figure(figsize=[5, 5])
    _scatter = np.array([[1,2,3,4,5],[5,4,3,2,1]])
    plt.scatter(_scatter[0], _scatter[1])
    plt.show()
