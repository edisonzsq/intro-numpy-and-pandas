import numpy as np

# x = [10, 15, 20] # default python list
print(x)
print(np.average(x)) # np.average() provided by numpy

y = np.array([1,2,3,4,5,10,12]) # numpy array
print(y)
print(np.mean(y)) # np.mean() provided by numpy

# Slicing is important to learn in Python
print(y[:5]) # slice from index 0 to before index 5
print(y[5:]) # slice from index 5 to the end
print(y[4:6]) # slice from index 4 to before index 6

z = np.array([[1,2,3],[5,6,7],[8,9,10]])
print("original z:", z)
print("flattened z:", z.flatten()) # flatten() used to convert 2d array to 1d


