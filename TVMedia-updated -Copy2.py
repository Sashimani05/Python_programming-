#!/usr/bin/env python
# coding: utf-8

# # Import necessary library

# In[1]:


#import Necessary Library
import pandas as pd
import numpy as np
from openpyxl import Workbook
import re


# In[2]:


import warnings
warnings.filterwarnings("ignore")


# In[3]:


#Display settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)


# # Read csv file 

# with open(r'C:\Users\saraswathy.rajaman\Documents\w84_Media_TV_Movie_Sections2.csv') as f:
#     print(f)

# In[4]:


df_TV_Movie=pd.read_csv(r'C:\Users\saraswathy.rajaman\Documents\w84_Media_TV_Movie_Sections2.csv',encoding='utf8')
#TV Media file


# In[5]:


#df_TV_Movie


# In[6]:


#df=pd.read_csv(r'C:\Users\saraswathy.rajaman\Documents\Fall_2020_2.csv',encoding = 'utf-8')


# In[7]:


#Making a copy 
df_TV_Movie_copy=df_TV_Movie.copy()


# with open(r'C:\Users\saraswathy.rajaman\Documents\Fall_2020.csv') as f:
#     print(f)

# In[8]:


df_Fall_2020=pd.read_excel(r'C:\Users\saraswathy.rajaman\Documents\Fall_2020.xlsx')
#read the fall file as DF


# In[9]:


#df_TVMov_Punch_Map=pd.read_csv(r'C:\Users\saraswathy.rajaman\Documents\TVMov_Punch_Map.csv',encoding="UTF-8")
#TVMovies Punch file 


# In[10]:


df_TV_Movie.rename(columns={'Unnamed: 6':'Sec_List_Heading','Unnamed: 7':'OneWave_Suppress','Show':'Show_Type','Unnamed: 8':'Shows_Name','Unnamed: 9':'Initial_Wave'}, inplace=True)
#Rename columns as suggested


# In[11]:


#Removing spl character
df_TV_Movie['F2020']=df_TV_Movie['F2020'].str.replace('*','')
df_TV_Movie['S2021']=df_TV_Movie['S2021'].str.replace('*','')


# In[12]:


df_TV_Movie=df_TV_Movie.drop(0)
#dropping first row from the DF


# # Remove one wave suppress -X values

# In[13]:


df_TV_Movie.drop(df_TV_Movie.index[df_TV_Movie['OneWave_Suppress'] == 'X'], inplace = True)


# In[14]:


#df_TV_Movie['OneWave_Suppress'].unique()
#check the unique values in that column  by that confirm the X is removed


# In[15]:


df_TV_Movie.columns = df_TV_Movie.columns.str.replace(' ', '')


# # check if the CCP is different between S2021 and F2020

# In[16]:


df_TV_Movie['compare'] = (df_TV_Movie['S2021'] == df_TV_Movie['F2020'])


# # Forward fill Clean type and list heading

# In[17]:


df_TV_Movie=df_TV_Movie.copy()
df_TV_Movie['cleantype']=df_TV_Movie['cleantype'].fillna(method='ffill')
#Forward fill cleatype as show


# In[18]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].replace('b', np.nan)
# replace b with np nan


# In[19]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].replace(r'^\s*$', np.nan, regex=True)
#Replace empty with np.nan


# In[20]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].fillna(method='ffill')
#Forward fill to get values in empty cell with list heading appropriately


# # Few items has # in sec heading- add # in one wave column for them 

# In[21]:


for i in range(len(df_TV_Movie)):
        value=df_TV_Movie.iloc[i,6]
        firstvalue=value[0]
        if firstvalue =='#':
                df_TV_Movie.iloc[i,7]='#'


# In[22]:


df_TV_Movie['Shows_Name']=df_TV_Movie['Shows_Name'].astype(str)


# In[23]:


for i in range(len(df_TV_Movie)):
        value=df_TV_Movie.iloc[i,8]
        firstvalue=value[0]
        if firstvalue =='#':
                df_TV_Movie.iloc[i,8]=value[1:]


# # For one wave item append # in show names

# In[24]:


for i in range(len(df_TV_Movie)):
    OneWave_Suppress=df_TV_Movie.iloc[i,7] 
    if OneWave_Suppress == '#': 
        df_TV_Movie.iloc[i,8]='#'+ df_TV_Movie.iloc[i,8]


# # Remove # from List heading or sec heading values

# In[25]:


for i in range(len(df_TV_Movie)):
        value=df_TV_Movie.iloc[i,6]
        firstvalue=value[0]
        if firstvalue =='#':
                df_TV_Movie.iloc[i,6]=value[1:]


# # Drop Empty rows where na in s2021

# In[26]:


#df_TV_Movie['S2021'].isna().value_counts()


# In[27]:


df_TV_Movie=df_TV_Movie.dropna(subset=['S2021'])


# In[28]:


#df_TV_Movie['S2021'].isna().value_counts()


# In[29]:


df_TV_Movie.to_csv(r'C:\Users\saraswathy.rajaman\Documents\df_TV_Movie_test.csv',index=False,header=True,encoding='cp1252')


# # TV1

# In[30]:


df_TV_Movie_TV1=df_TV_Movie.query('cleantype=="TV1" and OneWave_Suppress!="#"')
#filter TV1 from the source and save as DF


# In[31]:


#df_TV_Movie_TV1


# In[32]:


df_TV_Movie_TV1['F2020']=df_TV_Movie_TV1['F2020'].str.replace('nan','')
df_TV_Movie_TV1['S2021']=df_TV_Movie_TV1['S2021'].str.replace('nan','')
#if there is nan we are removing as being object data type appending 1 add's as nan1


# In[33]:


dftest_TV1={}
df_TV_Movie_PV_TV1={}
df_inner_PV_TV1={}
#V1_1W={}
value=['x','0','1','2','3','4','5','6','8','9']
j=0
PV=['x','0','1','2','3','4','5','6','8','9']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_TV1[name]=df_TV_Movie_TV1.copy()
    for i in range(len(df_TV_Movie_PV_TV1[name])):
        type=df_TV_Movie_PV_TV1[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_TV1[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_TV1[name].iloc[i,11]= str(df_TV_Movie_PV_TV1[name].iloc[i,11]) + str(value[j])
            
    dftest_TV1[name] = pd.DataFrame(df_TV_Movie_PV_TV1[name])
    df_inner_PV_TV1[name]= pd.merge(dftest_TV1[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_outer_PV_TV1[name]= pd.merge(dftest_TV1[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],how='leftouter')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #TV1_1W[name]=dftest_TV1[name].query('OneWave_Suppress=="#"')
    
    j +=1
 #append Punch variables and check for a matching value in fall 2020 file and store in dataframe for each punch value in col1  


# In[34]:


df_TV_Movie_TV1['F2020']=df_TV_Movie_TV1['F2020'].str.replace('nan','')
df_TV_Movie_TV1['S2021']=df_TV_Movie_TV1['S2021'].str.replace('nan','')
df_TV_Movie_TV1[['F2020']]=df_TV_Movie_TV1[["F2020"]].apply(pd.to_numeric)
df_TV_Movie_TV1[['S2021']]=df_TV_Movie_TV1[["S2021"]].apply(pd.to_numeric)
#convert columns to numeric to add 1 to the column


# In[35]:


df_TV_Movie_TV1['Col2PV']=''
#adding a col2pv so that we can update yes to them when the value is a col2 punchvalue this is used later to check if that is a col2 value


# In[36]:


#col2 punch value
for i in range(len(df_TV_Movie_TV1)):
    type=df_TV_Movie_TV1.iloc[i,0]
    cleantype=df_TV_Movie_TV1.iloc[i,1]
    if type == 'show':
        df_TV_Movie_TV1.iloc[i,11] = df_TV_Movie_TV1.iloc[i,11] +1
        df_TV_Movie_TV1.iloc[i,4] =  df_TV_Movie_TV1.iloc[i,4] + 1
        df_TV_Movie_TV1.iloc[i,17] = 'Yes'


# In[37]:


#coverting to numeric adds a decimal point so removing the decimal value 
#so that while appending a PV it is not appended next to this decimal value 
df_TV_Movie_TV1['F2020'] = df_TV_Movie_TV1['F2020'].astype(str).apply(lambda x: x.replace('.0',''))
df_TV_Movie_TV1['S2021'] = df_TV_Movie_TV1['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[38]:


df_TV_Movie_TV1['F2020']=df_TV_Movie_TV1['F2020'].str.replace('nan','')
df_TV_Movie_TV1['S2021']=df_TV_Movie_TV1['S2021'].str.replace('nan','')


# In[39]:


dftest_TV1_2={}
df_TV_Movie_PV_TV1_2={}
df_inner_PV_TV1_2={}
#TV1_1W_2={}

value=['4','5']
j=0
PV=['4','5']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    df_TV_Movie_PV_TV1_2[name]=df_TV_Movie_TV1.copy()
    for i in range(len(df_TV_Movie_PV_TV1_2[name])):
        type=df_TV_Movie_PV_TV1_2[name].iloc[i,0]
        if type == 'show':
            if df_TV_Movie_PV_TV1_2[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_TV1_2[name].iloc[i,11]= str(df_TV_Movie_PV_TV1_2[name].iloc[i,11]) + str(value[j])
            
    dftest_TV1_2[name] = pd.DataFrame(df_TV_Movie_PV_TV1_2[name])
    df_inner_PV_TV1_2[name]= pd.merge(dftest_TV1_2[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #TV1_1W_2[name]=dftest_TV1_2[name].query('OneWave_Suppress=="#"')
    j +=1


# In[40]:


PTV1= [df_inner_PV_TV1['0'],
           df_inner_PV_TV1['1'],
           df_inner_PV_TV1['2'], 
           df_inner_PV_TV1['3'], 
           df_inner_PV_TV1['4'],
           df_inner_PV_TV1['5'],
           df_inner_PV_TV1['6'],
           df_inner_PV_TV1['8'],
           df_inner_PV_TV1['9'],
           df_inner_PV_TV1['x'],
           df_inner_PV_TV1_2['4'],
           df_inner_PV_TV1_2['5'],
          ]


# In[41]:


TV1concat=pd.concat(PTV1)


# In[42]:


TV1concat['LastDigit_PV'] = TV1concat['F2020'].apply(lambda x: x[-1:])


# In[43]:


#TV1concat['LastDigit_PV'] 


# In[44]:


TV1concat['F2020_Updated']= TV1concat['S2021'] + TV1concat['LastDigit_PV']


# # TV1 One Wave

# In[45]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[46]:


dfOneW_TV1=dfOneW.query("cleantype=='TV1'")


# In[47]:


df_TV1=[TV1concat,dfOneW_TV1]


# In[48]:


df_TV1=pd.concat(df_TV1)


# In[49]:


#display(df_TV1)


# In[50]:


df_TV1= df_TV1.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[51]:


#df_TV1


# In[52]:


#df1_TV1=df_TV1.query("cleantype=='TV1'")


# In[53]:


#df_TV1.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV1concat.csv',header=True,index=False)


# In[54]:


df1w_TV1=df_TV1.query("OneWave_Suppress=='#'")


# In[55]:


dfnon1w_TV1=df_TV1.query("OneWave_Suppress!='#'")


# In[56]:


onewave_TV1={}
dfonewave_TV1={}

value=['x','0','1','2','3','4','5','6','8','9']
j=0
PV=['x','0','1','2','3','4','5','6','8','9']

for name in PV:
        
    onewave_TV1[name]=df1w_TV1.copy()
    for i in range(len(onewave_TV1[name])):
            onewave_TV1[name].iloc[i,2]= str(onewave_TV1[name].iloc[i,2]) + str(value[j])
            onewave_TV1[name].iloc[i,16]=onewave_TV1[name].iloc[i,6]
            onewave_TV1[name].iloc[i,36]=onewave_TV1[name].iloc[i,2]
            onewave_TV1[name].iloc[i,29]='0'
            onewave_TV1[name].iloc[i,26]='84'
    dfonewave_TV1[name] = pd.DataFrame(onewave_TV1[name])
      
    j +=1
#add Punch Value ,copy show names to detail1 CCP -S2021-F2021 updated column


# In[57]:


df1w_TV1[['S2021']]=df1w_TV1[["S2021"]].apply(pd.to_numeric)
#df1w_TV1['Col2PV']=''


# In[58]:


for i in range(len(df1w_TV1)):
    df1w_TV1.iloc[i,2] =  df1w_TV1.iloc[i,2] + 1
    df1w_TV1.iloc[i,34]='Yes'


# In[59]:


df1w_TV1['S2021'] = df1w_TV1['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[60]:


dfonew_TV1_2={}

value=['4','5']
j=0
PV=['4','5']
for name in PV:
    
    dfonew_TV1_2[name]=df1w_TV1.copy()
    for i in range(len(dfonew_TV1_2[name])):
        
            dfonew_TV1_2[name].iloc[i,2]= str(dfonew_TV1_2[name].iloc[i,2]) + str(value[j])
            dfonew_TV1_2[name].iloc[i,16]=dfonew_TV1_2[name].iloc[i,6]
            dfonew_TV1_2[name].iloc[i,36]=dfonew_TV1_2[name].iloc[i,2]     
            dfonew_TV1_2[name].iloc[i,29]='0'
            dfonew_TV1_2[name].iloc[i,26]='84'
            
    dfonew_TV1_2[name] = pd.DataFrame(dfonew_TV1_2[name])
    
    j +=1


# In[61]:


TV1onewave= [dfonewave_TV1['0'],
           dfonewave_TV1['1'],
           dfonewave_TV1['2'], 
           dfonewave_TV1['3'], 
           dfonewave_TV1['4'],
           dfonewave_TV1['5'],
           dfonewave_TV1['6'],
           dfonewave_TV1['8'],
           dfonewave_TV1['9'],
           dfonewave_TV1['x'],
           dfonew_TV1_2['4'],
           dfonew_TV1_2['5'],
          ]


# In[62]:


#dfonewave_TV1['1']


# In[63]:


TV1onewave=pd.concat(TV1onewave)


# In[64]:


TV1onewave['LastDigit_PV']=TV1onewave['S2021'].str.strip().str[-1]


# In[65]:


TV1onewave['SDID']='0'


# In[66]:


#TV1onewave['UCode']='U0'


# In[67]:


TV1onewave['StudyEntryID']='0'


# In[68]:


#TV1onewave['QUESTID']='0'
#TV1onewave['QuestionID']='0'


# In[69]:


TV1onewave.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV1#.csv',index=False,header=True)


# In[70]:


TV1=[dfnon1w_TV1,TV1onewave]


# In[71]:


TV1=pd.concat(TV1)


# In[72]:


TV1=TV1.sort_values(['Sec_List_Heading','LastDigit_PV', 'Col2PV'], 
               ascending=[True,
                          True,True])


# In[73]:


TV1['Tmpl']=TV1['Tmpl'].fillna(method='ffill')


# In[74]:


TV1['Super']=TV1['Super'].fillna(method='ffill')


# In[75]:


TV1['Detail3']=TV1['Detail3'].fillna(method='ffill')


# In[76]:


TV1=TV1.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])


# In[77]:


TV1['Category']=TV1['Category'].fillna(method='ffill')


# In[78]:


TV1['QLevel']=TV1['QLevel'].fillna(method='ffill')


# In[79]:


#TV1['UCode']=TV1['UCode'].fillna('U0')


# In[80]:


#TV1['QUESTID']=TV1['QUESTID'].fillna(method='ffill')


# In[81]:


#TV1['QuestionID']=TV1['QuestionID'].fillna(method='ffill')


# In[82]:


TV1['VersionID']='0'


# In[83]:


TV1['SID']='1857'


# In[84]:


TV1['SDID']=TV1['SDID'].fillna('0')


# In[85]:


TV1['Status']='Add'


# In[86]:


TV1['StudyAnswerID']='0'


# In[87]:


Listheading=TV1['Sec_List_Heading'].unique()


# In[88]:


#TV1['Sec_List_Heading'].value_counts()


# In[89]:


#LH={}
#for i in Listheading:
   # j=0
   # LH[j]=TV1.query('Sec_List_Heading=="i"')
   # print(LH[j].head(5))
    #df_TV_Movie.query('cleantype=="TV1"')
   # LH[j]=pd.DataFrame(LH[j])
   # j+=1


# In[90]:


g=TV1.groupby('Sec_List_Heading')


# In[91]:


i=0
n=0
TV1_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    TV1_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# #n

# In[92]:


n=0
for values in Listheading:
    TV1_LH[n]=TV1_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    TV1_LH[n]['Detail2']=TV1_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF    


# In[93]:


#g.get_group('Monday Through Friday Programs')


# In[94]:


#TV1_LH[8].head(5)


# In[95]:


TV1Frames=[TV1_LH[0],TV1_LH[1],TV1_LH[2],TV1_LH[3],TV1_LH[4],TV1_LH[5],TV1_LH[6],TV1_LH[7],TV1_LH[8]]


# In[96]:


TV1=pd.concat(TV1Frames)


# In[97]:


TV1=TV1.drop_duplicates(subset='F2020_Updated',keep='last')


# In[98]:


TV1['Detail1']=TV1['Detail1'].fillna(TV1['Shows_Name']) 


# In[99]:


TV1['Wave']=TV1['Wave'].fillna(TV1['Initial_Wave']) 


# In[100]:


TV1['Wave']=TV1['Wave'].astype(str)


# In[101]:


for i in range(len(TV1)):
        value=TV1.iloc[i,26]
        firstvalue=value[0]
        if firstvalue =='W':
                TV1.iloc[i,26]=value[1:]


# In[102]:


#TV1['QUESTID']=TV1['QUESTID'].fillna('0')


# In[103]:


#TV1['QuestionID']=TV1['QuestionID'].fillna('0')


# In[104]:


#TV1['QuestionID']=TV1['QuestionID'].fillna('0')
TV1['StudyEntryID']=TV1['StudyEntryID'].fillna('0')
#TV1['AnswerID']=TV1['AnswerID'].fillna('0')


# In[105]:


#condition=(TV1['compare']==False)


# In[106]:


#values=['0']


# In[107]:


TV1['Definition'] = TV1.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[108]:


TV1.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV1.csv',index=False,header=True)


# # TV2

# In[109]:


df_TV_Movie_TV2=df_TV_Movie.query('cleantype=="TV2" and OneWave_Suppress!="#"')


# In[110]:


df_TV_Movie_TV2['F2020']=df_TV_Movie_TV2['F2020'].str.replace('nan','')
df_TV_Movie_TV2['S2021']=df_TV_Movie_TV2['S2021'].str.replace('nan','')


# In[111]:


dftest_TV2={}
df_TV_Movie_PV_TV2={}
df_inner_PV_TV2={}
#V1_1W={}
value=['x','0','1','2','3','4','6','8','9']
j=0
PV=['x','0','1','2','3','4','6','8','9']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_TV2[name]=df_TV_Movie_TV2.copy()
    for i in range(len(df_TV_Movie_PV_TV2[name])):
        type=df_TV_Movie_PV_TV2[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_TV2[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_TV2[name].iloc[i,11]= str(df_TV_Movie_PV_TV2[name].iloc[i,11]) + str(value[j])
            
    dftest_TV2[name] = pd.DataFrame(df_TV_Movie_PV_TV2[name])
    df_inner_PV_TV2[name]= pd.merge(dftest_TV2[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #TV2_1W[name]=dftest_TV2[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[112]:


df_TV_Movie_TV2['F2020']=df_TV_Movie_TV2['F2020'].str.replace('nan','')
df_TV_Movie_TV2['S2021']=df_TV_Movie_TV2['S2021'].str.replace('nan','')
df_TV_Movie_TV2[['F2020']]=df_TV_Movie_TV2[["F2020"]].apply(pd.to_numeric)
df_TV_Movie_TV2[['S2021']]=df_TV_Movie_TV2[["S2021"]].apply(pd.to_numeric)


# In[113]:


df_TV_Movie_TV2['Col2PV']=''


# In[114]:


for i in range(len(df_TV_Movie_TV2)):
    type=df_TV_Movie_TV2.iloc[i,0]
    cleantype=df_TV_Movie_TV2.iloc[i,1]
    if type == 'show':
        df_TV_Movie_TV2.iloc[i,11] = df_TV_Movie_TV2.iloc[i,11] +1
        df_TV_Movie_TV2.iloc[i,4] =  df_TV_Movie_TV2.iloc[i,4] + 1
        df_TV_Movie_TV2.iloc[i,17] = 'Yes'
		


# In[115]:


df_TV_Movie_TV2['F2020'] = df_TV_Movie_TV2['F2020'].astype(str).apply(lambda x: x.replace('.0',''))
df_TV_Movie_TV2['S2021'] = df_TV_Movie_TV2['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[116]:


df_TV_Movie_TV2['F2020']=df_TV_Movie_TV2['F2020'].str.replace('nan','')
df_TV_Movie_TV2['S2021']=df_TV_Movie_TV2['S2021'].str.replace('nan','')


# In[117]:


dftest_TV2_2={}
df_TV_Movie_PV_TV2_2={}
df_inner_PV_TV2_2={}
#TV2_1W_2={}

value=['4','5']
j=0
PV=['4','5']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    df_TV_Movie_PV_TV2_2[name]=df_TV_Movie_TV2.copy()
    for i in range(len(df_TV_Movie_PV_TV2_2[name])):
        type=df_TV_Movie_PV_TV2_2[name].iloc[i,0]
        if type == 'show':
            if df_TV_Movie_PV_TV2_2[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_TV2_2[name].iloc[i,11]= str(df_TV_Movie_PV_TV2_2[name].iloc[i,11]) + str(value[j])
            
    dftest_TV2_2[name] = pd.DataFrame(df_TV_Movie_PV_TV2_2[name])
    df_inner_PV_TV2_2[name]= pd.merge(dftest_TV2_2[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #TV2_1W_2[name]=dftest_TV2_2[name].query('OneWave_Suppress=="#"')
    j +=1
	


# In[118]:


PTV2= [df_inner_PV_TV2['0'],
           df_inner_PV_TV2['1'],
           df_inner_PV_TV2['2'], 
           df_inner_PV_TV2['3'], 
           df_inner_PV_TV2['4'],
           #df_inner_PV_TV2['5'],
           df_inner_PV_TV2['6'],
           df_inner_PV_TV2['8'],
           df_inner_PV_TV2['9'],
           df_inner_PV_TV2['x'],
           df_inner_PV_TV2_2['4'],
           df_inner_PV_TV2_2['5'],
          ]


# In[119]:


TV2concat=pd.concat(PTV2)


# In[120]:


for i in range(len(TV2concat)):
        value=str(TV2concat.iloc[i,24])
        firstvalue=value[0]
        if firstvalue =='#':
                TV2concat.iloc[i,24]=value[1:]


# In[121]:


#TV2concat['Detail1'].isnull().value_counts()


# In[122]:


#TV2concat['Detail1'].nunique()


# In[123]:


TV2concat['Detail1']=TV2concat['Detail1'].astype(str)
TV2concat['Detail1']=TV2concat['Detail1'].replace(r'nan',np.nan,regex=True)


# ^ is the beginning of string anchor.
# $ is the end of string anchor.
# \s is the whitespace character class.
# * is zero-or-more repetition of.

# In[124]:


#TV2concat['Detail1'].isna().value_counts()


# In[125]:


#TV2concat['Detail1']


# In[126]:


#TV2concat['Detail1'].isna().value_counts()


# In[127]:


TV2concat['Detail1']=TV2concat['Detail1'].fillna(TV2concat['Shows_Name']) 


# In[128]:


TV2concat['Detail1']=TV2concat['Detail1'].astype(str)


# In[129]:


for i in range(len(TV2concat)):
        value=str(TV2concat.iloc[i,24])
        firstvalue=value[0]
        if value[0] =='#':
                TV2concat.iloc[i,24]=value[1:]


# In[130]:


#TV2concat.Detail1


# In[131]:


#TV2concat['Tmpl'].isna().value_counts()


# In[132]:


TV2concat['Tmpl']=TV2concat['Tmpl'].fillna('2')


# In[133]:


#TV2concat['Tmpl'].value_counts()


# In[134]:


TV2concat['LastDigit_PV'] = TV2concat['F2020'].apply(lambda x: x[-1:])


# In[135]:


TV2concat['F2020_Updated']= TV2concat['S2021'] + TV2concat['LastDigit_PV']


# # TV2 One Wave

# In[136]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[137]:


dfOneW_TV2=dfOneW.query("cleantype=='TV2'")


# In[138]:


df_TV2=[TV2concat,dfOneW_TV2]


# In[139]:


df_TV2=pd.concat(df_TV2)


# In[140]:



df_TV2= df_TV2.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[141]:


df1w_TV2=df_TV2.query("OneWave_Suppress=='#'")


# In[142]:


#df1w_TV2.head(5)


# In[143]:


dfnon1w_TV2=df_TV2.query("OneWave_Suppress!='#'")


# In[144]:


onewave_TV2={}
dfonewave_TV2={}

value=['x','0','1','2','3','4','6','8','9']
j=0
PV=['x','0','1','2','3','4','6','8','9']

for name in PV:
        
    onewave_TV2[name]=df1w_TV2.copy()
    for i in range(len(onewave_TV2[name])):
            onewave_TV2[name].iloc[i,2]= str(onewave_TV2[name].iloc[i,2]) + str(value[j])
            onewave_TV2[name].iloc[i,16]=onewave_TV2[name].iloc[i,6]
            onewave_TV2[name].iloc[i,36]=onewave_TV2[name].iloc[i,2]
            onewave_TV2[name].iloc[i,29]='0'
            onewave_TV2[name].iloc[i,26]='84'
    dfonewave_TV2[name] = pd.DataFrame(onewave_TV2[name])
      
    j +=1


# In[145]:


df1w_TV2[['S2021']]=df1w_TV2[["S2021"]].apply(pd.to_numeric)


# In[146]:



for i in range(len(df1w_TV2)):
    df1w_TV2.iloc[i,2] =  df1w_TV2.iloc[i,2] + 1
    df1w_TV2.iloc[i,34]='Yes'


# In[147]:


df1w_TV2['S2021'] = df1w_TV2['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[148]:


dfonew_TV2_2={}

value=['4','5']
j=0
PV=['4','5']
for name in PV:
    
    dfonew_TV2_2[name]=df1w_TV2.copy()
    for i in range(len(dfonew_TV2_2[name])):
        
            dfonew_TV2_2[name].iloc[i,2]= str(dfonew_TV2_2[name].iloc[i,2]) + str(value[j])
            dfonew_TV2_2[name].iloc[i,16]=dfonew_TV2_2[name].iloc[i,6]
            dfonew_TV2_2[name].iloc[i,36]=dfonew_TV2_2[name].iloc[i,2]     
            dfonew_TV2_2[name].iloc[i,29]='0'
            dfonew_TV2_2[name].iloc[i,26]='84'
            
    dfonew_TV2_2[name] = pd.DataFrame(dfonew_TV2_2[name])
    
    j +=1
	


# In[149]:


TV2onewave= [dfonewave_TV2['0'],
           dfonewave_TV2['1'],
           dfonewave_TV2['2'], 
           dfonewave_TV2['3'], 
           dfonewave_TV2['4'],
           #dfonewave_TV2['5'],
           dfonewave_TV2['6'],
           dfonewave_TV2['8'],
           dfonewave_TV2['9'],
           dfonewave_TV2['x'],
           dfonew_TV2_2['4'],
           dfonew_TV2_2['5'],
          ]


# In[150]:


TV2onewave=pd.concat(TV2onewave)


# In[151]:


TV2onewave['LastDigit_PV']=TV2onewave['S2021'].str.strip().str[-1]


# In[152]:


TV2onewave['SDID']='0'

#TV2onewave['UCode']='U0'
TV2onewave['StudyEntryID']='0'


# In[153]:


#TV2onewave['QUESTID']='0'
#TV2onewave['QuestionID']='0'
TV2onewave['Tmpl']='2'


# In[154]:


TV2onewave.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV2#.csv',index=False,header=True)


# In[155]:


TV2=[dfnon1w_TV2,TV2onewave]


# In[156]:


TV2=pd.concat(TV2)


# In[157]:


#TV2['Tmpl'].nunique()


# In[158]:


TV2['Tmpl']=TV2['Tmpl'].astype(str)


# In[159]:


#TV2['Tmpl'].unique()


# In[160]:


#TV2['Tmpl'].value_counts()


# In[161]:


TV2['Tmpl']=TV2['Tmpl'].str.replace('.0',"",regex=True)


# In[162]:


#TV2['Tmpl']=TV2['Tmpl'].str.replace(r'nan',np.nan,regex=True)


# In[163]:


TV2_tmpl3=TV2.query('Tmpl=="3"')


# In[164]:


TV2_tmpl2=TV2.query('Tmpl!="3"')


# In[165]:


TV2=TV2_tmpl2.copy()


# In[166]:


TV2=TV2.sort_values(['LastDigit_PV', 'Col2PV'], 
               ascending=[True,
                          True])
						  
#TV2['Tmpl']='2'


# In[167]:


TV2['Super']=TV2['Super'].fillna(method='ffill')
TV2['Detail3']=TV2['Detail3'].fillna(method='ffill')


# In[168]:


TV2=TV2.sort_values(['Sec_List_Heading', 'LastDigit_PV', 'Col2PV','Tmpl'], 
               ascending=[True,
                          True,True,True])
TV2['Category']=TV2['Category'].fillna(method='ffill')

#TV2['QUESTID']=TV2['QUESTID'].fillna(method='ffill')
#TV2['QuestionID']=TV2['QuestionID'].fillna(method='ffill')


# In[169]:


TV2['QLevel']=TV2['QLevel'].fillna(method='ffill')
TV2['Tmpl']=TV2['Tmpl'].fillna(method='ffill')


# In[170]:


#TV2onewave=TV2.query('OneWave_Suppress=="#"')


# In[171]:


#TV2non_onewave=TV2.query('OneWave_Suppress!="#"')


# In[172]:


#TV2onewave['Category']=TV2onewave['Category'].str.replace(r'- Net', '', regex=True)


# In[173]:


#TV2=[TV2non_onewave,TV2onewave]


# In[174]:


#TV2=pd.concat(TV2)


# In[175]:


TV2['VersionID']='0'
TV2['SID']='1857'
TV2['Status']='Add'
TV2['StudyAnswerID']='0'


# In[176]:


Listheading=TV2['Sec_List_Heading'].unique()
g=TV2.groupby('Sec_List_Heading')



# In[177]:


i=0
n=0
TV2_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    TV2_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[178]:


n=0
for values in Listheading:
    TV2_LH[n]=TV2_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    TV2_LH[n]['Detail2']=TV2_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF    


# In[179]:


TV2Frames=[TV2_LH[0],TV2_LH[1],TV2_LH[2],TV2_LH[3]]

TV2=pd.concat(TV2Frames)


# In[180]:


TV2=TV2.drop_duplicates(subset='F2020_Updated',keep='last')


# In[181]:


TV2['Detail1']=TV2['Detail1'].fillna(TV2['Shows_Name']) 


# In[182]:


TV2['Wave']=TV2['Wave'].fillna(TV2['Initial_Wave']) 


# In[183]:


TV2['Wave']=TV2['Wave'].astype(str)


# In[184]:


TV2['Wave']=TV2['Wave'].replace(r'W', '', regex=True)


# In[185]:


TV2['Wave']=TV2['Wave'].replace(r'nan', np.nan, regex=True)


# In[186]:


#TV2['Wave'].isna().value_counts()


# In[187]:


TV2['Wave']=TV2['Wave'].fillna('0')


# In[188]:


TV2['Definition'] = TV2.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[189]:


#TV2['Category'] = TV2.apply(lambda x:x['Category'].replace(r'- Net','',regex=True)  if x['OneWave_Suppress']=='#' else x['Category'], axis=1)
#replace(r'nan', np.nan, regex=True)


# In[190]:


#TV2['UCode']=TV2['UCode'].fillna('U0')
TV2['StudyEntryID']=TV2['StudyEntryID'].fillna('0')
#TV2['UCode']=TV2['UCode'].fillna('U0')
#TV2['QuestionID']=TV2['QuestionID'].fillna('0')
#TV2['QUESTID']=TV2['QUESTID'].fillna('0')
#TV2['AnswerID']=TV2['AnswerID'].fillna('0')


# In[191]:


#TV2['Tmpl']=TV2['Tmpl'].fillna('2')


# In[192]:


TV2=[TV2,TV2_tmpl3]


# In[193]:


TV2=pd.concat(TV2)


# In[194]:


TV2['VersionID']='0'
TV2['SID']='1857'
TV2['Status']='Add'
TV2['StudyAnswerID']='0'
#TV2['Tmpl']=TV2['Tmpl'].fillna('2')
TV2['SDID']=TV2['SDID'].fillna('0')


# In[195]:


TV2['Definition'] = TV2.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[196]:


TV2=TV2.drop_duplicates(subset='F2020_Updated',keep='last')


# In[197]:


#TV2


# In[198]:


TV2.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV2.csv',index=False,header=True)


# # SPTV1

# In[199]:


# col1 x,1,2,3,4,5,6 no col 2 values


# In[200]:


df_TV_Movie_SPTV1=df_TV_Movie.query('cleantype=="SPTV1" and OneWave_Suppress!="#"')


# In[201]:


df_TV_Movie_SPTV1['F2020']=df_TV_Movie_SPTV1['F2020'].str.replace('nan','')
df_TV_Movie_SPTV1['S2021']=df_TV_Movie_SPTV1['S2021'].str.replace('nan','')


# In[202]:


dftest_SPTV1={}
df_TV_Movie_PV_SPTV1={}
df_inner_PV_SPTV1={}
#TV1_1W={}
value=['x','1','2','3','4','5','6']
j=0
PV=['x','1','2','3','4','5','6']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_SPTV1[name]=df_TV_Movie_SPTV1.copy()
    for i in range(len(df_TV_Movie_PV_SPTV1[name])):
        type=df_TV_Movie_PV_SPTV1[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_SPTV1[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_SPTV1[name].iloc[i,11]= str(df_TV_Movie_PV_SPTV1[name].iloc[i,11]) + str(value[j])
            
    dftest_SPTV1[name] = pd.DataFrame(df_TV_Movie_PV_SPTV1[name])
    df_inner_PV_SPTV1[name]= pd.merge(dftest_SPTV1[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #SPTV1_1W[name]=dftest_SPTV1[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[203]:


PSPTV1= [  df_inner_PV_SPTV1['1'],
           df_inner_PV_SPTV1['2'], 
           df_inner_PV_SPTV1['3'], 
           df_inner_PV_SPTV1['4'],
           df_inner_PV_SPTV1['5'],
           df_inner_PV_SPTV1['6'],
           df_inner_PV_SPTV1['x'],
        ]


# In[204]:


SPTV1concat=pd.concat(PSPTV1)


# In[205]:


#SPTV1concat['Shows_Name'].value_counts()


# In[206]:


SPTV1concat['LastDigit_PV'] = SPTV1concat['F2020'].apply(lambda x: x[-1:])


# In[207]:


SPTV1concat['F2020_Updated']=SPTV1concat['S2021']+SPTV1concat['LastDigit_PV']


# In[208]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[209]:


dfOneW_SPTV1=dfOneW.query("cleantype=='SPTV1'")


# In[210]:


df_SPTV1=[SPTV1concat,dfOneW_SPTV1]


# In[211]:


df_SPTV1=pd.concat(df_SPTV1)


# In[212]:


df_SPTV1= df_SPTV1.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[213]:


df1w_SPTV1=df_SPTV1.query("OneWave_Suppress=='#'")


# In[214]:


dfnon1w_SPTV1=df_SPTV1.query("OneWave_Suppress!='#'")


# In[215]:


onewave_SPTV1={}
dfonewave_SPTV1={}


# In[216]:


value=['x','1','2','3','4','5','6']
j=0
PV=['x','1','2','3','4','5','6']

for name in PV:
        
    onewave_SPTV1[name]=df1w_SPTV1.copy()
    for i in range(len(onewave_SPTV1[name])):
            onewave_SPTV1[name].iloc[i,2]= str(onewave_SPTV1[name].iloc[i,2]) + str(value[j])
            onewave_SPTV1[name].iloc[i,16]=onewave_SPTV1[name].iloc[i,6]
            onewave_SPTV1[name].iloc[i,35]=onewave_SPTV1[name].iloc[i,2]
            onewave_SPTV1[name].iloc[i,29]='0'
            onewave_SPTV1[name].iloc[i,26]='84'
    dfonewave_SPTV1[name] = pd.DataFrame(onewave_SPTV1[name])
      
    j +=1
#add Punch Value ,copy show names to detail1 CCP -S2021-F2021 updated column


# In[217]:


SPTV1onewave= [
           dfonewave_SPTV1['1'],
           dfonewave_SPTV1['2'], 
           dfonewave_SPTV1['3'], 
           dfonewave_SPTV1['4'],
           dfonewave_SPTV1['5'],
           dfonewave_SPTV1['6'],
           dfonewave_SPTV1['x'],
           #dfonew_SPTV1_2['4'],
           #dfonew_SPTV1_2['5'],
          ]


# In[218]:



SPTV1onewave=pd.concat(SPTV1onewave)


# In[219]:


SPTV1onewave['LastDigit_PV']=SPTV1onewave['S2021'].str.strip().str[-1]


# In[220]:


SPTV1onewave['F2020_Updated']=SPTV1onewave['S2021']


# In[221]:


SPTV1onewave['SDID']='0'

#SPTV1onewave['UCode']='U0'
SPTV1onewave['StudyEntryID']='0'


# In[222]:


#SPTV1onewave['QUESTID']='0'
#SPTV1onewave['QuestionID']='0'


# In[223]:


#SPTV1onewave.head(5)


# In[224]:


SPTV1onewave.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV1#.csv',index=False,header=True,encoding='cp1252')


# In[225]:


SPTV1=[dfnon1w_SPTV1,SPTV1onewave]


# In[226]:


SPTV1=pd.concat(SPTV1)


# In[227]:


#SPTV1['Shows_Name']=SPTV1['Shows_Name'].astype(str)


# In[228]:


SPTV1=SPTV1.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
SPTV1['Tmpl']=SPTV1['Tmpl'].fillna(method='ffill')
SPTV1['Super']=SPTV1['Super'].fillna(method='ffill')
SPTV1['Detail3']=SPTV1['Detail3'].fillna(method='ffill')


# In[229]:


SPTV1=SPTV1.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])

SPTV1['QLevel']=SPTV1['QLevel'].fillna(method='ffill')


# In[230]:


SPTV1['VersionID']='0'
SPTV1['SID']='1857'
SPTV1['Status']='Add'
SPTV1['StudyAnswerID']='0'


# In[231]:


Listheading=SPTV1['Sec_List_Heading'].unique()
g=SPTV1.groupby('Sec_List_Heading')


# In[232]:


i=0
n=0
SPTV1_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    SPTV1_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[233]:


n=0
for values in Listheading:
    SPTV1_LH[n]=SPTV1_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[False
                        ])
    SPTV1_LH[n]['Detail2']=SPTV1_LH[n]['Detail2'].fillna(method='ffill')
    SPTV1['Category']="Spanish Television: "+SPTV1['Sec_List_Heading']
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[234]:


#n


# In[235]:


SPTV1Frames=pd.DataFrame()
SPTV1Frames = SPTV1Frames.append([SPTV1_LH[i] for i in range(n)])


# In[236]:


#SPTV1=pd.concat(SPTV1Frames)


# In[237]:


SPTV1['Detail1']=SPTV1['Detail1'].fillna(SPTV1['Shows_Name'])


# In[238]:


SPTV1['Wave']=SPTV1['Wave'].fillna(SPTV1['Initial_Wave']) 
SPTV1['Wave']=SPTV1['Wave'].astype(str)
SPTV1['Wave']=SPTV1['Wave'].replace(r'W', '', regex=True)
SPTV1['Wave']=SPTV1['Wave'].replace(r'nan', np.nan, regex=True)
#SPTV1['Wave'].isna().value_counts()
SPTV1['Wave']=SPTV1['Wave'].fillna('0')
SPTV1['SDID']=SPTV1['SDID'].fillna('0')
SPTV1['Definition'] = SPTV1.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[239]:


#SPTV1['UCode']=SPTV1['UCode'].fillna('U0')
SPTV1['StudyEntryID']=SPTV1['StudyEntryID'].fillna('0')
#SPTV1['UCode']=SPTV1['UCode'].fillna('U0')
#SPTV1['QuestionID']=SPTV1['QuestionID'].fillna('0')
#SPTV1['QUESTID']=SPTV1['QUESTID'].fillna('0')
#SPTV1['AnswerID']=SPTV1['AnswerID'].fillna('0')


# In[240]:


SPTV1=SPTV1.drop_duplicates(subset='F2020_Updated',keep='last')


# In[241]:



SPTV1.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV1.csv',index=False,header=True,encoding='cp1252')


# # SPTV4

# In[242]:


#No col2 value only 6 in col1


# In[243]:


df_TV_Movie_SPTV4=df_TV_Movie.query('cleantype=="SPTV4" and OneWave_Suppress!="#"')


# In[244]:


df_TV_Movie_SPTV4['F2020']=df_TV_Movie_SPTV4['F2020'].str.replace('nan','')
df_TV_Movie_SPTV4['S2021']=df_TV_Movie_SPTV4['S2021'].str.replace('nan','')


# In[245]:


dftest_SPTV4={}
df_TV_Movie_PV_SPTV4={}
df_inner_PV_SPTV4={}
#TV1_1W={}
value=['x','6']
j=0
PV=['x','6']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_SPTV4[name]=df_TV_Movie_SPTV4.copy()
    for i in range(len(df_TV_Movie_PV_SPTV4[name])):
        type=df_TV_Movie_PV_SPTV4[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_SPTV4[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_SPTV4[name].iloc[i,11]= str(df_TV_Movie_PV_SPTV4[name].iloc[i,11]) + str(value[j])
                
                            
    dftest_SPTV4[name] = pd.DataFrame(df_TV_Movie_PV_SPTV4[name])
    df_inner_PV_SPTV4[name]= pd.merge(dftest_SPTV4[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #SPTV4_1W[name]=dftest_SPTV4[name].query('OneWave_Suppress=="#"')
    
    j +=1
	


# In[246]:


df_TV_Movie_SPTV4['F2020']=df_TV_Movie_SPTV4['F2020'].str.replace('nan','')
df_TV_Movie_SPTV4['S2021']=df_TV_Movie_SPTV4['S2021'].str.replace('nan','')
df_TV_Movie_SPTV4[['F2020']]=df_TV_Movie_SPTV4[["F2020"]].apply(pd.to_numeric)
df_TV_Movie_SPTV4[['S2021']]=df_TV_Movie_SPTV4[["S2021"]].apply(pd.to_numeric)


# In[247]:



PSPTV4= [#df_inner_PV_SPTV4['0'],
           #df_inner_PV_SPTV4['1'],
           #df_inner_PV_SPTV4['2'], 
           #df_inner_PV_SPTV4['3'], 
           #df_inner_PV_SPTV4['4'],
           #df_inner_PV_SPTV4['5'],
           df_inner_PV_SPTV4['6'],
           #df_inner_PV_SPTV4['8'],
           #df_inner_PV_SPTV4['9'],
           #df_inner_PV_SPTV4['x'],
           #df_inner_PV_SPTV4_2['4'],
           #df_inner_PV_SPTV4_2['3'],
		   #df_inner_PV_SPTV4_2['1'],
           #df_inner_PV_SPTV4_2['5'],
          #df_inner_PV_SPTV4_2['5']
          ]


# In[248]:


SPTV4concat=pd.concat(PSPTV4)


# In[249]:


#SPTV4concat['Shows_Name'].value_counts()


# In[250]:


SPTV4concat['LastDigit_PV'] = SPTV4concat['F2020'].apply(lambda x: x[-1:])


# In[251]:


SPTV4concat['F2020_Updated']=SPTV4concat['S2021']+SPTV4concat['LastDigit_PV']


# In[252]:


SPTV4concat['Detail1']=SPTV4concat['Detail1'].astype(str)

for i in range(len(SPTV4concat)):
        value=SPTV4concat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                SPTV4concat.iloc[i,24]=value[1:]


# # SPTV4 Onewave

# In[253]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[254]:


dfOneW_SPTV4=dfOneW.query("cleantype=='SPTV4'")


# In[255]:


df_SPTV4=[SPTV4concat,dfOneW_SPTV4]


# In[256]:


df_SPTV4=pd.concat(df_SPTV4)


# In[257]:


df_SPTV4= df_SPTV4.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[258]:


df1w_SPTV4=df_SPTV4.query("OneWave_Suppress=='#'")


# In[259]:


dfnon1w_SPTV4=df_SPTV4.query("OneWave_Suppress!='#'")


# In[260]:


#dfnon1w_SPTV4['Shows_Name'].value_counts()


# In[261]:


onewave_SPTV4={}
dfonewave_SPTV4={}
value=['6']
j=0
PV=['6']

for name in PV:
        
    onewave_SPTV4[name]=df1w_SPTV4.copy()
    for i in range(len(onewave_SPTV4[name])):
            onewave_SPTV4[name].iloc[i,2]= str(onewave_SPTV4[name].iloc[i,2]) + str(value[j])
            onewave_SPTV4[name].iloc[i,16]=onewave_SPTV4[name].iloc[i,6]
            onewave_SPTV4[name].iloc[i,35]=onewave_SPTV4[name].iloc[i,2]
            onewave_SPTV4[name].iloc[i,29]='0'
            onewave_SPTV4[name].iloc[i,26]='84'
    dfonewave_SPTV4[name] = pd.DataFrame(onewave_SPTV4[name])
      
    j +=1
#add Punch Value ,copy show names to detail1 CCP -S2021-F2021 updated column


# In[262]:


SPTV4onewave= [#dfonewave_SPTV4['0'],
           #dfonewave_SPTV4['1'],
           #dfonewave_SPTV4['2'], 
           #dfonewave_SPTV4['3'], 
           #dfonewave_SPTV4['4'],
           #dfonewave_SPTV4['5'],
           dfonewave_SPTV4['6'],
           #dfonewave_SPTV4['8'],
           #dfonewave_SPTV4['9'],
           #dfonewave_SPTV4['x'],
           #dfonew_SPTV4_2['4'],
           #dfonew_SPTV4_2['5'],
          ]


# In[263]:



SPTV4onewave=pd.concat(SPTV4onewave)


# In[264]:


SPTV4onewave['LastDigit_PV']=SPTV4onewave['S2021'].str.strip().str[-1]


# In[265]:



SPTV4onewave['F2020_Updated']=SPTV4onewave['S2021']


# In[266]:


SPTV4onewave['SDID']='0'

#SPTV4onewave['UCode']='U0'
SPTV4onewave['StudyEntryID']='0'


# In[267]:


#SPTV4onewave['QUESTID']='0'
#SPTV4onewave['QuestionID']='0'


# In[268]:


#SPTV4onewave.head(5)


# In[269]:



SPTV4onewave.to_csv('SPTV4#.csv',index=False,header=True)


# In[270]:


#SPTV4onewave['Shows_Name'].value_counts()


# In[271]:



SPTV4=[dfnon1w_SPTV4,SPTV4onewave]


# In[272]:



SPTV4=pd.concat(SPTV4)


# In[273]:


#SPTV4['Shows_Name'].value_counts()


# In[274]:


SPTV4=SPTV4.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
SPTV4['Tmpl']=SPTV4['Tmpl'].fillna(method='ffill')
SPTV4['Super']=SPTV4['Super'].fillna(method='ffill')
SPTV4['Detail3']=SPTV4['Detail3'].fillna(method='ffill')


# In[275]:



SPTV4=SPTV4.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
SPTV4['Category']=SPTV4['Category'].fillna(method='ffill')
SPTV4['QLevel']=SPTV4['QLevel'].fillna(method='ffill')


# In[276]:


SPTV4['VersionID']='0'
SPTV4['SID']='1857'
SPTV4['Status']='Add'
SPTV4['StudyAnswerID']='0'


# In[277]:


SPTV4['Detail1']=SPTV4['Detail1'].fillna(SPTV4['Shows_Name'])


# In[278]:


SPTV4['Wave']=SPTV4['Wave'].fillna(SPTV4['Initial_Wave']) 
SPTV4['Wave']=SPTV4['Wave'].astype(str)
SPTV4['Wave']=SPTV4['Wave'].replace(r'W', '', regex=True)
SPTV4['Wave']=SPTV4['Wave'].replace(r'nan', np.nan, regex=True)
#SPTV4['Wave'].isna().value_counts()
SPTV4['Wave']=SPTV4['Wave'].fillna('0')
SPTV4['SDID']=SPTV4['SDID'].fillna('0')
SPTV4['Definition'] = SPTV4.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[279]:



#SPTV4['UCode']=SPTV4['UCode'].fillna('U0')
SPTV4['StudyEntryID']=SPTV4['StudyEntryID'].fillna('0')
#SPTV4['UCode']=SPTV4['UCode'].fillna('U0')
#SPTV4['QuestionID']=SPTV4['QuestionID'].fillna('0')
#SPTV4['QUESTID']=SPTV4['QUESTID'].fillna('0')
#SPTV4['AnswerID']=SPTV4['AnswerID'].fillna('0')


# In[280]:


#SPTV4=SPTV4.drop_duplicates(subset='F2020_Updated',keep='last')


# In[281]:



SPTV4=SPTV4.sort_values(['S2021' ], ascending=[True])


# In[282]:


SPTV4.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV4.csv',index=False,header=True,encoding='utf8')


# # SPTV3

# In[283]:


#no col 2 col1 6, x, 1 ,2, 3, 4


# In[284]:


df_TV_Movie_SPTV3=df_TV_Movie.query('cleantype=="SPTV3" and OneWave_Suppress!="#"')


# In[285]:


df_TV_Movie_SPTV3['F2020']=df_TV_Movie_SPTV3['F2020'].str.replace('nan','')
df_TV_Movie_SPTV3['S2021']=df_TV_Movie_SPTV3['S2021'].str.replace('nan','')


# In[286]:


dftest_SPTV3={}
df_TV_Movie_PV_SPTV3={}
df_inner_PV_SPTV3={}
#TV1_1W={}
value=['x','1','2','3','4','6']
j=0
PV=['x','1','2','3','4','6']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_SPTV3[name]=df_TV_Movie_SPTV3.copy()
    for i in range(len(df_TV_Movie_PV_SPTV3[name])):
        type=df_TV_Movie_PV_SPTV3[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_SPTV3[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_SPTV3[name].iloc[i,11]= str(df_TV_Movie_PV_SPTV3[name].iloc[i,11]) + str(value[j])
            
    dftest_SPTV3[name] = pd.DataFrame(df_TV_Movie_PV_SPTV3[name])
    df_inner_PV_SPTV3[name]= pd.merge(dftest_SPTV3[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #SPTV3_1W[name]=dftest_SPTV3[name].query('OneWave_Suppress=="#"')
    
    j +=1
	


# In[287]:


PSPTV3= [#df_inner_PV_SPTV3['0'],
           df_inner_PV_SPTV3['1'],
           df_inner_PV_SPTV3['2'], 
           df_inner_PV_SPTV3['3'], 
           df_inner_PV_SPTV3['4'],
           
           df_inner_PV_SPTV3['6'],
           
           df_inner_PV_SPTV3['x'],
           
          ]


# In[288]:


SPTV3concat=pd.concat(PSPTV3)


# In[289]:


SPTV3concat['LastDigit_PV'] = SPTV3concat['F2020'].apply(lambda x: x[-1])


# In[290]:



SPTV3concat['F2020_Updated']=SPTV3concat['S2021']+SPTV3concat['LastDigit_PV']


# In[291]:


SPTV3concat['Detail1']=SPTV3concat['Detail1'].astype(str)

for i in range(len(SPTV3concat)):
        value=SPTV3concat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                SPTV3concat.iloc[i,24]=value[1:]


# for i in range(len(SPTV3concat)):
#     if (SPTV3concat.iloc[i,45]!='Yes'):
#         SPTV3concat.iloc[i,47]= SPTV3concat.iloc[i,4] + SPTV3concat.iloc[i,46]

# # SPTV3 One Wave

# In[292]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[293]:


dfOneW_SPTV3=dfOneW.query("cleantype=='SPTV3'")


# In[294]:


df_SPTV3=[SPTV3concat,dfOneW_SPTV3]


# In[295]:


df_SPTV3=pd.concat(df_SPTV3)


# In[296]:


#df_SPTV3


# In[297]:


df_SPTV3= df_SPTV3.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[298]:


df1w_SPTV3=df_SPTV3.query("OneWave_Suppress=='#'")


# In[299]:


dfnon1w_SPTV3=df_SPTV3.query("OneWave_Suppress!='#'")


# In[300]:


#dfnon1w_SPTV3


# In[301]:


#df1w_SPTV3.info()


# In[302]:


onewave_SPTV3={}
dfonewave_SPTV3={}
value=['x','1','2','3','4','6']
j=0
PV=['x','1','2','3','4','6']

for name in PV:
        
    onewave_SPTV3[name]=df1w_SPTV3.copy()
    for i in range(len(onewave_SPTV3[name])):
            onewave_SPTV3[name].iloc[i,2]= str(onewave_SPTV3[name].iloc[i,2]) + str(value[j])
            onewave_SPTV3[name].iloc[i,16]=onewave_SPTV3[name].iloc[i,6]
            onewave_SPTV3[name].iloc[i,35]=onewave_SPTV3[name].iloc[i,2]
            onewave_SPTV3[name].iloc[i,29]='0'
            onewave_SPTV3[name].iloc[i,26]='84'
    dfonewave_SPTV3[name] = pd.DataFrame(onewave_SPTV3[name])
      
    j +=1
#add Punch Value ,copy show names to detail1 CCP -S2021-F2021 updated column


# In[303]:


SPTV3onewave= [
           dfonewave_SPTV3['1'],
           dfonewave_SPTV3['2'], 
           dfonewave_SPTV3['3'], 
           dfonewave_SPTV3['4'],
           #dfonewave_SPTV3['5'],
           dfonewave_SPTV3['6'],
          
           dfonewave_SPTV3['x'],
           
          ]


# In[304]:


SPTV3onewave=pd.concat(SPTV3onewave)


# In[305]:


SPTV3onewave['LastDigit_PV']=SPTV3onewave['S2021'].str.strip().str[-1]


# In[306]:


SPTV3onewave['F2020_Updated']=SPTV3onewave['S2021']


# In[307]:


SPTV3onewave['SDID']='0'

#SPTV3onewave['UCode']='U0'
SPTV3onewave['StudyEntryID']='0'


# In[308]:


#SPTV3onewave.head(5)
#SPTV3onewave['QUESTID']='0'
#SPTV3onewave['QuestionID']='0'


# In[309]:


SPTV3onewave.to_csv('SPTV3#.csv',index=False,header=True)


# In[310]:


SPTV3=[dfnon1w_SPTV3,SPTV3onewave]


# In[311]:


SPTV3=pd.concat(SPTV3)


# In[312]:


#SPTV3


# In[313]:


SPTV3=SPTV3.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
SPTV3['Tmpl']=SPTV3['Tmpl'].fillna(method='ffill')
SPTV3['Super']=SPTV3['Super'].fillna(method='ffill')
SPTV3['Detail3']=SPTV3['Detail3'].fillna(method='ffill')


# In[314]:


SPTV3=SPTV3.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
SPTV3['Category']=SPTV3['Category'].fillna(method='ffill')
SPTV3['QLevel']=SPTV3['QLevel'].fillna(method='ffill')


# In[315]:


SPTV3['VersionID']='0'
SPTV3['SID']='1857'
SPTV3['Status']='Add'
SPTV3['StudyAnswerID']='0'


# In[316]:


SPTV3['Detail1']=SPTV3['Detail1'].fillna(SPTV3['Shows_Name'])


# In[317]:


SPTV3['Wave']=SPTV3['Wave'].fillna(SPTV3['Initial_Wave']) 
SPTV3['Wave']=SPTV3['Wave'].astype(str)
SPTV3['Wave']=SPTV3['Wave'].replace(r'W', '', regex=True)
SPTV3['Wave']=SPTV3['Wave'].replace(r'nan', np.nan, regex=True)
#SPTV3['Wave'].isna().value_counts()
SPTV3['Wave']=SPTV3['Wave'].fillna('0')
SPTV3['SDID']=SPTV3['SDID'].fillna('0')
#SPTV3['Definition'] = SPTV3.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[318]:


#SPTV3


# In[319]:


#SPTV3['UCode'] = SPTV3.apply(lambda x: 'U0'  if x['UCode']==0 else x['UCode'], axis=1)


# In[320]:


#SPTV3['UCode']=SPTV3['UCode'].fillna('U0')
SPTV3['StudyEntryID']=SPTV3['StudyEntryID'].fillna('0')
#SPTV3['UCode']=SPTV3['UCode'].fillna('U0')
#SPTV3['QuestionID']=SPTV3['QuestionID'].fillna('0')
#SPTV3['QUESTID']=SPTV3['QUESTID'].fillna('0')
#SPTV3['AnswerID']=SPTV3['AnswerID'].fillna('0')


# In[321]:


#SPTV3


# In[322]:


#SPTV3['Definition'] = SPTV3.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[323]:


SPTV3['Definition'] ='0'
#all values are false in compare


# In[324]:


#SPTV3=SPTV3.drop_duplicates(subset='F2020_Updated',keep='last')


# In[325]:


SPTV3.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV3.csv',index=False,header=True,encoding='cp1252')


# # SPTV5.1

# In[326]:


# col1 ,6 col2 -no values


# In[327]:


df_TV_Movie_SPTV51=df_TV_Movie.query('cleantype=="SPTV5.1" and OneWave_Suppress!="#"')


# In[328]:


df_TV_Movie_SPTV51['F2020']=df_TV_Movie_SPTV51['F2020'].str.replace('nan','')
df_TV_Movie_SPTV51['S2021']=df_TV_Movie_SPTV51['S2021'].str.replace('nan','')


# In[329]:


dftest_SPTV51={}
df_TV_Movie_PV_SPTV51={}
df_inner_PV_SPTV51={}
#TV1_1W={}
value=['6','4']
j=0
PV=['6','4']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_SPTV51[name]=df_TV_Movie_SPTV51.copy()
    for i in range(len(df_TV_Movie_PV_SPTV51[name])):
        type=df_TV_Movie_PV_SPTV51[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_SPTV51[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_SPTV51[name].iloc[i,11]= str(df_TV_Movie_PV_SPTV51[name].iloc[i,11]) + str(value[j])
            
    dftest_SPTV51[name] = pd.DataFrame(df_TV_Movie_PV_SPTV51[name])
    df_inner_PV_SPTV51[name]= pd.merge(dftest_SPTV51[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #SPTV51_1W[name]=dftest_SPTV51[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[330]:


PSPTV51= [#df_inner_PV_SPTV51['0'],
           #df_inner_PV_SPTV51['1'],
           #df_inner_PV_SPTV51['2'], 
           #df_inner_PV_SPTV51['3'], 
           #df_inner_PV_SPTV51['4'],
           #df_inner_PV_SPTV51['5'],
           df_inner_PV_SPTV51['6'],
           
          ]


# In[331]:


SPTV51concat=pd.concat(PSPTV51)


# In[332]:


SPTV51concat['LastDigit_PV'] = SPTV51concat['F2020'].apply(lambda x: x[-1])


# In[333]:


SPTV51concat['F2020_Updated']=SPTV51concat['S2021']+SPTV51concat['LastDigit_PV']


# In[334]:


SPTV51concat['Detail1']=SPTV51concat['Detail1'].astype(str)

for i in range(len(SPTV51concat)):
        value=SPTV51concat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                SPTV51concat.iloc[i,24]=value[1:]


# # SPTV5.1 One wave

# In[335]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[336]:


dfOneW_SPTV51=dfOneW.query("cleantype=='SPTV5.1'")


# In[337]:


df_SPTV51=[SPTV51concat,dfOneW_SPTV51]


# In[338]:


df_SPTV51=pd.concat(df_SPTV51)


# In[339]:


df_SPTV51= df_SPTV51.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[340]:


df1w_SPTV51=df_SPTV51.query("OneWave_Suppress=='#'")


# In[341]:


dfnon1w_SPTV51=df_SPTV51.query("OneWave_Suppress!='#'")


# In[342]:


onewave_SPTV51={}
dfonewave_SPTV51={}
value=['6','1']
j=0
PV=['6','1']

for name in PV:
        
    onewave_SPTV51[name]=df1w_SPTV51.copy()
    for i in range(len(onewave_SPTV51[name])):
            onewave_SPTV51[name].iloc[i,2]= str(onewave_SPTV51[name].iloc[i,2]) + str(value[j])
            onewave_SPTV51[name].iloc[i,16]=onewave_SPTV51[name].iloc[i,6]
            onewave_SPTV51[name].iloc[i,35]=onewave_SPTV51[name].iloc[i,2]
            onewave_SPTV51[name].iloc[i,29]='0'
            onewave_SPTV51[name].iloc[i,26]='84'
    dfonewave_SPTV51[name] = pd.DataFrame(onewave_SPTV51[name])
      
    j +=1
#add Punch Value ,copy show names to detail1 CCP -S2021-F2021 updated column


# In[343]:


SPTV51onewave= [
          #dfonewave_SPTV51['1'],
           #dfonewave_SPTV51['5'],
           dfonewave_SPTV51['6'],
		  #dfonewave_SPTV51['4'],
           ]


# In[344]:


SPTV51onewave=pd.concat(SPTV51onewave)


# In[345]:


SPTV51onewave['LastDigit_PV']=SPTV51onewave['S2021'].str.strip().str[-1]


# In[346]:


SPTV51onewave['F2020_Updated']=SPTV51onewave['S2021']


# In[347]:


SPTV51onewave['SDID']='0'

#SPTV51onewave['UCode']='U0'
SPTV51onewave['StudyEntryID']='0'


# In[348]:


#SPTV51onewave['QUESTID']='0'
#SPTV51onewave['QuestionID']='0'


# In[349]:


SPTV51onewave.to_csv('SPTV51#.csv',index=False,header=True)


# In[350]:


SPTV51=[dfnon1w_SPTV51,SPTV51onewave]


# In[351]:


SPTV51=pd.concat(SPTV51)


# In[352]:


SPTV51=SPTV51.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
SPTV51['Tmpl']=SPTV51['Tmpl'].fillna(method='ffill')
SPTV51['Super']=SPTV51['Super'].fillna(method='ffill')
SPTV51['Detail3']=SPTV51['Detail3'].fillna(method='ffill')


# In[353]:


SPTV51=SPTV51.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
SPTV51['Category']=SPTV51['Category'].fillna(method='ffill')
SPTV51['QLevel']=SPTV51['QLevel'].fillna(method='ffill')


# In[354]:


SPTV51['VersionID']='0'
SPTV51['SID']='1857'
SPTV51['Status']='Add'
SPTV51['StudyAnswerID']='0'


# In[355]:


SPTV51['Detail1']=SPTV51['Detail1'].replace(r'nan', np.nan, regex=True)


# In[356]:


#SPTV1['Detail1']=SPTV1['Detail1'].replace(r'nan', np.nan, regex=True)

SPTV51['Detail1']=SPTV51['Detail1'].fillna(SPTV51['Shows_Name'])

SPTV51['Wave']=SPTV51['Wave'].fillna(SPTV51['Initial_Wave']) 

#SPTV51['Wave'].isna().value_counts()


# In[357]:


SPTV51['Wave']=SPTV51['Wave'].astype(str)
SPTV51['Wave']=SPTV51['Wave'].replace(r'W', '', regex=True)
SPTV51['Wave']=SPTV51['Wave'].replace(r'nan', np.nan, regex=True)


# In[358]:


SPTV51['Wave']=SPTV51['Wave'].fillna('0')
SPTV51['SDID']=SPTV51['SDID'].fillna('0')
SPTV51['Definition'] = SPTV51.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[359]:


#SPTV51['UCode']=SPTV51['UCode'].fillna('U0')
SPTV51['StudyEntryID']=SPTV51['StudyEntryID'].fillna('0')
#SPTV51['UCode']=SPTV51['UCode'].fillna('U0')


# In[360]:


#SPTV51['QuestionID']=SPTV51['QuestionID'].fillna('0')
#SPTV51['QUESTID']=SPTV51['QUESTID'].fillna('0')
#SPTV51['AnswerID']=SPTV51['AnswerID'].fillna('0')


# In[361]:


SPTV51=SPTV51.drop_duplicates(subset='F2020_Updated',keep='last')


# In[362]:


SPTV51.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV5.1.csv',index=False,header=True,encoding='cp1252')


# # SPTV5

# In[363]:


# No one wave items and no col2 items only 6 in col1 PV


# In[364]:


df_TV_Movie_SPTV5=df_TV_Movie.query('cleantype=="SPTV5" and OneWave_Suppress!="#"')


# In[365]:


df_TV_Movie_SPTV5['F2020']=df_TV_Movie_SPTV5['F2020'].str.replace('nan','')
df_TV_Movie_SPTV5['S2021']=df_TV_Movie_SPTV5['S2021'].str.replace('nan','')


# In[366]:


dftest_SPTV5={}
df_TV_Movie_PV_SPTV5={}
df_inner_PV_SPTV5={}
#TV1_1W={}
value=['6','1']
j=0
PV=['6','1']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_SPTV5[name]=df_TV_Movie_SPTV5.copy()
    for i in range(len(df_TV_Movie_PV_SPTV5[name])):
        type=df_TV_Movie_PV_SPTV5[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_SPTV5[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_SPTV5[name].iloc[i,11]= str(df_TV_Movie_PV_SPTV5[name].iloc[i,11]) + str(value[j])
            
    dftest_SPTV5[name] = pd.DataFrame(df_TV_Movie_PV_SPTV5[name])
    df_inner_PV_SPTV5[name]= pd.merge(dftest_SPTV5[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #SPTV5_1W[name]=dftest_SPTV5[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[367]:


SPTV5= [ df_inner_PV_SPTV5['6']]


# In[368]:


SPTV5=pd.concat(SPTV5)


# In[369]:


SPTV5['LastDigit_PV'] = SPTV5['F2020'].apply(lambda x: x[-1])


# In[370]:


SPTV5['F2020_Updated']=SPTV5['S2021']+SPTV5['LastDigit_PV']


# In[371]:


SPTV5['Detail1']=SPTV5['Detail1'].astype(str)

for i in range(len(SPTV5)):
        value=SPTV5.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                SPTV5.iloc[i,24]=value[1:]


# In[372]:


SPTV5=SPTV5.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
SPTV5['Tmpl']=SPTV5['Tmpl'].fillna(method='ffill')
SPTV5['Super']=SPTV5['Super'].fillna(method='ffill')
SPTV5['Detail3']=SPTV5['Detail3'].fillna(method='ffill')


# In[373]:


SPTV5=SPTV5.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
SPTV5['Category']=SPTV5['Category'].fillna(method='ffill')
SPTV5['QLevel']=SPTV5['QLevel'].fillna(method='ffill')
#SPTV5['QUESTID']=SPTV5['QUESTID'].fillna(method='ffill')
#SPTV5['QuestionID']=SPTV5['QuestionID'].fillna(method='ffill')


# In[374]:


SPTV5['VersionID']='0'
SPTV5['SID']='1857'
SPTV5['Status']='Add'
SPTV5['StudyAnswerID']='0'


# In[375]:


SPTV5['Detail1']=SPTV5['Detail1'].replace(r'nan', np.nan, regex=True)

SPTV5['Detail1']=SPTV5['Detail1'].fillna(SPTV5['Shows_Name'])


# In[376]:


SPTV5['Wave']=SPTV5['Wave'].fillna(SPTV5['Initial_Wave']) 
SPTV5['Wave']=SPTV5['Wave'].astype(str)
SPTV5['Wave']=SPTV5['Wave'].replace(r'W', '', regex=True)
SPTV5['Wave']=SPTV5['Wave'].replace(r'nan', np.nan, regex=True)
#SPTV5['Wave'].isna().value_counts()
SPTV5['Wave']=SPTV5['Wave'].fillna('0')
SPTV5['SDID']=SPTV5['SDID'].fillna('0')
SPTV5['Definition'] = SPTV5.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[377]:


#SPTV5['UCode']=SPTV5['UCode'].fillna('U0')
SPTV5['StudyEntryID']=SPTV5['StudyEntryID'].fillna('0')
#SPTV5['UCode']=SPTV5['UCode'].fillna('U0')
#SPTV5['QuestionID']=SPTV5['QuestionID'].fillna('0')
#SPTV5['QUESTID']=SPTV5['QUESTID'].fillna('0')
#SPTV5['AnswerID']=SPTV5['AnswerID'].fillna('0')


# In[378]:


SPTV5['Shows_Name']=SPTV5['Sec_List_Heading'] +":" + " "+ SPTV5['Shows_Name']


# In[379]:


SPTV5.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV5.csv',index=False,header=True)


# # SPTV2

# In[380]:


#col1 -X,1,2,3,4,6


# In[381]:


df_TV_Movie_SPTV2=df_TV_Movie.query('cleantype=="SPTV2" and OneWave_Suppress!="#"')


# In[382]:


df_TV_Movie_SPTV2['F2020']=df_TV_Movie_SPTV2['F2020'].str.replace('nan','')
df_TV_Movie_SPTV2['S2021']=df_TV_Movie_SPTV2['S2021'].str.replace('nan','')


# In[383]:


dftest_SPTV2={}
df_TV_Movie_PV_SPTV2={}
df_inner_PV_SPTV2={}
#TV1_1W={}
value=['x','1','2','3','4','6']
j=0
PV=['x','1','2','3','4','6']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_SPTV2[name]=df_TV_Movie_SPTV2.copy()
    for i in range(len(df_TV_Movie_PV_SPTV2[name])):
        type=df_TV_Movie_PV_SPTV2[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_SPTV2[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_SPTV2[name].iloc[i,11]= str(df_TV_Movie_PV_SPTV2[name].iloc[i,11]) + str(value[j])
            
    dftest_SPTV2[name] = pd.DataFrame(df_TV_Movie_PV_SPTV2[name])
    df_inner_PV_SPTV2[name]= pd.merge(dftest_SPTV2[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #SPTV2_1W[name]=dftest_SPTV2[name].query('OneWave_Suppress=="#"')
    
    j +=1
	


# In[384]:


PSPTV2= [df_inner_PV_SPTV2['x'],
        #df_inner_PV_SPTV2['0'],
           df_inner_PV_SPTV2['1'],
           df_inner_PV_SPTV2['2'], 
           df_inner_PV_SPTV2['3'], 
           df_inner_PV_SPTV2['4'],
           
           df_inner_PV_SPTV2['6'],
           
          ]


# In[385]:


SPTV2concat=pd.concat(PSPTV2)


# In[386]:


SPTV2concat['LastDigit_PV'] = SPTV2concat['F2020'].apply(lambda x: x[-1])


# In[387]:


SPTV2concat['F2020_Updated']=SPTV2concat['S2021']+SPTV2concat['LastDigit_PV']


# In[388]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[389]:


dfOneW_SPTV2=dfOneW.query("cleantype=='SPTV2'")


# In[390]:


#No one wave items


# In[391]:


SPTV2=SPTV2concat.copy()


# In[392]:


SPTV2=SPTV2.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
 
SPTV2['Tmpl']=SPTV2['Tmpl'].fillna(method='ffill')
SPTV2['Super']=SPTV2['Super'].fillna(method='ffill')
SPTV2['Detail3']=SPTV2['Detail3'].fillna(method='ffill')


# In[393]:


SPTV2=SPTV2.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
SPTV2['Category']=SPTV2['Category'].fillna(method='ffill')
SPTV2['QLevel']=SPTV2['QLevel'].fillna(method='ffill')


# In[394]:


SPTV2['VersionID']='0'
SPTV2['SID']='1857'
SPTV2['Status']='Add'
SPTV2['StudyAnswerID']='0'


# In[395]:


SPTV2['Definition'] = SPTV2.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[396]:


SPTV2=SPTV2.drop_duplicates(subset='F2020_Updated',keep='last')


# In[397]:


SPTV2.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV2.csv',index=False,header=True,encoding='cp1252')


# # TV3 Punch Values

# 1	6
# 1	X 
# 1	1
# 1	2
# 1	3
# 1	4
# 1	8
# 1	9
# 1	0
# 2	5
# 2	4
# No one wave items in TV3 and TV4

# In[398]:


df_TV_Movie_TV3=df_TV_Movie.query('cleantype=="TV3" and OneWave_Suppress!="#"')


# In[399]:


df_TV_Movie_TV3['F2020']=df_TV_Movie_TV3['F2020'].str.replace('nan','')
df_TV_Movie_TV3['S2021']=df_TV_Movie_TV3['S2021'].str.replace('nan','')


# In[400]:


dftest_TV3={}
df_TV_Movie_PV_TV3={}
df_inner_PV_TV3={}
#TV3_1W={}
value=['x','0','1','2','3','4','6','8','9']
j=0
PV=['x','0','1','2','3','4','6','8','9']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_TV3[name]=df_TV_Movie_TV3.copy()
    for i in range(len(df_TV_Movie_PV_TV3[name])):
        type=df_TV_Movie_PV_TV3[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_TV3[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_TV3[name].iloc[i,11]= str(df_TV_Movie_PV_TV3[name].iloc[i,11]) + str(value[j])
            
    dftest_TV3[name] = pd.DataFrame(df_TV_Movie_PV_TV3[name])
    df_inner_PV_TV3[name]= pd.merge(dftest_TV3[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #TV3_1W[name]=dftest_TV3[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[401]:


df_TV_Movie_TV3['F2020']=df_TV_Movie_TV3['F2020'].str.replace('nan','')
df_TV_Movie_TV3['S2021']=df_TV_Movie_TV3['S2021'].str.replace('nan','')
df_TV_Movie_TV3[['F2020']]=df_TV_Movie_TV3[["F2020"]].apply(pd.to_numeric)
df_TV_Movie_TV3[['S2021']]=df_TV_Movie_TV3[["S2021"]].apply(pd.to_numeric)


# In[402]:


df_TV_Movie_TV3['Col2PV']=''


# In[403]:


for i in range(len(df_TV_Movie_TV3)):
    type=df_TV_Movie_TV3.iloc[i,0]
    cleantype=df_TV_Movie_TV3.iloc[i,1]
    if type == 'show':
        df_TV_Movie_TV3.iloc[i,11] = df_TV_Movie_TV3.iloc[i,11] +1
        df_TV_Movie_TV3.iloc[i,4] =  df_TV_Movie_TV3.iloc[i,4] + 1
        df_TV_Movie_TV3.iloc[i,17] = 'Yes'


# In[404]:


df_TV_Movie_TV3['F2020'] = df_TV_Movie_TV3['F2020'].astype(str).apply(lambda x: x.replace('.0',''))
df_TV_Movie_TV3['S2021'] = df_TV_Movie_TV3['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[405]:


df_TV_Movie_TV3['F2020']=df_TV_Movie_TV3['F2020'].str.replace('nan','')
df_TV_Movie_TV3['S2021']=df_TV_Movie_TV3['S2021'].str.replace('nan','')


# In[406]:


dftest_TV3_2={}
df_TV_Movie_PV_TV3_2={}
df_inner_PV_TV3_2={}
#TV3_1W_2={}

value=['4','5']
j=0
PV=['4','5']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    df_TV_Movie_PV_TV3_2[name]=df_TV_Movie_TV3.copy()
    for i in range(len(df_TV_Movie_PV_TV3_2[name])):
        type=df_TV_Movie_PV_TV3_2[name].iloc[i,0]
        if type == 'show':
            if df_TV_Movie_PV_TV3_2[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_TV3_2[name].iloc[i,11]= str(df_TV_Movie_PV_TV3_2[name].iloc[i,11]) + str(value[j])
            
    dftest_TV3_2[name] = pd.DataFrame(df_TV_Movie_PV_TV3_2[name])
    df_inner_PV_TV3_2[name]= pd.merge(dftest_TV3_2[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #TV3_1W_2[name]=dftest_TV3_2[name].query('OneWave_Suppress=="#"')
    j +=1
	


# In[407]:


PTV3= [df_inner_PV_TV3['0'],
           df_inner_PV_TV3['1'],
           df_inner_PV_TV3['2'], 
           df_inner_PV_TV3['3'], 
           df_inner_PV_TV3['4'],
           #df_inner_PV_TV3['5'],
           df_inner_PV_TV3['6'],
           df_inner_PV_TV3['8'],
           df_inner_PV_TV3['9'],
           df_inner_PV_TV3['x'],
           df_inner_PV_TV3_2['4'],
           df_inner_PV_TV3_2['5'],
		   #df_inner_PV_TV3_2['1'],
           #df_inner_PV_TV3_2['2']
          ]
		  


# In[408]:


TV3concat=pd.concat(PTV3)


# In[409]:


for i in range(len(TV3concat)):
        value=TV3concat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                TV3concat.iloc[i,24]=value[1:]


# In[410]:


#TV3concat['Detail1'].value_counts()


# In[411]:


TV3concat['LastDigit_PV'] = TV3concat['F2020'].apply(lambda x: x[-1])


# In[412]:


TV3concat['F2020_Updated']= TV3concat['S2021'] + TV3concat['LastDigit_PV']


# In[413]:


#TV3concat.to_csv(r"C:\Users\saraswathy.rajaman\Documents\TV3.csv",index=False,header=True)


# In[414]:


TV3concat= TV3concat.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[415]:



TV3=TV3concat.copy()


# In[416]:


TV3['VersionID']='0'
TV3['SID']='1857'
TV3['Status']='Add'
TV3['StudyAnswerID']='0'


# In[417]:


TV3['Definition'] = TV3.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[418]:


TV3.to_csv(r"C:\Users\saraswathy.rajaman\Documents\TV3.csv",index=False,header=True)


# # TV4 Punch Values

# In[ ]:





# In[419]:


#--------------------------------------
#Columns	Punch Value	Label	PunchVarible
#1	6	Yes	TV4
#1	8	Full	TV4
#1	9	Most	TV4
#1	0	Some	TV4
#*******************
#2	5	Your Own Home	TV4
#2	1	Someone Else's Home	TV4
#2	6	Hotel/Motel	TV4
#2	3	Bar/Restaurant	TV4
#2	4	Somewhere Else	TV4

#No one wave items in TV4


# In[420]:


df_TV_Movie_TV4=df_TV_Movie.query('cleantype=="TV4"')


# In[421]:


df_TV_Movie_TV4['F2020']=df_TV_Movie_TV4['F2020'].str.replace('nan','')
df_TV_Movie_TV4['S2021']=df_TV_Movie_TV4['S2021'].str.replace('nan','')


# In[422]:


dftest_TV4={}
df_TV_Movie_PV_TV4={}
df_inner_PV_TV4={}
#TV4_1W={}
value=['0','6','8','9']
j=0
PV=['0','6','8','9']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_TV4[name]=df_TV_Movie_TV4.copy()
    for i in range(len(df_TV_Movie_PV_TV4[name])):
        type=df_TV_Movie_PV_TV4[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_TV4[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_TV4[name].iloc[i,11]= str(df_TV_Movie_PV_TV4[name].iloc[i,11]) + str(value[j])
            
    dftest_TV4[name] = pd.DataFrame(df_TV_Movie_PV_TV4[name])
    df_inner_PV_TV4[name]= pd.merge(dftest_TV4[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #TV4_1W[name]=dftest_TV4[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[423]:


df_TV_Movie_TV4['F2020']=df_TV_Movie_TV4['F2020'].str.replace('nan','')
df_TV_Movie_TV4['S2021']=df_TV_Movie_TV4['S2021'].str.replace('nan','')
df_TV_Movie_TV4[['F2020']]=df_TV_Movie_TV4[["F2020"]].apply(pd.to_numeric)
df_TV_Movie_TV4[['S2021']]=df_TV_Movie_TV4[["S2021"]].apply(pd.to_numeric)


# In[424]:


df_TV_Movie_TV4['Col2PV']=''


# In[425]:


for i in range(len(df_TV_Movie_TV4)):
    type=df_TV_Movie_TV4.iloc[i,0]
    cleantype=df_TV_Movie_TV4.iloc[i,1]
    if type == 'show':
        df_TV_Movie_TV4.iloc[i,11] = df_TV_Movie_TV4.iloc[i,11] +1
        df_TV_Movie_TV4.iloc[i,4] =  df_TV_Movie_TV4.iloc[i,4] + 1
        df_TV_Movie_TV4.iloc[i,17] = 'Yes'
		


# In[426]:


df_TV_Movie_TV4['F2020'] = df_TV_Movie_TV4['F2020'].astype(str).apply(lambda x: x.replace('.0',''))
df_TV_Movie_TV4['S2021'] = df_TV_Movie_TV4['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[427]:



df_TV_Movie_TV4['F2020']=df_TV_Movie_TV4['F2020'].str.replace('nan','')
df_TV_Movie_TV4['S2021']=df_TV_Movie_TV4['S2021'].str.replace('nan','')


# In[428]:


dftest_TV4_2={}
df_TV_Movie_PV_TV4_2={}
df_inner_PV_TV4_2={}
#TV4_1W_2={}

value=['1','3','4','5','6']
j=0
PV=['1','3','4','5','6']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    df_TV_Movie_PV_TV4_2[name]=df_TV_Movie_TV4.copy()
    for i in range(len(df_TV_Movie_PV_TV4_2[name])):
        type=df_TV_Movie_PV_TV4_2[name].iloc[i,0]
        if type == 'show':
            if df_TV_Movie_PV_TV4_2[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_TV4_2[name].iloc[i,11]= str(df_TV_Movie_PV_TV4_2[name].iloc[i,11]) + str(value[j])
            
    dftest_TV4_2[name] = pd.DataFrame(df_TV_Movie_PV_TV4_2[name])
    df_inner_PV_TV4_2[name]= pd.merge(dftest_TV4_2[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #TV4_1W_2[name]=dftest_TV4_2[name].query('OneWave_Suppress=="#"')
    j +=1
	


# In[429]:


PTV4= [df_inner_PV_TV4['0'],
           df_inner_PV_TV4['6'],
           df_inner_PV_TV4['8'], 
           df_inner_PV_TV4['9'], 
           df_inner_PV_TV4_2['4'],
           df_inner_PV_TV4_2['5'],
           df_inner_PV_TV4_2['6'],
		   df_inner_PV_TV4_2['1'],
           df_inner_PV_TV4_2['3'],
          ]


# In[430]:


TV4concat=pd.concat(PTV4)


# In[431]:


TV4concat['LastDigit_PV'] = TV4concat['F2020'].apply(lambda x: x[-1])


# In[432]:


TV4concat['F2020_Updated']= TV4concat['S2021'] + TV4concat['LastDigit_PV']


# In[433]:


for i in range(len(TV4concat)):
        value=TV4concat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                TV4concat.iloc[i,24]=value[1:]


# In[434]:


TV4concat= TV4concat.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[435]:


TV4=TV4concat.copy()


# In[436]:


TV4['VersionID']='0'
TV4['SID']='1857'
TV4['Status']='Add'
TV4['StudyAnswerID']='0'


# In[437]:


TV4=TV4.drop_duplicates(subset='F2020_Updated',keep='last')


# In[438]:


TV4['Detail1']=TV4['Detail1'].fillna(TV4['Shows_Name']) 


# In[439]:


TV4['Definition'] = TV4.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[440]:


TV4.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV4.csv',index=False,header=True)


# # TV5 Punch values

# In[441]:


#only col1 value -6,5,1,4-no col2 values


# In[442]:


df_TV_Movie_TV5=df_TV_Movie.query('cleantype=="TV5" and OneWave_Suppress!="#"')


# In[443]:


df_TV_Movie_TV5['F2020']=df_TV_Movie_TV5['F2020'].str.replace('nan','')
df_TV_Movie_TV5['S2021']=df_TV_Movie_TV5['S2021'].str.replace('nan','')


# In[444]:


dftest_TV5={}
df_TV_Movie_PV_TV5={}
df_inner_PV_TV5={}
#TV5_1W={}
value=['1','4','5','6']
j=0
PV=['1','4','5','6']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_TV5[name]=df_TV_Movie_TV5.copy()
    for i in range(len(df_TV_Movie_PV_TV5[name])):
        type=df_TV_Movie_PV_TV5[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_TV5[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_TV5[name].iloc[i,11]= str(df_TV_Movie_PV_TV5[name].iloc[i,11]) + str(value[j])
            
    dftest_TV5[name] = pd.DataFrame(df_TV_Movie_PV_TV5[name])
    df_inner_PV_TV5[name]= pd.merge(dftest_TV5[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #TV5_1W[name]=dftest_TV5[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[445]:


PTV5= [df_inner_PV_TV5['1'],
           df_inner_PV_TV5['6'],
           df_inner_PV_TV5['5'], 
           df_inner_PV_TV5['4'], 
                    
          ]


# In[446]:


TV5concat=pd.concat(PTV5)


# In[447]:


for i in range(len(TV5concat)):
        value=str(TV5concat.iloc[i,24])
        firstvalue=value[0]
        if firstvalue =='#':
                TV5concat.iloc[i,24]=value[1:]


# In[448]:



TV5concat['LastDigit_PV'] = TV5concat['F2020'].apply(lambda x: x[-1])


# In[449]:



TV5concat['F2020_Updated']= TV5concat['S2021'] + TV5concat['LastDigit_PV']


# In[450]:



dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[451]:


dfOneW_TV5=dfOneW.query("cleantype=='TV5'")


# In[452]:



df_TV5=[TV5concat,dfOneW_TV5]


# In[453]:


df_TV5=pd.concat(df_TV5)


# In[454]:


df_TV5= df_TV5.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[455]:


df1w_TV5=df_TV5.query("OneWave_Suppress=='#'")


# In[456]:


dfnon1w_TV5=df_TV5.query("OneWave_Suppress!='#'")


# In[457]:


onewave_TV5={}
dfonewave_TV5={}

value=['1','6','5','4']
j=0
PV=['1','6','5','4']

for name in PV:
        
    onewave_TV5[name]=df1w_TV5.copy()
    for i in range(len(onewave_TV5[name])):
            onewave_TV5[name].iloc[i,2]= str(onewave_TV5[name].iloc[i,2]) + str(value[j])
            onewave_TV5[name].iloc[i,16]=onewave_TV5[name].iloc[i,6]
            onewave_TV5[name].iloc[i,35]=onewave_TV5[name].iloc[i,2]
            onewave_TV5[name].iloc[i,29]='0'
            onewave_TV5[name].iloc[i,26]='84'
    dfonewave_TV5[name] = pd.DataFrame(onewave_TV5[name])
      
    j +=1
#add Punch Value ,copy show names to detail1 CCP -S2021-F2021 updated column


# In[458]:


TV5onewave= [dfonewave_TV5['1'],
           dfonewave_TV5['6'],
           dfonewave_TV5['5'], 
           dfonewave_TV5['4'],                
           
          ]


# In[459]:


TV5onewave=pd.concat(TV5onewave)


# In[460]:



TV5onewave['LastDigit_PV']=TV5onewave['S2021'].str.strip().str[-1]


# In[461]:


TV5onewave['SDID']='0'
TV5onewave['SID']='1857'
#TV5onewave['UCode']='U0'
TV5onewave['StudyEntryID']='0'
#TV5onewave['QUESTID']='0'
#TV5onewave['QuestionID']='0'


# In[462]:



TV5onewave.to_csv('TV5#.csv',index=False,header=True)


# In[463]:


TV5=[dfnon1w_TV5,TV5onewave]


# In[464]:


TV5=pd.concat(TV5)


# In[465]:


TV5=TV5.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
TV5['Tmpl']=TV5['Tmpl'].fillna(method='ffill')
TV5['Super']=TV5['Super'].fillna(method='ffill')
TV5['Detail3']=TV5['Detail3'].fillna(method='ffill')


# In[466]:


TV5=TV5.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
TV5['Category']=TV5['Category'].fillna(method='ffill')
TV5['QLevel']=TV5['QLevel'].fillna(method='ffill')


# In[467]:


#TV5['QUESTID']=TV5['QUESTID'].fillna('0')
#TV5['QuestionID']=TV5['QuestionID'].fillna('0')
TV5['SDID']=TV5['SDID'].fillna('0')


# In[468]:


TV5['VersionID']='0'
TV5['SID']='1857'


# In[469]:


TV5['Status']='Add'
TV5['StudyAnswerID']='0'


# In[470]:


TV5['Definition'] = TV5.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[471]:


TV5['Detail1']=TV5['Detail1'].fillna(TV5['Shows_Name'])


# In[472]:


TV5['Wave']=TV5['Wave'].fillna('0')


# In[473]:


#TV5['UCode']=TV5['UCode'].fillna('U0')


# In[474]:


Listheading=TV5['Sec_List_Heading'].unique()
g=TV5.groupby('Sec_List_Heading')


# In[475]:


i=0
n=0
TV5_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    TV5_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[476]:


n=0
for values in Listheading:
    TV5_LH[n]=TV5_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    TV5_LH[n]['Detail2']=TV5_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF    


# In[477]:


#n


# In[478]:


TV5Frames=[TV5_LH[0],TV5_LH[1],TV5_LH[2],TV5_LH[3],TV5_LH[4],TV5_LH[5],TV5_LH[6],TV5_LH[7],TV5_LH[8],TV5_LH[9]]


# In[479]:


TV5=pd.concat(TV5Frames)


# In[480]:


TV5=TV5.drop_duplicates(subset='F2020_Updated',keep='last')


# In[481]:


TV5['Wave']=TV5['Wave'].replace(r'^\s*$',np.nan,regex=True)
TV5['StudyEntryID']=TV5['StudyEntryID'].replace(r'^\s*$',np.nan,regex=True)
#TV5['AnswerID']=TV5['AnswerID'].replace(r'^\s*$',np.nan,regex=True)
#TV5['UCode']=TV5['UCode'].replace(r'^\s*$',np.nan,regex=True)


# In[482]:


#TV5['Wave'].isna().value_counts()


# In[483]:


TV5['Wave']=TV5['Wave'].fillna('0')


# In[484]:


#TV5['Wave'].isna().value_counts()


# In[485]:


TV5['StudyEntryID']=TV5['StudyEntryID'].fillna('0')


# In[486]:


#TV5['AnswerID']=TV5['AnswerID'].fillna('0')


# In[487]:


#TV5['UCode']=TV5['UCode'].fillna('U0')


# In[488]:


#TV2['Wave']=TV2['Wave'].fillna(TV2)


# In[489]:



TV5.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV5.csv',index=False,header=True)


# # TV6 Punch Values

# In[490]:


#col1- 5, 1,4 no col 2 values


# In[491]:


df_TV_Movie_TV6=df_TV_Movie.query('cleantype=="TV6" and OneWave_Suppress!="#"')


# In[492]:


df_TV_Movie_TV6['F2020']=df_TV_Movie_TV6['F2020'].str.replace('nan','')
df_TV_Movie_TV6['S2021']=df_TV_Movie_TV6['S2021'].str.replace('nan','')


# In[493]:


dftest_TV6={}
df_TV_Movie_PV_TV6={}
df_inner_PV_TV6={}
#TV6_1W={}
value=['1','5','4','6']
j=0
PV=['1','5','4','6']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_TV6[name]=df_TV_Movie_TV6.copy()
    for i in range(len(df_TV_Movie_PV_TV6[name])):
        type=df_TV_Movie_PV_TV6[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_TV6[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_TV6[name].iloc[i,11]= str(df_TV_Movie_PV_TV6[name].iloc[i,11]) + str(value[j])
            
    dftest_TV6[name] = pd.DataFrame(df_TV_Movie_PV_TV6[name])
    df_inner_PV_TV6[name]= pd.merge(dftest_TV6[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #TV6_1W[name]=dftest_TV6[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[494]:


PTV6= [
           df_inner_PV_TV6['1'],
           df_inner_PV_TV6['4'],
           df_inner_PV_TV6['5'],
           df_inner_PV_TV6['6'],
           
          ]


# In[495]:


TV6concat=pd.concat(PTV6)


# In[496]:


for i in range(len(TV6concat)):
        value=str(TV6concat.iloc[i,24])
        firstvalue=value[0]
        if firstvalue =='#':
                TV6concat.iloc[i,24]=value[1:]


# In[497]:


#TV6concat['Detail1']


# In[498]:


TV6concat['LastDigit_PV'] = TV6concat['F2020'].apply(lambda x: x[-1])


# In[499]:


TV6concat['F2020_Updated']= TV6concat['S2021'] + TV6concat['LastDigit_PV']


# In[500]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[501]:


dfOneW_TV6=dfOneW.query("cleantype=='TV6'")


# In[502]:


df_TV6=[TV6concat,dfOneW_TV6]


# In[503]:


df_TV6=pd.concat(df_TV6)


# In[504]:


df_TV6= df_TV6.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[505]:


df1w_TV6=df_TV6.query("OneWave_Suppress=='#'")


# In[506]:


dfnon1w_TV6=df_TV6.query("OneWave_Suppress!='#'")


# In[507]:


onewave_TV6={}
dfonewave_TV6={}

value=['1','5','4','6']
j=0
PV=['1','5','4','6']

for name in PV:
        
    onewave_TV6[name]=df1w_TV6.copy()
    for i in range(len(onewave_TV6[name])):
            onewave_TV6[name].iloc[i,2]= str(onewave_TV6[name].iloc[i,2]) + str(value[j])
            onewave_TV6[name].iloc[i,16]=onewave_TV6[name].iloc[i,6]
            onewave_TV6[name].iloc[i,35]=onewave_TV6[name].iloc[i,2]
            onewave_TV6[name].iloc[i,29]='0'
            onewave_TV6[name].iloc[i,26]='84'
    dfonewave_TV6[name] = pd.DataFrame(onewave_TV6[name])
      
    j +=1
#add Punch Value ,copy show names to detail1 CCP -S2021-F2021 updated column


# In[508]:


TV6onewave= [dfonewave_TV6['1'],
           dfonewave_TV6['5'],
           dfonewave_TV6['4'],
             dfonewave_TV6['6'],
           
          ]


# In[509]:


TV6onewave=pd.concat(TV6onewave)


# In[510]:


TV6onewave['LastDigit_PV']=TV6onewave['S2021'].str.strip().str[-1]


# In[511]:


TV6onewave['SDID']='0'

#TV6onewave['UCode']='U0'
TV6onewave['StudyEntryID']='0'


# In[512]:


#TV6onewave['QUESTID']='0'
#TV6onewave['QuestionID']='0'


# In[513]:



TV6onewave.to_csv('TV6#.csv',index=False,header=True)


# In[514]:


TV6=[dfnon1w_TV6,TV6onewave]


# In[515]:


TV6=pd.concat(TV6)


# In[516]:



TV6=TV6.sort_values(['cleantype', 'LastDigit_PV'],ascending=[True, True])
						  
TV6['Tmpl']=TV6['Tmpl'].fillna(method='ffill')
TV6['Super']=TV6['Super'].fillna(method='ffill')
TV6['Detail3']=TV6['Detail3'].fillna(method='ffill')


# In[517]:


TV6=TV6.sort_values(['cleantype', 'Sec_List_Heading'],ascending=[True,True])
TV6['Category']=TV6['Category'].fillna(method='ffill')
TV6['QLevel']=TV6['QLevel'].fillna(method='ffill')
#TV6['QUESTID']=TV6['QUESTID'].fillna('0')
#TV6['QuestionID']=TV6['QuestionID'].fillna('0')
#TV6['UCode']=TV6['UCode'].fillna('U0')
TV6['SDID']=TV6['SDID'].fillna('0')


# In[518]:


Listheading=TV6['Sec_List_Heading'].unique()
g=TV6.groupby('Sec_List_Heading')


# In[519]:


i=0
n=0
TV6_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    TV6_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[520]:


n=0
for values in Listheading:
    TV6_LH[n]=TV6_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    TV6_LH[n]['Detail2']=TV6_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF    


# In[521]:


TV6Frames=[TV6_LH[0]]


# In[522]:


TV6=pd.concat(TV6Frames)


# In[523]:


TV6['Definition'] = TV6.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[524]:


TV6['VersionID']='0'
TV6['SID']='1857'
TV6['Status']='Add'
TV6['StudyAnswerID']='0'


# In[525]:


TV6=TV6.drop_duplicates(subset='F2020_Updated',keep='last')


# In[526]:


TV6.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV6.csv',index=False,header=True)


# # add_cable

# In[527]:


#col1-1,2 no col 2 values


# In[528]:


df_TV_Movie_ac=df_TV_Movie.query('cleantype=="add_cabl" and OneWave_Suppress!="#"')


# In[529]:



df_TV_Movie_ac['F2020']=df_TV_Movie_ac['F2020'].str.replace('nan','')
df_TV_Movie_ac['S2021']=df_TV_Movie_ac['S2021'].str.replace('nan','')


# In[530]:


dftest_ac={}
df_TV_Movie_PV_ac={}
df_inner_PV_ac={}
#ac_1W={}
value=['1','2']
j=0
PV=['1','2']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_ac[name]=df_TV_Movie_ac.copy()
    for i in range(len(df_TV_Movie_PV_ac[name])):
        type=df_TV_Movie_PV_ac[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_ac[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_ac[name].iloc[i,11]= str(df_TV_Movie_PV_ac[name].iloc[i,11]) + str(value[j])
            
    dftest_ac[name] = pd.DataFrame(df_TV_Movie_PV_ac[name])
    df_inner_PV_ac[name]= pd.merge(dftest_ac[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #ac_1W[name]=dftest_ac[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[531]:


Pac= [
           df_inner_PV_ac['1'],
           df_inner_PV_ac['2'], 
           
          ]


# In[532]:


acconcat=pd.concat(Pac)


# In[533]:


acconcat['Detail1']=acconcat['Detail1'].astype(str)


# In[534]:


for i in range(len(acconcat)):
        value=acconcat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                acconcat.iloc[i,24]=value[1:]


# In[535]:


acconcat['LastDigit_PV'] = acconcat['F2020'].apply(lambda x: x[-1])


# In[536]:



acconcat['F2020_Updated']= acconcat['S2021'] + acconcat['LastDigit_PV']


# # Add cable one wave

# In[537]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[538]:


dfOneW_ac=dfOneW.query("cleantype=='add_cabl'")


# In[539]:



df_ac=[acconcat,dfOneW_ac]


# In[540]:


df_ac=pd.concat(df_ac)


# In[541]:


df_ac= df_ac.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[542]:


df1w_ac=df_ac.query("OneWave_Suppress=='#'")


# In[543]:


dfnon1w_ac=df_ac.query("OneWave_Suppress!='#'")


# In[544]:


onewave_ac={}
dfonewave_ac={}

value=['1','2']
j=0
PV=['1','2']

for name in PV:
        
    onewave_ac[name]=df1w_ac.copy()
    for i in range(len(onewave_ac[name])):
            onewave_ac[name].iloc[i,2]= str(onewave_ac[name].iloc[i,2]) + str(value[j])
            onewave_ac[name].iloc[i,16]=onewave_ac[name].iloc[i,6]
            onewave_ac[name].iloc[i,35]=onewave_ac[name].iloc[i,2]
            onewave_ac[name].iloc[i,29]='0'
            onewave_ac[name].iloc[i,26]='84'
    dfonewave_ac[name] = pd.DataFrame(onewave_ac[name])
      
    j +=1
#add Punch Value ,copy show names to detail1 CCP -S2021-F2021 updated column


# In[545]:


aconewave= [onewave_ac['1'],
           onewave_ac['2']
           ]
		  


# In[546]:


aconewave=pd.concat(aconewave)


# In[547]:


aconewave['LastDigit_PV']=aconewave['S2021'].str.strip().str[-1]


# In[548]:


aconewave['SDID']='0'

#aconewave['UCode']='U0'
aconewave['StudyEntryID']='0'


# In[549]:


aconewave['Shows_Name']=aconewave['Detail1']
aconewave['Wave']='0'
#aconewave['AnswerID']='0'


# In[550]:


#aconewave['QUESTID']='0'
#aconewave['QuestionID']='0'


# In[551]:


aconewave.to_csv('ac#.csv',index=False,header=True)


# In[552]:


ac=[dfnon1w_ac,aconewave]


# In[553]:


ac=pd.concat(ac)


# In[554]:


ac=ac.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
ac['Tmpl']=ac['Tmpl'].fillna(method='ffill')
ac['Super']=ac['Super'].fillna(method='ffill')
ac['Detail3']=ac['Detail3'].fillna(method='ffill')


# In[555]:


ac=ac.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
ac['Category']=ac['Category'].fillna(method='ffill')
ac['QLevel']=ac['QLevel'].fillna(method='ffill')


# In[556]:


Listheading=ac['Sec_List_Heading'].unique()


# In[557]:


g=ac.groupby('Sec_List_Heading')


# In[558]:


i=0
n=0
ac_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    ac_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[559]:


n=0
for values in Listheading:
    ac_LH[n]=ac_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    ac_LH[n]['Detail2']=ac_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[560]:


#n


# In[561]:


acFrames=pd.DataFrame()
acFrames = acFrames.append([ac_LH[i] for i in range(n)])


# In[562]:



ac=acFrames.copy()


# In[563]:



ac['Shows_Name']=ac['Shows_Name'].astype(str)


# In[564]:


ac['Detail1']=ac['Detail1'].replace(r'nan', np.nan, regex=True)


# In[565]:


ac['Detail1']=ac['Detail1'].fillna(ac['Shows_Name'])


# In[566]:


ac['Wave']=ac['Wave'].fillna(ac['Initial_Wave']) 
ac['Wave']=ac['Wave'].astype(str)
ac['Wave']=ac['Wave'].replace(r'W', '', regex=True)
ac['Wave']=ac['Wave'].replace(r'nan', np.nan, regex=True)
#ac['Wave'].isna().value_counts()
ac['Wave']=ac['Wave'].fillna('0')
ac['SDID']=ac['SDID'].fillna('0')
ac['Definition'] = ac.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[567]:



#ac['UCode']=ac['UCode'].fillna('U0')
ac['StudyEntryID']=ac['StudyEntryID'].fillna('0')
#ac['UCode']=ac['UCode'].fillna('U0')
#ac['QuestionID']=ac['QuestionID'].fillna('0')
#ac['QUESTID']=ac['QUESTID'].fillna('0')
#ac['AnswerID']=ac['AnswerID'].fillna('0')


# In[568]:


ac['VersionID']='0'
ac['SID']='1857'
ac['Status']='Add'
ac['StudyAnswerID']='0'


# In[569]:


#ac['Sec_List_Heading'].unique()


# In[570]:


ac=ac.drop_duplicates(subset='F2020_Updated',keep='last')


# In[571]:


#ac.duplicated().value_counts()


# In[572]:



ac.to_csv(r'C:\Users\saraswathy.rajaman\Documents\ac.csv',index=False,header=True)


# # Movie 

# In[573]:


#Movies Punch Variable
#col1-1,2,3,4,5


# In[574]:


df_TV_Movie_M=df_TV_Movie.query('cleantype=="Movie" and OneWave_Suppress!="#"')


# In[575]:


#df_TV_Movie_M.to_csv(r"C:\Users\saraswathy.rajaman\Documents\df_TV_Movie_M.csv",header=True,index=False)


# In[576]:


df_TV_Movie_M['F2020']=df_TV_Movie_M['F2020'].str.replace('nan','')
df_TV_Movie_M['S2021']=df_TV_Movie_M['S2021'].str.replace('nan','')


# In[577]:


dftest_M={}
df_TV_Movie_PV_M={}
df_inner_PV_M={}
#M_1W={}
value=['1','2','3','4','5']
j=0
PV=['1','2','3','4','5']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_M[name]=df_TV_Movie_M.copy()
    for i in range(len(df_TV_Movie_PV_M[name])):
        type=df_TV_Movie_PV_M[name].iloc[i,0]
        if type == 'show':
            
            if df_TV_Movie_PV_M[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_M[name].iloc[i,11]= str(df_TV_Movie_PV_M[name].iloc[i,11]) + str(value[j])
            
    dftest_M[name] = pd.DataFrame(df_TV_Movie_PV_M[name])
    df_inner_PV_M[name]= pd.merge(dftest_M[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #M_1W[name]=dftest_M[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[578]:


PM= [      df_inner_PV_M['1'],
           df_inner_PV_M['2'], 
           df_inner_PV_M['3'], 
           df_inner_PV_M['4'],
           df_inner_PV_M['5'],
                    ]


# In[579]:


Mconcat=pd.concat(PM)


# In[580]:


Mconcat['Detail1']=Mconcat['Detail1'].astype(str)


# In[581]:


for i in range(len(Mconcat)):
        value=Mconcat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                Mconcat.iloc[i,24]=value[1:]


# In[582]:


#Mconcat.to_csv(r"C:\Users\saraswathy.rajaman\Documents\Mconcat.csv",index=False,header=True)


# In[583]:


Mconcat['LastDigit_PV'] = Mconcat['F2020'].apply(lambda x: x[-1])


# In[584]:



Mconcat['F2020_Updated']= Mconcat['S2021'] + Mconcat['LastDigit_PV']


# In[585]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[586]:


dfOneW_M=dfOneW.query("cleantype=='Movie'")


# In[587]:



df_M=[Mconcat,dfOneW_M]


# In[588]:


df_M=pd.concat(df_M)


# # Movie onewave

# In[589]:



df_M= df_M.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[590]:


df1w_M=df_M.query("OneWave_Suppress=='#'")


# In[591]:


dfnon1w_M=df_M.query("OneWave_Suppress!='#'")


# In[592]:


onewave_M={}
dfonewave_M={}

value=['1','2','3','4','5']
j=0
PV=['1','2','3','4','5']

for name in PV:
        
    onewave_M[name]=df1w_M.copy()
    for i in range(len(onewave_M[name])):
            onewave_M[name].iloc[i,2]= str(onewave_M[name].iloc[i,2]) + str(value[j])
            onewave_M[name].iloc[i,16]=onewave_M[name].iloc[i,6]
            onewave_M[name].iloc[i,35]=onewave_M[name].iloc[i,2]
            onewave_M[name].iloc[i,29]='0'
            onewave_M[name].iloc[i,26]='84'
    dfonewave_M[name] = pd.DataFrame(onewave_M[name])
      
    j +=1
#add Punch Value ,copy show names to detail1 CCP -S2021-F2021 updated column


# In[593]:


Monewave= [dfonewave_M['1'],
           dfonewave_M['2'],
           dfonewave_M['3'], 
           dfonewave_M['4'],
           dfonewave_M['5']
           
          ]


# In[594]:


Monewave=pd.concat(Monewave)


# In[595]:



Monewave['LastDigit_PV']=Monewave['S2021'].str.strip().str[-1]


# In[596]:


Monewave['SDID']='0'

#Monewave['UCode']='U0'
Monewave['StudyEntryID']='0'


# In[597]:


#Monewave['QUESTID']='0'
#Monewave['QuestionID']='0'


# In[598]:


Monewave.to_csv('M1.csv',index=False,header=True)


# In[599]:


M=[dfnon1w_M,Monewave]


# In[600]:


M=pd.concat(M)


# In[601]:


M=M.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
M['Tmpl']=M['Tmpl'].fillna(method='ffill')
M['Super']=M['Super'].fillna(method='ffill')
M['Detail3']=M['Detail3'].fillna(method='ffill')
#M['Detail2']=M['Detail2'].fillna(method='ffill')


# In[602]:


M=M.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
M['Category']=M['Category'].fillna(method='ffill')
M['QLevel']=M['QLevel'].fillna(method='ffill')


# In[603]:


M['VersionID']='0'
M['SID']='1857'
M['Status']='Add'
M['StudyAnswerID']='0'


# In[604]:


Listheading=M['Sec_List_Heading'].unique()


# In[605]:


g=M.groupby('Sec_List_Heading')


# In[606]:


i=0
n=0
M_LH={}
for Sec_List_Heading, g_df in g:
   # print (Sec_List_Heading)
    M_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[607]:


n=0
for values in Listheading:
    M_LH[n]=M_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    M_LH[n]['Detail2']=M_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[608]:


MFrames=pd.DataFrame()
MFrames = MFrames.append([M_LH[i] for i in range(n)])


# In[609]:


M=MFrames.copy()


# In[610]:


M['Shows_Name']=M['Shows_Name'].astype(str)


# In[611]:


M['Detail1']=M['Detail1'].replace(r'nan', np.nan, regex=True)


# In[612]:


M['Detail1']=M['Detail1'].fillna(M['Shows_Name'])


# In[613]:




M['Wave']=M['Wave'].fillna(M['Initial_Wave']) 
M['Wave']=M['Wave'].astype(str)
M['Wave']=M['Wave'].replace(r'W', '', regex=True)
M['Wave']=M['Wave'].replace(r'nan', np.nan, regex=True)
#M['Wave'].isna().value_counts()


# In[614]:


M['Wave']=M['Wave'].fillna('0')
M['SDID']=M['SDID'].fillna('0')
M['Definition'] = M.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[615]:


#M['UCode']=M['UCode'].fillna('U0')
M['StudyEntryID']=M['StudyEntryID'].fillna('0')
#M['UCode']=M['UCode'].fillna('U0')

#QUESTID
#AnswerID


# In[616]:


#M['QuestionID']=M['QuestionID'].fillna('0')
#M['QUESTID']=M['QUESTID'].fillna('0')
#M['AnswerID']=M['AnswerID'].fillna('0')


# In[617]:


#M['Detail1'] = M.apply(lambda x: x[1:]  if x['compare']==False else x['Definition'], axis=1)


# In[618]:


M=M.drop_duplicates(subset='F2020_Updated',keep='last')


# In[619]:


#M.duplicated().value_counts()


# In[620]:


M.to_csv(r'C:\Users\saraswathy.rajaman\Documents\Movie1.csv',index=False,header=True)


# # Cable Punch Values

# In[621]:


#col1-0,1,6,8,9 no col 2 values


# In[622]:


df_TV_Movie_C=df_TV_Movie.query('cleantype=="cable" and OneWave_Suppress!="#"')


# In[623]:


df_TV_Movie_C['Shows_Name']=df_TV_Movie_C['Sec_List_Heading'] +":" + " "+df_TV_Movie_C['Shows_Name']


# In[624]:


#df_TV_Movie_C


# In[625]:


df_TV_Movie_C['F2020']=df_TV_Movie_C['F2020'].str.replace('nan','')
df_TV_Movie_C['S2021']=df_TV_Movie_C['S2021'].str.replace('nan','')


# In[626]:


dftest_C={}
df_TV_Movie_PV_C={}
df_inner_PV_C={}
#C_1W={}
value=['0','6','8','9','1']
j=0
PV=['0','6','8','9','1']
for name in PV:
    #df_TV_Movie_PV[name]=pd.DataFrame()
    
    df_TV_Movie_PV_C[name]=df_TV_Movie_C.copy()
    for i in range(len(df_TV_Movie_PV_C[name])):
        #type=df_TV_Movie_PV_C[name].iloc[i,0]
        #if type == 'show':
            
            #if df_TV_Movie_PV_C[name].iloc[i,11] !="":
            
                df_TV_Movie_PV_C[name].iloc[i,11]= str(df_TV_Movie_PV_C[name].iloc[i,11]) + str(value[j])
            
    dftest_C[name] = pd.DataFrame(df_TV_Movie_PV_C[name])
    df_inner_PV_C[name]= pd.merge(dftest_C[name], df_Fall_2020, left_on=['F2020'], right_on=['CCP'],suffixes=('_left','_right'),how='left')
    #df_inner_PV[name]= pd.merge(df_TV_Movie_PV[name], df_Fall_2020, on='CCP', how='inner')
    #C_1W[name]=dftest_C[name].query('OneWave_Suppress=="#"')
    
    j +=1


# In[627]:


PC= [df_inner_PV_C['0'],
     df_inner_PV_C['1'],
           df_inner_PV_C['6'],
           df_inner_PV_C['8'],
           df_inner_PV_C['9'],
           
          ]


# In[628]:


Cconcat=pd.concat(PC)


# In[629]:


Cconcat['Detail1']=Cconcat['Detail1'].astype(str)


# In[630]:


for i in range(len(Cconcat)):
        value=Cconcat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                Cconcat.iloc[i,24]=value[1:]


# In[631]:


Cconcat['LastDigit_PV'] = Cconcat['F2020'].apply(lambda x: x[-1])


# In[632]:


Cconcat['F2020_Updated']= Cconcat['S2021'] + Cconcat['LastDigit_PV']


# In[633]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[634]:



dfOneW_C=dfOneW.query("cleantype=='cable'")


# In[635]:


df_C=[Cconcat,dfOneW_C]


# In[636]:


df_C=pd.concat(df_C)


# In[637]:


df_C= df_C.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# # Cable one wave 

# In[638]:


df1w_C=df_C.query("OneWave_Suppress=='#'")


# In[639]:


dfnon1w_C=df_C.query("OneWave_Suppress!='#'")


# In[640]:


onewave_C={}
dfonewave_C={}

value=['0','6','8','9','1']
j=0
PV=['0','6','8','9','1']
for name in PV:
        
    onewave_C[name]=df1w_C.copy()
           
    for i in range(len(onewave_C[name])):
        type=df_TV_Movie_PV_C[name].iloc[i,0]
        if type == 'show':
                      
            onewave_C[name].iloc[i,2]= str(onewave_C[name].iloc[i,2]) + str(value[j])
            onewave_C[name].iloc[i,16]=onewave_C[name].iloc[i,6]
            onewave_C[name].iloc[i,35]=onewave_C[name].iloc[i,2]
            onewave_C[name].iloc[i,29]='0'
            onewave_C[name].iloc[i,26]='84'
    dfonewave_C[name] = pd.DataFrame(onewave_C[name])
      
    j +=1
#add Punch Value ,copy show names to detail1 CCP -S2021-F2021 updated column


# In[641]:



Conewave= [dfonewave_C['0'],
           dfonewave_C['6'],
           dfonewave_C['8'], 
           dfonewave_C['9'],
           dfonewave_C['1'],
           
          ]


# In[642]:


Conewave=pd.concat(Conewave)


# In[643]:


Conewave['LastDigit_PV']=Conewave['S2021'].str.strip().str[-1]


# In[644]:


Conewave['SDID']='0'

#Conewave['UCode']='U0'
Conewave['StudyEntryID']='0'


# In[645]:


#Conewave['QUESTID']='0'
#Conewave['QuestionID']='0'


# In[646]:


Conewave['Detail1']=Conewave['Detail1'].astype(str)


# In[647]:


#Conewave


# In[648]:


Conewave['Shows_Name']=Conewave['Shows_Name'].apply(lambda x : x[1:])


# In[649]:


Conewave['Shows_Name']=Conewave['Sec_List_Heading'] +":" + " "+ Conewave['Shows_Name']


# In[650]:


#Conewave


# In[651]:


Conewave['Shows_Name']='#'+ Conewave['Shows_Name']


# In[652]:


#Conewave['Shows_Name']= Conewave['Detail1']


# In[653]:



#Conewave.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\C#.csv',index=False,header=True)


# In[654]:


#Conewave


# In[655]:



C=[dfnon1w_C,Conewave]


# In[656]:


C=pd.concat(C)


# In[657]:


#C.columns


# In[658]:


#C


# In[659]:


C=C.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
C['Tmpl']=C['Tmpl'].fillna(method='ffill')
C['Super']=C['Super'].fillna(method='ffill')
C['Detail3']=C['Detail3'].fillna(method='ffill')


# In[660]:




C=C.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
C['Category']=C['Category'].fillna(method='ffill')
C['QLevel']=C['QLevel'].fillna(method='ffill')


# In[661]:


C['VersionID']='0'
C['SID']='1857'
C['Status']='Add'
C['StudyAnswerID']='0'


# In[662]:


Listheading=C['Sec_List_Heading'].unique()


# In[663]:


g=C.groupby('Sec_List_Heading')


# In[664]:


i=0
n=0
C_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    C_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas


# In[ ]:





# In[665]:


n=0
for values in Listheading:
    C_LH[n]=C_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    C_LH[n]['Detail2']=C_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[666]:


#n


# # Append all 57 DF for each sec values in cable 
# 

# In[667]:


CFrames=pd.DataFrame()
CFrames = CFrames.append([C_LH[i] for i in range(n)])


# In[668]:


C=CFrames.copy()


# In[669]:


#C['Detail1']=C['Detail1'].fillna(C['Shows_Name']) 


# In[670]:


C['Detail1']=C['Detail1'].fillna(C['Shows_Name'])


# In[671]:


C['Wave']=C['Wave'].fillna(C['Initial_Wave']) 
C['Wave']=C['Wave'].astype(str)
C['Wave']=C['Wave'].replace(r'W', '', regex=True)


# In[672]:


C['Wave']=C['Wave'].replace(r'nan', np.nan, regex=True)
C['Wave'].isna().value_counts()
C['Wave']=C['Wave'].fillna('0')


# In[673]:


# if the CCP is different in S2021 than F2020 then Defenition is 0


# In[674]:


C['Definition'] = C.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[675]:


C=C.drop_duplicates(subset='F2020_Updated',keep='last')


# In[676]:


#check duplicates


# In[677]:


#C.duplicated().value_counts()


# In[678]:



C.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Cable1.csv',index=False,header=True)


# # TVMedia file

# In[679]:


Final_Frames=[TV1,TV2,TV3,TV4,TV5,TV6,SPTV1,SPTV2,SPTV3,SPTV4,SPTV5,SPTV51,ac,M,C]


# In[680]:


TVmedia=pd.concat(Final_Frames)


# In[681]:


#TVmedia.columns


# In[682]:


TVmedia['QLevel'] =TVmedia['QLevel'].astype(np.int64)
#TVmedia['Wave'] =TVmedia['Wave'].astype(int)


# In[683]:


TVmedia['Tmpl'] =TVmedia['Tmpl'].astype(np.int64)


# In[684]:


TVmedia['QUESTID']=TVmedia['QUESTID'].fillna(0)


# In[685]:


#TVmedia['QUESTID'].isna().value_counts()


# In[686]:


TVmedia['QUESTID'] =TVmedia['QUESTID'].astype(np.int32)


# In[687]:


TVmedia['AnswerID']=TVmedia['AnswerID'].fillna(0)


# In[688]:


TVmedia['UCode']=TVmedia['UCode'].fillna('U0')


# In[689]:


TVmedia['AnswerID'] =TVmedia['AnswerID'].astype(np.int32)


# In[690]:


TVmedia['SDID'] =TVmedia['SDID'].astype(np.int32)


# In[691]:


TVmedia['SID'] =TVmedia['SID'].astype(np.int32)


# In[692]:


TVmedia['StudyAnswerID'] =TVmedia['StudyAnswerID'].astype(np.int32)


# In[693]:


TVmedia['StudyEntryID']=TVmedia['StudyEntryID'].fillna(0)


# In[694]:


#TVmedia['StudyEntryID'].isna().value_counts()


# In[695]:


TVmedia['StudyEntryID'] =TVmedia['StudyEntryID'].astype(np.int32)


# In[696]:


#TVmedia['QLevel'].dtype


# In[697]:


TVmedia['Wave'] =TVmedia['Wave'].astype(float)
TVmedia['Wave'] =TVmedia['Wave'].astype(np.int32)


# In[ ]:





# In[698]:


TVmedia['SDID'] =TVmedia['SDID'].astype(float)
TVmedia['SDID'] =TVmedia['SDID'].astype(int)


# In[699]:


TVmedia['QuestionID'] =TVmedia['QuestionID'].fillna(0)


# In[700]:


TVmedia['QuestionID'] =TVmedia['QuestionID'].astype(float)
TVmedia['QuestionID'] =TVmedia['QuestionID'].astype(int)


# In[701]:


TVmedia['AnswerID'] =TVmedia['AnswerID'].astype(float)
TVmedia['AnswerID'] =TVmedia['AnswerID'].astype(int)


# In[702]:


TVmedia_copy=TVmedia.copy()


# In[703]:


TVmedia_fall = TVmedia.merge(df_Fall_2020.drop_duplicates(), on=['CCP'], 
                   how='outer', indicator=True)


# In[705]:


TVmedia_fall.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Tvmediaandfall.csv',index=False,header=True,encoding='cp1252')


# In[706]:


TVmedia.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\test.csv',index=False,header=True,encoding='cp1252')


# # Remove W83 # value in detail1

# In[707]:



TVmedia.drop(['Fox', 'W84','W83','W82','S2020','W81','F2019','QID','Detail1'], axis=1, inplace=True)


# In[708]:


#TVmedia.columns


# In[709]:


#TVmedia=TVmedia.drop(["StatisticID","CatSynID","NoteID","statusid"],axis=1,inplace=True)
TVmedia.drop(['StatisticID', 'CatSynID','NoteID','statusid','CCP'], axis=1, inplace=True)


# In[710]:


TVmedia.rename(columns={'F2020_Updated':'CCP','Shows_Name':'Detail1','VersionID':'Version'},inplace=True)


# In[711]:


#TVmedia.columns


# In[712]:


TVmedia['EditedBy']='codebookcreator'
TVmedia['EditedDate']=pd.to_datetime('today')
TVmedia['StudyEntryID']='0'
TVmedia['SID']='1952'


# add an empty column
#Mydataframe.insert(0,'Roll Number','')


# In[713]:


TVmedia['StudyEntryID'] =TVmedia['StudyEntryID'].astype(np.int32)


# In[714]:


TVmedia['Version'] =TVmedia['Version'].astype(np.int32)


# In[715]:


TVmedia['Imported']=''
TVmedia['Min']=''
TVmedia['Max']=''


# In[716]:


TVmedia['Min'] =TVmedia['Min'].apply(pd.to_numeric)
#df_TV_Movie_TV1[['F2020']]=df_TV_Movie_TV1[["F2020"]].apply(pd.to_numeric)
#df_TV_Movie_TV1[['S2021']]=df_TV_Movie_TV1[["S2021"]].apply(pd.to_numeric)


# In[717]:


TVmedia['Max'] =TVmedia['Max'].apply(pd.to_numeric)


# In[718]:


#TVmedia['Definition'] = TVmedia.apply(lambda x: '' if x['Definition']==0 else x['Definition'], axis=1)


# In[719]:


TVmedia['Definition'] = TVmedia['Definition'].replace(['0', 0], np.nan)


# In[720]:


#TVmedia.head(50)


# In[721]:


#TVmedia.info()


# In[722]:


#TVmedia_copy=TVmedia.copy()


# In[723]:


TVmedia=TVmedia[["StudyEntryID","SID","Version","Category","Super","Tmpl","Time Period","Detail1","Detail2",
"Detail3","Detail4","UCode","Definition","CCP","ORD","Wave","Status","Full_Label","QLevel","QUESTID","AnswerID","EditedBy","EditedDate","SDID",
"StudyAnswerID","QuestionID","Imported","Min","Max"]]


# In[724]:


TVmedia = TVmedia.astype( {"QLevel":'int32', "QUESTID":'int32', "AnswerID":'int32',"QuestionID":'int32',"SID":'int64', "SDID":'int32', "Version":'int32', "Wave":'int32', "Min":'float',"Max":'float', "StudyEntryID":'int64',"Imported":'bool'} )


# In[725]:


#TVmedia=TVmedia.dropna(subset=['CCP'])


# In[726]:


#TVmedia['CCP'].isna().value_counts()


# # TVmedia to csv file

# In[727]:


TVmedia_copy=TVmedia.copy()


# In[728]:


TVmedia_copy.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Spring2021_withcolumns.csv',index=False,header=True,encoding='cp1252')


# In[729]:


TVmedia.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Spring-2021.csv',index=False,header=True,encoding='cp1252')


# In[730]:


from sqlalchemy import create_engine
#engine = create_engine('sqlite://', echo=False)


# In[731]:


#TVmedia.to_sql(name="tmp_EditedRecords_Test", con=engine,  schema="dbo")


# In[732]:


DB = {'server':'internalSQLdev.mridevops.com','database':'Codebook_Taxonomy','driver':'driver=SQL Server Native Client 11.0','pyodb_d':'SQL Server Native Client 11.0'}
#engine=create_engine('mssql+pyodbc://'+ DB['server']+'/'+ DB['database']+'?'+ DB['driver'])


# In[733]:



engine = create_engine('mssql+pyodbc://' + DB['server'] + '/' + DB['database'] + '?' + DB['driver'], fast_executemany = True)


# In[734]:


import pyodbc 


# import pyodbc 
# 
# server_name = "internalSQLdev.mridevops.com"
# db_name = "Codebook_Taxonomy"
# 
# server = "Server="+str(server_name)
# db = "Database="+str(db_name)
# key = "Driver={SQL Server Native Client 11.0};"+server+";"+db+";"+"Trusted_Connection=yes;"
# 
# cnxn = pyodbc.connect(key)

# In[ ]:





# In[738]:


conn = pyodbc.connect('Driver={'+DB['pyodb_d']+'}; Server='+DB['server']+';Database='+DB['database']+'; Trusted_Connection=yes;')


# In[ ]:


#cursor = conn.cursor()


# 
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="mydatabase"
# )*/"""
# 
# #mycursor = DB.cursor()
# 
# 

# In[ ]:


#cursor.execute('DROP TABLE dbo.tmp_Spring2021_Test')


# In[ ]:


conn.commit()


# In[ ]:


with engine.begin() as connection:
    TVmedia.to_sql(name="tmp_EditedRecords_Hold_testsql",con=engine,schema="dbo",if_exists='append', chunksize=1000,index=False)
#df.to_sql('db_table2', engine, if_exists='replace')


# In[ ]:


#TVmedia.shape


# In[ ]:


#pwd


# TVmedia.info()

# import platform
# print(platform.python_version())

# In[740]:





# In[ ]:




