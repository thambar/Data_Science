#!/usr/bin/env python
# coding: utf-8

# # Welcome to NumPy!

# In[1]:


import numpy as np 
import pandas as pd


# NumPy arrays are faster and more compact than Python lists. An array consumes less memory and is convenient to use

# In[9]:


a = np.arange(23)
a2 = a[np.newaxis, :]

a2


# In[7]:


a2.shape


# In[11]:


a = np.array([1, 2, 3, 4, 5, 6])


# In[12]:


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# In[13]:


print(a[0])


# In[16]:


(a[2,0])


# In[25]:


np.zeros(8)


# The function empty creates an array whose initial content is random and depends on the state of the memory.

# In[27]:


# Create an empty array with 2 elements
np.empty(5) 


# You can also use np.linspace() to create an array with values that are spaced linearly in a specified interval:

# In[28]:


np.linspace(0, 10, num=5)


# In[29]:


arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])


# In[30]:


np.sort(arr)

