#!/usr/bin/env python
# coding: utf-8

# In[1]:


### is
x = y = 3
x is y


# In[2]:


[3] is [3]


# In[3]:


### checking whether an element is in a string
42 in [2, 39, 42]


# In[4]:


77 in [99, 524, 78, 9]


# In[7]:


### none

## empty value constant
def f():
    x = 2
f() is None


# In[8]:


# define a function f
def f():
    # set a local variable x to 2
    x = 2

# call the function f and check if it returns None
print(f() is None)  # this will print True


# In[ ]:




