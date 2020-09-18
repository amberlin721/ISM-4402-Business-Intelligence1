#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'C:/Users/xlin8/OneDrive/Desktop/ISM 4402/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
    .format(db_file))
sql = "select name from sqlite_master where type = 'table' "
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[9]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'C:/Users/xlin8/OneDrive/Desktop/ISM 4402/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
    .format(db_file))
sql = 'select * from scores'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[ ]:




