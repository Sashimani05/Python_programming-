#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[ ]:


import pandas as pd
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=internalSQLdev.mridevops.com;'
                      'Database=Codebook_Taxonomy;'
                      'Trusted_Connection=yes;')
Prev_Dict_StudyEntryID = '411'

Prev_Dict_VersionID = '13'

query = "EXEC [app_Codebook_Read] @VersionID = {0}, @StudyEntryID = {1}".format(Prev_Dict_VersionID, Prev_Dict_StudyEntryID)
df = pd.read_sql_query(query, conn)

print(df)
print(type(df))


# In[ ]:


#om Codebook_Taxonomy.dbo.tmp_editedrecords_test

