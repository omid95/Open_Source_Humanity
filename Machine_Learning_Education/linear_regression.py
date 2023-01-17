from itertools import starmap

x = [1,2,3]

def mean(x):
   """ calculate the mean of the list of numbers"""
   return sum(x)/len(x)

def variance(list_x):
    """calculates the variance of the list of numbers"""
    m = mean(list_x)
    return sum(map(lambda x: ((x-m)**2)/len(list_x), list_x))

def covariance(list_x, list_y):
    """calculate the covariance between two lists of numbers"""
    mx = mean(list_x)
    my = mean(list_y)
    return (sum(starmap(lambda x, y : ((x-mx)*(y-my))/len(list_x), zip(list_x, list_y))))

def linearRegression(list_x, list_y):
    """calculates the coefficients for the linear regression line using the least squares method
       Returns a tuple representing the y-intercept and slope of the line"""
    b1 = covariance(list_x, list_y) / variance(list_x)
    b0 = mean(list_y) - b1*mean(x)
    return b0, b1

def predict(list_x, list_y, unknown_x_list):
    """Predicts the y-value for a given x-value based on the linear regression line"""
    b0, b1 = linearRegression(list_x, list_y)
    result = b0+b1*unknown_x_list
    return result


#testing the functions
print("mean" + str(mean(x)))
print("variance" + str(variance(x)))
print("covariance" + str(covariance([1,2,3], [1,2,3])))
print("linear regression" + str(linearRegression([1,2,3], [1,2,3])))
print("prediction" + str(predict([1,2,3], [1,2,3], 4)))

