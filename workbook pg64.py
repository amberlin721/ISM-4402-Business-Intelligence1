#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:/Users/xlin8/OneDrive/Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


def score_to_numeric(x):
    if x=='female':
        return 1
    if x=='male':
        return 0
df['GenderinNumericValue']= df['gender'].apply(score_to_numeric)
df.tail()


# In[4]:


import statsmodels.formula.api as sm
result = sm.ols(
 formula='grade ~ exercise + hours + GenderinNumericValue', 
data=df).fit()
result.summary()


# In[ ]:




