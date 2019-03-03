import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

if (__name__ == '__main__'):
    mu = 1
    sigma = 3
    num = 1000

    rand_data = np.random.normal(mu, sigma, num)
    count, bins, ignore = plt.hist(rand_data, 30, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins-mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
    plt.show()