
#####################
#                   #
#      Python       #
#                   #
#####################


#--- Containers --- #

#Lists
#A list is the Python equivalent of an array
#but is resizeable and can contain elements of different types:


#Dictionaries
#iterate over the keys in a dict
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))

#dict.items() to access index and corresponding values
for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))

#dict comprehensions
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x : x**2 for x in nums if x%2==0}

#Sets
animals = {'cat', 'dog'}

animals.remove('cat')
animals.add('camel') 

#sets are unorded
animals = {'cat', 'dog', 'camel'}
for id, animal in enumerate(animals):
    print('#%d: %s' %(id+1, animal))

#set comprehensions
from math import sqrt
nums = {sqrt(x) for x in range(30)}

#Tuples
#A tuple is an (immutable) ordered list of values
#tuples can be used as keys in dictionaries and as elements of sets
d = {(x,x+1): x for x in range(10)}
t=(5,6)


#--- Functions --- #

def sign(x):
    if x > 0:
        return 'positive'
    if x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-2,0,4]:
    print(sign(x))

#define functions to take optional keyword arguments
def hello(name, loud=False):
    if loud:
        print('HELLO %s' % name.upper())
    else:
        print('Hello %s' % name)

hello('Lee')
hello('Chris',loud=True)


#--- Classes --- #

class Greeter(object):

    #Constructor
    def __init__(self, name):
        self.name = name
    
    #Instance method
    def greet(self, loud=False):
        if loud:
            print('HELLO %s' % self.name.upper())
        else:
            print('Hello %s' % self.name)

g = Greeter('Fred')
g.greet()
g.greet(loud=True)



#####################
#                   #
#       Numpy       #
#                   #
#####################

#Numpy is the core library for scientific computing in Python

#--- Arrays --- #

#We can initialize numpy arrays from nested Python lists, and access elements using square brackets

import numpy as np
a = np.array([1,2,3])
a[0]=5

b = np.array([[1,2,3],[4,5,6]])

#functions to create arrays
#Numpy also provides many functions to create arrays

#array filled with zero
a = np.zeros((2,2))
b = np.zeros((1,2))

#constant array
c = np.full((5,2),7)

#identity matrix
d = np.eye(3)

#array filled with one
e = np.ones((2,2,2))

#array filled with random values
f = np.random.random((2,3,4))

#Array indexing
#Slicing
#Since arrays may be multidimensional, you must specify a slice for each dimension of the array
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a[:2,:]

#modify the value in slice will change the value in original array 
b[0,0] = 432

#create rank 2 array with shape (3,4)
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
row_r1 = a[1,:] 
row_r2 = a[1:2, :]
print(row_r2, row_r2.shape)

a = np.array([[1,2], [3, 4], [5, 6]])
#a[[0, 1, 2], [0, 1, 0]] = np.array([a[0, 0], a[1, 1], a[2, 0]])
#a[[0,0],[1,1]] = np.array(a[0,1],a[0,1])

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
b = np.array([0, 2, 0, 1])
a[np.arange(4), b] += 10
print(a)

#Boolean array indexing
bool_idx = (a>2)
print(bool_idx)

























