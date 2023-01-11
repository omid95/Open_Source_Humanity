from itertools import starmap
points = ([1,2,4], [1,2,3])

def mean(xs):
    return sum(xs)/len(xs)


def predict(x, linreg):
    """Predicts the y-value for a given x-value based on the linear regression line"""
    b0, b1 = linreg
    return b0 + b1 * x

def cost(points, linreg):
    """calculates the cost for a given set of predictions and actual y values """
    xs, ys = points
    return (1 / (2 * len(xs))) * sum (starmap(lambda x, y : (predict(x, linreg) - y)**2, zip(xs, ys)))

def gradientDescent(lr, iters, linreg):
    """gradientDescent algorithm to minimize the cost function 
       and find the optimal values for the slope and y-intercept"""

    b0, b1 = linreg
    xs, ys = points
    deltaB0 = (lr / len(xs))*sum(starmap(lambda x, y: (predict(x, linreg)-y), zip(xs, ys)))
    deltaB1 = (lr/ len(xs))*sum(starmap(lambda x, y: ((predict(x, linreg)-y)*x), zip(xs, ys)))
    newB0 = b0 - deltaB0
    newB1 = b1 - deltaB1

    if iters == 0:
        return (b0, b1)

    else:
        return gradientDescent(lr, iters -1, (newB0, newB1))

def linearRegression():
    """returns the tuple for the predicted slope and y-intercept"""
    return gradientDescent(0.01, 100, (0,0))
    


print(mean([1,2,3]))
print(predict(1, (0,1)))
print(cost(points, (3,4)))
print(linearRegression())
