x = [1,2,3]

def mean(x):
   """ calculate the mean of the list of numbers"""
   return sum(x)/len(x)

def variance(list_x):
    """calculates the variance of the list of numbers"""
    m = mean(list_x)
    v=0
    for x in list_x:
        v += ((x - m)**2)/len(list_x)
    return v

def covariance(list_x, list_y):
    """calculate the covariance between two lists of numbers"""
    mx = mean(list_x)
    my = mean(list_y)
    cv = 0
    for x, y in zip(list_x, list_y):
        cv += ((x-mx)*(y-my))/len(list_x)

    return cv

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
print(mean(x))
print(variance(x))
print(covariance([1,2,3], [1,2,3]))
print(linearRegression([1,2,3], [1,2,3]))
print(predict([1,2,3], [1,2,3], 4))

