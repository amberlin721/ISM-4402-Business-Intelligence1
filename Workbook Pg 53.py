#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
Location = "C:/Users/xlin8/OneDrive/Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.tail()


# In[2]:


df.take(np.random.permutation(len(df))[:500])


# In[ ]:




