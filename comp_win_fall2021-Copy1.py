#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[111]:


import pandas as pd
import numpy as np


# In[112]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)


# In[113]:


#with open(r'C:\Users\saraswathy.rajaman\Documents\df_all.csv') as f: print(f)


# In[114]:


#df1=pd.read_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Winter-2021.csv', encoding='cp1252')
df1=pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\Winter_dev_2.xlsx','Pre_save')


# In[116]:


df2=pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\Winter_dev_2.xlsx','Post_dev')


# In[117]:


df3=df1.rename(columns=lambda x:x+'_input')
df4=df2.rename(columns=lambda x:x+'_postsave')


# In[118]:


#merge_src_process=pd.merge(df1,df2,on='CCP',how='left',indicator=True)


# In[119]:


df3['CCP_input'] = df3['CCP_input'].str.rstrip()
df4['CCP_postsave']=df4['CCP_postsave'].str.strip()


# In[120]:


merge_src_process1=pd.merge(df3,df4,left_on='CCP_input',right_on='CCP_postsave',how='outer',indicator=True)


# In[121]:


merge_src_process1.columns


# In[122]:


merge_src_process1.shape


# In[123]:


merge_src_process1['comp_Detail1']=merge_src_process1['Detail1_input']==merge_src_process1['Detail1_postsave']


# In[124]:


merge_src_process1['comp_wave']=merge_src_process1['Wave_input']==merge_src_process1['Wave_postsave']


# In[125]:


merge_src_process1['comp_ansid']=merge_src_process1['AnswerID_input']==merge_src_process1['AnswerID_postsave']


# In[126]:


merge_src_process1=merge_src_process1[['Detail1_input','Detail1_postsave', 'CCP_input','CCP_postsave','Wave_input','Wave_postsave','comp_Detail1', 'comp_wave','AnswerID_input','AnswerID_postsave','comp_ansid','_merge','Super_input','Super_postsave','Category_input','Category_postsave','Detail2_input','Detail2_postsave','Detail3_input','Detail3_postsave','Detail4_input','Detail4_postsave']]


# In[127]:


merge_src_process1.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\merge_inpspr_postdev.csv',index=False,header=True)


# In[128]:


#display(merge_src_process1)


# In[129]:


merge_src_process1.shape


# In[130]:


from sqlalchemy import create_engine


# In[ ]:


DB = {'server':'internalSQLdev.mridevops.com','database':'Codebook_Taxonomy','driver':'driver=SQL Server Native Client 11.0','pyodb_d':'SQL Server Native Client 11.0'}
#engine=create_engine('mssql+pyodbc://'+ DB['server']+'/'+ DB['database']+'?'+ DB['driver'])


# In[ ]:



engine = create_engine('mssql+pyodbc://' + DB['server'] + '/' + DB['database'] + '?' + DB['driver'], fast_executemany = True)


# In[ ]:


import pyodbc


# In[ ]:


conn = pyodbc.connect('Driver={'+DB['pyodb_d']+'}; Server='+DB['server']+';Database='+DB['database']+'; Trusted_Connection=yes;')


# In[ ]:


conn.commit()


# In[ ]:


with engine.begin() as connection:
    merge_src_process1.to_sql(name="tmp_EditedRecords_compwin_postsav",con=engine,schema="dbo",if_exists='replace', chunksize=1000,index=False)
#df.to_sql('db_table2', engine, if_exists='replace')

