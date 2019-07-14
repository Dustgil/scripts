import numpy as np
import matplotlib.pyplot as plt

def linregression(data):
    # create matrix
    A = np.array([1,1]) # starting row to make dimensions work for cleaner code.
    for point in data:
        row = [1, point[0]]
        A = np.vstack([A, row])

    A = np.delete(A, (0), axis=0) # delete starting row to get correct matrix

    T = A.transpose()

    TA = np.matmul(T, A)
    inv = np.linalg.inv(TA)

    l = []
    for e in data:
        l.append(e[1])

    y = np.array(l)
    y = y.transpose()



    v = np.matmul(inv, T)
    v = np.matmul(v, y)

    print(v)


    # now seperate the data points into their x and y-coordinates to prep for plotting
    x = []
    y = []

    for e in data:
        x.append(e[0])
        y.append(e[1])


    # here we use the found slope and intercept for the line of best fit.
    abline_values = [v[1] * i + v[0] for i in x]

    # plot individual datapoints
    plt.scatter(x,y)
    # plot line of best fit
    plt.plot(x, abline_values)
    plt.show()

# input data
input_data = [[0,1],[1,3],[2,4],[3,4]]

linregression(input_data)
