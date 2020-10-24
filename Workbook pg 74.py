#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
 columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[7]:


import matplotlib.pyplot as plt
df.plot()
displayText = "WOW!"
xloc = 1
yloc = df['Grades'].max()
xtext = -320
ytext = -200
plt.annotate(displayText,
 xy=(xloc, yloc),
 xytext=(xtext,ytext), 
 xycoords=('axes fraction', 'data'),
 textcoords='offset points')


# In[ ]:




