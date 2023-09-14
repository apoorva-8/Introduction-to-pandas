#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


import os


# In[7]:


os.getcwd()


# In[12]:


os.chdir("C:\\Users\\STUDENT\\Desktop")


# In[13]:


os.getcwd()


# In[14]:


data=pd.read_csv("retail_sales_dataset.csv")


# # To view some parts of data to know column names

# In[15]:


data.head()


# In[16]:


data.tail()


# # To see short summary of data

# In[17]:


data.info()


# # Statistical Inferences

# In[19]:


data.describe()


# # This function helps you to check if there in which row and which column your data has missing values.

# In[20]:


data.isnull()


# In[ ]:




