#!/usr/bin/env python
# coding: utf-8

# In[1]:


# string

"""
python string is a sequence of characters
"""

## indexing and slicing

s = "The youngest pope was 11 years old"
print(s[0])


# In[2]:


print(s[1:3])


# In[3]:


print(s[-3:-1])


# In[5]:


print(s[-3:])


# In[7]:


x = s.split() ### creates a string array of words
print(x[-3] + " " + x[-1] + " " + x[2] + "s")


# In[ ]:




