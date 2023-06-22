#!/usr/bin/env python
# coding: utf-8

# # Import necessary library

# In[ ]:


#import Necessary Library
import pandas as pd
import numpy as np
from openpyxl import Workbook
import re


# In[ ]:


import warnings
warnings.filterwarnings("ignore")


# In[ ]:


#Display settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)


# # Read csv file 

# with open(r'C:\Users\saraswathy.rajaman\Documents\w84_Media_TV_Movie_Sections2.csv') as f:
#     print(f)

# In[ ]:


df_TV_Movie=pd.read_csv(r'C:\Users\saraswathy.rajaman\Documents\w84_Media_TV_Movie_Sections2.csv',encoding='utf8')
#TV Media file


# In[ ]:


#df_TV_Movie


# In[ ]:


#df=pd.read_csv(r'C:\Users\saraswathy.rajaman\Documents\Fall_2020_2.csv',encoding = 'utf-8')


# In[ ]:


#Making a copy 
df_TV_Movie_copy=df_TV_Movie.copy()


# with open(r'C:\Users\saraswathy.rajaman\Documents\Fall_2020.csv') as f:
#     print(f)

# In[ ]:


df_Fall_2020=pd.read_excel(r'C:\Users\saraswathy.rajaman\Documents\Fall_2020.xlsx')
#read the fall file as DF


# In[ ]:


#df_TVMov_Punch_Map=pd.read_csv(r'C:\Users\saraswathy.rajaman\Documents\TVMov_Punch_Map.csv',encoding="UTF-8")
#TVMovies Punch file 


# In[ ]:


df_TV_Movie.rename(columns={'Unnamed: 6':'Sec_List_Heading','Unnamed: 7':'OneWave_Suppress','Show':'Show_Type','Unnamed: 8':'Shows_Name','Unnamed: 9':'Initial_Wave'}, inplace=True)
#Rename columns as suggested


# In[ ]:


#Removing spl character
df_TV_Movie['F2020']=df_TV_Movie['F2020'].str.replace('*','')
df_TV_Movie['S2021']=df_TV_Movie['S2021'].str.replace('*','')


# In[ ]:


df_TV_Movie=df_TV_Movie.drop(0)
#dropping first row from the DF


# # Remove one wave suppress -X values

# In[ ]:


df_TV_Movie.drop(df_TV_Movie.index[df_TV_Movie['OneWave_Suppress'] == 'X'], inplace = True)


# In[ ]:


#df_TV_Movie['OneWave_Suppress'].unique()
#check the unique values in that column  by that confirm the X is removed


# In[ ]:


df_TV_Movie.columns = df_TV_Movie.columns.str.replace(' ', '')


# # check if the CCP is different between S2021 and F2020

# In[ ]:


df_TV_Movie['compare'] = (df_TV_Movie['S2021'] == df_TV_Movie['F2020'])


# # Forward fill Clean type and list heading

# In[ ]:


df_TV_Movie=df_TV_Movie.copy()
df_TV_Movie['cleantype']=df_TV_Movie['cleantype'].fillna(method='ffill')
#Forward fill cleatype as show


# In[ ]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].replace('b', np.nan)
# replace b with np nan


# In[ ]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].replace(r'^\s*$', np.nan, regex=True)
#Replace empty with np.nan


# In[ ]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].fillna(method='ffill')
#Forward fill to get values in empty cell with list heading appropriately


# # Few items has # in sec heading- add # in one wave column for them 

# In[ ]:


for i in range(len(df_TV_Movie)):
        value=df_TV_Movie.iloc[i,6]
        firstvalue=value[0]
        if firstvalue =='#':
                df_TV_Movie.iloc[i,7]='#'


# In[ ]:


df_TV_Movie['Shows_Name']=df_TV_Movie['Shows_Name'].astype(str)


# In[ ]:


for i in range(len(df_TV_Movie)):
        value=df_TV_Movie.iloc[i,8]
        firstvalue=value[0]
        if firstvalue =='#':
                df_TV_Movie.iloc[i,8]=value[1:]


# # For one wave item append # in show names

# In[ ]:


for i in range(len(df_TV_Movie)):
    OneWave_Suppress=df_TV_Movie.iloc[i,7] 
    if OneWave_Suppress == '#': 
        df_TV_Movie.iloc[i,8]='#'+ df_TV_Movie.iloc[i,8]


# # Remove # from List heading or sec heading values

# In[ ]:


for i in range(len(df_TV_Movie)):
        value=df_TV_Movie.iloc[i,6]
        firstvalue=value[0]
        if firstvalue =='#':
                df_TV_Movie.iloc[i,6]=value[1:]


# # Drop Empty rows where na in s2021

# In[ ]:


#df_TV_Movie['S2021'].isna().value_counts()


# In[ ]:


df_TV_Movie=df_TV_Movie.dropna(subset=['S2021'])


# In[ ]:


#df_TV_Movie['S2021'].isna().value_counts()


# In[ ]:


df_TV_Movie.to_csv(r'C:\Users\saraswathy.rajaman\Documents\df_TV_Movie_test.csv',index=False,header=True,encoding='cp1252')


# # TV1

# In[ ]:


df_TV_Movie_TV1=df_TV_Movie.query('cleantype=="TV1" and OneWave_Suppress!="#"')
#filter TV1 from the source and save as DF


# In[ ]:


#df_TV_Movie_TV1


# In[ ]:


df_TV_Movie_TV1['F2020']=df_TV_Movie_TV1['F2020'].str.replace('nan','')
df_TV_Movie_TV1['S2021']=df_TV_Movie_TV1['S2021'].str.replace('nan','')
#if there is nan we are removing as being object data type appending 1 add's as nan1


# In[ ]:


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


# In[ ]:


df_TV_Movie_TV1['F2020']=df_TV_Movie_TV1['F2020'].str.replace('nan','')
df_TV_Movie_TV1['S2021']=df_TV_Movie_TV1['S2021'].str.replace('nan','')
df_TV_Movie_TV1[['F2020']]=df_TV_Movie_TV1[["F2020"]].apply(pd.to_numeric)
df_TV_Movie_TV1[['S2021']]=df_TV_Movie_TV1[["S2021"]].apply(pd.to_numeric)
#convert columns to numeric to add 1 to the column


# In[ ]:


df_TV_Movie_TV1['Col2PV']=''
#adding a col2pv so that we can update yes to them when the value is a col2 punchvalue this is used later to check if that is a col2 value


# In[ ]:


#col2 punch value
for i in range(len(df_TV_Movie_TV1)):
    type=df_TV_Movie_TV1.iloc[i,0]
    cleantype=df_TV_Movie_TV1.iloc[i,1]
    if type == 'show':
        df_TV_Movie_TV1.iloc[i,11] = df_TV_Movie_TV1.iloc[i,11] +1
        df_TV_Movie_TV1.iloc[i,4] =  df_TV_Movie_TV1.iloc[i,4] + 1
        df_TV_Movie_TV1.iloc[i,17] = 'Yes'


# In[ ]:


#coverting to numeric adds a decimal point so removing the decimal value 
#so that while appending a PV it is not appended next to this decimal value 
df_TV_Movie_TV1['F2020'] = df_TV_Movie_TV1['F2020'].astype(str).apply(lambda x: x.replace('.0',''))
df_TV_Movie_TV1['S2021'] = df_TV_Movie_TV1['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[ ]:


df_TV_Movie_TV1['F2020']=df_TV_Movie_TV1['F2020'].str.replace('nan','')
df_TV_Movie_TV1['S2021']=df_TV_Movie_TV1['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


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


# In[ ]:


TV1concat=pd.concat(PTV1)


# In[ ]:


TV1concat['LastDigit_PV'] = TV1concat['F2020'].apply(lambda x: x[-1:])


# In[ ]:


#TV1concat['LastDigit_PV'] 


# In[ ]:


TV1concat['F2020_Updated']= TV1concat['S2021'] + TV1concat['LastDigit_PV']


# # TV1 One Wave

# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_TV1=dfOneW.query("cleantype=='TV1'")


# In[ ]:


df_TV1=[TV1concat,dfOneW_TV1]


# In[ ]:


df_TV1=pd.concat(df_TV1)


# In[ ]:


#display(df_TV1)


# In[ ]:


df_TV1= df_TV1.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


#df_TV1


# In[ ]:


#df1_TV1=df_TV1.query("cleantype=='TV1'")


# In[ ]:


#df_TV1.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV1concat.csv',header=True,index=False)


# In[ ]:


df1w_TV1=df_TV1.query("OneWave_Suppress=='#'")


# In[ ]:


dfnon1w_TV1=df_TV1.query("OneWave_Suppress!='#'")


# In[ ]:


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


# In[ ]:


df1w_TV1[['S2021']]=df1w_TV1[["S2021"]].apply(pd.to_numeric)
#df1w_TV1['Col2PV']=''


# In[ ]:


for i in range(len(df1w_TV1)):
    df1w_TV1.iloc[i,2] =  df1w_TV1.iloc[i,2] + 1
    df1w_TV1.iloc[i,34]='Yes'


# In[ ]:


df1w_TV1['S2021'] = df1w_TV1['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[ ]:


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


# In[ ]:


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


# In[ ]:


#dfonewave_TV1['1']


# In[ ]:


TV1onewave=pd.concat(TV1onewave)


# In[ ]:


TV1onewave['LastDigit_PV']=TV1onewave['S2021'].str.strip().str[-1]


# In[ ]:


TV1onewave['SDID']='0'


# In[ ]:


TV1onewave['UCode']='U0'


# In[ ]:


TV1onewave['StudyEntryID']='0'


# In[ ]:


TV1onewave['QUESTID']='0'
TV1onewave['QuestionID']='0'


# In[ ]:


#TV1onewave.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV1#.csv',index=False,header=True)


# In[ ]:


TV1=[dfnon1w_TV1,TV1onewave]


# In[ ]:


TV1=pd.concat(TV1)


# In[ ]:


TV1=TV1.sort_values(['Sec_List_Heading','LastDigit_PV', 'Col2PV'], 
               ascending=[True,
                          True,True])


# In[ ]:


TV1['Tmpl']=TV1['Tmpl'].fillna(method='ffill')


# In[ ]:


TV1['Super']=TV1['Super'].fillna(method='ffill')


# In[ ]:


TV1['Detail3']=TV1['Detail3'].fillna(method='ffill')


# In[ ]:


TV1=TV1.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])


# In[ ]:


TV1['Category']=TV1['Category'].fillna(method='ffill')


# In[ ]:


TV1['QLevel']=TV1['QLevel'].fillna(method='ffill')


# In[ ]:


TV1['UCode']=TV1['UCode'].fillna('U0')


# In[ ]:


#TV1['QUESTID']=TV1['QUESTID'].fillna(method='ffill')


# In[ ]:


#TV1['QuestionID']=TV1['QuestionID'].fillna(method='ffill')


# In[ ]:


TV1['VersionID']='0'


# In[ ]:


TV1['SID']='1857'


# In[ ]:


TV1['SDID']=TV1['SDID'].fillna('0')


# In[ ]:


TV1['Status']='Add'


# In[ ]:


TV1['StudyAnswerID']='0'


# In[ ]:


Listheading=TV1['Sec_List_Heading'].unique()


# In[ ]:


#TV1['Sec_List_Heading'].value_counts()


# In[ ]:


#LH={}
#for i in Listheading:
   # j=0
   # LH[j]=TV1.query('Sec_List_Heading=="i"')
   # print(LH[j].head(5))
    #df_TV_Movie.query('cleantype=="TV1"')
   # LH[j]=pd.DataFrame(LH[j])
   # j+=1


# In[ ]:


g=TV1.groupby('Sec_List_Heading')


# In[ ]:


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

# In[ ]:


n=0
for values in Listheading:
    TV1_LH[n]=TV1_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    TV1_LH[n]['Detail2']=TV1_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF    


# In[ ]:


#g.get_group('Monday Through Friday Programs')


# In[ ]:


#TV1_LH[8].head(5)


# In[ ]:


TV1Frames=[TV1_LH[0],TV1_LH[1],TV1_LH[2],TV1_LH[3],TV1_LH[4],TV1_LH[5],TV1_LH[6],TV1_LH[7],TV1_LH[8]]


# In[ ]:


TV1=pd.concat(TV1Frames)


# In[ ]:


TV1=TV1.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


TV1['Detail1']=TV1['Detail1'].fillna(TV1['Shows_Name']) 


# In[ ]:


TV1['Wave']=TV1['Wave'].fillna(TV1['Initial_Wave']) 


# In[ ]:


TV1['Wave']=TV1['Wave'].astype(str)


# In[ ]:


for i in range(len(TV1)):
        value=TV1.iloc[i,26]
        firstvalue=value[0]
        if firstvalue =='W':
                TV1.iloc[i,26]=value[1:]


# In[ ]:


TV1['QUESTID']=TV1['QUESTID'].fillna('0')


# In[ ]:


TV1['QuestionID']=TV1['QuestionID'].fillna('0')


# In[ ]:


TV1['QuestionID']=TV1['QuestionID'].fillna('0')
TV1['StudyEntryID']=TV1['StudyEntryID'].fillna('0')
TV1['AnswerID']=TV1['AnswerID'].fillna('0')


# In[ ]:


#condition=(TV1['compare']==False)


# In[ ]:


#values=['0']


# In[ ]:


TV1['Definition'] = TV1.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


#TV1.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV1.csv',index=False,header=True)


# # TV2

# In[ ]:


df_TV_Movie_TV2=df_TV_Movie.query('cleantype=="TV2" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_TV2['F2020']=df_TV_Movie_TV2['F2020'].str.replace('nan','')
df_TV_Movie_TV2['S2021']=df_TV_Movie_TV2['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


df_TV_Movie_TV2['F2020']=df_TV_Movie_TV2['F2020'].str.replace('nan','')
df_TV_Movie_TV2['S2021']=df_TV_Movie_TV2['S2021'].str.replace('nan','')
df_TV_Movie_TV2[['F2020']]=df_TV_Movie_TV2[["F2020"]].apply(pd.to_numeric)
df_TV_Movie_TV2[['S2021']]=df_TV_Movie_TV2[["S2021"]].apply(pd.to_numeric)


# In[ ]:


df_TV_Movie_TV2['Col2PV']=''


# In[ ]:


for i in range(len(df_TV_Movie_TV2)):
    type=df_TV_Movie_TV2.iloc[i,0]
    cleantype=df_TV_Movie_TV2.iloc[i,1]
    if type == 'show':
        df_TV_Movie_TV2.iloc[i,11] = df_TV_Movie_TV2.iloc[i,11] +1
        df_TV_Movie_TV2.iloc[i,4] =  df_TV_Movie_TV2.iloc[i,4] + 1
        df_TV_Movie_TV2.iloc[i,17] = 'Yes'
		


# In[ ]:


df_TV_Movie_TV2['F2020'] = df_TV_Movie_TV2['F2020'].astype(str).apply(lambda x: x.replace('.0',''))
df_TV_Movie_TV2['S2021'] = df_TV_Movie_TV2['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[ ]:


df_TV_Movie_TV2['F2020']=df_TV_Movie_TV2['F2020'].str.replace('nan','')
df_TV_Movie_TV2['S2021']=df_TV_Movie_TV2['S2021'].str.replace('nan','')


# In[ ]:


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
	


# In[ ]:


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


# In[ ]:


TV2concat=pd.concat(PTV2)


# In[ ]:


for i in range(len(TV2concat)):
        value=str(TV2concat.iloc[i,24])
        firstvalue=value[0]
        if firstvalue =='#':
                TV2concat.iloc[i,24]=value[1:]


# In[ ]:


#TV2concat['Detail1'].isnull().value_counts()


# In[ ]:


#TV2concat['Detail1'].nunique()


# In[ ]:


TV2concat['Detail1']=TV2concat['Detail1'].astype(str)
TV2concat['Detail1']=TV2concat['Detail1'].replace(r'nan',np.nan,regex=True)


# ^ is the beginning of string anchor.
# $ is the end of string anchor.
# \s is the whitespace character class.
# * is zero-or-more repetition of.

# In[ ]:


#TV2concat['Detail1'].isna().value_counts()


# In[ ]:


#TV2concat['Detail1']


# In[ ]:


#TV2concat['Detail1'].isna().value_counts()


# In[ ]:


TV2concat['Detail1']=TV2concat['Detail1'].fillna(TV2concat['Shows_Name']) 


# In[ ]:


TV2concat['Detail1']=TV2concat['Detail1'].astype(str)


# In[ ]:


for i in range(len(TV2concat)):
        value=str(TV2concat.iloc[i,24])
        firstvalue=value[0]
        if value[0] =='#':
                TV2concat.iloc[i,24]=value[1:]


# In[ ]:


#TV2concat.Detail1


# In[ ]:


#TV2concat['Tmpl'].isna().value_counts()


# In[ ]:


TV2concat['Tmpl']=TV2concat['Tmpl'].fillna('2')


# In[ ]:


#TV2concat['Tmpl'].value_counts()


# In[ ]:


TV2concat['LastDigit_PV'] = TV2concat['F2020'].apply(lambda x: x[-1:])


# In[ ]:


TV2concat['F2020_Updated']= TV2concat['S2021'] + TV2concat['LastDigit_PV']


# # TV2 One Wave

# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_TV2=dfOneW.query("cleantype=='TV2'")


# In[ ]:


df_TV2=[TV2concat,dfOneW_TV2]


# In[ ]:


df_TV2=pd.concat(df_TV2)


# In[ ]:



df_TV2= df_TV2.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


df1w_TV2=df_TV2.query("OneWave_Suppress=='#'")


# In[ ]:


#df1w_TV2.head(5)


# In[ ]:


dfnon1w_TV2=df_TV2.query("OneWave_Suppress!='#'")


# In[ ]:


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


# In[ ]:


df1w_TV2[['S2021']]=df1w_TV2[["S2021"]].apply(pd.to_numeric)


# In[ ]:



for i in range(len(df1w_TV2)):
    df1w_TV2.iloc[i,2] =  df1w_TV2.iloc[i,2] + 1
    df1w_TV2.iloc[i,34]='Yes'


# In[ ]:


df1w_TV2['S2021'] = df1w_TV2['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[ ]:


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
	


# In[ ]:


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


# In[ ]:


TV2onewave=pd.concat(TV2onewave)


# In[ ]:


TV2onewave['LastDigit_PV']=TV2onewave['S2021'].str.strip().str[-1]


# In[ ]:


TV2onewave['SDID']='0'

TV2onewave['UCode']='U0'
TV2onewave['StudyEntryID']='0'


# In[ ]:


TV2onewave['QUESTID']='0'
TV2onewave['QuestionID']='0'
TV2onewave['Tmpl']='2'


# In[ ]:


#TV2onewave.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV2#.csv',index=False,header=True)


# In[ ]:


TV2=[dfnon1w_TV2,TV2onewave]


# In[ ]:


TV2=pd.concat(TV2)


# In[ ]:


#TV2['Tmpl'].nunique()


# In[ ]:


TV2['Tmpl']=TV2['Tmpl'].astype(str)


# In[ ]:


#TV2['Tmpl'].unique()


# In[ ]:


#TV2['Tmpl'].value_counts()


# In[ ]:


TV2['Tmpl']=TV2['Tmpl'].str.replace('.0',"",regex=True)


# In[ ]:


#TV2['Tmpl']=TV2['Tmpl'].str.replace(r'nan',np.nan,regex=True)


# In[ ]:


TV2_tmpl3=TV2.query('Tmpl=="3"')


# In[ ]:


TV2_tmpl2=TV2.query('Tmpl!="3"')


# In[ ]:


TV2=TV2_tmpl2.copy()


# In[ ]:


TV2=TV2.sort_values(['LastDigit_PV', 'Col2PV'], 
               ascending=[True,
                          True])
						  
#TV2['Tmpl']='2'


# In[ ]:


TV2['Super']=TV2['Super'].fillna(method='ffill')
TV2['Detail3']=TV2['Detail3'].fillna(method='ffill')


# In[ ]:


TV2=TV2.sort_values(['Sec_List_Heading', 'LastDigit_PV', 'Col2PV','Tmpl'], 
               ascending=[True,
                          True,True,True])
TV2['Category']=TV2['Category'].fillna(method='ffill')

#TV2['QUESTID']=TV2['QUESTID'].fillna(method='ffill')
#TV2['QuestionID']=TV2['QuestionID'].fillna(method='ffill')


# In[ ]:


TV2['QLevel']=TV2['QLevel'].fillna(method='ffill')
TV2['Tmpl']=TV2['Tmpl'].fillna(method='ffill')


# In[ ]:


#TV2onewave=TV2.query('OneWave_Suppress=="#"')


# In[ ]:


#TV2non_onewave=TV2.query('OneWave_Suppress!="#"')


# In[ ]:


#TV2onewave['Category']=TV2onewave['Category'].str.replace(r'- Net', '', regex=True)


# In[ ]:


#TV2=[TV2non_onewave,TV2onewave]


# In[ ]:


#TV2=pd.concat(TV2)


# In[ ]:


TV2['VersionID']='0'
TV2['SID']='1857'
TV2['Status']='Add'
TV2['StudyAnswerID']='0'


# In[ ]:


Listheading=TV2['Sec_List_Heading'].unique()
g=TV2.groupby('Sec_List_Heading')



# In[ ]:


i=0
n=0
TV2_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    TV2_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[ ]:


n=0
for values in Listheading:
    TV2_LH[n]=TV2_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    TV2_LH[n]['Detail2']=TV2_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF    


# In[ ]:


TV2Frames=[TV2_LH[0],TV2_LH[1],TV2_LH[2],TV2_LH[3]]

TV2=pd.concat(TV2Frames)


# In[ ]:


TV2=TV2.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


TV2['Detail1']=TV2['Detail1'].fillna(TV2['Shows_Name']) 


# In[ ]:


TV2['Wave']=TV2['Wave'].fillna(TV2['Initial_Wave']) 


# In[ ]:


TV2['Wave']=TV2['Wave'].astype(str)


# In[ ]:


TV2['Wave']=TV2['Wave'].replace(r'W', '', regex=True)


# In[ ]:


TV2['Wave']=TV2['Wave'].replace(r'nan', np.nan, regex=True)


# In[ ]:


#TV2['Wave'].isna().value_counts()


# In[ ]:


TV2['Wave']=TV2['Wave'].fillna('0')


# In[ ]:


TV2['Definition'] = TV2.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


#TV2['Category'] = TV2.apply(lambda x:x['Category'].replace(r'- Net','',regex=True)  if x['OneWave_Suppress']=='#' else x['Category'], axis=1)
#replace(r'nan', np.nan, regex=True)


# In[ ]:


TV2['UCode']=TV2['UCode'].fillna('U0')
TV2['StudyEntryID']=TV2['StudyEntryID'].fillna('0')
TV2['UCode']=TV2['UCode'].fillna('U0')
TV2['QuestionID']=TV2['QuestionID'].fillna('0')
TV2['QUESTID']=TV2['QUESTID'].fillna('0')
TV2['AnswerID']=TV2['AnswerID'].fillna('0')


# In[ ]:


#TV2['Tmpl']=TV2['Tmpl'].fillna('2')


# In[ ]:


TV2=[TV2,TV2_tmpl3]


# In[ ]:


TV2=pd.concat(TV2)


# In[ ]:


TV2['VersionID']='0'
TV2['SID']='1857'
TV2['Status']='Add'
TV2['StudyAnswerID']='0'
#TV2['Tmpl']=TV2['Tmpl'].fillna('2')
TV2['SDID']=TV2['SDID'].fillna('0')


# In[ ]:


TV2['Definition'] = TV2.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


TV2=TV2.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


#TV2


# In[ ]:


#TV2.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV2.csv',index=False,header=True)


# # SPTV1

# In[ ]:


# col1 x,1,2,3,4,5,6 no col 2 values


# In[ ]:


df_TV_Movie_SPTV1=df_TV_Movie.query('cleantype=="SPTV1" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_SPTV1['F2020']=df_TV_Movie_SPTV1['F2020'].str.replace('nan','')
df_TV_Movie_SPTV1['S2021']=df_TV_Movie_SPTV1['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


PSPTV1= [  df_inner_PV_SPTV1['1'],
           df_inner_PV_SPTV1['2'], 
           df_inner_PV_SPTV1['3'], 
           df_inner_PV_SPTV1['4'],
           df_inner_PV_SPTV1['5'],
           df_inner_PV_SPTV1['6'],
           df_inner_PV_SPTV1['x'],
        ]


# In[ ]:


SPTV1concat=pd.concat(PSPTV1)


# In[ ]:


#SPTV1concat['Shows_Name'].value_counts()


# In[ ]:


SPTV1concat['LastDigit_PV'] = SPTV1concat['F2020'].apply(lambda x: x[-1:])


# In[ ]:


SPTV1concat['F2020_Updated']=SPTV1concat['S2021']+SPTV1concat['LastDigit_PV']


# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_SPTV1=dfOneW.query("cleantype=='SPTV1'")


# In[ ]:


df_SPTV1=[SPTV1concat,dfOneW_SPTV1]


# In[ ]:


df_SPTV1=pd.concat(df_SPTV1)


# In[ ]:


df_SPTV1= df_SPTV1.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


df1w_SPTV1=df_SPTV1.query("OneWave_Suppress=='#'")


# In[ ]:


dfnon1w_SPTV1=df_SPTV1.query("OneWave_Suppress!='#'")


# In[ ]:


onewave_SPTV1={}
dfonewave_SPTV1={}


# In[ ]:


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


# In[ ]:


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


# In[ ]:



SPTV1onewave=pd.concat(SPTV1onewave)


# In[ ]:


SPTV1onewave['LastDigit_PV']=SPTV1onewave['S2021'].str.strip().str[-1]


# In[ ]:


SPTV1onewave['F2020_Updated']=SPTV1onewave['S2021']


# In[ ]:


SPTV1onewave['SDID']='0'

SPTV1onewave['UCode']='U0'
SPTV1onewave['StudyEntryID']='0'


# In[ ]:


SPTV1onewave['QUESTID']='0'
SPTV1onewave['QuestionID']='0'


# In[ ]:


#SPTV1onewave.head(5)


# In[ ]:


#SPTV1onewave.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV1#.csv',index=False,header=True,encoding='cp1252')


# In[ ]:


SPTV1=[dfnon1w_SPTV1,SPTV1onewave]


# In[ ]:


SPTV1=pd.concat(SPTV1)


# In[ ]:


#SPTV1['Shows_Name']=SPTV1['Shows_Name'].astype(str)


# In[ ]:


SPTV1=SPTV1.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
SPTV1['Tmpl']=SPTV1['Tmpl'].fillna(method='ffill')
SPTV1['Super']=SPTV1['Super'].fillna(method='ffill')
SPTV1['Detail3']=SPTV1['Detail3'].fillna(method='ffill')


# In[ ]:


SPTV1=SPTV1.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])

SPTV1['QLevel']=SPTV1['QLevel'].fillna(method='ffill')


# In[ ]:


SPTV1['VersionID']='0'
SPTV1['SID']='1857'
SPTV1['Status']='Add'
SPTV1['StudyAnswerID']='0'


# In[ ]:


Listheading=SPTV1['Sec_List_Heading'].unique()
g=SPTV1.groupby('Sec_List_Heading')


# In[ ]:


i=0
n=0
SPTV1_LH={}
for Sec_List_Heading, g_df in g:
    print (Sec_List_Heading)
    SPTV1_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[ ]:


n=0
for values in Listheading:
    SPTV1_LH[n]=SPTV1_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[False
                        ])
    SPTV1_LH[n]['Detail2']=SPTV1_LH[n]['Detail2'].fillna(method='ffill')
    SPTV1['Category']="Spanish Television: "+SPTV1['Sec_List_Heading']
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[ ]:


n


# In[ ]:


SPTV1Frames=pd.DataFrame()
SPTV1Frames = SPTV1Frames.append([SPTV1_LH[i] for i in range(n)])


# In[ ]:


#SPTV1=pd.concat(SPTV1Frames)


# In[ ]:


SPTV1['Detail1']=SPTV1['Detail1'].fillna(SPTV1['Shows_Name'])


# In[ ]:


SPTV1['Wave']=SPTV1['Wave'].fillna(SPTV1['Initial_Wave']) 
SPTV1['Wave']=SPTV1['Wave'].astype(str)
SPTV1['Wave']=SPTV1['Wave'].replace(r'W', '', regex=True)
SPTV1['Wave']=SPTV1['Wave'].replace(r'nan', np.nan, regex=True)
#SPTV1['Wave'].isna().value_counts()
SPTV1['Wave']=SPTV1['Wave'].fillna('0')
SPTV1['SDID']=SPTV1['SDID'].fillna('0')
SPTV1['Definition'] = SPTV1.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


SPTV1['UCode']=SPTV1['UCode'].fillna('U0')
SPTV1['StudyEntryID']=SPTV1['StudyEntryID'].fillna('0')
SPTV1['UCode']=SPTV1['UCode'].fillna('U0')
SPTV1['QuestionID']=SPTV1['QuestionID'].fillna('0')
SPTV1['QUESTID']=SPTV1['QUESTID'].fillna('0')
SPTV1['AnswerID']=SPTV1['AnswerID'].fillna('0')


# In[ ]:


SPTV1=SPTV1.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:



#SPTV1.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV1.csv',index=False,header=True,encoding='cp1252')


# # SPTV4

# In[ ]:


#No col2 value only 6 in col1


# In[ ]:


df_TV_Movie_SPTV4=df_TV_Movie.query('cleantype=="SPTV4" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_SPTV4['F2020']=df_TV_Movie_SPTV4['F2020'].str.replace('nan','')
df_TV_Movie_SPTV4['S2021']=df_TV_Movie_SPTV4['S2021'].str.replace('nan','')


# In[ ]:


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
	


# In[ ]:


df_TV_Movie_SPTV4['F2020']=df_TV_Movie_SPTV4['F2020'].str.replace('nan','')
df_TV_Movie_SPTV4['S2021']=df_TV_Movie_SPTV4['S2021'].str.replace('nan','')
df_TV_Movie_SPTV4[['F2020']]=df_TV_Movie_SPTV4[["F2020"]].apply(pd.to_numeric)
df_TV_Movie_SPTV4[['S2021']]=df_TV_Movie_SPTV4[["S2021"]].apply(pd.to_numeric)


# In[ ]:



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


# In[ ]:


SPTV4concat=pd.concat(PSPTV4)


# In[ ]:


#SPTV4concat['Shows_Name'].value_counts()


# In[ ]:


SPTV4concat['LastDigit_PV'] = SPTV4concat['F2020'].apply(lambda x: x[-1:])


# In[ ]:


SPTV4concat['F2020_Updated']=SPTV4concat['S2021']+SPTV4concat['LastDigit_PV']


# In[ ]:


SPTV4concat['Detail1']=SPTV4concat['Detail1'].astype(str)

for i in range(len(SPTV4concat)):
        value=SPTV4concat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                SPTV4concat.iloc[i,24]=value[1:]


# # SPTV4 Onewave

# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_SPTV4=dfOneW.query("cleantype=='SPTV4'")


# In[ ]:


df_SPTV4=[SPTV4concat,dfOneW_SPTV4]


# In[ ]:


df_SPTV4=pd.concat(df_SPTV4)


# In[ ]:


df_SPTV4= df_SPTV4.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


df1w_SPTV4=df_SPTV4.query("OneWave_Suppress=='#'")


# In[ ]:


dfnon1w_SPTV4=df_SPTV4.query("OneWave_Suppress!='#'")


# In[ ]:


#dfnon1w_SPTV4['Shows_Name'].value_counts()


# In[ ]:


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


# In[ ]:


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


# In[ ]:



SPTV4onewave=pd.concat(SPTV4onewave)


# In[ ]:


SPTV4onewave['LastDigit_PV']=SPTV4onewave['S2021'].str.strip().str[-1]


# In[ ]:



SPTV4onewave['F2020_Updated']=SPTV4onewave['S2021']


# In[ ]:


SPTV4onewave['SDID']='0'

SPTV4onewave['UCode']='U0'
SPTV4onewave['StudyEntryID']='0'


# In[ ]:


SPTV4onewave['QUESTID']='0'
SPTV4onewave['QuestionID']='0'


# In[ ]:


#SPTV4onewave.head(5)


# In[ ]:



SPTV4onewave.to_csv('SPTV4#.csv',index=False,header=True)


# In[ ]:


#SPTV4onewave['Shows_Name'].value_counts()


# In[ ]:



SPTV4=[dfnon1w_SPTV4,SPTV4onewave]


# In[ ]:



SPTV4=pd.concat(SPTV4)


# In[ ]:


#SPTV4['Shows_Name'].value_counts()


# In[ ]:


SPTV4=SPTV4.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
SPTV4['Tmpl']=SPTV4['Tmpl'].fillna(method='ffill')
SPTV4['Super']=SPTV4['Super'].fillna(method='ffill')
SPTV4['Detail3']=SPTV4['Detail3'].fillna(method='ffill')


# In[ ]:



SPTV4=SPTV4.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
SPTV4['Category']=SPTV4['Category'].fillna(method='ffill')
SPTV4['QLevel']=SPTV4['QLevel'].fillna(method='ffill')


# In[ ]:


SPTV4['VersionID']='0'
SPTV4['SID']='1857'
SPTV4['Status']='Add'
SPTV4['StudyAnswerID']='0'


# In[ ]:


SPTV4['Detail1']=SPTV4['Detail1'].fillna(SPTV4['Shows_Name'])


# In[ ]:


SPTV4['Wave']=SPTV4['Wave'].fillna(SPTV4['Initial_Wave']) 
SPTV4['Wave']=SPTV4['Wave'].astype(str)
SPTV4['Wave']=SPTV4['Wave'].replace(r'W', '', regex=True)
SPTV4['Wave']=SPTV4['Wave'].replace(r'nan', np.nan, regex=True)
#SPTV4['Wave'].isna().value_counts()
SPTV4['Wave']=SPTV4['Wave'].fillna('0')
SPTV4['SDID']=SPTV4['SDID'].fillna('0')
SPTV4['Definition'] = SPTV4.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:



SPTV4['UCode']=SPTV4['UCode'].fillna('U0')
SPTV4['StudyEntryID']=SPTV4['StudyEntryID'].fillna('0')
SPTV4['UCode']=SPTV4['UCode'].fillna('U0')
SPTV4['QuestionID']=SPTV4['QuestionID'].fillna('0')
SPTV4['QUESTID']=SPTV4['QUESTID'].fillna('0')
SPTV4['AnswerID']=SPTV4['AnswerID'].fillna('0')


# In[ ]:


#SPTV4=SPTV4.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:



SPTV4=SPTV4.sort_values(['S2021' ], ascending=[True])


# In[ ]:


#SPTV4.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV4.csv',index=False,header=True,encoding='utf8')


# # SPTV3

# In[ ]:


#no col 2 col1 6, x, 1 ,2, 3, 4


# In[ ]:


df_TV_Movie_SPTV3=df_TV_Movie.query('cleantype=="SPTV3" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_SPTV3['F2020']=df_TV_Movie_SPTV3['F2020'].str.replace('nan','')
df_TV_Movie_SPTV3['S2021']=df_TV_Movie_SPTV3['S2021'].str.replace('nan','')


# In[ ]:


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
	


# In[ ]:


PSPTV3= [#df_inner_PV_SPTV3['0'],
           df_inner_PV_SPTV3['1'],
           df_inner_PV_SPTV3['2'], 
           df_inner_PV_SPTV3['3'], 
           df_inner_PV_SPTV3['4'],
           
           df_inner_PV_SPTV3['6'],
           
           df_inner_PV_SPTV3['x'],
           
          ]


# In[ ]:


SPTV3concat=pd.concat(PSPTV3)


# In[ ]:


SPTV3concat['LastDigit_PV'] = SPTV3concat['F2020'].apply(lambda x: x[-1])


# In[ ]:



SPTV3concat['F2020_Updated']=SPTV3concat['S2021']+SPTV3concat['LastDigit_PV']


# In[ ]:


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

# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_SPTV3=dfOneW.query("cleantype=='SPTV3'")


# In[ ]:


df_SPTV3=[SPTV3concat,dfOneW_SPTV3]


# In[ ]:


df_SPTV3=pd.concat(df_SPTV3)


# In[ ]:


#df_SPTV3


# In[ ]:


df_SPTV3= df_SPTV3.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


df1w_SPTV3=df_SPTV3.query("OneWave_Suppress=='#'")


# In[ ]:


dfnon1w_SPTV3=df_SPTV3.query("OneWave_Suppress!='#'")


# In[ ]:


#dfnon1w_SPTV3


# In[ ]:


#df1w_SPTV3.info()


# In[ ]:


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


# In[ ]:


SPTV3onewave= [
           dfonewave_SPTV3['1'],
           dfonewave_SPTV3['2'], 
           dfonewave_SPTV3['3'], 
           dfonewave_SPTV3['4'],
           #dfonewave_SPTV3['5'],
           dfonewave_SPTV3['6'],
          
           dfonewave_SPTV3['x'],
           
          ]


# In[ ]:


SPTV3onewave=pd.concat(SPTV3onewave)


# In[ ]:


SPTV3onewave['LastDigit_PV']=SPTV3onewave['S2021'].str.strip().str[-1]


# In[ ]:


SPTV3onewave['F2020_Updated']=SPTV3onewave['S2021']


# In[ ]:


SPTV3onewave['SDID']='0'

SPTV3onewave['UCode']='U0'
SPTV3onewave['StudyEntryID']='0'


# In[ ]:


#SPTV3onewave.head(5)
SPTV3onewave['QUESTID']='0'
SPTV3onewave['QuestionID']='0'


# In[ ]:


SPTV3onewave.to_csv('SPTV3#.csv',index=False,header=True)


# In[ ]:


SPTV3=[dfnon1w_SPTV3,SPTV3onewave]


# In[ ]:


SPTV3=pd.concat(SPTV3)


# In[ ]:


#SPTV3


# In[ ]:


SPTV3=SPTV3.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
SPTV3['Tmpl']=SPTV3['Tmpl'].fillna(method='ffill')
SPTV3['Super']=SPTV3['Super'].fillna(method='ffill')
SPTV3['Detail3']=SPTV3['Detail3'].fillna(method='ffill')


# In[ ]:


SPTV3=SPTV3.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
SPTV3['Category']=SPTV3['Category'].fillna(method='ffill')
SPTV3['QLevel']=SPTV3['QLevel'].fillna(method='ffill')


# In[ ]:


SPTV3['VersionID']='0'
SPTV3['SID']='1857'
SPTV3['Status']='Add'
SPTV3['StudyAnswerID']='0'


# In[ ]:


SPTV3['Detail1']=SPTV3['Detail1'].fillna(SPTV3['Shows_Name'])


# In[ ]:


SPTV3['Wave']=SPTV3['Wave'].fillna(SPTV3['Initial_Wave']) 
SPTV3['Wave']=SPTV3['Wave'].astype(str)
SPTV3['Wave']=SPTV3['Wave'].replace(r'W', '', regex=True)
SPTV3['Wave']=SPTV3['Wave'].replace(r'nan', np.nan, regex=True)
#SPTV3['Wave'].isna().value_counts()
SPTV3['Wave']=SPTV3['Wave'].fillna('0')
SPTV3['SDID']=SPTV3['SDID'].fillna('0')
#SPTV3['Definition'] = SPTV3.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


#SPTV3


# In[ ]:


#SPTV3['UCode'] = SPTV3.apply(lambda x: 'U0'  if x['UCode']==0 else x['UCode'], axis=1)


# In[ ]:


#SPTV3['UCode']=SPTV3['UCode'].fillna('U0')
SPTV3['StudyEntryID']=SPTV3['StudyEntryID'].fillna('0')
SPTV3['UCode']=SPTV3['UCode'].fillna('U0')
#SPTV3['QuestionID']=SPTV3['QuestionID'].fillna('0')
#SPTV3['QUESTID']=SPTV3['QUESTID'].fillna('0')
SPTV3['AnswerID']=SPTV3['AnswerID'].fillna('0')


# In[ ]:


#SPTV3


# In[ ]:


#SPTV3['Definition'] = SPTV3.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


SPTV3['Definition'] ='0'
#all values are false in compare


# In[ ]:


#SPTV3=SPTV3.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


##SPTV3.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV3.csv',index=False,header=True,encoding='cp1252')


# # SPTV5.1

# In[ ]:


# col1 ,6 col2 -no values


# In[ ]:


df_TV_Movie_SPTV51=df_TV_Movie.query('cleantype=="SPTV5.1" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_SPTV51['F2020']=df_TV_Movie_SPTV51['F2020'].str.replace('nan','')
df_TV_Movie_SPTV51['S2021']=df_TV_Movie_SPTV51['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


PSPTV51= [#df_inner_PV_SPTV51['0'],
           #df_inner_PV_SPTV51['1'],
           #df_inner_PV_SPTV51['2'], 
           #df_inner_PV_SPTV51['3'], 
           #df_inner_PV_SPTV51['4'],
           #df_inner_PV_SPTV51['5'],
           df_inner_PV_SPTV51['6'],
           
          ]


# In[ ]:


SPTV51concat=pd.concat(PSPTV51)


# In[ ]:


SPTV51concat['LastDigit_PV'] = SPTV51concat['F2020'].apply(lambda x: x[-1])


# In[ ]:


SPTV51concat['F2020_Updated']=SPTV51concat['S2021']+SPTV51concat['LastDigit_PV']


# In[ ]:


SPTV51concat['Detail1']=SPTV51concat['Detail1'].astype(str)

for i in range(len(SPTV51concat)):
        value=SPTV51concat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                SPTV51concat.iloc[i,24]=value[1:]


# # SPTV5.1 One wave

# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_SPTV51=dfOneW.query("cleantype=='SPTV5.1'")


# In[ ]:


df_SPTV51=[SPTV51concat,dfOneW_SPTV51]


# In[ ]:


df_SPTV51=pd.concat(df_SPTV51)


# In[ ]:


df_SPTV51= df_SPTV51.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


df1w_SPTV51=df_SPTV51.query("OneWave_Suppress=='#'")


# In[ ]:


dfnon1w_SPTV51=df_SPTV51.query("OneWave_Suppress!='#'")


# In[ ]:


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


# In[ ]:


SPTV51onewave= [
          #dfonewave_SPTV51['1'],
           #dfonewave_SPTV51['5'],
           dfonewave_SPTV51['6'],
		  #dfonewave_SPTV51['4'],
           ]


# In[ ]:


SPTV51onewave=pd.concat(SPTV51onewave)


# In[ ]:


SPTV51onewave['LastDigit_PV']=SPTV51onewave['S2021'].str.strip().str[-1]


# In[ ]:


SPTV51onewave['F2020_Updated']=SPTV51onewave['S2021']


# In[ ]:


SPTV51onewave['SDID']='0'

SPTV51onewave['UCode']='U0'
SPTV51onewave['StudyEntryID']='0'


# In[ ]:


SPTV51onewave['QUESTID']='0'
SPTV51onewave['QuestionID']='0'


# In[ ]:


SPTV51onewave.to_csv('SPTV51#.csv',index=False,header=True)


# In[ ]:


SPTV51=[dfnon1w_SPTV51,SPTV51onewave]


# In[ ]:


SPTV51=pd.concat(SPTV51)


# In[ ]:


SPTV51=SPTV51.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
SPTV51['Tmpl']=SPTV51['Tmpl'].fillna(method='ffill')
SPTV51['Super']=SPTV51['Super'].fillna(method='ffill')
SPTV51['Detail3']=SPTV51['Detail3'].fillna(method='ffill')


# In[ ]:


SPTV51=SPTV51.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
SPTV51['Category']=SPTV51['Category'].fillna(method='ffill')
SPTV51['QLevel']=SPTV51['QLevel'].fillna(method='ffill')


# In[ ]:


SPTV51['VersionID']='0'
SPTV51['SID']='1857'
SPTV51['Status']='Add'
SPTV51['StudyAnswerID']='0'


# In[ ]:


SPTV51['Detail1']=SPTV51['Detail1'].replace(r'nan', np.nan, regex=True)


# In[ ]:


#SPTV1['Detail1']=SPTV1['Detail1'].replace(r'nan', np.nan, regex=True)

SPTV51['Detail1']=SPTV51['Detail1'].fillna(SPTV51['Shows_Name'])

SPTV51['Wave']=SPTV51['Wave'].fillna(SPTV51['Initial_Wave']) 

#SPTV51['Wave'].isna().value_counts()


# In[ ]:


SPTV51['Wave']=SPTV51['Wave'].astype(str)
SPTV51['Wave']=SPTV51['Wave'].replace(r'W', '', regex=True)
SPTV51['Wave']=SPTV51['Wave'].replace(r'nan', np.nan, regex=True)


# In[ ]:


SPTV51['Wave']=SPTV51['Wave'].fillna('0')
SPTV51['SDID']=SPTV51['SDID'].fillna('0')
SPTV51['Definition'] = SPTV51.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


SPTV51['UCode']=SPTV51['UCode'].fillna('U0')
SPTV51['StudyEntryID']=SPTV51['StudyEntryID'].fillna('0')
SPTV51['UCode']=SPTV51['UCode'].fillna('U0')


# In[ ]:


SPTV51['QuestionID']=SPTV51['QuestionID'].fillna('0')
SPTV51['QUESTID']=SPTV51['QUESTID'].fillna('0')
SPTV51['AnswerID']=SPTV51['AnswerID'].fillna('0')


# In[ ]:


SPTV51=SPTV51.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


#SPTV51.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV5.1.csv',index=False,header=True,encoding='cp1252')


# # SPTV5

# In[ ]:


# No one wave items and no col2 items only 6 in col1 PV


# In[ ]:


df_TV_Movie_SPTV5=df_TV_Movie.query('cleantype=="SPTV5" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_SPTV5['F2020']=df_TV_Movie_SPTV5['F2020'].str.replace('nan','')
df_TV_Movie_SPTV5['S2021']=df_TV_Movie_SPTV5['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


SPTV5= [ df_inner_PV_SPTV5['6']]


# In[ ]:


SPTV5=pd.concat(SPTV5)


# In[ ]:


SPTV5['LastDigit_PV'] = SPTV5['F2020'].apply(lambda x: x[-1])


# In[ ]:


SPTV5['F2020_Updated']=SPTV5['S2021']+SPTV5['LastDigit_PV']


# In[ ]:


SPTV5['Detail1']=SPTV5['Detail1'].astype(str)

for i in range(len(SPTV5)):
        value=SPTV5.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                SPTV5.iloc[i,24]=value[1:]


# In[ ]:


SPTV5=SPTV5.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
SPTV5['Tmpl']=SPTV5['Tmpl'].fillna(method='ffill')
SPTV5['Super']=SPTV5['Super'].fillna(method='ffill')
SPTV5['Detail3']=SPTV5['Detail3'].fillna(method='ffill')


# In[ ]:


SPTV5=SPTV5.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
SPTV5['Category']=SPTV5['Category'].fillna(method='ffill')
SPTV5['QLevel']=SPTV5['QLevel'].fillna(method='ffill')
#SPTV5['QUESTID']=SPTV5['QUESTID'].fillna(method='ffill')
#SPTV5['QuestionID']=SPTV5['QuestionID'].fillna(method='ffill')


# In[ ]:


SPTV5['VersionID']='0'
SPTV5['SID']='1857'
SPTV5['Status']='Add'
SPTV5['StudyAnswerID']='0'


# In[ ]:


SPTV5['Detail1']=SPTV5['Detail1'].replace(r'nan', np.nan, regex=True)

SPTV5['Detail1']=SPTV5['Detail1'].fillna(SPTV5['Shows_Name'])


# In[ ]:


SPTV5['Wave']=SPTV5['Wave'].fillna(SPTV5['Initial_Wave']) 
SPTV5['Wave']=SPTV5['Wave'].astype(str)
SPTV5['Wave']=SPTV5['Wave'].replace(r'W', '', regex=True)
SPTV5['Wave']=SPTV5['Wave'].replace(r'nan', np.nan, regex=True)
#SPTV5['Wave'].isna().value_counts()
SPTV5['Wave']=SPTV5['Wave'].fillna('0')
SPTV5['SDID']=SPTV5['SDID'].fillna('0')
SPTV5['Definition'] = SPTV5.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


SPTV5['UCode']=SPTV5['UCode'].fillna('U0')
SPTV5['StudyEntryID']=SPTV5['StudyEntryID'].fillna('0')
SPTV5['UCode']=SPTV5['UCode'].fillna('U0')
SPTV5['QuestionID']=SPTV5['QuestionID'].fillna('0')
SPTV5['QUESTID']=SPTV5['QUESTID'].fillna('0')
SPTV5['AnswerID']=SPTV5['AnswerID'].fillna('0')


# In[ ]:


SPTV5['Shows_Name']=SPTV5['Sec_List_Heading'] +":" + " "+ SPTV5['Shows_Name']


# In[ ]:


#SPTV5.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV5.csv',index=False,header=True)


# # SPTV2

# In[ ]:


#col1 -X,1,2,3,4,6


# In[ ]:


df_TV_Movie_SPTV2=df_TV_Movie.query('cleantype=="SPTV2" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_SPTV2['F2020']=df_TV_Movie_SPTV2['F2020'].str.replace('nan','')
df_TV_Movie_SPTV2['S2021']=df_TV_Movie_SPTV2['S2021'].str.replace('nan','')


# In[ ]:


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
	


# In[ ]:


PSPTV2= [df_inner_PV_SPTV2['x'],
        #df_inner_PV_SPTV2['0'],
           df_inner_PV_SPTV2['1'],
           df_inner_PV_SPTV2['2'], 
           df_inner_PV_SPTV2['3'], 
           df_inner_PV_SPTV2['4'],
           
           df_inner_PV_SPTV2['6'],
           
          ]


# In[ ]:


SPTV2concat=pd.concat(PSPTV2)


# In[ ]:


SPTV2concat['LastDigit_PV'] = SPTV2concat['F2020'].apply(lambda x: x[-1])


# In[ ]:


SPTV2concat['F2020_Updated']=SPTV2concat['S2021']+SPTV2concat['LastDigit_PV']


# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_SPTV2=dfOneW.query("cleantype=='SPTV2'")


# In[ ]:


#No one wave items


# In[ ]:


SPTV2=SPTV2concat.copy()


# In[ ]:


SPTV2=SPTV2.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
 
SPTV2['Tmpl']=SPTV2['Tmpl'].fillna(method='ffill')
SPTV2['Super']=SPTV2['Super'].fillna(method='ffill')
SPTV2['Detail3']=SPTV2['Detail3'].fillna(method='ffill')


# In[ ]:


SPTV2=SPTV2.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
SPTV2['Category']=SPTV2['Category'].fillna(method='ffill')
SPTV2['QLevel']=SPTV2['QLevel'].fillna(method='ffill')


# In[ ]:


SPTV2['VersionID']='0'
SPTV2['SID']='1857'
SPTV2['Status']='Add'
SPTV2['StudyAnswerID']='0'


# In[ ]:


SPTV2['Definition'] = SPTV2.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


SPTV2=SPTV2.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


#SPTV2.to_csv(r'C:\Users\saraswathy.rajaman\Documents\SPTV2.csv',index=False,header=True,encoding='cp1252')


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

# In[ ]:


df_TV_Movie_TV3=df_TV_Movie.query('cleantype=="TV3" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_TV3['F2020']=df_TV_Movie_TV3['F2020'].str.replace('nan','')
df_TV_Movie_TV3['S2021']=df_TV_Movie_TV3['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


df_TV_Movie_TV3['F2020']=df_TV_Movie_TV3['F2020'].str.replace('nan','')
df_TV_Movie_TV3['S2021']=df_TV_Movie_TV3['S2021'].str.replace('nan','')
df_TV_Movie_TV3[['F2020']]=df_TV_Movie_TV3[["F2020"]].apply(pd.to_numeric)
df_TV_Movie_TV3[['S2021']]=df_TV_Movie_TV3[["S2021"]].apply(pd.to_numeric)


# In[ ]:


df_TV_Movie_TV3['Col2PV']=''


# In[ ]:


for i in range(len(df_TV_Movie_TV3)):
    type=df_TV_Movie_TV3.iloc[i,0]
    cleantype=df_TV_Movie_TV3.iloc[i,1]
    if type == 'show':
        df_TV_Movie_TV3.iloc[i,11] = df_TV_Movie_TV3.iloc[i,11] +1
        df_TV_Movie_TV3.iloc[i,4] =  df_TV_Movie_TV3.iloc[i,4] + 1
        df_TV_Movie_TV3.iloc[i,17] = 'Yes'


# In[ ]:


df_TV_Movie_TV3['F2020'] = df_TV_Movie_TV3['F2020'].astype(str).apply(lambda x: x.replace('.0',''))
df_TV_Movie_TV3['S2021'] = df_TV_Movie_TV3['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[ ]:


df_TV_Movie_TV3['F2020']=df_TV_Movie_TV3['F2020'].str.replace('nan','')
df_TV_Movie_TV3['S2021']=df_TV_Movie_TV3['S2021'].str.replace('nan','')


# In[ ]:


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
	


# In[ ]:


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
		  


# In[ ]:


TV3concat=pd.concat(PTV3)


# In[ ]:


for i in range(len(TV3concat)):
        value=TV3concat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                TV3concat.iloc[i,24]=value[1:]


# In[ ]:


#TV3concat['Detail1'].value_counts()


# In[ ]:


TV3concat['LastDigit_PV'] = TV3concat['F2020'].apply(lambda x: x[-1])


# In[ ]:


TV3concat['F2020_Updated']= TV3concat['S2021'] + TV3concat['LastDigit_PV']


# In[ ]:


#TV3concat.to_csv(r"C:\Users\saraswathy.rajaman\Documents\TV3.csv",index=False,header=True)


# In[ ]:


TV3concat= TV3concat.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:



TV3=TV3concat.copy()


# In[ ]:


TV3['VersionID']='0'
TV3['SID']='1857'
TV3['Status']='Add'
TV3['StudyAnswerID']='0'


# In[ ]:


TV3['Definition'] = TV3.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


#TV3.to_csv(r"C:\Users\saraswathy.rajaman\Documents\TV3.csv",index=False,header=True)


# # TV4 Punch Values

# In[ ]:





# In[ ]:


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


# In[ ]:


df_TV_Movie_TV4=df_TV_Movie.query('cleantype=="TV4"')


# In[ ]:


df_TV_Movie_TV4['F2020']=df_TV_Movie_TV4['F2020'].str.replace('nan','')
df_TV_Movie_TV4['S2021']=df_TV_Movie_TV4['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


df_TV_Movie_TV4['F2020']=df_TV_Movie_TV4['F2020'].str.replace('nan','')
df_TV_Movie_TV4['S2021']=df_TV_Movie_TV4['S2021'].str.replace('nan','')
df_TV_Movie_TV4[['F2020']]=df_TV_Movie_TV4[["F2020"]].apply(pd.to_numeric)
df_TV_Movie_TV4[['S2021']]=df_TV_Movie_TV4[["S2021"]].apply(pd.to_numeric)


# In[ ]:


df_TV_Movie_TV4['Col2PV']=''


# In[ ]:


for i in range(len(df_TV_Movie_TV4)):
    type=df_TV_Movie_TV4.iloc[i,0]
    cleantype=df_TV_Movie_TV4.iloc[i,1]
    if type == 'show':
        df_TV_Movie_TV4.iloc[i,11] = df_TV_Movie_TV4.iloc[i,11] +1
        df_TV_Movie_TV4.iloc[i,4] =  df_TV_Movie_TV4.iloc[i,4] + 1
        df_TV_Movie_TV4.iloc[i,17] = 'Yes'
		


# In[ ]:


df_TV_Movie_TV4['F2020'] = df_TV_Movie_TV4['F2020'].astype(str).apply(lambda x: x.replace('.0',''))
df_TV_Movie_TV4['S2021'] = df_TV_Movie_TV4['S2021'].astype(str).apply(lambda x: x.replace('.0',''))


# In[ ]:



df_TV_Movie_TV4['F2020']=df_TV_Movie_TV4['F2020'].str.replace('nan','')
df_TV_Movie_TV4['S2021']=df_TV_Movie_TV4['S2021'].str.replace('nan','')


# In[ ]:


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
	


# In[ ]:


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


# In[ ]:


TV4concat=pd.concat(PTV4)


# In[ ]:


TV4concat['LastDigit_PV'] = TV4concat['F2020'].apply(lambda x: x[-1])


# In[ ]:


TV4concat['F2020_Updated']= TV4concat['S2021'] + TV4concat['LastDigit_PV']


# In[ ]:


for i in range(len(TV4concat)):
        value=TV4concat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                TV4concat.iloc[i,24]=value[1:]


# In[ ]:


TV4concat= TV4concat.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


TV4=TV4concat.copy()


# In[ ]:


TV4['VersionID']='0'
TV4['SID']='1857'
TV4['Status']='Add'
TV4['StudyAnswerID']='0'


# In[ ]:


TV4=TV4.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


TV4['Detail1']=TV4['Detail1'].fillna(TV4['Shows_Name']) 


# In[ ]:


TV4['Definition'] = TV4.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


#TV4.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV4.csv',index=False,header=True)


# # TV5 Punch values

# In[ ]:


#only col1 value -6,5,1,4-no col2 values


# In[ ]:


df_TV_Movie_TV5=df_TV_Movie.query('cleantype=="TV5" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_TV5['F2020']=df_TV_Movie_TV5['F2020'].str.replace('nan','')
df_TV_Movie_TV5['S2021']=df_TV_Movie_TV5['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


PTV5= [df_inner_PV_TV5['1'],
           df_inner_PV_TV5['6'],
           df_inner_PV_TV5['5'], 
           df_inner_PV_TV5['4'], 
                    
          ]


# In[ ]:


TV5concat=pd.concat(PTV5)


# In[ ]:


for i in range(len(TV5concat)):
        value=str(TV5concat.iloc[i,24])
        firstvalue=value[0]
        if firstvalue =='#':
                TV5concat.iloc[i,24]=value[1:]


# In[ ]:



TV5concat['LastDigit_PV'] = TV5concat['F2020'].apply(lambda x: x[-1])


# In[ ]:



TV5concat['F2020_Updated']= TV5concat['S2021'] + TV5concat['LastDigit_PV']


# In[ ]:



dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_TV5=dfOneW.query("cleantype=='TV5'")


# In[ ]:



df_TV5=[TV5concat,dfOneW_TV5]


# In[ ]:


df_TV5=pd.concat(df_TV5)


# In[ ]:


df_TV5= df_TV5.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


df1w_TV5=df_TV5.query("OneWave_Suppress=='#'")


# In[ ]:


dfnon1w_TV5=df_TV5.query("OneWave_Suppress!='#'")


# In[ ]:


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


# In[ ]:


TV5onewave= [dfonewave_TV5['1'],
           dfonewave_TV5['6'],
           dfonewave_TV5['5'], 
           dfonewave_TV5['4'],                
           
          ]


# In[ ]:


TV5onewave=pd.concat(TV5onewave)


# In[ ]:



TV5onewave['LastDigit_PV']=TV5onewave['S2021'].str.strip().str[-1]


# In[ ]:


TV5onewave['SDID']='0'
TV5onewave['SID']='1857'
TV5onewave['UCode']='U0'
TV5onewave['StudyEntryID']='0'
TV5onewave['QUESTID']='0'
TV5onewave['QuestionID']='0'


# In[ ]:



TV5onewave.to_csv('TV5#.csv',index=False,header=True)


# In[ ]:


TV5=[dfnon1w_TV5,TV5onewave]


# In[ ]:


TV5=pd.concat(TV5)


# In[ ]:


TV5=TV5.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
TV5['Tmpl']=TV5['Tmpl'].fillna(method='ffill')
TV5['Super']=TV5['Super'].fillna(method='ffill')
TV5['Detail3']=TV5['Detail3'].fillna(method='ffill')


# In[ ]:


TV5=TV5.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
TV5['Category']=TV5['Category'].fillna(method='ffill')
TV5['QLevel']=TV5['QLevel'].fillna(method='ffill')


# In[ ]:


TV5['QUESTID']=TV5['QUESTID'].fillna('0')
TV5['QuestionID']=TV5['QuestionID'].fillna('0')
TV5['SDID']=TV5['SDID'].fillna('0')


# In[ ]:


TV5['VersionID']='0'
TV5['SID']='1857'


# In[ ]:


TV5['Status']='Add'
TV5['StudyAnswerID']='0'


# In[ ]:


TV5['Definition'] = TV5.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


TV5['Detail1']=TV5['Detail1'].fillna(TV5['Shows_Name'])


# In[ ]:


TV5['Wave']=TV5['Wave'].fillna('0')


# In[ ]:


TV5['UCode']=TV5['UCode'].fillna('U0')


# In[ ]:


Listheading=TV5['Sec_List_Heading'].unique()
g=TV5.groupby('Sec_List_Heading')


# In[ ]:


i=0
n=0
TV5_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    TV5_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[ ]:


n=0
for values in Listheading:
    TV5_LH[n]=TV5_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    TV5_LH[n]['Detail2']=TV5_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF    


# In[ ]:


#n


# In[ ]:


TV5Frames=[TV5_LH[0],TV5_LH[1],TV5_LH[2],TV5_LH[3],TV5_LH[4],TV5_LH[5],TV5_LH[6],TV5_LH[7],TV5_LH[8],TV5_LH[9]]


# In[ ]:


TV5=pd.concat(TV5Frames)


# In[ ]:


TV5=TV5.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


TV5['Wave']=TV5['Wave'].replace(r'^\s*$',np.nan,regex=True)
TV5['StudyEntryID']=TV5['StudyEntryID'].replace(r'^\s*$',np.nan,regex=True)
TV5['AnswerID']=TV5['AnswerID'].replace(r'^\s*$',np.nan,regex=True)
TV5['UCode']=TV5['UCode'].replace(r'^\s*$',np.nan,regex=True)


# In[ ]:


TV5['Wave'].isna().value_counts()


# In[ ]:


TV5['Wave']=TV5['Wave'].fillna('0')


# In[ ]:


TV5['Wave'].isna().value_counts()


# In[ ]:


TV5['StudyEntryID']=TV5['StudyEntryID'].fillna('0')


# In[ ]:


TV5['AnswerID']=TV5['AnswerID'].fillna('0')


# In[ ]:


TV5['UCode']=TV5['UCode'].fillna('U0')


# In[ ]:


#TV2['Wave']=TV2['Wave'].fillna(TV2)


# In[ ]:



#TV5.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV5.csv',index=False,header=True)


# # TV6 Punch Values

# In[ ]:


#col1- 5, 1,4 no col 2 values


# In[ ]:


df_TV_Movie_TV6=df_TV_Movie.query('cleantype=="TV6" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_TV6['F2020']=df_TV_Movie_TV6['F2020'].str.replace('nan','')
df_TV_Movie_TV6['S2021']=df_TV_Movie_TV6['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


PTV6= [
           df_inner_PV_TV6['1'],
           df_inner_PV_TV6['4'],
           df_inner_PV_TV6['5'],
           df_inner_PV_TV6['6'],
           
          ]


# In[ ]:


TV6concat=pd.concat(PTV6)


# In[ ]:


for i in range(len(TV6concat)):
        value=str(TV6concat.iloc[i,24])
        firstvalue=value[0]
        if firstvalue =='#':
                TV6concat.iloc[i,24]=value[1:]


# In[ ]:


#TV6concat['Detail1']


# In[ ]:


TV6concat['LastDigit_PV'] = TV6concat['F2020'].apply(lambda x: x[-1])


# In[ ]:


TV6concat['F2020_Updated']= TV6concat['S2021'] + TV6concat['LastDigit_PV']


# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_TV6=dfOneW.query("cleantype=='TV6'")


# In[ ]:


df_TV6=[TV6concat,dfOneW_TV6]


# In[ ]:


df_TV6=pd.concat(df_TV6)


# In[ ]:


df_TV6= df_TV6.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


df1w_TV6=df_TV6.query("OneWave_Suppress=='#'")


# In[ ]:


dfnon1w_TV6=df_TV6.query("OneWave_Suppress!='#'")


# In[ ]:


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


# In[ ]:


TV6onewave= [dfonewave_TV6['1'],
           dfonewave_TV6['5'],
           dfonewave_TV6['4'],
             dfonewave_TV6['6'],
           
          ]


# In[ ]:


TV6onewave=pd.concat(TV6onewave)


# In[ ]:


TV6onewave['LastDigit_PV']=TV6onewave['S2021'].str.strip().str[-1]


# In[ ]:


TV6onewave['SDID']='0'

TV6onewave['UCode']='U0'
TV6onewave['StudyEntryID']='0'


# In[ ]:


TV6onewave['QUESTID']='0'
TV6onewave['QuestionID']='0'


# In[ ]:



TV6onewave.to_csv('TV6#.csv',index=False,header=True)


# In[ ]:


TV6=[dfnon1w_TV6,TV6onewave]


# In[ ]:


TV6=pd.concat(TV6)


# In[ ]:



TV6=TV6.sort_values(['cleantype', 'LastDigit_PV'],ascending=[True, True])
						  
TV6['Tmpl']=TV6['Tmpl'].fillna(method='ffill')
TV6['Super']=TV6['Super'].fillna(method='ffill')
TV6['Detail3']=TV6['Detail3'].fillna(method='ffill')


# In[ ]:


TV6=TV6.sort_values(['cleantype', 'Sec_List_Heading'],ascending=[True,True])
TV6['Category']=TV6['Category'].fillna(method='ffill')
TV6['QLevel']=TV6['QLevel'].fillna(method='ffill')
TV6['QUESTID']=TV6['QUESTID'].fillna('0')
TV6['QuestionID']=TV6['QuestionID'].fillna('0')
TV6['UCode']=TV6['UCode'].fillna('U0')
TV6['SDID']=TV6['SDID'].fillna('0')


# In[ ]:


Listheading=TV6['Sec_List_Heading'].unique()
g=TV6.groupby('Sec_List_Heading')


# In[ ]:


i=0
n=0
TV6_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    TV6_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[ ]:


n=0
for values in Listheading:
    TV6_LH[n]=TV6_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    TV6_LH[n]['Detail2']=TV6_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF    


# In[ ]:


TV6Frames=[TV6_LH[0]]


# In[ ]:


TV6=pd.concat(TV6Frames)


# In[ ]:


TV6['Definition'] = TV6.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


TV6['VersionID']='0'
TV6['SID']='1857'
TV6['Status']='Add'
TV6['StudyAnswerID']='0'


# In[ ]:


TV6=TV6.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


#TV6.to_csv(r'C:\Users\saraswathy.rajaman\Documents\TV6.csv',index=False,header=True)


# # add_cable

# In[ ]:


#col1-1,2 no col 2 values


# In[ ]:


df_TV_Movie_ac=df_TV_Movie.query('cleantype=="add_cabl" and OneWave_Suppress!="#"')


# In[ ]:



df_TV_Movie_ac['F2020']=df_TV_Movie_ac['F2020'].str.replace('nan','')
df_TV_Movie_ac['S2021']=df_TV_Movie_ac['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


Pac= [
           df_inner_PV_ac['1'],
           df_inner_PV_ac['2'], 
           
          ]


# In[ ]:


acconcat=pd.concat(Pac)


# In[ ]:


acconcat['Detail1']=acconcat['Detail1'].astype(str)


# In[ ]:


for i in range(len(acconcat)):
        value=acconcat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                acconcat.iloc[i,24]=value[1:]


# In[ ]:


acconcat['LastDigit_PV'] = acconcat['F2020'].apply(lambda x: x[-1])


# In[ ]:



acconcat['F2020_Updated']= acconcat['S2021'] + acconcat['LastDigit_PV']


# # Add cable one wave

# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_ac=dfOneW.query("cleantype=='add_cabl'")


# In[ ]:



df_ac=[acconcat,dfOneW_ac]


# In[ ]:


df_ac=pd.concat(df_ac)


# In[ ]:


df_ac= df_ac.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


df1w_ac=df_ac.query("OneWave_Suppress=='#'")


# In[ ]:


dfnon1w_ac=df_ac.query("OneWave_Suppress!='#'")


# In[ ]:


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


# In[ ]:


aconewave= [onewave_ac['1'],
           onewave_ac['2']
           ]
		  


# In[ ]:


aconewave=pd.concat(aconewave)


# In[ ]:


aconewave['LastDigit_PV']=aconewave['S2021'].str.strip().str[-1]


# In[ ]:


aconewave['SDID']='0'

aconewave['UCode']='U0'
aconewave['StudyEntryID']='0'


# In[ ]:


aconewave['Shows_Name']=aconewave['Detail1']
aconewave['Wave']='0'
aconewave['AnswerID']='0'


# In[ ]:


aconewave['QUESTID']='0'
aconewave['QuestionID']='0'


# In[ ]:


aconewave.to_csv('ac#.csv',index=False,header=True)


# In[ ]:


ac=[dfnon1w_ac,aconewave]


# In[ ]:


ac=pd.concat(ac)


# In[ ]:


ac=ac.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
ac['Tmpl']=ac['Tmpl'].fillna(method='ffill')
ac['Super']=ac['Super'].fillna(method='ffill')
ac['Detail3']=ac['Detail3'].fillna(method='ffill')


# In[ ]:


ac=ac.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
ac['Category']=ac['Category'].fillna(method='ffill')
ac['QLevel']=ac['QLevel'].fillna(method='ffill')


# In[ ]:


Listheading=ac['Sec_List_Heading'].unique()


# In[ ]:


g=ac.groupby('Sec_List_Heading')


# In[ ]:


i=0
n=0
ac_LH={}
for Sec_List_Heading, g_df in g:
    print (Sec_List_Heading)
    ac_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[ ]:


n=0
for values in Listheading:
    ac_LH[n]=ac_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    ac_LH[n]['Detail2']=ac_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[ ]:


#n


# In[ ]:


acFrames=pd.DataFrame()
acFrames = acFrames.append([ac_LH[i] for i in range(n)])


# In[ ]:



ac=acFrames.copy()


# In[ ]:



ac['Shows_Name']=ac['Shows_Name'].astype(str)


# In[ ]:


ac['Detail1']=ac['Detail1'].replace(r'nan', np.nan, regex=True)


# In[ ]:


ac['Detail1']=ac['Detail1'].fillna(ac['Shows_Name'])


# In[ ]:


ac['Wave']=ac['Wave'].fillna(ac['Initial_Wave']) 
ac['Wave']=ac['Wave'].astype(str)
ac['Wave']=ac['Wave'].replace(r'W', '', regex=True)
ac['Wave']=ac['Wave'].replace(r'nan', np.nan, regex=True)
#ac['Wave'].isna().value_counts()
ac['Wave']=ac['Wave'].fillna('0')
ac['SDID']=ac['SDID'].fillna('0')
ac['Definition'] = ac.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:



ac['UCode']=ac['UCode'].fillna('U0')
ac['StudyEntryID']=ac['StudyEntryID'].fillna('0')
ac['UCode']=ac['UCode'].fillna('U0')
ac['QuestionID']=ac['QuestionID'].fillna('0')
ac['QUESTID']=ac['QUESTID'].fillna('0')
ac['AnswerID']=ac['AnswerID'].fillna('0')


# In[ ]:


ac['VersionID']='0'
ac['SID']='1857'
ac['Status']='Add'
ac['StudyAnswerID']='0'


# In[ ]:


#ac['Sec_List_Heading'].unique()


# In[ ]:


ac=ac.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


#ac.duplicated().value_counts()


# In[ ]:



#ac.to_csv(r'C:\Users\saraswathy.rajaman\Documents\ac.csv',index=False,header=True)


# # Movie 

# In[ ]:


#Movies Punch Variable
#col1-1,2,3,4,5


# In[ ]:


df_TV_Movie_M=df_TV_Movie.query('cleantype=="Movie" and OneWave_Suppress!="#"')


# In[ ]:


#df_TV_Movie_M.to_csv(r"C:\Users\saraswathy.rajaman\Documents\df_TV_Movie_M.csv",header=True,index=False)


# In[ ]:


df_TV_Movie_M['F2020']=df_TV_Movie_M['F2020'].str.replace('nan','')
df_TV_Movie_M['S2021']=df_TV_Movie_M['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


PM= [      df_inner_PV_M['1'],
           df_inner_PV_M['2'], 
           df_inner_PV_M['3'], 
           df_inner_PV_M['4'],
           df_inner_PV_M['5'],
                    ]


# In[ ]:


Mconcat=pd.concat(PM)


# In[ ]:


Mconcat['Detail1']=Mconcat['Detail1'].astype(str)


# In[ ]:


for i in range(len(Mconcat)):
        value=Mconcat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                Mconcat.iloc[i,24]=value[1:]


# In[ ]:


#Mconcat.to_csv(r"C:\Users\saraswathy.rajaman\Documents\Mconcat.csv",index=False,header=True)


# In[ ]:


Mconcat['LastDigit_PV'] = Mconcat['F2020'].apply(lambda x: x[-1])


# In[ ]:



Mconcat['F2020_Updated']= Mconcat['S2021'] + Mconcat['LastDigit_PV']


# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:


dfOneW_M=dfOneW.query("cleantype=='Movie'")


# In[ ]:



df_M=[Mconcat,dfOneW_M]


# In[ ]:


df_M=pd.concat(df_M)


# # Movie onewave

# In[ ]:



df_M= df_M.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# In[ ]:


df1w_M=df_M.query("OneWave_Suppress=='#'")


# In[ ]:


dfnon1w_M=df_M.query("OneWave_Suppress!='#'")


# In[ ]:


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


# In[ ]:


Monewave= [dfonewave_M['1'],
           dfonewave_M['2'],
           dfonewave_M['3'], 
           dfonewave_M['4'],
           dfonewave_M['5']
           
          ]


# In[ ]:


Monewave=pd.concat(Monewave)


# In[ ]:



Monewave['LastDigit_PV']=Monewave['S2021'].str.strip().str[-1]


# In[ ]:


Monewave['SDID']='0'

Monewave['UCode']='U0'
Monewave['StudyEntryID']='0'


# In[ ]:


Monewave['QUESTID']='0'
Monewave['QuestionID']='0'


# In[ ]:


Monewave.to_csv('M1.csv',index=False,header=True)


# In[ ]:


M=[dfnon1w_M,Monewave]


# In[ ]:


M=pd.concat(M)


# In[ ]:


M=M.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
M['Tmpl']=M['Tmpl'].fillna(method='ffill')
M['Super']=M['Super'].fillna(method='ffill')
M['Detail3']=M['Detail3'].fillna(method='ffill')
#M['Detail2']=M['Detail2'].fillna(method='ffill')


# In[ ]:


M=M.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
M['Category']=M['Category'].fillna(method='ffill')
M['QLevel']=M['QLevel'].fillna(method='ffill')


# In[ ]:


M['VersionID']='0'
M['SID']='1857'
M['Status']='Add'
M['StudyAnswerID']='0'


# In[ ]:


Listheading=M['Sec_List_Heading'].unique()


# In[ ]:


g=M.groupby('Sec_List_Heading')


# In[ ]:


i=0
n=0
M_LH={}
for Sec_List_Heading, g_df in g:
    print (Sec_List_Heading)
    M_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas DF


# In[ ]:


n=0
for values in Listheading:
    M_LH[n]=M_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    M_LH[n]['Detail2']=M_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[ ]:


MFrames=pd.DataFrame()
MFrames = MFrames.append([M_LH[i] for i in range(n)])


# In[ ]:


M=MFrames.copy()


# In[ ]:


M['Shows_Name']=M['Shows_Name'].astype(str)


# In[ ]:


M['Detail1']=M['Detail1'].replace(r'nan', np.nan, regex=True)


# In[ ]:


M['Detail1']=M['Detail1'].fillna(M['Shows_Name'])


# In[ ]:




M['Wave']=M['Wave'].fillna(M['Initial_Wave']) 
M['Wave']=M['Wave'].astype(str)
M['Wave']=M['Wave'].replace(r'W', '', regex=True)
M['Wave']=M['Wave'].replace(r'nan', np.nan, regex=True)
#M['Wave'].isna().value_counts()


# In[ ]:


M['Wave']=M['Wave'].fillna('0')
M['SDID']=M['SDID'].fillna('0')
M['Definition'] = M.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


M['UCode']=M['UCode'].fillna('U0')
M['StudyEntryID']=M['StudyEntryID'].fillna('0')
M['UCode']=M['UCode'].fillna('U0')

#QUESTID
#AnswerID


# In[ ]:


M['QuestionID']=M['QuestionID'].fillna('0')
M['QUESTID']=M['QUESTID'].fillna('0')
M['AnswerID']=M['AnswerID'].fillna('0')


# In[ ]:


#M['Detail1'] = M.apply(lambda x: x[1:]  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


M=M.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


#M.duplicated().value_counts()


# In[ ]:


#M.to_csv(r'C:\Users\saraswathy.rajaman\Documents\Movie1.csv',index=False,header=True)


# # Cable Punch Values

# In[ ]:


#col1-0,1,6,8,9 no col 2 values


# In[ ]:


df_TV_Movie_C=df_TV_Movie.query('cleantype=="cable" and OneWave_Suppress!="#"')


# In[ ]:


df_TV_Movie_C['Shows_Name']=df_TV_Movie_C['Sec_List_Heading'] +":" + " "+df_TV_Movie_C['Shows_Name']


# In[ ]:


#df_TV_Movie_C


# In[ ]:


df_TV_Movie_C['F2020']=df_TV_Movie_C['F2020'].str.replace('nan','')
df_TV_Movie_C['S2021']=df_TV_Movie_C['S2021'].str.replace('nan','')


# In[ ]:


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


# In[ ]:


PC= [df_inner_PV_C['0'],
     df_inner_PV_C['1'],
           df_inner_PV_C['6'],
           df_inner_PV_C['8'],
           df_inner_PV_C['9'],
           
          ]


# In[ ]:


Cconcat=pd.concat(PC)


# In[ ]:


Cconcat['Detail1']=Cconcat['Detail1'].astype(str)


# In[ ]:


for i in range(len(Cconcat)):
        value=Cconcat.iloc[i,24]
        firstvalue=value[0]
        if firstvalue =='#':
                Cconcat.iloc[i,24]=value[1:]


# In[ ]:


Cconcat['LastDigit_PV'] = Cconcat['F2020'].apply(lambda x: x[-1])


# In[ ]:


Cconcat['F2020_Updated']= Cconcat['S2021'] + Cconcat['LastDigit_PV']


# In[ ]:


dfOneW=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[ ]:



dfOneW_C=dfOneW.query("cleantype=='cable'")


# In[ ]:


df_C=[Cconcat,dfOneW_C]


# In[ ]:


df_C=pd.concat(df_C)


# In[ ]:


df_C= df_C.drop(['Fox', 'W83','W84','W82','W81','F2019','S2020','QID','StatisticID','CatSynID','NoteID','statusid' ], axis=1)


# # Cable one wave 

# In[ ]:


df1w_C=df_C.query("OneWave_Suppress=='#'")


# In[ ]:


dfnon1w_C=df_C.query("OneWave_Suppress!='#'")


# In[ ]:


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


# In[ ]:



Conewave= [dfonewave_C['0'],
           dfonewave_C['6'],
           dfonewave_C['8'], 
           dfonewave_C['9'],
           dfonewave_C['1'],
           
          ]


# In[ ]:


Conewave=pd.concat(Conewave)


# In[ ]:


Conewave['LastDigit_PV']=Conewave['S2021'].str.strip().str[-1]


# In[ ]:


Conewave['SDID']='0'

Conewave['UCode']='U0'
Conewave['StudyEntryID']='0'


# In[ ]:


Conewave['QUESTID']='0'
Conewave['QuestionID']='0'


# In[ ]:


Conewave['Detail1']=Conewave['Detail1'].astype(str)


# In[ ]:


#Conewave


# In[ ]:


Conewave['Shows_Name']=Conewave['Shows_Name'].apply(lambda x : x[1:])


# In[ ]:


Conewave['Shows_Name']=Conewave['Sec_List_Heading'] +":" + " "+ Conewave['Shows_Name']


# In[ ]:


#Conewave


# In[ ]:


Conewave['Shows_Name']='#'+ Conewave['Shows_Name']


# In[ ]:


#Conewave['Shows_Name']= Conewave['Detail1']


# In[ ]:



#Conewave.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\C#.csv',index=False,header=True)


# In[ ]:


#Conewave


# In[ ]:



C=[dfnon1w_C,Conewave]


# In[ ]:


C=pd.concat(C)


# In[ ]:


#C.columns


# In[ ]:


#C


# In[ ]:


C=C.sort_values(['cleantype', 'LastDigit_PV'], 
               ascending=[True,
                          True])
						  
C['Tmpl']=C['Tmpl'].fillna(method='ffill')
C['Super']=C['Super'].fillna(method='ffill')
C['Detail3']=C['Detail3'].fillna(method='ffill')


# In[ ]:




C=C.sort_values(['cleantype', 'Sec_List_Heading'], 
               ascending=[True,
                          True])
C['Category']=C['Category'].fillna(method='ffill')
C['QLevel']=C['QLevel'].fillna(method='ffill')


# In[ ]:


C['VersionID']='0'
C['SID']='1857'
C['Status']='Add'
C['StudyAnswerID']='0'


# In[ ]:


Listheading=C['Sec_List_Heading'].unique()


# In[ ]:


g=C.groupby('Sec_List_Heading')


# In[ ]:


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





# In[ ]:


n=0
for values in Listheading:
    C_LH[n]=C_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    C_LH[n]['Detail2']=C_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[ ]:


#n


# # Append all 57 DF for each sec values in cable 
# 

# In[ ]:


CFrames=pd.DataFrame()
CFrames = CFrames.append([C_LH[i] for i in range(n)])


# In[ ]:


C=CFrames.copy()


# In[ ]:


#C['Detail1']=C['Detail1'].fillna(C['Shows_Name']) 


# In[ ]:


C['Detail1']=C['Detail1'].fillna(C['Shows_Name'])


# In[ ]:


C['Wave']=C['Wave'].fillna(C['Initial_Wave']) 
C['Wave']=C['Wave'].astype(str)
C['Wave']=C['Wave'].replace(r'W', '', regex=True)


# In[ ]:


C['Wave']=C['Wave'].replace(r'nan', np.nan, regex=True)
C['Wave'].isna().value_counts()
C['Wave']=C['Wave'].fillna('0')


# In[ ]:


# if the CCP is different in S2021 than F2020 then Defenition is 0


# In[ ]:


C['Definition'] = C.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[ ]:


C=C.drop_duplicates(subset='F2020_Updated',keep='last')


# In[ ]:


#check duplicates


# In[ ]:


#C.duplicated().value_counts()


# In[ ]:



#C.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Cable1.csv',index=False,header=True)


# # TVMedia file

# In[ ]:


Final_Frames=[TV1,TV2,TV3,TV4,TV5,TV6,SPTV1,SPTV2,SPTV3,SPTV4,SPTV5,SPTV51,ac,M,C]


# In[ ]:


TVmedia=pd.concat(Final_Frames)


# In[ ]:


#TVmedia.columns


# In[ ]:


TVmedia['QLevel'] =TVmedia['QLevel'].astype(np.int64)
#TVmedia['Wave'] =TVmedia['Wave'].astype(int)


# In[ ]:


TVmedia['Tmpl'] =TVmedia['Tmpl'].astype(np.int64)


# In[ ]:


TVmedia['QUESTID'] =TVmedia['QUESTID'].astype(np.int32)


# In[ ]:


TVmedia['AnswerID'] =TVmedia['AnswerID'].astype(np.int32)


# In[ ]:


TVmedia['SDID'] =TVmedia['SDID'].astype(np.int32)


# In[ ]:


TVmedia['SID'] =TVmedia['SID'].astype(np.int32)


# In[ ]:


TVmedia['StudyAnswerID'] =TVmedia['StudyAnswerID'].astype(np.int32)


# In[ ]:


TVmedia['StudyEntryID'] =TVmedia['StudyEntryID'].astype(np.int32)


# In[ ]:


#TVmedia['QLevel'].dtype


# In[ ]:


TVmedia['Wave'] =TVmedia['Wave'].astype(float)
TVmedia['Wave'] =TVmedia['Wave'].astype(np.int32)


# In[ ]:





# In[ ]:


TVmedia['SDID'] =TVmedia['SDID'].astype(float)
TVmedia['SDID'] =TVmedia['SDID'].astype(int)


# In[ ]:


TVmedia['QuestionID'] =TVmedia['QuestionID'].astype(float)
TVmedia['QuestionID'] =TVmedia['QuestionID'].astype(int)


# In[ ]:


TVmedia['AnswerID'] =TVmedia['AnswerID'].astype(float)
TVmedia['AnswerID'] =TVmedia['AnswerID'].astype(int)


# In[ ]:


TVmedia_copy=TVmedia.copy()


# In[ ]:


TVmedia.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\test.csv',index=False,header=True,encoding='cp1252')


# # Remove W83 # value in detail1

# In[ ]:



TVmedia.drop(['Fox', 'W84','W83','W82','S2020','W81','F2019','QID','Detail1'], axis=1, inplace=True)


# In[ ]:


#TVmedia.columns


# In[ ]:


#TVmedia=TVmedia.drop(["StatisticID","CatSynID","NoteID","statusid"],axis=1,inplace=True)
TVmedia.drop(['StatisticID', 'CatSynID','NoteID','statusid','CCP'], axis=1, inplace=True)


# In[ ]:


TVmedia.rename(columns={'F2020_Updated':'CCP','Shows_Name':'Detail1','VersionID':'Version'},inplace=True)


# In[ ]:


#TVmedia.columns


# In[ ]:


TVmedia['EditedBy']='codebookcreator'
TVmedia['EditedDate']=pd.to_datetime('today')
TVmedia['StudyEntryID']='0'
TVmedia['SID']='1952'


# add an empty column
#Mydataframe.insert(0,'Roll Number','')


# In[ ]:


TVmedia['StudyEntryID'] =TVmedia['StudyEntryID'].astype(np.int32)


# In[ ]:


TVmedia['Version'] =TVmedia['Version'].astype(np.int32)


# In[ ]:


TVmedia['Imported']=''
TVmedia['Min']=''
TVmedia['Max']=''


# In[ ]:


TVmedia['Min'] =TVmedia['Min'].apply(pd.to_numeric)
#df_TV_Movie_TV1[['F2020']]=df_TV_Movie_TV1[["F2020"]].apply(pd.to_numeric)
#df_TV_Movie_TV1[['S2021']]=df_TV_Movie_TV1[["S2021"]].apply(pd.to_numeric)


# In[ ]:


TVmedia['Max'] =TVmedia['Max'].apply(pd.to_numeric)


# In[ ]:


#TVmedia['Definition'] = TVmedia.apply(lambda x: '' if x['Definition']==0 else x['Definition'], axis=1)


# In[ ]:


TVmedia['Definition'] = TVmedia['Definition'].replace(['0', 0], np.nan)


# In[ ]:


#TVmedia.head(50)


# In[ ]:


#TVmedia.info()


# In[ ]:


#TVmedia_copy=TVmedia.copy()


# In[ ]:


TVmedia=TVmedia[["StudyEntryID","SID","Version","Category","Super","Tmpl","Time Period","Detail1","Detail2",
"Detail3","Detail4","UCode","Definition","CCP","ORD","Wave","Status","Full_Label","QLevel","QUESTID","AnswerID","EditedBy","EditedDate","SDID",
"StudyAnswerID","QuestionID","Imported","Min","Max"]]


# In[ ]:


TVmedia = TVmedia.astype( {"QLevel":'int32', "QUESTID":'int32', "AnswerID":'int32',"QuestionID":'int32',"SID":'int64', "SDID":'int32', "Version":'int32', "Wave":'int32', "Min":'float',"Max":'float', "StudyEntryID":'int64',"Imported":'bool'} )


# In[ ]:


#TVmedia=TVmedia.dropna(subset=['CCP'])


# In[ ]:


#TVmedia['CCP'].isna().value_counts()


# # TVmedia to csv file

# In[ ]:


TVmedia_copy=TVmedia.copy()


# In[ ]:


TVmedia_copy.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Spring2021_withcolumns.csv',index=False,header=True,encoding='cp1252')


# In[ ]:


TVmedia.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Spring-2021.csv',index=False,header=True,encoding='cp1252')


# In[ ]:


from sqlalchemy import create_engine
#engine = create_engine('sqlite://', echo=False)


# In[ ]:


#TVmedia.to_sql(name="tmp_EditedRecords_Test", con=engine,  schema="dbo")


# In[ ]:


DB = {'server':'internalSQLdev.mridevops.com','database':'Codebook_Taxonomy','driver':'driver=SQL Server Native Client 11.0','pyodb_d':'SQL Server Native Client 11.0'}
#engine=create_engine('mssql+pyodbc://'+ DB['server']+'/'+ DB['database']+'?'+ DB['driver'])


# In[ ]:



engine = create_engine('mssql+pyodbc://' + DB['server'] + '/' + DB['database'] + '?' + DB['driver'], fast_executemany = True)


# In[ ]:


import pyodbc 


# In[ ]:


#dsn="DRIVER={SQLSERVER};server=internalSQLdev.mridevops.com;database=Codebook_Taxonomy;uid=sashi.rajamani;pwd=Tanuarjun@2019"


# In[ ]:


#cnxn = pyodbc.connect(dsn)


# In[ ]:


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
    TVmedia.to_sql(name="tmp_EditedRecords_Hold_testsql",con=engine,schema="dbo",if_exists='replace', chunksize=1000,index=False)
#df.to_sql('db_table2', engine, if_exists='replace')


# In[ ]:


print("SPing-2021 Ingested successfully")


# In[ ]:


#pwd


# TVmedia.info()

# import platform
# print(platform.python_version())

# In[ ]:




