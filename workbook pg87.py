#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/xlin8/OneDrive/Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[22]:


df.plot.scatter(x='hours',y='grade')
plt.show()


# In[ ]:




