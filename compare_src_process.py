#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[1]:


import sys
sys.path.insert(0, "path/to/your/venv")


# In[23]:


import pandas as pd
import numpy as np


# In[49]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)


# In[52]:


df1=pd.read_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Source_DB.csv')


# In[53]:


df1.columns


# In[54]:


df1.head(5)


# In[66]:


df1.shape


# In[65]:


df2.shape


# In[55]:


df2=pd.read_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Process_DB.csv')


# In[56]:


df2.head(5)


# In[57]:


df2.columns


# In[58]:


df3=df1.rename(columns=lambda x:x+'_srcdb')
df4=df2.rename(columns=lambda x:x+'_processdb')


# In[87]:


df_join_outer=df3.merge(right=df4,left_on=df3.columns.to_list(),right_on=df4.columns.to_list(),how='outer')


# In[88]:


df_join_outer.shape


# In[89]:


display(df_join_outer)


# In[90]:


df_join_outer['compare_CCP']=(df_join_inner['CCP_srcdb'] ==df_join_inner['CCP_processdb'])


# In[91]:


df_join_outer['compare_FL']=(df_join_inner['Full_Label_srcdb'] ==df_join_inner['Full_Label_processdb'])


# In[92]:


df_join_outer['compare_ansid']=(df_join_inner['AnswerID_srcdb'] ==df_join_inner['AnswerID_processdb'])


# In[94]:


display(df_join_outer)


# In[97]:


df_join_outer.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\df_join_outer.csv',index=False,header=True)


# In[27]:


df1.head(5)


# In[10]:


from io import StringIO


# In[12]:


different_locations = (df1 != df2)


# In[13]:


changed_from = df1.values[different_locations]
changed_to = df2.values[different_locations]


# In[16]:


difference = different_locations.stack()
changed = difference[difference]
difference = pd.DataFrame({'df1_values': changed_from, 'df2_values': changed_to}, index=changed.index)


# In[17]:


print(difference)


# In[ ]:




