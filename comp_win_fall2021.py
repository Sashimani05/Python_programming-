#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


with open(r'C:\Users\saraswathy.rajaman\Documents\df_all.csv') as f: print(f)


# In[23]:


df1=pd.read_csv('C:\\Users\\saraswathy.rajaman\\Documents\\df_all.csv', encoding='cp1252')


# In[24]:


df2=pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\Fall2021.xlsx')


# In[25]:


df3=df1.rename(columns=lambda x:x+'_input')
df4=df2.rename(columns=lambda x:x+'_dict')


# In[26]:


merge_src_process=pd.merge(df1,df2,on='CCP',how='left',indicator=True)


# In[27]:


merge_src_process1=pd.merge(df3,df4,left_on='CCP_input',right_on='CCP_dict',how='left',indicator=True)


# In[28]:


merge_src_process1.columns


# In[29]:


merge_src_process1.shape


# In[36]:


merge_src_process1['comp_Detail1']=merge_src_process1['Shows_Name_input']==merge_src_process1['Detail1_dict']


# In[37]:


merge_src_process1['comp_wave']=merge_src_process1['wave_input']==merge_src_process1['Wave_dict']


# In[38]:


merge_src_process1=merge_src_process1[['Shows_Name_input','Detail1_dict', 'W2021_input','CCP_dict','wave_input','Wave_dict','comp_Detail1', 'comp_wave','_merge']]


# In[39]:


merge_src_process1.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\merge_inp_dict.csv',index=False,header=True)


# In[ ]:





# In[ ]:




