#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/xlin8/OneDrive/Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
df.hist()


# In[6]:


df.hist(column="age", by="gender")


# In[ ]:




