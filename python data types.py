#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## PYTHON DATA STRUCTURES
"""
INCLUDE; lists, dictionaries, sets, and tuples
"""

"""
pythpn lists
> are a collection of items that are mutable and ordered
> are denoted by brackets [] and can contain elements of different types
> multiple values can be stored in the lists
> elements in the list can be accessed by indexing and slicing
> lists can store and manage a collection of related data
"""


# In[2]:


# consider a list of fruits

### create a list of fruits
fruits = ['apples', 'bananas', 'oranges', 'grapes', 'mangoes']
print(fruits)


# In[3]:


# accessing the elements in the list
print(fruits [0])

#### apples are in position 1[0] in the list


# In[5]:


## we can access the elements in the list using a negative index
print(fruits [-1])

## Remember indexing in python begins with 0, 1, 2, 3 etc ##


# In[6]:


### iterating over a list
for fruit in fruits:
    print(fruit)


# In[7]:


# list concatenation
more_fruits = ['beetroot', 'tomatoes']
all_fruits = fruits + more_fruits
print(all_fruits)


# In[8]:


### sorting lists
all_fruits.sort()
print(all_fruits)


# In[10]:


all_fruits.reverse()
print(all_fruits)


# In[11]:


## counting occurance of an element in a list
count_beetroot = all_fruits.count('beetroot')
print(count_beetroot)


# In[12]:


## clearing a list
all_fruits.clear()
print(all_fruits)


# In[16]:


# mixed lists
lst = [40, 'apples', True, 33.44]
print(lst)


# In[20]:


### appending elements to a list
numbers = [10, 20, 30, 40, 50, 60]
numbers.append(70)
numbers.append(80)
numbers.append(90)
numbers.append(100)
print(numbers)


# In[21]:


## removing the last element in the list
numbers .pop()
print(numbers)


# In[22]:


## Slicing
## python has an accurate syntax for accessing sublists; this syntax is called slicing
nums = list(range(10))
print(nums)


# In[23]:


print(nums[3:5]) ## Gets a slice from index 2 to 4


# In[24]:


print(nums[3:]) ## Gets a slice from index 2 to the end


# In[25]:


print(nums[:3]) #### slices the list from the start to index 2


# In[26]:


print(nums[:]) ### slices the whole list


# In[27]:


print(nums[-1])


# In[29]:


nums[2:4] = [6,8] ### assigns new sublist to a slice
print(nums)


# In[30]:


### list comprehensions

"""
when programming, we often want to transform one data type to another.
for example, consider the code below
"""

numbers = [1, 2, 3, 4, 5]
squared_numbers = []

# calculating the Loop function to calculate the square of each number

for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)


# In[31]:


# we can simplify this code using comprehensions

# list comprehension

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)


# In[33]:


##### list comprehensions can also have conditions
## list comprehension with if statement

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


# In[34]:


## Dictionaries

d = {'cat': 'cute', 'dog': 'furry'} ## create a new dictionary with some data
print(d['cat']) ## get an entry from the dictionary


# In[35]:


print('cat' in d)


# In[36]:


print(d['lion'])


# In[37]:


print(d.get('lion', 'N/A')) ## GET AN ELEMENT WITH A DEFUALT; PRINTS "N/A"


# In[38]:


print(d.get('fish', 'N/A'))  ## GET AN ELEMENT WITH A DEFUALT; PRINTS "N/A"


# In[39]:


del d['dog']  ## remove an element from the dictionary
print(d.get('dog', "N/A"))


# In[40]:


d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A {} has {} legs'.format(animal, legs))


# In[41]:


d = {'Alex': 1, 'Sam': 2}
for person, offsprings in d.items():
    print('{} has {} offsprings'.format(person, offsprings))


# In[42]:


"""
dictionary comprehensions
are similar to list comprehensions, but allows easy construction of dictionaries
consider the example below
"""

nums = [0, 1, 2, 3, 4, 5, 6]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0} ## squares of even numbers
print(even_num_to_square)


# In[44]:


nums = [0, 1, 2, 3, 4, 5, 6]
odd_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0} ## squares of even numbers
print(odd_num_to_square)


# In[45]:


### SETS  as data types in python

animals = {'dog', 'cat'}
print('cat' in animals) """code checks if an element is in a set. if the element is present, it prints TRUE"""


# In[46]:


print(len(animals)) ## code prints the number of animals in the set


# In[47]:


animals.add('dog') ## adds dog to the list
print(len(animals)) ## nothing happens because dog is already in the set


# In[48]:


animals.add('elephant') ## adds an animals to the list
print(len(animals))


# In[53]:


animals.remove('elephant')
print(len(animals))


# In[52]:


animals.remove('dog')
print(len(animals))


# In[54]:


### PYTHON LOOPS
"""
Iterating over a set has the same syntax as over a list.
However, since the set is unordered, we cannot assume the order of elements in a loop
"""

animals = {'cat', 'dog', 'fish'}
for idx, animals in enumerate(animals):
    print('#{}: {}'.format(idx + 1, animals)) ## gives 1 as the first index


# In[55]:


fruits = ['apple', 'banana', 'mango', 'grape']

for i, fruit in enumerate(fruits): ### gives 0 as first index
    print(f"Index: {i}, Fruit: {fruit}")


# In[56]:


for i, fruit in enumerate(fruits, 1): ## gives 1 as first index
    print(f"Index: {i}, Fruit: {fruit}")


# In[57]:


animals = {'cat', 'dog', 'fish'}
for idx, animals in enumerate(animals):
    print('Animal {}: {}'.format(idx + 1, animals)) ## gives 1 as the first inde


# In[59]:


animals = {'cat', 'dog', 'fish'}
for idx, animals in enumerate(animals):
    print('animal {} is a {}'.format(idx + 1, animals)) ## gives 1 as the first inde


# In[64]:


"""
We can have a set of comprehensions
Like lists and dictionaries
We can construct sets using set comprehensions
"""
from math import sqrt
print({int(sqrt(x)) for x in range(30)})


# In[62]:


##### TUPLES ####

"""
A tuple is an immutable ordered list of values.
is somewhat similar to a list
can be used as keys in dictionaries and elements in sets
"""
d = {(x, x +1): x for x in range(10)} ## a dictionary with tuple keys
t = (5, 6) ## a mere tuple
print(t)


# In[63]:


print(type(t))


# In[65]:


print(d[t])


# In[66]:


print(d)


# In[67]:


print(d[(1, 2)])


# In[70]:


#### PYTHON FUNCTIONS
"""
Python functions are defined using the the keyword; def
consider the example below
"""
def add_numbers(a, b):
    return a + b

## call the add_numbers function and print the result
num1 = 10
num2 = 23
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")


# In[71]:


#### PYTHON FUNCTIONS
"""
Python functions are defined using the the keyword; def
consider the example below
"""
def add_numbers(a, b):
    return a + b

## call the add_numbers function and print the result
num1 = 10
num2 = 23
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")


# In[72]:


# Function to calculate the product of two numbers

def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the product
    """
    return a * b
# call the multiply_numbers function and print the result
num3 = 20
num4 = 25
result = multiply_numbers(num3, num4)
print(f"The product of {num3} and {num4} is: {result}")


# In[73]:


# Lambda function to calculate the square of a number
square = lambda x: x ** 2

## call the square lambda function and print the result
num5 = 7
result = square(num5)
print(result)


# In[74]:


### here is how to define functions to take optional keyword arguments
def greet(name, age=None, location=None):
    """
    Greets a person with their name and optionally their age and location
    """
    message = f"Hello, {name}!"
    if age is not None:
        message += f" You are {age} years old."
    if location is not None:
        message += f"You are from {location}."
    return message

### calling great function with different arguments
print(greet("Ali"))


# In[75]:


print(greet("Bob", age=25))


# In[76]:


print(greet("Charlie", age=30, location="New York"))


# In[ ]:




