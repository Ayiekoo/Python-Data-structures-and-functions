#!/usr/bin/env python
# coding: utf-8

# In[3]:


### checking duplicates in a list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
            
print(duplicates)


# In[4]:


### we can write a simple code for the same
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)


# In[ ]:





# In[ ]:




