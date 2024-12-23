#function are the building blocks of neural network and they can represented in sevral 
#ways 

#with math
"""
f1(x) = x^2
f2(x) = max(x, 0)
"""
#both functions take in input for transformation 


"""
diagrams 
* draw an x-y plane (where x refers to the horizontal axis and y refers to the vertical axis)
* Plot a bunch of points, where the x cordinates of the points are usually inputs of the function
    over some range range, and the y-coordinates are the output of the  function over that range

* Connect these plotted point
"""

#another way is  thinking about functions in terms of boxes 
"""
* we can think of  functions as that takes in numbers as input and 
    produce numbers as output 
* they are minifactories that have their own rules
"""

#finally code 
#we can describe this functions using code 
#some numpy for preparation 
from typing import List
import numpy as np 
print("python list operations:")
a= [1,2,3]
b = [4,5,6]
print("a+b", a+b)
print("a*b has no meaning for python lists")
print()
print("numpy array operations: ")
a = np.array([1, 2, 3])
b = np.array([4,5, 6])
print("a+b:", a+b)
print("a*b:", a*b)

#2d is also available 
print('a:')
print(a)
print('a.sum(axis=0):', a.sum(axis=0))
print('a.sum(axis=1):', a.sum(axis=0))

a = np.array([1, 2, 3], [4, 5, 5])
b = np.array([10, 20, 30])

print("a+b:\n", a+b)

#function with ype signature helps us to handle the complexities 
#of the type of function we are going to be writing. 
#an example is given below 
def __init__(self, 
             layers: List[Layer],
             loss: Loss,
             learning_rate: float = 0.01
             ) -> None:
    
#basic functions in Numpy

def square(x: ndarray) ->ndarray:
    '''
    Square each element in the input ndarray.
    '''

    return np.power(x, 2)

def leaky_relu(x: ndarray) -> ndarray:
    '''
    Apply "Leaky Relu" function to each element in ndarry.
    '''
    return np.maximum(0.2 * x, x )
#in Numpy, many functions can be applied to ndarrays either 
#by writing np.function_name(ndarray)
# nd.array_function_name.
#ndarray.T 
#np.transpose(ndarray, (1, 0))