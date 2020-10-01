#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:/Users/xlin8/OneDrive/Desktop/ISM 4402/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]
# Create names for the four groups
group_names = ['F', 'D', 'C', 'B', 'A']
df['LetterGrade'] = pd.cut(df['grade'], bins,
 labels=group_names)
df.tail()


# In[4]:


# Create the bin dividers
bins = [0, 80, 100]
# Create names for the two groups
group_names = ['Fail','Pass']
df['MasterProgram'] = pd.cut(df['grade'], bins,
 labels=group_names)
df.head()


# In[6]:


pd.value_counts(df['MasterProgram'])


# In[ ]:




