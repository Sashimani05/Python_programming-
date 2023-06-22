#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[3]:


import pandas as pd
import zipfile

zip_file=zipfile.ZipFile((r"C:\Users\saraswathy.rajaman\Documents\Output.zip"))
dfs = []
for i in range(len(zip_file.namelist())):
    df=pd.read_csv(zip_file.open(zipfile.ZipFile.namelist(zip_file)[i]),header='infer', sep='|',encoding='UTF-8', on_bad_lines='skip')
    dfs.append(df)
    i=i+1
full_df = pd.concat(dfs, ignore_index=True)


# In[4]:


df_RLD=full_df.copy()


# In[5]:


#if duplicated deducted in RLD write in a sepeprate file and exit

boolean = df_RLD.duplicated().any() 
if boolean==True: 
    print ("We found duplicate records in the RLD File.Please check the file") 
    RLD_Duplicated=df_RLD.duplicated(subset=None,keep=First) 
    RLD_Duplicated.to_csv(r'C:\Users\saraswathy.rajaman\Documents\RLD_Duplicates.csv',index=False,header=True)
else:
    print("NO Duplicated record found")
exit()


# In[ ]:




