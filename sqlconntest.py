#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[ ]:


from sqlalchemy import create_engine


# In[ ]:


DB = {'server':'internalSQLdev.mridevops.com','database':'Codebook_Taxonomy','driver':'driver=SQL Server Native Client 11.0','pyodb_d':'SQL Server Native Client 11.0'}
#engine=create_engine('mssql+pyodbc://'+ DB['server']+'/'+ DB['database']+'?'+ DB['driver'])


# In[ ]:



engine = create_engine('mssql+pyodbc://' + DB['server'] + '/' + DB['database'] + '?' + DB['driver'], fast_executemany = True)


# In[ ]:


import pyodbc 


# In[ ]:


conn = pyodbc.connect('Driver={'+DB['pyodb_d']+'}; Server='+DB['server']+';Database='+DB['database']+'; Trusted_Connection=yes; Integrated Security=true')


# In[6]:


import pandas as pd
#data = [4, 14, 17, 22, 26, 29, 33, 35, 35, 38]

#convert list to DataFrame
#df = pd.DataFrame(data, columns=['points'])


# In[8]:


with open(r'C:\Users\saraswathy.rajaman\Documents\Spring-2021.csv') as f: print(f)


# In[9]:


df=pd.read_csv(r'C:\Users\saraswathy.rajaman\Documents\Spring-2021.csv',encoding='cp1252')


# In[ ]:


conn.commit()


# In[ ]:


with engine.begin() as connection:
    df.to_sql(name="tmp_EditedRecords_testsqlingest",con=engine,schema="dbo",if_exists='replace', chunksize=100,index=False)
#df.to_sql('db_table2', engine, if_exists='replace')

