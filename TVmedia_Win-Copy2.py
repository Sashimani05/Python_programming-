#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Libraries-and-Display-settings" data-toc-modified-id="Libraries-and-Display-settings-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Libraries and Display settings</a></span></li><li><span><a href="#Load-the-file-from-Excel-sheet" data-toc-modified-id="Load-the-file-from-Excel-sheet-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Load the file from Excel sheet</a></span></li><li><span><a href="#Drop-First-row" data-toc-modified-id="Drop-First-row-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Drop First row</a></span></li><li><span><a href="#Fix-column-names" data-toc-modified-id="Fix-column-names-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Fix column names</a></span></li><li><span><a href="#add-compare-column-to-compare-S2022-and-F2021" data-toc-modified-id="add-compare-column-to-compare-S2022-and-F2021-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>add compare column to compare S2022 and F2021</a></span></li><li><span><a href="#Remove-*-from-S2022-and-F2020" data-toc-modified-id="Remove-*-from-S2022-and-F2020-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Remove * from S2022 and F2020</a></span></li><li><span><a href="#Remove-X-in-onewave/Suppress-column" data-toc-modified-id="Remove-X-in-onewave/Suppress-column-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Remove X in onewave/Suppress column</a></span></li><li><span><a href="#forward-fill-cleantype-and-list-heading" data-toc-modified-id="forward-fill-cleantype-and-list-heading-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>forward fill cleantype and list heading</a></span></li><li><span><a href="#Remove-b-from-sec-list-heading" data-toc-modified-id="Remove-b-from-sec-list-heading-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Remove b from sec list heading</a></span></li><li><span><a href="#Few-items-has-#-in-sec-heading--add-#-in-one-wave-column-for-them" data-toc-modified-id="Few-items-has-#-in-sec-heading--add-#-in-one-wave-column-for-them-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Few items has # in sec heading- add # in one wave column for them</a></span></li><li><span><a href="#For-one-wave-item-append-#-in-show-names" data-toc-modified-id="For-one-wave-item-append-#-in-show-names-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>For one wave item append # in show names</a></span></li><li><span><a href="#Remove-#-from-List-heading-or-sec-heading-values" data-toc-modified-id="Remove-#-from-List-heading-or-sec-heading-values-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Remove # from List heading or sec heading values</a></span></li><li><span><a href="#Group-TVmedia-as-different-Dataframe-on-cleantype" data-toc-modified-id="Group-TVmedia-as-different-Dataframe-on-cleantype-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>Group TVmedia as different Dataframe on cleantype</a></span></li><li><span><a href="#Add-Cable-PV" data-toc-modified-id="Add-Cable-PV-14"><span class="toc-item-num">14&nbsp;&nbsp;</span>Add Cable PV</a></span></li><li><span><a href="#SPTV4-Punch-Values-append" data-toc-modified-id="SPTV4-Punch-Values-append-15"><span class="toc-item-num">15&nbsp;&nbsp;</span>SPTV4 Punch Values append</a></span></li><li><span><a href="#SPTV51-Punch-Values-append" data-toc-modified-id="SPTV51-Punch-Values-append-16"><span class="toc-item-num">16&nbsp;&nbsp;</span>SPTV51 Punch Values append</a></span></li><li><span><a href="#SPTV1" data-toc-modified-id="SPTV1-17"><span class="toc-item-num">17&nbsp;&nbsp;</span>SPTV1</a></span></li><li><span><a href="#Seperate-col1-and-col2-PV" data-toc-modified-id="Seperate-col1-and-col2-PV-18"><span class="toc-item-num">18&nbsp;&nbsp;</span>Seperate col1 and col2 PV</a></span></li><li><span><a href="#Taking-a-look-at-Punch-values" data-toc-modified-id="Taking-a-look-at-Punch-values-19"><span class="toc-item-num">19&nbsp;&nbsp;</span>Taking a look at Punch values</a></span></li><li><span><a href="#PV_Dataframe-grouping-with-col1-PV" data-toc-modified-id="PV_Dataframe-grouping-with-col1-PV-20"><span class="toc-item-num">20&nbsp;&nbsp;</span>PV_Dataframe grouping with col1 PV</a></span></li><li><span><a href="#PV_Dataframe-grouping-with-col2-PV" data-toc-modified-id="PV_Dataframe-grouping-with-col2-PV-21"><span class="toc-item-num">21&nbsp;&nbsp;</span>PV_Dataframe grouping with col2 PV</a></span></li><li><span><a href="#Dataframe-grouping-on-One-wave" data-toc-modified-id="Dataframe-grouping-on-One-wave-22"><span class="toc-item-num">22&nbsp;&nbsp;</span>Dataframe grouping on One wave</a></span></li><li><span><a href="#TV1-_col1-PV" data-toc-modified-id="TV1-_col1-PV-23"><span class="toc-item-num">23&nbsp;&nbsp;</span>TV1 _col1 PV</a></span></li><li><span><a href="#PV_col2-adding-them-for-TV1" data-toc-modified-id="PV_col2-adding-them-for-TV1-24"><span class="toc-item-num">24&nbsp;&nbsp;</span>PV_col2 adding them for TV1</a></span></li><li><span><a href="#PV_col1-TV3" data-toc-modified-id="PV_col1-TV3-25"><span class="toc-item-num">25&nbsp;&nbsp;</span>PV_col1-TV3</a></span></li><li><span><a href="#PV_col2-TV3" data-toc-modified-id="PV_col2-TV3-26"><span class="toc-item-num">26&nbsp;&nbsp;</span>PV_col2 TV3</a></span></li><li><span><a href="#TV4-PV_col1" data-toc-modified-id="TV4-PV_col1-27"><span class="toc-item-num">27&nbsp;&nbsp;</span>TV4 PV_col1</a></span></li><li><span><a href="#TV4-col2-PV" data-toc-modified-id="TV4-col2-PV-28"><span class="toc-item-num">28&nbsp;&nbsp;</span>TV4 col2 PV</a></span></li><li><span><a href="#TV2-col1_Punch-variable" data-toc-modified-id="TV2-col1_Punch-variable-29"><span class="toc-item-num">29&nbsp;&nbsp;</span>TV2 col1_Punch variable</a></span></li><li><span><a href="#TV2-col2-PV" data-toc-modified-id="TV2-col2-PV-30"><span class="toc-item-num">30&nbsp;&nbsp;</span>TV2 col2 PV</a></span></li><li><span><a href="#SPTV2" data-toc-modified-id="SPTV2-31"><span class="toc-item-num">31&nbsp;&nbsp;</span>SPTV2</a></span></li><li><span><a href="#SPTV3" data-toc-modified-id="SPTV3-32"><span class="toc-item-num">32&nbsp;&nbsp;</span>SPTV3</a></span></li><li><span><a href="#SPTV5" data-toc-modified-id="SPTV5-33"><span class="toc-item-num">33&nbsp;&nbsp;</span>SPTV5</a></span></li><li><span><a href="#TV5" data-toc-modified-id="TV5-34"><span class="toc-item-num">34&nbsp;&nbsp;</span>TV5</a></span></li><li><span><a href="#TV6" data-toc-modified-id="TV6-35"><span class="toc-item-num">35&nbsp;&nbsp;</span>TV6</a></span></li><li><span><a href="#Movies" data-toc-modified-id="Movies-36"><span class="toc-item-num">36&nbsp;&nbsp;</span>Movies</a></span></li><li><span><a href="#Cable" data-toc-modified-id="Cable-37"><span class="toc-item-num">37&nbsp;&nbsp;</span>Cable</a></span></li><li><span><a href="#Concat-all-DF" data-toc-modified-id="Concat-all-DF-38"><span class="toc-item-num">38&nbsp;&nbsp;</span>Concat all DF</a></span></li></ul></div>

# ## Libraries and Display settings

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


# ## Load the file from Excel sheet

# In[4]:


df_TV_Movie = pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\MasterMaps.xlsx', sheet_name='TV_Movie')


# In[5]:


df_PunchMap = pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\MasterMaps.xlsx', sheet_name='PunchMap')


# In[6]:


df_Fall_2021 = pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\Fall2021.xlsx', )


# In[7]:


df_TV_showtypes = pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\MasterMaps.xlsx', sheet_name='TVshowTypes')


# ## Drop First row

# In[8]:


df_TV_Movie=df_TV_Movie.drop(0)


# ## Fix column names

# In[9]:


df_TV_Movie=df_TV_Movie.rename(columns={'S2022':'W2021','Line Type':'Line_Type','clean type':'clean_type','Unnamed: 6':'Sec_List_Heading','Unnamed: 7':'OneWave_Suppress','Unnamed: 8':'Shows_Name',})


# ## add compare column to compare S2022 and F2021

# In[10]:


df_TV_Movie['compare'] = (df_TV_Movie['W2021'] == df_TV_Movie['F2021'])


# In[11]:


df_TV_Movie['col2pv'] = ''


# ## Remove * from S2022 and F2020

# In[12]:


#Removing spl character
df_TV_Movie['W2021']=df_TV_Movie['W2021'].str.replace('*','')
df_TV_Movie['F2021']=df_TV_Movie['F2021'].str.replace('*','')


# ## Remove X in onewave/Suppress column

# In[13]:


df_TV_Movie.drop(df_TV_Movie.index[df_TV_Movie['OneWave_Suppress'] == 'X'], inplace = True)


# ## forward fill cleantype and list heading 

# In[14]:


df_TV_Movie=df_TV_Movie.copy()
df_TV_Movie['clean_type']=df_TV_Movie['clean_type'].fillna(method='ffill')
#Forward fill cleatype as show


# ## Remove b from sec list heading

# In[15]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].replace('b', np.nan)


# In[16]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].replace(r'^\s*$', np.nan, regex=True)


# In[17]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].fillna(method='ffill')


# ## Few items has # in sec heading- add # in one wave column for them 

# In[18]:


df_TV_Movie['Shows_Name']=df_TV_Movie['Shows_Name'].astype(str)


# ## For one wave item append # in show names

# In[19]:


df_TV_Movie['Shows_Name'] = df_TV_Movie.apply(lambda x: '#'+x['Shows_Name']  if x['OneWave_Suppress']=='#' else x['Shows_Name'], axis=1)


# ## Remove # from List heading or sec heading values

# In[20]:


df_TV_Movie['Sec_List_Heading'] = df_TV_Movie['Sec_List_Heading'].apply(lambda a: str(a).replace('#',''))


# In[21]:


df_TV_Movie['wave'] = df_TV_Movie['wave'].apply(lambda a: str(a).replace('W',''))


# In[22]:


df_TV_Movie=df_TV_Movie.dropna(subset=['W2021'])


# In[23]:


df_TV_Movie.to_csv(r'C:\Users\saraswathy.rajaman\Documents\df_TV_Moviespr.csv',index=False,header=True,encoding='cp1252')


# In[24]:


df_TV_Movie.columns


# In[25]:


df_TV_Movie=df_TV_Movie[['clean_type','W2021','Sec_List_Heading', 'OneWave_Suppress', 'Shows_Name','wave',
'F2021','compare','col2pv']]


# In[26]:


df_TV_Movie=df_TV_Movie.rename(columns={'wave':'Initial_wave'})
df_TV_Movie['Initial_wave']=df_TV_Movie['Initial_wave'].replace(r'nan',np.nan, regex=True)


# ## Group TVmedia as different Dataframe on cleantype

# In[27]:


#group data based on cleantype into different dataframes
data={}
grouped = df_TV_Movie.groupby('clean_type')
for group in grouped.groups.keys():
    #print(group)
    data[group] = grouped.get_group(group)
    


# In[28]:


#data['add_cabl']


# In[29]:


df_PunchMap=df_PunchMap.rename(columns={'Clean Type':'Clean_Type'})


# In[30]:


#group_data = df.groupby(['Alphabet','Words'])['COUNTER'].sum()
PV={}
grouped = df_PunchMap.groupby('Clean_Type')
for group in grouped.groups.keys():
    #print(group)
    PV[group] = grouped.get_group(group)


# ## Add Cable PV 

# In[31]:


#PV['add_cable']


# In[32]:


Punch_variable=PV['add_cable']['PunchValue']


# In[33]:


#data['add_cabl']['F2021']=data['add_cabl'].apply(lambda x:x['F2021']+'1', axis=1)


# In[34]:


datapv={}
add_cab=[]
for i in Punch_variable:
   
    datapv[i]=data['add_cabl'].copy()

    datapv[i]['F2021']=datapv[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv[i]['W2021']=datapv[i].apply(lambda x:x['W2021']+str(i), axis=1)
    
    add_cab.append(datapv[i])
    
    


# In[35]:


add_cab=pd.concat(add_cab)


# In[36]:


df_merge_add_cab= pd.merge(add_cab, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[37]:


df_merge_add_cab['LastDigit_PV']=df_merge_add_cab['W2021'].str.strip().str[-1]


# In[38]:


df_merge_add_cab=df_merge_add_cab.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_add_cab['Tmpl']=df_merge_add_cab['Tmpl'].fillna(method='ffill')
df_merge_add_cab['Super']=df_merge_add_cab['Super'].fillna(method='ffill')
df_merge_add_cab['Detail3']=df_merge_add_cab['Detail3'].fillna(method='ffill')


# In[39]:


df_merge_add_cab=df_merge_add_cab.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_add_cab['Category']=df_merge_add_cab['Category'].fillna(method='ffill')
df_merge_add_cab['QLevel']=df_merge_add_cab['QLevel'].fillna(method='ffill')
df_merge_add_cab['Detail2']=df_merge_add_cab['Detail2'].fillna(method='ffill')


# ## SPTV4 Punch Values append

# In[40]:


PV_SPTV4=PV['SPTV4']['PunchValue']


# In[41]:


datapv_SPTV4={}
SPTV4=[]
for i in PV_SPTV4:
    
    datapv_SPTV4[i]=data['SPTV4'].copy()

    datapv_SPTV4[i]['F2021']=datapv_SPTV4[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV4[i]['W2021']=datapv_SPTV4[i].apply(lambda x:x['W2021']+str(i), axis=1)
    
    SPTV4.append(datapv_SPTV4[i])
    


# In[42]:


SPTV4=pd.concat(SPTV4)


# In[43]:


df_merge_SPTV4= pd.merge(SPTV4, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# ## SPTV51 Punch Values append

# In[44]:


PV_SPTV51=PV['SPTV5.1']['PunchValue']


# In[45]:


#data['SPTV5.1']


# In[46]:


datapv_SPTV51={}
SPTV51=[]
for i in PV_SPTV51:
    
    datapv_SPTV51[i]=data['SPTV5.1'].copy()

    datapv_SPTV51[i]['F2021']=datapv_SPTV51[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV51[i]['W2021']=datapv_SPTV51[i].apply(lambda x:x['W2021']+str(i), axis=1)
    
    SPTV51.append(datapv_SPTV51[i])


# In[47]:


SPTV51=pd.concat(SPTV51)


# In[48]:


df_merge_SPTV51= pd.merge(SPTV51, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[49]:


df_merge_SPTV51['LastDigit_PV']=df_merge_SPTV51['W2021'].str.strip().str[-1]


# In[50]:


df_merge_SPTV51=df_merge_SPTV51.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_SPTV51['Tmpl']=df_merge_SPTV51['Tmpl'].fillna(method='ffill')
df_merge_SPTV51['Super']=df_merge_SPTV51['Super'].fillna(method='ffill')
df_merge_SPTV51['Detail3']=df_merge_SPTV51['Detail3'].fillna(method='ffill')


# In[51]:


#display(df_merge_SPTV51)


# ## SPTV1

# In[52]:


PV_SPTV1=PV['SPTV1']['PunchValue']


# In[53]:


datapv_SPTV1={}
SPTV1=[]
for i in PV_SPTV1:
    
    datapv_SPTV1[i]=data['SPTV1'].copy()

    datapv_SPTV1[i]['F2021']=datapv_SPTV1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV1[i]['W2021']=datapv_SPTV1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    SPTV1.append(datapv_SPTV1[i])
	


# In[54]:


SPTV1=pd.concat(SPTV1)


# In[55]:


SPTV1.F2021 = SPTV1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()
SPTV1['F2021'] = SPTV1['F2021'].apply(lambda a: str(a).replace('X','x'))
SPTV1['W2021'] = SPTV1['W2021'].apply(lambda a: str(a).replace('X','x'))
df_merge_SPTV1=pd.merge(SPTV1,df_Fall_2021,left_on='F2021',right_on='CCP',how='left')


# In[56]:


df_merge_SPTV1['LastDigit_PV']=df_merge_SPTV1['W2021'].str.strip().str[-1]


# In[57]:


df_merge_SPTV1=df_merge_SPTV1.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_SPTV1['Tmpl']=df_merge_SPTV1['Tmpl'].fillna(method='ffill')
df_merge_SPTV1['Super']=df_merge_SPTV1['Super'].fillna(method='ffill')
df_merge_SPTV1['Detail3']=df_merge_SPTV1['Detail3'].fillna(method='ffill')


# In[58]:


df_merge_SPTV1=df_merge_SPTV1.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_SPTV1['Category']=df_merge_SPTV1['Category'].fillna(method='ffill')
df_merge_SPTV1['QLevel']=df_merge_SPTV1['QLevel'].fillna(method='ffill')
#df_merge_cable_col1['Detail2']=df_merge_cable_col1['Detail2'].fillna(method='ffill')


# ## Seperate col1 and col2 PV

# In[59]:


#group_data = df.groupby(['Alphabet','Words'])['COUNTER'].sum()
df_PunchMap_col2=df_PunchMap.query('Columns==2')
#df_PunchMap_col2
#df_PunchMap


# ## Taking a look at Punch values 

# In[60]:


df_PunchMap_col1=df_PunchMap.query('Columns==1')
#df_PunchMap_col1


# ## PV_Dataframe grouping with col1 PV 

# In[61]:


PV1={}
grouped1 = df_PunchMap_col1.groupby('Clean_Type')
for group1 in grouped1.groups.keys():
    PV1[group1] = grouped1.get_group(group1)
    #print(group1)


# ## PV_Dataframe grouping with col2 PV 

# In[62]:


PV2={}
grouped2 = df_PunchMap_col2.groupby('Clean_Type')
for group2 in grouped2.groups.keys():
    PV2[group2] = grouped2.get_group(group2)
    #print("list that has col2 PV:",group2)
   


# ## Dataframe grouping on One wave

# In[63]:


df_TV_Movie_onewave=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[64]:


df_TV_Movie_Non_1W=df_TV_Movie.query('OneWave_Suppress!="#"')


# In[65]:


data_1w={}
grouped = df_TV_Movie_onewave.groupby('clean_type')
for group in grouped.groups.keys():
    #print(group)
    data_1w[group] = grouped.get_group(group)


# In[66]:


data_Non_1W={}
grouped = df_TV_Movie_Non_1W.groupby('clean_type')
for group in grouped.groups.keys():
    #print(group)
    data_Non_1W[group] = grouped.get_group(group)


# In[67]:


#data_Non_1W['TV2']


# In[68]:


#PV2['TV1']


# ## TV1 _col1 PV

# In[69]:


PV1_TV1_col1=PV1['TV1']['PunchValue']


# In[70]:


datapv_TV1_col1={}
TV1_col1=[]
for i in PV1_TV1_col1:
    
    datapv_TV1_col1[i]=data['TV1'].copy()

    datapv_TV1_col1[i]['F2021']=datapv_TV1_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV1_col1[i]['W2021']=datapv_TV1_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV1_col1.append(datapv_TV1_col1[i])


# In[71]:


TV1_col1=pd.concat(TV1_col1)


# In[72]:


#TV1_col1.head()


# In[73]:


TV1_col1['F2021'] = TV1_col1['F2021'].apply(lambda a: str(a).replace('X','x'))
TV1_col1['W2021'] = TV1_col1['W2021'].apply(lambda a: str(a).replace('X','x'))


# In[74]:


TV1_col1.F2021 = TV1_col1.F2021.astype(str)
df_Fall_2021.CCP = df_Fall_2021.CCP.astype(str)


# In[75]:



TV1_col1.F2021 = TV1_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[76]:


#TV1.F2021 =TV1.F2021.str.encode('cp1252')


# In[77]:


#TV1.F2021=TV1.F2021.str.replace('b','')


# In[78]:


#df_Fall_2021.CCP = df_Fall_2021.CCP.str.encode('cp1252')
#df_Fall_2021.CCP.dtype


# In[79]:


df_merge_TV1_col1=pd.merge(TV1_col1,df_Fall_2021,left_on=['F2021'],right_on=['CCP'],how='inner')


# In[80]:


#df_merge_TV11=TV1.merge(df_Fall_2021, how='left', left_on='F2021', right_on='CCP',indicator=True)


# ## PV_col2 adding them for TV1

# In[81]:


PV2_TV1_col2=PV2['TV1']['PunchValue']


# In[82]:


data_2={}


# In[83]:


data_2['TV1']=data['TV1'].copy()


# In[84]:


data_2['TV1']['F2021']=data_2['TV1']['F2021'].apply(pd.to_numeric)
data_2['TV1']['W2021']=data_2['TV1']['W2021'].apply(pd.to_numeric)


# In[85]:


data_2['TV1']['F2021']=data_2['TV1']['F2021']+1
data_2['TV1']['W2021']=data_2['TV1']['W2021']+1


# In[86]:


#data_2['TV1']


# In[87]:


data_2['TV1']['F2021']=data_2['TV1']['F2021'].astype(str)
data_2['TV1']['W2021']=data_2['TV1']['W2021'].astype(str)


# In[88]:


datapv_TV1_col2={}
TV1_col2=[]
for i in PV2_TV1_col2:
    
    datapv_TV1_col2[i]=data_2['TV1'].copy()

    datapv_TV1_col2[i]['F2021']=datapv_TV1_col2[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV1_col2[i]['W2021']=datapv_TV1_col2[i].apply(lambda x:x['W2021']+str(i), axis=1)
    datapv_TV1_col2[i]['col2pv']='yes'
    TV1_col2.append(datapv_TV1_col2[i])


# In[89]:


TV1_col2=pd.concat(TV1_col2)
#TV1_col2.head()


# In[90]:


TV1_col2.F2021 = TV1_col2.F2021.astype(str)
df_Fall_2021.CCP = df_Fall_2021.CCP.astype(str)


# In[91]:


TV1_col2.F2021 = TV1_col2.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[92]:


df_merge_TV1_col2=pd.merge(TV1_col2,df_Fall_2021,left_on=['F2021'],right_on=['CCP'],how='inner')


# In[93]:


df_merge_TV1=[df_merge_TV1_col1,df_merge_TV1_col2]


# In[94]:


df_merge_TV1=pd.concat(df_merge_TV1)


# In[95]:


df_merge_TV1['LastDigit_PV']=df_merge_TV1['W2021'].str.strip().str[-1]


# In[96]:


df_merge_TV1=df_merge_TV1.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_TV1['Tmpl']=df_merge_TV1['Tmpl'].fillna(method='ffill')
df_merge_TV1['Super']=df_merge_TV1['Super'].fillna(method='ffill')
df_merge_TV1['Detail3']=df_merge_TV1['Detail3'].fillna(method='ffill')


# In[97]:


df_merge_TV1=df_merge_TV1.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_TV1['Category']=df_merge_TV1['Category'].fillna(method='ffill')
df_merge_TV1['QLevel']=df_merge_TV1['QLevel'].fillna(method='ffill')
#df_merge_TV1['Detail2']=df_merge_TV1['Detail2'].fillna(method='ffill')


# In[98]:


Listheading=df_merge_TV1['Sec_List_Heading'].unique()


# In[99]:



g=df_merge_TV1.groupby('Sec_List_Heading')


# In[100]:


i=0
n=0
df_merge_TV1_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    df_merge_TV1_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas


# In[101]:


n=0
for values in Listheading:
    df_merge_TV1_LH[n]=df_merge_TV1_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    df_merge_TV1_LH[n]['Detail2']=df_merge_TV1_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[102]:


df_merge_TV1_Frames=pd.DataFrame()
df_merge_TV1_Frames = df_merge_TV1_Frames.append([df_merge_TV1_LH[i] for i in range(n)])


# In[103]:


#df_merge_TV1_Frames


# ## PV_col1-TV3

# In[104]:


PV1_TV3_col1=PV1['TV3']['PunchValue']
#PV1_TV3_col1


# In[105]:


datapv_TV3_col1={}
TV3_col1=[]
for i in PV1_TV3_col1:
    
    datapv_TV3_col1[i]=data['TV3'].copy()

    datapv_TV3_col1[i]['F2021']=datapv_TV3_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV3_col1[i]['W2021']=datapv_TV3_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV3_col1.append(datapv_TV3_col1[i])


# In[106]:


TV3_col1=pd.concat(TV3_col1)


# In[107]:


#TV3_col1


# In[108]:



TV3_col1['F2021'] = TV3_col1['F2021'].apply(lambda a: str(a).replace('X','x'))
TV3_col1['W2021'] = TV3_col1['W2021'].apply(lambda a: str(a).replace('X','x'))


# In[109]:



TV3_col1.F2021 = TV3_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[110]:


df_merge_TV3_col1= pd.merge(TV3_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='inner')


# In[111]:


#df_merge_TV3_col1


# ## PV_col2 TV3

# In[112]:


PV2_TV3=PV2['TV3']['PunchValue']


# In[113]:


data_2={}


# In[114]:


data_2['TV3']=data['TV3'].copy()


# In[115]:


data_2['TV3']['F2021']=data_2['TV3']['F2021'].apply(pd.to_numeric)
data_2['TV3']['W2021']=data_2['TV3']['W2021'].apply(pd.to_numeric)


# In[116]:


data_2['TV3']['F2021']=data_2['TV3']['F2021']+1
data_2['TV3']['W2021']=data_2['TV3']['W2021']+1


# In[117]:


data_2['TV3']['F2021']=data_2['TV3']['F2021'].astype(str)
data_2['TV3']['W2021']=data_2['TV3']['W2021'].astype(str)


# In[118]:


datapv_TV3_col2={}
TV3_col2=[]
for i in PV2_TV3:
    
    datapv_TV3_col2[i]=data_2['TV3'].copy()

    datapv_TV3_col2[i]['F2021']=datapv_TV3_col2[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV3_col2[i]['W2021']=datapv_TV3_col2[i].apply(lambda x:x['W2021']+str(i), axis=1)
    datapv_TV3_col2[i]['col2pv']='yes'
    TV3_col2.append(datapv_TV3_col2[i])


# In[119]:


TV3_col2=pd.concat(TV3_col2)
#TV3_col2.head()


# In[120]:


TV3_col2.F2021 = TV3_col2.F2021.astype(str)
df_Fall_2021.CCP = df_Fall_2021.CCP.astype(str)


# In[121]:


TV3_col2.F2021 = TV3_col2.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[122]:


df_merge_TV3_col2=pd.merge(TV3_col2,df_Fall_2021,left_on=['F2021'],right_on=['CCP'],how='inner')


# In[123]:


df_merge_TV3=[df_merge_TV3_col1,df_merge_TV3_col2]


# In[124]:


df_merge_TV3=pd.concat(df_merge_TV3)


# ## TV4 PV_col1

# In[125]:


PV1_TV4_col1=PV1['TV4']['PunchValue']


# In[126]:


#PV1_TV4_col1


# In[127]:


datapv_TV4_col1={}
TV4_col1=[]
for i in PV1_TV4_col1:
    
    datapv_TV4_col1[i]=data['TV4'].copy()

    datapv_TV4_col1[i]['F2021']=datapv_TV4_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV4_col1[i]['W2021']=datapv_TV4_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV4_col1.append(datapv_TV4_col1[i])


# In[128]:


TV4_col1=pd.concat(TV4_col1)


# In[129]:


TV4_col1.F2021 = TV4_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()
df_merge_TV4_col1= pd.merge(TV4_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='inner')


# ## TV4 col2 PV

# In[130]:


PV2_TV4=PV2['TV4']['PunchValue']


# In[131]:


#PV2_TV4


# In[132]:


data_2={}


# In[133]:


data_2['TV4']=data['TV4'].copy()


# In[134]:


data_2['TV4']['F2021']=data_2['TV4']['F2021'].apply(pd.to_numeric)
data_2['TV4']['W2021']=data_2['TV4']['W2021'].apply(pd.to_numeric)


# In[135]:


data_2['TV4']['F2021']=data_2['TV4']['F2021']+1
data_2['TV4']['W2021']=data_2['TV4']['W2021']+1


# In[136]:


data_2['TV4']['F2021']=data_2['TV4']['F2021'].astype(str)
data_2['TV4']['W2021']=data_2['TV4']['W2021'].astype(str)


# In[137]:


datapv_TV4_col2={}
TV4_col2=[]
for i in PV2_TV4:
    
    datapv_TV4_col2[i]=data_2['TV4'].copy()

    datapv_TV4_col2[i]['F2021']=datapv_TV4_col2[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV4_col2[i]['W2021']=datapv_TV4_col2[i].apply(lambda x:x['W2021']+str(i), axis=1)
    datapv_TV4_col2[i]['col2pv']='yes'
    TV4_col2.append(datapv_TV4_col2[i])


# In[138]:


TV4_col2=pd.concat(TV4_col2)


# In[139]:


#TV4_col2


# In[140]:


TV4_col2.F2021 = TV4_col2.F2021.astype(str)
df_Fall_2021.CCP = df_Fall_2021.CCP.astype(str)


# In[141]:



TV4_col2.F2021 = TV4_col2.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[142]:


df_merge_TV4_col2=pd.merge(TV4_col2,df_Fall_2021,left_on=['F2021'],right_on=['CCP'],how='inner')


# In[143]:


#df_merge_TV4_col2


# In[144]:


df_merge_TV4=[df_merge_TV4_col1,df_merge_TV4_col2]


# In[145]:


df_merge_TV4=pd.concat(df_merge_TV4)


# ## TV2 col1_Punch variable

# # It has one wave items so seperated them and adding PV to avoid duplicate values

# In[146]:


PV1_TV2_col1=PV1['TV2']['PunchValue']


# In[147]:


#data['TV2']


# In[148]:


data['TV2'].to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\TV2source.csv',index=False,header=True,encoding='cp1252')


# In[149]:


datapv_TV2_col1={}
TV2_col1=[]
for i in PV1_TV2_col1:
    
    datapv_TV2_col1[i]=data['TV2'].copy()

    datapv_TV2_col1[i]['F2021']=datapv_TV2_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV2_col1[i]['W2021']=datapv_TV2_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV2_col1.append(datapv_TV2_col1[i])


# In[150]:


TV2_col1=pd.concat(TV2_col1)


# In[151]:


#TV2_col1


# In[152]:


#TV2_col1


# In[153]:



TV2_col1.F2021 = TV2_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()
TV2_col1['F2021'] = TV2_col1['F2021'].apply(lambda a: str(a).replace('X','x'))
TV2_col1['W2021'] = TV2_col1['W2021'].apply(lambda a: str(a).replace('X','x'))
df_merge_TV2_col1= pd.merge(TV2_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='inner')


# In[154]:


#df_merge_TV2_col1


# In[155]:


NR_TV2_col1 = pd.merge(TV2_col1,df_merge_TV2_col1, how = 'outer',left_on='F2021',right_on='CCP',indicator=True).loc[lambda x : x['_merge']=='left_only']


# In[156]:


NR_TV2_col1=NR_TV2_col1[['clean_type_x', 'W2021_x', 'Sec_List_Heading_x', 'OneWave_Suppress_x','Initial_wave_x', 'Shows_Name_x', 'F2021_x', 'compare_x', 'col2pv_x']]


# In[157]:


NR_TV2_col1=NR_TV2_col1.rename(columns={'clean_type_x':'clean_type', 'W2021_x':'W2021', 'Sec_List_Heading_x':'Sec_List_Heading', 'Initial_wave_x':'Initial_wave','OneWave_Suppress_x':'OneWave_Suppress', 'Shows_Name_x':'Shows_Name', 'F2021_x':'F2021', 'compare_x':'compare', 'col2pv_x':'col2pv'})


# In[158]:


#NR_TV2_col1.columns


# In[159]:


df_merge_TV2_col1=[df_merge_TV2_col1,NR_TV2_col1]


# In[160]:


df_merge_TV2_col1=pd.concat(df_merge_TV2_col1)


# In[161]:


#df_merge_TV2_col1


# In[162]:


#df_merge_TV2_col1.shape


# ## TV2 col2 PV

# In[163]:


PV2_TV2_col2=PV2['TV2']['PunchValue']


# In[164]:


data_2={}


# In[165]:


data_2['TV2']=data['TV2'].copy()


# In[166]:



data_2['TV2']['F2021']=data_2['TV2']['F2021'].apply(pd.to_numeric)
data_2['TV2']['W2021']=data_2['TV2']['W2021'].apply(pd.to_numeric)


# In[167]:



data_2['TV2']['F2021']=data_2['TV2']['F2021']+1
data_2['TV2']['W2021']=data_2['TV2']['W2021']+1


# In[168]:


#data['TV2']['F2021']


# In[169]:


#data_2['TV2']['F2021']


# In[170]:



data_2['TV2']['F2021']=data_2['TV2']['F2021'].astype(str)
data_2['TV2']['W2021']=data_2['TV2']['W2021'].astype(str)


# In[171]:


#data_2['TV2']


# In[172]:


datapv_TV2_col2={}
TV2_col2=[]
for i in PV2_TV2_col2:
    
    datapv_TV2_col2[i]=data_2['TV2'].copy()

    datapv_TV2_col2[i]['F2021']=datapv_TV2_col2[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV2_col2[i]['W2021']=datapv_TV2_col2[i].apply(lambda x:x['W2021']+str(i), axis=1)
    datapv_TV2_col2[i]['col2pv']='yes'
    TV2_col2.append(datapv_TV2_col2[i])


# In[173]:


TV2_col2=pd.concat(TV2_col2)


# In[174]:


#TV2_col2


# In[175]:


#TV2_col2.nunique()


# In[176]:


TV2_col2.F2021 = TV2_col2.F2021.astype(str)
df_Fall_2021.CCP = df_Fall_2021.CCP.astype(str)


# In[177]:



TV2_col2.F2021 = TV2_col2.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[178]:


df_merge_TV2_col2=pd.merge(TV2_col2,df_Fall_2021,left_on=['F2021'],right_on=['CCP'],how='inner')


# In[179]:


NR_TV2_col2 = pd.merge(TV2_col2,df_merge_TV2_col2, how = 'outer',left_on='F2021',right_on='CCP',indicator=True).loc[lambda x : x['_merge']=='left_only']


# In[180]:


NR_TV2_col2=NR_TV2_col2[['clean_type_x', 'W2021_x', 'Sec_List_Heading_x', 'OneWave_Suppress_x', 'Initial_wave_x','Shows_Name_x', 'F2021_x', 'compare_x', 'col2pv_x']]


# In[181]:



NR_TV2_col2=NR_TV2_col2.rename(columns={'clean_type_x':'clean_type', 'W2021_x':'W2021', 'Sec_List_Heading_x':'Sec_List_Heading', 'OneWave_Suppress_x':'OneWave_Suppress','Initial_wave_x':'Initial_wave', 'Shows_Name_x':'Shows_Name', 'F2021_x':'F2021', 'compare_x':'compare', 'col2pv_x':'col2pv'})


# In[182]:


#NR_TV2_col2


# In[183]:


df_merge_TV2_col2=[df_merge_TV2_col2,NR_TV2_col2]


# In[184]:



df_merge_TV2_col2=pd.concat(df_merge_TV2_col2)


# In[185]:



#df_merge_TV2_col2


# In[186]:


#df_merge_TV2_col2


# In[187]:


df_merge_TV2=[df_merge_TV2_col1,df_merge_TV2_col2]


# In[188]:


df_merge_TV2=pd.concat(df_merge_TV2)


# In[189]:


df_merge_TV2['LastDigit_PV']=df_merge_TV2['W2021'].str.strip().str[-1]


# In[190]:


df_merge_TV2.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\TV2b4fill.csv',index=False,header=True,encoding='cp1252')


# In[191]:


df_merge_TV2_tmpl3=df_merge_TV2.query("Shows_Name=='Litton Weekend Adventure net (includes Free Enterprise, Hearts of Heroes, Oh Baby, Outback Adventures)'|Shows_Name=='CBS Dream Team net (includes Hope In The Wild, Innovation Nation, Lucky Dog, Mission Unstoppable)'")
#df.query("users=='rachel' | users=='jeff'")


# In[192]:


df_merge_TV2_tmpl3


# In[193]:


df_merge_TV2_tmpl3 = df_merge_TV2_tmpl3.dropna(subset=['Category'])


# In[194]:


#df_merge_TV2_tmpl3


# In[195]:


#df_merge_TV2_tmpl2=df_merge_TV2.query('Tmpl!="3"')
df_merge_TV2_tmpl_not3=df_merge_TV2.query("Shows_Name!='Litton Weekend Adventure net (includes Free Enterprise, Hearts of Heroes, Oh Baby, Outback Adventures)'& Shows_Name!='CBS Dream Team net (includes Hope In The Wild, Innovation Nation, Lucky Dog, Mission Unstoppable)'")
#df.query("users=='rachel' | users=='jeff'")


# In[196]:


#df_merge_TV2_tmpl_not3.shape


# In[197]:


df_merge_TV2=df_merge_TV2_tmpl_not3.copy()


# In[198]:


#df_merge_TV2


# In[199]:


df_merge_TV2=df_merge_TV2.sort_values(['col2pv','Sec_List_Heading','Tmpl','Category'], 
               ascending=[True,True,True,True],na_position='last')
df_merge_TV2['Category']=df_merge_TV2['Category'].fillna(method='ffill')
df_merge_TV2['QLevel']=df_merge_TV2['QLevel'].fillna(method='ffill')
df_merge_TV2['Tmpl']=df_merge_TV2['Tmpl'].fillna(method='ffill')
#df_merge_TV2['Detail2']=df_merge_TV2['Detail2'].fillna(method='ffill')


# In[200]:


df_merge_TV2=df_merge_TV2.sort_values(['col2pv','Sec_List_Heading','LastDigit_PV','Detail3'], 
               ascending=[True,True,True,True],na_position='last')
						  

df_merge_TV2['Super']=df_merge_TV2['Super'].fillna(method='ffill')
df_merge_TV2['Detail3']=df_merge_TV2['Detail3'].fillna(method='ffill')


# In[201]:


Listheading=df_merge_TV2['Sec_List_Heading'].unique()


# In[202]:


g=df_merge_TV2.groupby('Sec_List_Heading')


# In[203]:


i=0
n=0
df_merge_TV2_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    df_merge_TV2_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas


# In[204]:


n=0
for values in Listheading:
    df_merge_TV2_LH[n]=df_merge_TV2_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    df_merge_TV2_LH[n]['Detail2']=df_merge_TV2_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[205]:


df_merge_TV2_Frames=pd.DataFrame()
df_merge_TV2_Frames = df_merge_TV2_Frames.append([df_merge_TV2_LH[i] for i in range(n)])


# In[206]:


df_merge_TV2_Frames=[df_merge_TV2_Frames,df_merge_TV2_tmpl3]


# In[207]:


df_merge_TV2_Frames=pd.concat(df_merge_TV2_Frames)


# In[208]:


df_merge_TV2_Frames=df_merge_TV2_Frames.drop_duplicates(subset='W2021',keep='last')


# In[209]:


df_merge_TV2_Frames.shape


# In[210]:


df_merge_TV2_Frames.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\TV2.csv',index=False,header=True,encoding='cp1252')


# ## SPTV2

# In[211]:


PV1_SPTV2_col1=PV1['SPTV2']['PunchValue']


# In[212]:


datapv_SPTV2_col1={}
SPTV2_col1=[]
for i in PV1_SPTV2_col1:
    
    datapv_SPTV2_col1[i]=data['SPTV2'].copy()

    datapv_SPTV2_col1[i]['F2021']=datapv_SPTV2_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV2_col1[i]['W2021']=datapv_SPTV2_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    SPTV2_col1.append(datapv_SPTV2_col1[i])


# In[213]:


SPTV2_col1=pd.concat(SPTV2_col1)


# In[214]:



SPTV2_col1.F2021 = SPTV2_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[215]:


SPTV2_col1['F2021'] = SPTV2_col1['F2021'].apply(lambda a: str(a).replace('X','x'))
SPTV2_col1['W2021'] = SPTV2_col1['W2021'].apply(lambda a: str(a).replace('X','x'))


# In[216]:


df_merge_SPTV2_col1= pd.merge(SPTV2_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[217]:


df_merge_SPTV2_col1['LastDigit_PV']=df_merge_SPTV2_col1['W2021'].str.strip().str[-1]


# In[218]:



df_merge_SPTV2_col1=df_merge_SPTV2_col1.sort_values(['Sec_List_Heading'],ascending=[True])
df_merge_SPTV2_col1['Category']=df_merge_SPTV2_col1['Category'].fillna(method='ffill')
df_merge_SPTV2_col1['QLevel']=df_merge_SPTV2_col1['QLevel'].fillna(method='ffill')
df_merge_SPTV2_col1['Tmpl']=df_merge_SPTV2_col1['Tmpl'].fillna(method='ffill')
df_merge_SPTV2_col1['Super']=df_merge_SPTV2_col1['Super'].fillna(method='ffill')
#df_merge_cable_col1['Detail2']=df_merge_cable_col1['Detail2'].fillna(method='ffill')


# In[219]:


df_merge_SPTV2_col1['Tmpl']=df_merge_SPTV2_col1['Tmpl'].fillna(2)


# In[220]:


df_merge_SPTV2_col1['Super']=df_merge_SPTV2_col1['Super'].fillna('Media - Television')


# In[221]:


df_merge_SPTV2_col1=df_merge_SPTV2_col1.sort_values(['LastDigit_PV','Detail3'],ascending=[True,True],na_position = 'last')

df_merge_SPTV2_col1['Detail3']=df_merge_SPTV2_col1['Detail3'].fillna(method='ffill')


# In[222]:


#df_merge_SPTV2_col1


# In[223]:



#df_merge_SPTV2_col1['Detail3']=df_merge_SPTV2_col1['Detail3'].fillna('Watch 1 time a month')


# In[224]:


df_merge_SPTV2_col1['QLevel']=df_merge_SPTV2_col1['QLevel'].fillna(4)


# In[225]:


df_merge_SPTV2_col1['Category']=df_merge_SPTV2_col1['Category'].fillna('Spanish Television: Once A Week Programs')


# In[226]:


#df_merge_SPTV2_col1


# ## SPTV3

# In[227]:


PV1_SPTV3_col1=PV1['SPTV3']['PunchValue']


# In[228]:


datapv_SPTV3_col1={}
SPTV3_col1=[]
for i in PV1_SPTV3_col1:
    
    datapv_SPTV3_col1[i]=data['SPTV3'].copy()

    datapv_SPTV3_col1[i]['F2021']=datapv_SPTV3_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV3_col1[i]['W2021']=datapv_SPTV3_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    SPTV3_col1.append(datapv_SPTV3_col1[i])


# In[229]:


SPTV3_col1=pd.concat(SPTV3_col1)


# In[230]:


SPTV3_col1.F2021 = SPTV3_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[231]:


SPTV3_col1['F2021'] = SPTV3_col1['F2021'].apply(lambda a: str(a).replace('X','x'))
SPTV3_col1['W2021'] = SPTV3_col1['W2021'].apply(lambda a: str(a).replace('X','x'))


# In[232]:


df_merge_SPTV3_col1= pd.merge(SPTV3_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[233]:


#df_merge_SPTV3_col1


# ## SPTV5 

# In[234]:


PV1_SPTV5_col1=PV1['SPTV5']['PunchValue']


# In[235]:


datapv_SPTV5_col1={}
SPTV5_col1=[]
for i in PV1_SPTV5_col1:
    
    datapv_SPTV5_col1[i]=data['SPTV5'].copy()

    datapv_SPTV5_col1[i]['F2021']=datapv_SPTV5_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV5_col1[i]['W2021']=datapv_SPTV5_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    SPTV5_col1.append(datapv_SPTV5_col1[i])


# In[236]:


SPTV5_col1=pd.concat(SPTV5_col1)


# In[237]:


SPTV5_col1.F2021 = SPTV5_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[238]:



df_merge_SPTV5_col1= pd.merge(SPTV5_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[239]:


df_merge_SPTV5_col1['Shows_Name'] = df_merge_SPTV5_col1.apply(lambda x: x['Sec_List_Heading']+': '+x['Shows_Name']  if x['OneWave_Suppress']!='#' else x['Shows_Name'], axis=1)


# In[240]:


df_merge_SPTV5_col1['Shows_Name'] = df_merge_SPTV5_col1.apply(lambda x: x['Shows_Name'].lstrip("#")  if x['OneWave_Suppress']=='#' else x['Shows_Name'], axis=1)


# In[241]:


df_merge_SPTV5_col1['Shows_Name'] = df_merge_SPTV5_col1.apply(lambda x:'#'+ x['Sec_List_Heading']+': '+x['Shows_Name']  if x['OneWave_Suppress']=='#' else x['Shows_Name'], axis=1)


# ## TV5 

# In[242]:


PV1_TV5_col1=PV1['TV5']['PunchValue']


# In[243]:


datapv_TV5_col1={}
TV5_col1=[]
for i in PV1_TV5_col1:
    
    datapv_TV5_col1[i]=data['TV5'].copy()

    datapv_TV5_col1[i]['F2021']=datapv_TV5_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV5_col1[i]['W2021']=datapv_TV5_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV5_col1.append(datapv_TV5_col1[i])
	


# In[244]:


TV5_col1=pd.concat(TV5_col1)


# In[245]:


TV5_col1.F2021 = TV5_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[246]:


df_merge_TV5_col1= pd.merge(TV5_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[247]:


#df_merge_TV5_col1


# In[248]:


df_merge_TV5=df_merge_TV5_col1.copy()


# In[249]:


df_merge_TV5['LastDigit_PV']=df_merge_TV5['W2021'].str.strip().str[-1]


# In[250]:


df_merge_TV5=df_merge_TV5.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_TV5['Tmpl']=df_merge_TV5['Tmpl'].fillna(method='ffill')
df_merge_TV5['Super']=df_merge_TV5['Super'].fillna(method='ffill')
df_merge_TV5['Detail3']=df_merge_TV5['Detail3'].fillna(method='ffill')


# In[251]:


df_merge_TV5=df_merge_TV5.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_TV5['Category']=df_merge_TV5['Category'].fillna(method='ffill')
df_merge_TV5['QLevel']=df_merge_TV5['QLevel'].fillna(method='ffill')
#df_merge_TV5['Detail2']=df_merge_TV5['Detail2'].fillna(method='ffill')


# In[252]:


Listheading=df_merge_TV5['Sec_List_Heading'].unique()


# In[253]:


g=df_merge_TV5.groupby('Sec_List_Heading')


# In[254]:


i=0
n=0
df_merge_TV5_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    df_merge_TV5_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas


# In[255]:



n=0
for values in Listheading:
    df_merge_TV5_LH[n]=df_merge_TV5_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    df_merge_TV5_LH[n]['Detail2']=df_merge_TV5_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF


# In[256]:


df_merge_TV5_Frames=pd.DataFrame()


# In[257]:


df_merge_TV5_Frames = df_merge_TV5_Frames.append([df_merge_TV5_LH[i] for i in range(n)])


# ## TV6 

# In[258]:


PV1_TV6_col1=PV1['TV6']['PunchValue']


# In[259]:


datapv_TV6_col1={}
TV6_col1=[]
for i in PV1_TV6_col1:
    
    datapv_TV6_col1[i]=data['TV6'].copy()

    datapv_TV6_col1[i]['F2021']=datapv_TV6_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV6_col1[i]['W2021']=datapv_TV6_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV6_col1.append(datapv_TV6_col1[i])


# In[260]:


TV6_col1=pd.concat(TV6_col1)


# In[261]:



TV6_col1.F2021 = TV6_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[262]:


df_merge_TV6_col1= pd.merge(TV6_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[263]:


df_merge_TV6=df_merge_TV6_col1.copy()


# In[264]:


df_merge_TV6['LastDigit_PV']=df_merge_TV6['W2021'].str.strip().str[-1]


# In[265]:


df_merge_TV6=df_merge_TV6.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_TV6['Tmpl']=df_merge_TV6['Tmpl'].fillna(method='ffill')
df_merge_TV6['Super']=df_merge_TV6['Super'].fillna(method='ffill')
df_merge_TV6['Detail3']=df_merge_TV6['Detail3'].fillna(method='ffill')


# In[266]:



df_merge_TV6=df_merge_TV6.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_TV6['Category']=df_merge_TV6['Category'].fillna(method='ffill')
df_merge_TV6['QLevel']=df_merge_TV6['QLevel'].fillna(method='ffill')


# ## Movies 

# In[267]:


PV1_movies_col1=PV1['movies']['PunchValue']


# In[268]:


datapv_movies_col1={}
movies_col1=[]
for i in PV1_movies_col1:
    
    datapv_movies_col1[i]=data['Movie'].copy()

    datapv_movies_col1[i]['F2021']=datapv_movies_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_movies_col1[i]['W2021']=datapv_movies_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    movies_col1.append(datapv_movies_col1[i])
	


# In[269]:


movies_col1=pd.concat(movies_col1)


# In[270]:


movies_col1.F2021 = movies_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[271]:


df_merge_movies_col1= pd.merge(movies_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[272]:


df_merge_movies_col1['LastDigit_PV']=df_merge_movies_col1['W2021'].str.strip().str[-1]


# In[273]:


df_merge_movies_col1=df_merge_movies_col1.sort_values(['LastDigit_PV'],ascending=[True])
						  
df_merge_movies_col1['Tmpl']=df_merge_movies_col1['Tmpl'].fillna(method='ffill')
df_merge_movies_col1['Super']=df_merge_movies_col1['Super'].fillna(method='ffill')
df_merge_movies_col1['Detail3']=df_merge_movies_col1['Detail3'].fillna(method='ffill')


# In[274]:


df_merge_movies_col1=df_merge_movies_col1.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_movies_col1['Category']=df_merge_movies_col1['Category'].fillna(method='ffill')
df_merge_movies_col1['QLevel']=df_merge_movies_col1['QLevel'].fillna(method='ffill')
df_merge_movies_col1['Detail2']=df_merge_movies_col1['Detail2'].fillna(method='ffill')


# ## Cable

# In[275]:


PV1_cable_col1=PV1['cable']['PunchValue']


# In[276]:


datapv_cable_col1={}
cable_col1=[]
for i in PV1_cable_col1:
    
    datapv_cable_col1[i]=data['cable'].copy()

    datapv_cable_col1[i]['F2021']=datapv_cable_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_cable_col1[i]['W2021']=datapv_cable_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    cable_col1.append(datapv_cable_col1[i])


# In[277]:


cable_col1=pd.concat(cable_col1)


# In[278]:


cable_col1.F2021 = cable_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[279]:



df_merge_cable_col1= pd.merge(cable_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[280]:


df_merge_cable_col1['LastDigit_PV']=df_merge_cable_col1['W2021'].str.strip().str[-1]


# In[281]:


df_merge_cable_col1=df_merge_cable_col1.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_cable_col1['Tmpl']=df_merge_cable_col1['Tmpl'].fillna(method='ffill')
df_merge_cable_col1['Super']=df_merge_cable_col1['Super'].fillna(method='ffill')
df_merge_cable_col1['Detail3']=df_merge_cable_col1['Detail3'].fillna(method='ffill')


# In[282]:


df_merge_cable_col1=df_merge_cable_col1.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_cable_col1['Category']=df_merge_cable_col1['Category'].fillna(method='ffill')
df_merge_cable_col1['QLevel']=df_merge_cable_col1['QLevel'].fillna(method='ffill')
#df_merge_cable_col1['Detail2']=df_merge_cable_col1['Detail2'].fillna(method='ffill')


# In[283]:


#df_merge_cable_col1.columns


# In[284]:


df_merge_cable_col1['Shows_Name'] = df_merge_cable_col1.apply(lambda x: x['Sec_List_Heading']+': '+x['Shows_Name']  if x['OneWave_Suppress']!='#' else x['Shows_Name'], axis=1)


# In[285]:


df_merge_cable_col1['Shows_Name'] = df_merge_cable_col1.apply(lambda x: x['Shows_Name'].lstrip("#")  if x['OneWave_Suppress']=='#' else x['Shows_Name'], axis=1)
#df_merge_cable_col1['Shows_Name'] = df_merge_cable_col1['Shows_Name'].lstrip("#")

#lambda x:x['Category'].replace(r'- Net','',regex=True)


# In[286]:


df_merge_cable_col1['Shows_Name'] = df_merge_cable_col1.apply(lambda x:'#'+ x['Sec_List_Heading']+': '+x['Shows_Name']  if x['OneWave_Suppress']=='#' else x['Shows_Name'], axis=1)


# ## Concat all DF

# In[287]:


df_all=[df_merge_TV1_Frames,
        df_merge_TV3,
        df_merge_TV2_Frames,
        df_merge_TV4,
        df_merge_TV5_Frames,
        df_merge_TV6,
        df_merge_SPTV1,
        df_merge_SPTV2_col1,
        df_merge_SPTV3_col1,
        df_merge_SPTV4,
        df_merge_SPTV5_col1,
        df_merge_SPTV51,
        df_merge_movies_col1,
        df_merge_cable_col1,      
        df_merge_add_cab]


# In[288]:


df_all=pd.concat(df_all)


# In[289]:


#display(df_all.head())


# In[290]:


df_all.drop(['StatisticID', 'CatSynID','NoteID','statusid'], axis=1, inplace=True)


# In[291]:


df_all['EditedBy']='codebookcreator'
df_all['EditedDate']=pd.to_datetime('today')
df_all['StudyEntryID']=434
df_all['VersionID']=0
df_all['SID']=1913


# In[292]:


df_all['Status']='Add'


# In[293]:


df_all['Definition'] = df_all.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[294]:


df_all['Definition']=df_all['Definition'].fillna('0')


# In[295]:


#df_all


# In[296]:


df_all['UCode']=df_all['UCode'].fillna('U0')
df_all['QuestionID']=df_all['QuestionID'].fillna(0)
df_all['QUESTID']=df_all['QUESTID'].fillna(0)
df_all['SDID']=df_all['SDID'].fillna(0)
df_all['Initial_wave']=df_all['Initial_wave'].replace(r'nan',np.nan, regex=True)
df_all['Initial_wave']=df_all['Initial_wave'].fillna(0)


# In[297]:


#df_all['Initial_wave'].unique()


# In[298]:


#df_all['Initial_wave']=df_all['Initial_wave'].replace(r'W', '', regex=True)


# In[299]:


df_all['StudyAnswerID']=0


# In[300]:


df_all['Full_Label']=''
df_all['ORD']=''


# In[301]:


#df_all['wave']=df_all['wave'].fillna(0)
df_all['AnswerID']=df_all['AnswerID'].fillna(0)


# In[302]:


df_all['Imported']=''
df_all['Min']=''
df_all['Max']=''


# In[303]:


df_all=df_all.sort_values(['Category','Detail1','Detail3'],ascending=[True,True,True])


# In[304]:


#df_all.isna().value_counts()


# In[305]:


#df_all = df_all.astype( {"QLevel":'int32', "QUESTID":'int32', "AnswerID":'int32',"QuestionID":'int32',"SID":'int64', "SDID":'int32', "VersionID":'int32', "Wave":'int32', "Min":'float',"Max":'float', "StudyEntryID":'int64',"Imported":'bool'} )


# In[306]:


df_all.to_csv(r"C:\Users\saraswathy.rajaman\Documents\df_all.csv",index=False,header=True,encoding='cp1252')


# In[307]:


df_all.drop(['clean_type', 'Detail1','F2021','compare','col2pv','LastDigit_PV','QID','CCP','Wave'], axis=1, inplace=True)


# In[308]:


df_all.rename(columns={'W2021':'CCP','Shows_Name':'Detail1','VersionID':'Version','Initial_wave':'Wave'},inplace=True)


# In[309]:


#df_all


# In[310]:


#df_all.Imported.isna().value_counts()


# In[311]:


df_all=df_all[["StudyEntryID","SID","Version","Category","Super","Tmpl","Time Period","Detail1","Detail2",
"Detail3","Detail4","UCode","Definition","CCP","ORD","Wave","Status","Full_Label","QLevel","QUESTID","AnswerID","EditedBy","EditedDate","SDID",
"StudyAnswerID","QuestionID","Imported","Min","Max"]]


# In[312]:


df_all['Max'] =df_all['Max'].apply(pd.to_numeric)
df_all['Min'] =df_all['Min'].apply(pd.to_numeric)


# In[313]:


#df_all.info()
df_all['Wave']=df_all['Wave'].fillna(0)
#df_all['Wave'].isna().value_counts()


# In[314]:


#df_all.shape


# #df_all.Wave.dtype()
# df_all['Wave'] = pd.to_numeric(df_all['Wave'], errors="coerce")

# df_all['Wave'] =df_all['Wave'].astype(int)

# In[315]:


#df_all.Tmpl.isna().value_counts()


# In[316]:


df_all = df_all.astype( {"QLevel":'int32',
                         "QUESTID":'int32',
                         "AnswerID":'int32',
                         "QuestionID":'int64', 
                         "SDID":'int32', 
                         "Version":'int32', 
                         "Min":'float',
                         "Max":'float', 
                         "StudyEntryID":'int64',
                         "Imported":'bool',
                         "Tmpl":'int64',
                         "Wave":'int32',
                         "StudyAnswerID":'int32'} )


# In[317]:


#df_all.info()


# In[318]:


df_all=df_all.sort_values(['Category','Detail1','Detail3'],ascending=[True,True,True])


# In[319]:


df_all.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Winter-2021.csv',index=False,header=True,encoding='cp1252')


# In[320]:


from sqlalchemy import create_engine
#engine = create_engine('sqlite://', echo=False)


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
    df_all.to_sql(name="tmp_EditedRecords_Hold_test1",con=engine,schema="dbo",if_exists='replace', chunksize=1000,index=False)
#df.to_sql('db_table2', engine, if_exists='replace')


# In[ ]:




