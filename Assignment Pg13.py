#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("C:/Users/xlin8/OneDrive/Desktop/weekly_call_data/weekdata_*"):
 df = pd.read_excel(f)
 all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[ ]:




