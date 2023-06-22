#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Libraries-and-Display-settings" data-toc-modified-id="Libraries-and-Display-settings-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Libraries and Display settings</a></span></li><li><span><a href="#Load-the-file-from-Excel-sheet" data-toc-modified-id="Load-the-file-from-Excel-sheet-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Load the file from Excel sheet</a></span></li><li><span><a href="#Drop-First-row" data-toc-modified-id="Drop-First-row-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Drop First row</a></span></li><li><span><a href="#Fix-column-names" data-toc-modified-id="Fix-column-names-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Fix column names</a></span></li><li><span><a href="#add-compare-column-to-compare-S2022-and-F2021" data-toc-modified-id="add-compare-column-to-compare-S2022-and-F2021-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>add compare column to compare S2022 and F2021</a></span></li><li><span><a href="#Remove-*-from-S2022-and-F2020" data-toc-modified-id="Remove-*-from-S2022-and-F2020-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Remove * from S2022 and F2020</a></span></li><li><span><a href="#Remove-X-in-onewave/Suppress-column" data-toc-modified-id="Remove-X-in-onewave/Suppress-column-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Remove X in onewave/Suppress column</a></span></li><li><span><a href="#forward-fill-cleantype-and-list-heading" data-toc-modified-id="forward-fill-cleantype-and-list-heading-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>forward fill cleantype and list heading</a></span></li><li><span><a href="#Remove-b-from-sec-list-heading" data-toc-modified-id="Remove-b-from-sec-list-heading-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Remove b from sec list heading</a></span></li><li><span><a href="#Few-items-has-#-in-sec-heading--add-#-in-one-wave-column-for-them" data-toc-modified-id="Few-items-has-#-in-sec-heading--add-#-in-one-wave-column-for-them-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Few items has # in sec heading- add # in one wave column for them</a></span></li><li><span><a href="#For-one-wave-item-append-#-in-show-names" data-toc-modified-id="For-one-wave-item-append-#-in-show-names-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>For one wave item append # in show names</a></span></li><li><span><a href="#Remove-#-from-List-heading-or-sec-heading-values" data-toc-modified-id="Remove-#-from-List-heading-or-sec-heading-values-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Remove # from List heading or sec heading values</a></span></li><li><span><a href="#Group-TVmedia-as-different-Dataframe-on-cleantype" data-toc-modified-id="Group-TVmedia-as-different-Dataframe-on-cleantype-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>Group TVmedia as different Dataframe on cleantype</a></span></li><li><span><a href="#Add-Cable-PV" data-toc-modified-id="Add-Cable-PV-14"><span class="toc-item-num">14&nbsp;&nbsp;</span>Add Cable PV</a></span></li><li><span><a href="#SPTV4-Punch-Values-append" data-toc-modified-id="SPTV4-Punch-Values-append-15"><span class="toc-item-num">15&nbsp;&nbsp;</span>SPTV4 Punch Values append</a></span></li><li><span><a href="#SPTV51-Punch-Values-append" data-toc-modified-id="SPTV51-Punch-Values-append-16"><span class="toc-item-num">16&nbsp;&nbsp;</span>SPTV51 Punch Values append</a></span></li><li><span><a href="#SPTV1" data-toc-modified-id="SPTV1-17"><span class="toc-item-num">17&nbsp;&nbsp;</span>SPTV1</a></span></li><li><span><a href="#Seperate-col1-and-col2-PV" data-toc-modified-id="Seperate-col1-and-col2-PV-18"><span class="toc-item-num">18&nbsp;&nbsp;</span>Seperate col1 and col2 PV</a></span></li><li><span><a href="#Taking-a-look-at-Punch-values" data-toc-modified-id="Taking-a-look-at-Punch-values-19"><span class="toc-item-num">19&nbsp;&nbsp;</span>Taking a look at Punch values</a></span></li><li><span><a href="#PV_Dataframe-grouping-with-col1-PV" data-toc-modified-id="PV_Dataframe-grouping-with-col1-PV-20"><span class="toc-item-num">20&nbsp;&nbsp;</span>PV_Dataframe grouping with col1 PV</a></span></li><li><span><a href="#PV_Dataframe-grouping-with-col2-PV" data-toc-modified-id="PV_Dataframe-grouping-with-col2-PV-21"><span class="toc-item-num">21&nbsp;&nbsp;</span>PV_Dataframe grouping with col2 PV</a></span></li><li><span><a href="#Dataframe-grouping-on-One-wave" data-toc-modified-id="Dataframe-grouping-on-One-wave-22"><span class="toc-item-num">22&nbsp;&nbsp;</span>Dataframe grouping on One wave</a></span></li><li><span><a href="#TV1-_col1-PV" data-toc-modified-id="TV1-_col1-PV-23"><span class="toc-item-num">23&nbsp;&nbsp;</span>TV1 _col1 PV</a></span></li><li><span><a href="#PV_col2-adding-them-for-TV1" data-toc-modified-id="PV_col2-adding-them-for-TV1-24"><span class="toc-item-num">24&nbsp;&nbsp;</span>PV_col2 adding them for TV1</a></span></li><li><span><a href="#PV_col1-TV3" data-toc-modified-id="PV_col1-TV3-25"><span class="toc-item-num">25&nbsp;&nbsp;</span>PV_col1-TV3</a></span></li><li><span><a href="#PV_col2-TV3" data-toc-modified-id="PV_col2-TV3-26"><span class="toc-item-num">26&nbsp;&nbsp;</span>PV_col2 TV3</a></span></li><li><span><a href="#TV4-PV_col1" data-toc-modified-id="TV4-PV_col1-27"><span class="toc-item-num">27&nbsp;&nbsp;</span>TV4 PV_col1</a></span></li><li><span><a href="#TV4-col2-PV" data-toc-modified-id="TV4-col2-PV-28"><span class="toc-item-num">28&nbsp;&nbsp;</span>TV4 col2 PV</a></span></li><li><span><a href="#TV2-col1_Punch-variable" data-toc-modified-id="TV2-col1_Punch-variable-29"><span class="toc-item-num">29&nbsp;&nbsp;</span>TV2 col1_Punch variable</a></span></li><li><span><a href="#TV2-col2-PV" data-toc-modified-id="TV2-col2-PV-30"><span class="toc-item-num">30&nbsp;&nbsp;</span>TV2 col2 PV</a></span></li><li><span><a href="#SPTV2" data-toc-modified-id="SPTV2-31"><span class="toc-item-num">31&nbsp;&nbsp;</span>SPTV2</a></span></li><li><span><a href="#SPTV3" data-toc-modified-id="SPTV3-32"><span class="toc-item-num">32&nbsp;&nbsp;</span>SPTV3</a></span></li><li><span><a href="#SPTV5" data-toc-modified-id="SPTV5-33"><span class="toc-item-num">33&nbsp;&nbsp;</span>SPTV5</a></span></li><li><span><a href="#TV5" data-toc-modified-id="TV5-34"><span class="toc-item-num">34&nbsp;&nbsp;</span>TV5</a></span></li><li><span><a href="#TV6" data-toc-modified-id="TV6-35"><span class="toc-item-num">35&nbsp;&nbsp;</span>TV6</a></span></li><li><span><a href="#Movies" data-toc-modified-id="Movies-36"><span class="toc-item-num">36&nbsp;&nbsp;</span>Movies</a></span></li><li><span><a href="#Cable" data-toc-modified-id="Cable-37"><span class="toc-item-num">37&nbsp;&nbsp;</span>Cable</a></span></li><li><span><a href="#Concat-all-DF" data-toc-modified-id="Concat-all-DF-38"><span class="toc-item-num">38&nbsp;&nbsp;</span>Concat all DF</a></span></li></ul></div>

# ## Libraries and Display settings

# In[52]:


#import Necessary Library
import pandas as pd
import numpy as np
from openpyxl import Workbook
import re


# In[53]:


import warnings
warnings.filterwarnings("ignore")


# In[54]:


#Display settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)


# ## Load the file from Excel sheet

# In[55]:


df_TV_Movie = pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\MasterMaps.xlsx', sheet_name='TV_Movie')


# In[56]:


df_PunchMap = pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\MasterMaps.xlsx', sheet_name='PunchMap')


# In[57]:


df_Fall_2021 = pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\F2021_v32.xlsx', )


# In[58]:


df_TV_showtypes = pd.read_excel('C:\\Users\\saraswathy.rajaman\\Downloads\\MasterMaps.xlsx', sheet_name='TVshowTypes')


# ## Drop First row

# In[59]:


df_TV_Movie=df_TV_Movie.drop(0)


# ## Fix column names

# In[60]:


df_TV_Movie=df_TV_Movie.rename(columns={'S2022':'W2021','Line Type':'Line_Type','clean type':'clean_type','Unnamed: 6':'Sec_List_Heading','Unnamed: 7':'OneWave_Suppress','Unnamed: 8':'Shows_Name',})


# ## add compare column to compare S2022 and F2021

# In[61]:


df_TV_Movie['compare'] = (df_TV_Movie['W2021'] == df_TV_Movie['F2021'])


# In[62]:


df_TV_Movie['col2pv'] = ''


# ## Remove * from S2022 and F2020

# In[63]:


#Removing spl character
df_TV_Movie['W2021']=df_TV_Movie['W2021'].str.replace('*','')
df_TV_Movie['F2021']=df_TV_Movie['F2021'].str.replace('*','')


# ## Remove X in onewave/Suppress column

# In[64]:


df_TV_Movie.drop(df_TV_Movie.index[df_TV_Movie['OneWave_Suppress'] == 'X'], inplace = True)


# ## forward fill cleantype and list heading 

# In[65]:


df_TV_Movie=df_TV_Movie.copy()
df_TV_Movie['clean_type']=df_TV_Movie['clean_type'].fillna(method='ffill')
#Forward fill cleatype as show


# ## Remove b from sec list heading

# In[66]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].replace('b', np.nan)


# In[67]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].replace(r'^\s*$', np.nan, regex=True)


# In[68]:


df_TV_Movie['Sec_List_Heading']=df_TV_Movie['Sec_List_Heading'].fillna(method='ffill')


# ## Few items has # in sec heading- add # in one wave column for them 

# In[69]:


df_TV_Movie['Shows_Name']=df_TV_Movie['Shows_Name'].astype(str)


# ## For one wave item append # in show names

# In[70]:


df_TV_Movie['Shows_Name'] = df_TV_Movie.apply(lambda x: '#'+x['Shows_Name']  if x['OneWave_Suppress']=='#' else x['Shows_Name'], axis=1)


# ## Remove # from List heading or sec heading values

# In[71]:


df_TV_Movie['Sec_List_Heading'] = df_TV_Movie['Sec_List_Heading'].apply(lambda a: str(a).replace('#',''))


# In[72]:


df_TV_Movie['wave'] = df_TV_Movie['wave'].apply(lambda a: str(a).replace('W',''))


# In[73]:


df_TV_Movie=df_TV_Movie.dropna(subset=['W2021'])


# In[74]:


df_TV_Movie.to_csv(r'C:\Users\saraswathy.rajaman\Documents\df_TV_Moviespr.csv',index=False,header=True,encoding='cp1252')


# In[75]:


df_TV_Movie.columns


# In[76]:


df_TV_Movie=df_TV_Movie[['clean_type','W2021','Sec_List_Heading', 'OneWave_Suppress', 'Shows_Name','wave',
'F2021','compare','col2pv']]


# In[77]:


df_TV_Movie=df_TV_Movie.rename(columns={'wave':'Initial_wave'})
df_TV_Movie['Initial_wave']=df_TV_Movie['Initial_wave'].replace(r'nan',np.nan, regex=True)


# ## Group TVmedia as different Dataframe on cleantype

# In[78]:


#group data based on cleantype into different dataframes
data={}
grouped = df_TV_Movie.groupby('clean_type')
for group in grouped.groups.keys():
    #print(group)
    data[group] = grouped.get_group(group)
    


# In[79]:


#data['add_cabl']


# In[80]:


df_PunchMap=df_PunchMap.rename(columns={'Clean Type':'Clean_Type'})


# In[81]:


#group_data = df.groupby(['Alphabet','Words'])['COUNTER'].sum()
PV={}
grouped = df_PunchMap.groupby('Clean_Type')
for group in grouped.groups.keys():
    #print(group)
    PV[group] = grouped.get_group(group)


# ## Add Cable PV 

# In[82]:


#PV['add_cable']


# In[83]:


Punch_variable=PV['add_cable']['PunchValue']


# In[84]:


#data['add_cabl']['F2021']=data['add_cabl'].apply(lambda x:x['F2021']+'1', axis=1)


# In[85]:


datapv={}
add_cab=[]
for i in Punch_variable:
   
    datapv[i]=data['add_cabl'].copy()

    datapv[i]['F2021']=datapv[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv[i]['W2021']=datapv[i].apply(lambda x:x['W2021']+str(i), axis=1)
    
    add_cab.append(datapv[i])
    
    


# In[86]:


add_cab=pd.concat(add_cab)


# In[87]:


df_merge_add_cab= pd.merge(add_cab, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[88]:


df_merge_add_cab['LastDigit_PV']=df_merge_add_cab['W2021'].str.strip().str[-1]


# In[89]:


df_merge_add_cab=df_merge_add_cab.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_add_cab['Tmpl']=df_merge_add_cab['Tmpl'].fillna(method='ffill')
df_merge_add_cab['Super']=df_merge_add_cab['Super'].fillna(method='ffill')
df_merge_add_cab['Detail3']=df_merge_add_cab['Detail3'].fillna(method='ffill')


# In[90]:


df_merge_add_cab=df_merge_add_cab.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_add_cab['Category']=df_merge_add_cab['Category'].fillna(method='ffill')
df_merge_add_cab['QLevel']=df_merge_add_cab['QLevel'].fillna(method='ffill')
df_merge_add_cab['Detail2']=df_merge_add_cab['Detail2'].fillna(method='ffill')


# ## SPTV4 Punch Values append

# In[91]:


PV_SPTV4=PV['SPTV4']['PunchValue']


# In[92]:


datapv_SPTV4={}
SPTV4=[]
for i in PV_SPTV4:
    
    datapv_SPTV4[i]=data['SPTV4'].copy()

    datapv_SPTV4[i]['F2021']=datapv_SPTV4[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV4[i]['W2021']=datapv_SPTV4[i].apply(lambda x:x['W2021']+str(i), axis=1)
    
    SPTV4.append(datapv_SPTV4[i])
    


# In[93]:


SPTV4=pd.concat(SPTV4)


# In[94]:


df_merge_SPTV4= pd.merge(SPTV4, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# ## SPTV51 Punch Values append

# In[95]:


PV_SPTV51=PV['SPTV5.1']['PunchValue']


# In[96]:


#data['SPTV5.1']


# In[97]:


datapv_SPTV51={}
SPTV51=[]
for i in PV_SPTV51:
    
    datapv_SPTV51[i]=data['SPTV5.1'].copy()

    datapv_SPTV51[i]['F2021']=datapv_SPTV51[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV51[i]['W2021']=datapv_SPTV51[i].apply(lambda x:x['W2021']+str(i), axis=1)
    
    SPTV51.append(datapv_SPTV51[i])


# In[98]:


SPTV51=pd.concat(SPTV51)


# In[99]:


df_merge_SPTV51= pd.merge(SPTV51, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[100]:


df_merge_SPTV51['LastDigit_PV']=df_merge_SPTV51['W2021'].str.strip().str[-1]


# In[101]:


df_merge_SPTV51=df_merge_SPTV51.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_SPTV51['Tmpl']=df_merge_SPTV51['Tmpl'].fillna(method='ffill')
df_merge_SPTV51['Super']=df_merge_SPTV51['Super'].fillna(method='ffill')
df_merge_SPTV51['Detail3']=df_merge_SPTV51['Detail3'].fillna(method='ffill')


# In[102]:


#display(df_merge_SPTV51)


# ## SPTV1

# In[103]:


PV_SPTV1=PV['SPTV1']['PunchValue']


# In[104]:


datapv_SPTV1={}
SPTV1=[]
for i in PV_SPTV1:
    
    datapv_SPTV1[i]=data['SPTV1'].copy()

    datapv_SPTV1[i]['F2021']=datapv_SPTV1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV1[i]['W2021']=datapv_SPTV1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    SPTV1.append(datapv_SPTV1[i])
	


# In[105]:


SPTV1=pd.concat(SPTV1)


# In[106]:


SPTV1.F2021 = SPTV1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()
SPTV1['F2021'] = SPTV1['F2021'].apply(lambda a: str(a).replace('X','x'))
SPTV1['W2021'] = SPTV1['W2021'].apply(lambda a: str(a).replace('X','x'))
df_merge_SPTV1=pd.merge(SPTV1,df_Fall_2021,left_on='F2021',right_on='CCP',how='left')


# In[107]:


df_merge_SPTV1['LastDigit_PV']=df_merge_SPTV1['W2021'].str.strip().str[-1]


# In[108]:


df_merge_SPTV1=df_merge_SPTV1.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_SPTV1['Tmpl']=df_merge_SPTV1['Tmpl'].fillna(method='ffill')
df_merge_SPTV1['Super']=df_merge_SPTV1['Super'].fillna(method='ffill')
df_merge_SPTV1['Detail3']=df_merge_SPTV1['Detail3'].fillna(method='ffill')


# In[109]:


df_merge_SPTV1=df_merge_SPTV1.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_SPTV1['Category']=df_merge_SPTV1['Category'].fillna(method='ffill')
df_merge_SPTV1['QLevel']=df_merge_SPTV1['QLevel'].fillna(method='ffill')
#df_merge_cable_col1['Detail2']=df_merge_cable_col1['Detail2'].fillna(method='ffill')


# ## Seperate col1 and col2 PV

# In[110]:


#group_data = df.groupby(['Alphabet','Words'])['COUNTER'].sum()
df_PunchMap_col2=df_PunchMap.query('Columns==2')
#df_PunchMap_col2
#df_PunchMap


# ## Taking a look at Punch values 

# In[111]:


df_PunchMap_col1=df_PunchMap.query('Columns==1')
#df_PunchMap_col1


# ## PV_Dataframe grouping with col1 PV 

# In[112]:


PV1={}
grouped1 = df_PunchMap_col1.groupby('Clean_Type')
for group1 in grouped1.groups.keys():
    PV1[group1] = grouped1.get_group(group1)
    #print(group1)


# ## PV_Dataframe grouping with col2 PV 

# In[113]:


PV2={}
grouped2 = df_PunchMap_col2.groupby('Clean_Type')
for group2 in grouped2.groups.keys():
    PV2[group2] = grouped2.get_group(group2)
    #print("list that has col2 PV:",group2)
   


# ## Dataframe grouping on One wave

# In[114]:


df_TV_Movie_onewave=df_TV_Movie.query('OneWave_Suppress=="#"')


# In[115]:


df_TV_Movie_Non_1W=df_TV_Movie.query('OneWave_Suppress!="#"')


# In[116]:


data_1w={}
grouped = df_TV_Movie_onewave.groupby('clean_type')
for group in grouped.groups.keys():
    #print(group)
    data_1w[group] = grouped.get_group(group)


# In[117]:


data_Non_1W={}
grouped = df_TV_Movie_Non_1W.groupby('clean_type')
for group in grouped.groups.keys():
    #print(group)
    data_Non_1W[group] = grouped.get_group(group)


# In[118]:


#data_Non_1W['TV2']


# In[119]:


#PV2['TV1']


# ## TV1 _col1 PV

# In[120]:


PV1_TV1_col1=PV1['TV1']['PunchValue']


# In[121]:


datapv_TV1_col1={}
TV1_col1=[]
for i in PV1_TV1_col1:
    
    datapv_TV1_col1[i]=data['TV1'].copy()

    datapv_TV1_col1[i]['F2021']=datapv_TV1_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV1_col1[i]['W2021']=datapv_TV1_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV1_col1.append(datapv_TV1_col1[i])


# In[122]:


TV1_col1=pd.concat(TV1_col1)


# In[123]:


#TV1_col1.head()


# In[124]:


TV1_col1['F2021'] = TV1_col1['F2021'].apply(lambda a: str(a).replace('X','x'))
TV1_col1['W2021'] = TV1_col1['W2021'].apply(lambda a: str(a).replace('X','x'))


# In[125]:


TV1_col1.F2021 = TV1_col1.F2021.astype(str)
df_Fall_2021.CCP = df_Fall_2021.CCP.astype(str)


# In[126]:



TV1_col1.F2021 = TV1_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[127]:


#TV1.F2021 =TV1.F2021.str.encode('cp1252')


# In[128]:


#TV1.F2021=TV1.F2021.str.replace('b','')


# In[129]:


#df_Fall_2021.CCP = df_Fall_2021.CCP.str.encode('cp1252')
#df_Fall_2021.CCP.dtype


# In[130]:


df_merge_TV1_col1=pd.merge(TV1_col1,df_Fall_2021,left_on=['F2021'],right_on=['CCP'],how='inner')


# In[133]:


#df_merge_TV11=TV1.merge(df_Fall_2021, how='left', left_on='F2021', right_on='CCP',indicator=True)


# ## PV_col2 adding them for TV1

# In[132]:


PV2_TV1_col2=PV2['TV1']['PunchValue']


# In[134]:


data_2={}


# In[135]:


data_2['TV1']=data['TV1'].copy()


# In[136]:


data_2['TV1']['F2021']=data_2['TV1']['F2021'].apply(pd.to_numeric)
data_2['TV1']['W2021']=data_2['TV1']['W2021'].apply(pd.to_numeric)


# In[137]:


data_2['TV1']['F2021']=data_2['TV1']['F2021']+1
data_2['TV1']['W2021']=data_2['TV1']['W2021']+1


# In[138]:


#data_2['TV1']


# In[139]:


data_2['TV1']['F2021']=data_2['TV1']['F2021'].astype(str)
data_2['TV1']['W2021']=data_2['TV1']['W2021'].astype(str)


# In[140]:


datapv_TV1_col2={}
TV1_col2=[]
for i in PV2_TV1_col2:
    
    datapv_TV1_col2[i]=data_2['TV1'].copy()

    datapv_TV1_col2[i]['F2021']=datapv_TV1_col2[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV1_col2[i]['W2021']=datapv_TV1_col2[i].apply(lambda x:x['W2021']+str(i), axis=1)
    datapv_TV1_col2[i]['col2pv']='yes'
    TV1_col2.append(datapv_TV1_col2[i])


# In[141]:


TV1_col2=pd.concat(TV1_col2)
#TV1_col2.head()


# In[142]:


TV1_col2.F2021 = TV1_col2.F2021.astype(str)
df_Fall_2021.CCP = df_Fall_2021.CCP.astype(str)


# In[143]:


TV1_col2.F2021 = TV1_col2.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[144]:


df_merge_TV1_col2=pd.merge(TV1_col2,df_Fall_2021,left_on=['F2021'],right_on=['CCP'],how='inner')


# In[145]:


df_merge_TV1=[df_merge_TV1_col1,df_merge_TV1_col2]


# In[146]:


df_merge_TV1=pd.concat(df_merge_TV1)


# In[147]:


df_merge_TV1['LastDigit_PV']=df_merge_TV1['W2021'].str.strip().str[-1]


# In[148]:


df_merge_TV1=df_merge_TV1.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_TV1['Tmpl']=df_merge_TV1['Tmpl'].fillna(method='ffill')
df_merge_TV1['Super']=df_merge_TV1['Super'].fillna(method='ffill')
df_merge_TV1['Detail3']=df_merge_TV1['Detail3'].fillna(method='ffill')


# In[149]:


df_merge_TV1=df_merge_TV1.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_TV1['Category']=df_merge_TV1['Category'].fillna(method='ffill')
df_merge_TV1['QLevel']=df_merge_TV1['QLevel'].fillna(method='ffill')
#df_merge_TV1['Detail2']=df_merge_TV1['Detail2'].fillna(method='ffill')


# In[150]:


Listheading=df_merge_TV1['Sec_List_Heading'].unique()


# In[151]:



g=df_merge_TV1.groupby('Sec_List_Heading')


# In[152]:


i=0
n=0
df_merge_TV1_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    df_merge_TV1_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas


# In[153]:


n=0
for values in Listheading:
    df_merge_TV1_LH[n]=df_merge_TV1_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    df_merge_TV1_LH[n]['Detail2']=df_merge_TV1_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[154]:


df_merge_TV1_Frames=pd.DataFrame()
df_merge_TV1_Frames = df_merge_TV1_Frames.append([df_merge_TV1_LH[i] for i in range(n)])


# In[155]:


#df_merge_TV1_Frames


# ## PV_col1-TV3

# In[156]:


PV1_TV3_col1=PV1['TV3']['PunchValue']
#PV1_TV3_col1


# In[157]:


datapv_TV3_col1={}
TV3_col1=[]
for i in PV1_TV3_col1:
    
    datapv_TV3_col1[i]=data['TV3'].copy()

    datapv_TV3_col1[i]['F2021']=datapv_TV3_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV3_col1[i]['W2021']=datapv_TV3_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV3_col1.append(datapv_TV3_col1[i])


# In[158]:


TV3_col1=pd.concat(TV3_col1)


# In[159]:


#TV3_col1


# In[160]:



TV3_col1['F2021'] = TV3_col1['F2021'].apply(lambda a: str(a).replace('X','x'))
TV3_col1['W2021'] = TV3_col1['W2021'].apply(lambda a: str(a).replace('X','x'))


# In[161]:



TV3_col1.F2021 = TV3_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[162]:


df_merge_TV3_col1= pd.merge(TV3_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='inner')


# In[163]:


#df_merge_TV3_col1


# ## PV_col2 TV3

# In[164]:


PV2_TV3=PV2['TV3']['PunchValue']


# In[165]:


data_2={}


# In[166]:


data_2['TV3']=data['TV3'].copy()


# In[167]:


data_2['TV3']['F2021']=data_2['TV3']['F2021'].apply(pd.to_numeric)
data_2['TV3']['W2021']=data_2['TV3']['W2021'].apply(pd.to_numeric)


# In[168]:


data_2['TV3']['F2021']=data_2['TV3']['F2021']+1
data_2['TV3']['W2021']=data_2['TV3']['W2021']+1


# In[169]:


data_2['TV3']['F2021']=data_2['TV3']['F2021'].astype(str)
data_2['TV3']['W2021']=data_2['TV3']['W2021'].astype(str)


# In[170]:


datapv_TV3_col2={}
TV3_col2=[]
for i in PV2_TV3:
    
    datapv_TV3_col2[i]=data_2['TV3'].copy()

    datapv_TV3_col2[i]['F2021']=datapv_TV3_col2[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV3_col2[i]['W2021']=datapv_TV3_col2[i].apply(lambda x:x['W2021']+str(i), axis=1)
    datapv_TV3_col2[i]['col2pv']='yes'
    TV3_col2.append(datapv_TV3_col2[i])


# In[171]:


TV3_col2=pd.concat(TV3_col2)
#TV3_col2.head()


# In[172]:


TV3_col2.F2021 = TV3_col2.F2021.astype(str)
df_Fall_2021.CCP = df_Fall_2021.CCP.astype(str)


# In[173]:


TV3_col2.F2021 = TV3_col2.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[174]:


df_merge_TV3_col2=pd.merge(TV3_col2,df_Fall_2021,left_on=['F2021'],right_on=['CCP'],how='inner')


# In[175]:


df_merge_TV3=[df_merge_TV3_col1,df_merge_TV3_col2]


# In[176]:


df_merge_TV3=pd.concat(df_merge_TV3)


# ## TV4 PV_col1

# In[1010]:


PV1_TV4_col1=PV1['TV4']['PunchValue']


# In[1011]:


#PV1_TV4_col1


# In[1012]:


datapv_TV4_col1={}
TV4_col1=[]
for i in PV1_TV4_col1:
    
    datapv_TV4_col1[i]=data['TV4'].copy()

    datapv_TV4_col1[i]['F2021']=datapv_TV4_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV4_col1[i]['W2021']=datapv_TV4_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV4_col1.append(datapv_TV4_col1[i])


# In[1013]:


TV4_col1=pd.concat(TV4_col1)


# In[1014]:


TV4_col1.F2021 = TV4_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()
df_merge_TV4_col1= pd.merge(TV4_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='inner')


# ## TV4 col2 PV

# In[1015]:


PV2_TV4=PV2['TV4']['PunchValue']


# In[1016]:


#PV2_TV4


# In[1017]:


data_2={}


# In[1018]:


data_2['TV4']=data['TV4'].copy()


# In[1019]:


data_2['TV4']['F2021']=data_2['TV4']['F2021'].apply(pd.to_numeric)
data_2['TV4']['W2021']=data_2['TV4']['W2021'].apply(pd.to_numeric)


# In[1020]:


data_2['TV4']['F2021']=data_2['TV4']['F2021']+1
data_2['TV4']['W2021']=data_2['TV4']['W2021']+1


# In[1021]:


data_2['TV4']['F2021']=data_2['TV4']['F2021'].astype(str)
data_2['TV4']['W2021']=data_2['TV4']['W2021'].astype(str)


# In[1022]:


datapv_TV4_col2={}
TV4_col2=[]
for i in PV2_TV4:
    
    datapv_TV4_col2[i]=data_2['TV4'].copy()

    datapv_TV4_col2[i]['F2021']=datapv_TV4_col2[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV4_col2[i]['W2021']=datapv_TV4_col2[i].apply(lambda x:x['W2021']+str(i), axis=1)
    datapv_TV4_col2[i]['col2pv']='yes'
    TV4_col2.append(datapv_TV4_col2[i])


# In[1023]:


TV4_col2=pd.concat(TV4_col2)


# In[1024]:


#TV4_col2


# In[1025]:


TV4_col2.F2021 = TV4_col2.F2021.astype(str)
df_Fall_2021.CCP = df_Fall_2021.CCP.astype(str)


# In[1026]:



TV4_col2.F2021 = TV4_col2.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[1027]:


df_merge_TV4_col2=pd.merge(TV4_col2,df_Fall_2021,left_on=['F2021'],right_on=['CCP'],how='inner')


# In[1028]:


#df_merge_TV4_col2


# In[1029]:


df_merge_TV4=[df_merge_TV4_col1,df_merge_TV4_col2]


# In[1030]:


df_merge_TV4=pd.concat(df_merge_TV4)


# ## TV2 col1_Punch variable

# # It has one wave items so seperated them and adding PV to avoid duplicate values

# In[1031]:


PV1_TV2_col1=PV1['TV2']['PunchValue']


# In[1032]:


#data['TV2']


# In[1033]:


data['TV2'].to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\TV2source.csv',index=False,header=True,encoding='cp1252')


# In[1034]:


datapv_TV2_col1={}
TV2_col1=[]
for i in PV1_TV2_col1:
    
    datapv_TV2_col1[i]=data['TV2'].copy()

    datapv_TV2_col1[i]['F2021']=datapv_TV2_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV2_col1[i]['W2021']=datapv_TV2_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV2_col1.append(datapv_TV2_col1[i])


# In[1035]:


TV2_col1=pd.concat(TV2_col1)


# In[1036]:


#TV2_col1


# In[1037]:


#TV2_col1


# In[1038]:



TV2_col1.F2021 = TV2_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()
TV2_col1['F2021'] = TV2_col1['F2021'].apply(lambda a: str(a).replace('X','x'))
TV2_col1['W2021'] = TV2_col1['W2021'].apply(lambda a: str(a).replace('X','x'))
df_merge_TV2_col1= pd.merge(TV2_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='inner')


# In[1039]:


#df_merge_TV2_col1


# In[1040]:


NR_TV2_col1 = pd.merge(TV2_col1,df_merge_TV2_col1, how = 'outer',left_on='F2021',right_on='CCP',indicator=True).loc[lambda x : x['_merge']=='left_only']


# In[1041]:


NR_TV2_col1=NR_TV2_col1[['clean_type_x', 'W2021_x', 'Sec_List_Heading_x', 'OneWave_Suppress_x','Initial_wave_x', 'Shows_Name_x', 'F2021_x', 'compare_x', 'col2pv_x']]


# In[1042]:


NR_TV2_col1=NR_TV2_col1.rename(columns={'clean_type_x':'clean_type', 'W2021_x':'W2021', 'Sec_List_Heading_x':'Sec_List_Heading', 'Initial_wave_x':'Initial_wave','OneWave_Suppress_x':'OneWave_Suppress', 'Shows_Name_x':'Shows_Name', 'F2021_x':'F2021', 'compare_x':'compare', 'col2pv_x':'col2pv'})


# In[1043]:


#NR_TV2_col1.columns


# In[1044]:


df_merge_TV2_col1=[df_merge_TV2_col1,NR_TV2_col1]


# In[1045]:


df_merge_TV2_col1=pd.concat(df_merge_TV2_col1)


# In[1046]:


#df_merge_TV2_col1


# In[1047]:


#df_merge_TV2_col1.shape


# ## TV2 col2 PV

# In[1048]:


PV2_TV2_col2=PV2['TV2']['PunchValue']


# In[1049]:


data_2={}


# In[1050]:


data_2['TV2']=data['TV2'].copy()


# In[1051]:



data_2['TV2']['F2021']=data_2['TV2']['F2021'].apply(pd.to_numeric)
data_2['TV2']['W2021']=data_2['TV2']['W2021'].apply(pd.to_numeric)


# In[1052]:



data_2['TV2']['F2021']=data_2['TV2']['F2021']+1
data_2['TV2']['W2021']=data_2['TV2']['W2021']+1


# In[1053]:


#data['TV2']['F2021']


# In[1054]:


#data_2['TV2']['F2021']


# In[1055]:



data_2['TV2']['F2021']=data_2['TV2']['F2021'].astype(str)
data_2['TV2']['W2021']=data_2['TV2']['W2021'].astype(str)


# In[1056]:


#data_2['TV2']


# In[1057]:


datapv_TV2_col2={}
TV2_col2=[]
for i in PV2_TV2_col2:
    
    datapv_TV2_col2[i]=data_2['TV2'].copy()

    datapv_TV2_col2[i]['F2021']=datapv_TV2_col2[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV2_col2[i]['W2021']=datapv_TV2_col2[i].apply(lambda x:x['W2021']+str(i), axis=1)
    datapv_TV2_col2[i]['col2pv']='yes'
    TV2_col2.append(datapv_TV2_col2[i])


# In[1058]:


TV2_col2=pd.concat(TV2_col2)


# In[1059]:


#TV2_col2


# In[1060]:


#TV2_col2.nunique()


# In[1061]:


TV2_col2.F2021 = TV2_col2.F2021.astype(str)
df_Fall_2021.CCP = df_Fall_2021.CCP.astype(str)


# In[1062]:



TV2_col2.F2021 = TV2_col2.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[1063]:


df_merge_TV2_col2=pd.merge(TV2_col2,df_Fall_2021,left_on=['F2021'],right_on=['CCP'],how='inner')


# In[1064]:


NR_TV2_col2 = pd.merge(TV2_col2,df_merge_TV2_col2, how = 'outer',left_on='F2021',right_on='CCP',indicator=True).loc[lambda x : x['_merge']=='left_only']


# In[1065]:


NR_TV2_col2=NR_TV2_col2[['clean_type_x', 'W2021_x', 'Sec_List_Heading_x', 'OneWave_Suppress_x', 'Initial_wave_x','Shows_Name_x', 'F2021_x', 'compare_x', 'col2pv_x']]


# In[1066]:



NR_TV2_col2=NR_TV2_col2.rename(columns={'clean_type_x':'clean_type', 'W2021_x':'W2021', 'Sec_List_Heading_x':'Sec_List_Heading', 'OneWave_Suppress_x':'OneWave_Suppress','Initial_wave_x':'Initial_wave', 'Shows_Name_x':'Shows_Name', 'F2021_x':'F2021', 'compare_x':'compare', 'col2pv_x':'col2pv'})


# In[1067]:


#NR_TV2_col2


# In[1068]:


df_merge_TV2_col2=[df_merge_TV2_col2,NR_TV2_col2]


# In[1069]:



df_merge_TV2_col2=pd.concat(df_merge_TV2_col2)


# In[1070]:



#df_merge_TV2_col2


# In[1071]:


#df_merge_TV2_col2


# In[1072]:


df_merge_TV2=[df_merge_TV2_col1,df_merge_TV2_col2]


# In[1073]:


df_merge_TV2=pd.concat(df_merge_TV2)


# In[1074]:


df_merge_TV2['LastDigit_PV']=df_merge_TV2['W2021'].str.strip().str[-1]


# In[1075]:


df_merge_TV2.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\TV2b4fill.csv',index=False,header=True,encoding='cp1252')


# In[1080]:


df_merge_TV2_tmpl3=df_merge_TV2.query("Shows_Name=='Litton Weekend Adventure net (includes Free Enterprise, Hearts of Heroes, Oh Baby, Outback Adventures)'|Shows_Name=='CBS Dream Team net (includes Hope In The Wild, Innovation Nation, Lucky Dog, Mission Unstoppable)'")
#df.query("users=='rachel' | users=='jeff'")


# In[1086]:


df_merge_TV2_tmpl3


# In[1090]:


df_merge_TV2_tmpl3 = df_merge_TV2_tmpl3.dropna(subset=['Category'])


# In[1091]:


#df_merge_TV2_tmpl3


# In[949]:


#df_merge_TV2_tmpl2=df_merge_TV2.query('Tmpl!="3"')
df_merge_TV2_tmpl_not3=df_merge_TV2.query("Shows_Name!='Litton Weekend Adventure net (includes Free Enterprise, Hearts of Heroes, Oh Baby, Outback Adventures)'& Shows_Name!='CBS Dream Team net (includes Hope In The Wild, Innovation Nation, Lucky Dog, Mission Unstoppable)'")
#df.query("users=='rachel' | users=='jeff'")


# In[951]:


#df_merge_TV2_tmpl_not3.shape


# In[882]:


df_merge_TV2=df_merge_TV2_tmpl_not3.copy()


# In[ ]:


#df_merge_TV2


# In[883]:


df_merge_TV2=df_merge_TV2.sort_values(['col2pv','Sec_List_Heading','Tmpl','Category'], 
               ascending=[True,True,True,True],na_position='last')
df_merge_TV2['Category']=df_merge_TV2['Category'].fillna(method='ffill')
df_merge_TV2['QLevel']=df_merge_TV2['QLevel'].fillna(method='ffill')
df_merge_TV2['Tmpl']=df_merge_TV2['Tmpl'].fillna(method='ffill')
#df_merge_TV2['Detail2']=df_merge_TV2['Detail2'].fillna(method='ffill')


# In[884]:


df_merge_TV2=df_merge_TV2.sort_values(['col2pv','Sec_List_Heading','LastDigit_PV','Detail3'], 
               ascending=[True,True,True,True],na_position='last')
						  

df_merge_TV2['Super']=df_merge_TV2['Super'].fillna(method='ffill')
df_merge_TV2['Detail3']=df_merge_TV2['Detail3'].fillna(method='ffill')


# In[885]:


Listheading=df_merge_TV2['Sec_List_Heading'].unique()


# In[886]:


g=df_merge_TV2.groupby('Sec_List_Heading')


# In[887]:


i=0
n=0
df_merge_TV2_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    df_merge_TV2_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas


# In[888]:


n=0
for values in Listheading:
    df_merge_TV2_LH[n]=df_merge_TV2_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    df_merge_TV2_LH[n]['Detail2']=df_merge_TV2_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF 


# In[889]:


df_merge_TV2_Frames=pd.DataFrame()
df_merge_TV2_Frames = df_merge_TV2_Frames.append([df_merge_TV2_LH[i] for i in range(n)])


# In[890]:


df_merge_TV2_Frames=[df_merge_TV2_Frames,df_merge_TV2_tmpl3]


# In[891]:


df_merge_TV2_Frames=pd.concat(df_merge_TV2_Frames)


# In[892]:


df_merge_TV2_Frames=df_merge_TV2_Frames.drop_duplicates(subset='W2021',keep='last')


# In[952]:


df_merge_TV2_Frames.shape


# In[894]:


df_merge_TV2_Frames.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\TV2.csv',index=False,header=True,encoding='cp1252')


# ## SPTV2

# In[397]:


PV1_SPTV2_col1=PV1['SPTV2']['PunchValue']


# In[398]:


datapv_SPTV2_col1={}
SPTV2_col1=[]
for i in PV1_SPTV2_col1:
    
    datapv_SPTV2_col1[i]=data['SPTV2'].copy()

    datapv_SPTV2_col1[i]['F2021']=datapv_SPTV2_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV2_col1[i]['W2021']=datapv_SPTV2_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    SPTV2_col1.append(datapv_SPTV2_col1[i])


# In[399]:


SPTV2_col1=pd.concat(SPTV2_col1)


# In[400]:



SPTV2_col1.F2021 = SPTV2_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[401]:


SPTV2_col1['F2021'] = SPTV2_col1['F2021'].apply(lambda a: str(a).replace('X','x'))
SPTV2_col1['W2021'] = SPTV2_col1['W2021'].apply(lambda a: str(a).replace('X','x'))


# In[402]:


df_merge_SPTV2_col1= pd.merge(SPTV2_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[403]:


df_merge_SPTV2_col1['LastDigit_PV']=df_merge_SPTV2_col1['W2021'].str.strip().str[-1]


# In[404]:



df_merge_SPTV2_col1=df_merge_SPTV2_col1.sort_values(['Sec_List_Heading'],ascending=[True])
df_merge_SPTV2_col1['Category']=df_merge_SPTV2_col1['Category'].fillna(method='ffill')
df_merge_SPTV2_col1['QLevel']=df_merge_SPTV2_col1['QLevel'].fillna(method='ffill')
df_merge_SPTV2_col1['Tmpl']=df_merge_SPTV2_col1['Tmpl'].fillna(method='ffill')
df_merge_SPTV2_col1['Super']=df_merge_SPTV2_col1['Super'].fillna(method='ffill')
#df_merge_cable_col1['Detail2']=df_merge_cable_col1['Detail2'].fillna(method='ffill')


# In[405]:


df_merge_SPTV2_col1['Tmpl']=df_merge_SPTV2_col1['Tmpl'].fillna(2)


# In[406]:


df_merge_SPTV2_col1['Super']=df_merge_SPTV2_col1['Super'].fillna('Media - Television')


# In[420]:


df_merge_SPTV2_col1=df_merge_SPTV2_col1.sort_values(['LastDigit_PV','Detail3'],ascending=[True,True],na_position = 'last')

df_merge_SPTV2_col1['Detail3']=df_merge_SPTV2_col1['Detail3'].fillna(method='ffill')


# In[421]:


#df_merge_SPTV2_col1


# In[477]:



#df_merge_SPTV2_col1['Detail3']=df_merge_SPTV2_col1['Detail3'].fillna('Watch 1 time a month')


# In[478]:


df_merge_SPTV2_col1['QLevel']=df_merge_SPTV2_col1['QLevel'].fillna(4)


# In[479]:


df_merge_SPTV2_col1['Category']=df_merge_SPTV2_col1['Category'].fillna('Spanish Television: Once A Week Programs')


# In[480]:


#df_merge_SPTV2_col1


# ## SPTV3

# In[344]:


PV1_SPTV3_col1=PV1['SPTV3']['PunchValue']


# In[345]:


datapv_SPTV3_col1={}
SPTV3_col1=[]
for i in PV1_SPTV3_col1:
    
    datapv_SPTV3_col1[i]=data['SPTV3'].copy()

    datapv_SPTV3_col1[i]['F2021']=datapv_SPTV3_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV3_col1[i]['W2021']=datapv_SPTV3_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    SPTV3_col1.append(datapv_SPTV3_col1[i])


# In[346]:


SPTV3_col1=pd.concat(SPTV3_col1)


# In[347]:


SPTV3_col1.F2021 = SPTV3_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[348]:


SPTV3_col1['F2021'] = SPTV3_col1['F2021'].apply(lambda a: str(a).replace('X','x'))
SPTV3_col1['W2021'] = SPTV3_col1['W2021'].apply(lambda a: str(a).replace('X','x'))


# In[349]:


df_merge_SPTV3_col1= pd.merge(SPTV3_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[350]:


#df_merge_SPTV3_col1


# ## SPTV5 

# In[351]:


PV1_SPTV5_col1=PV1['SPTV5']['PunchValue']


# In[352]:


datapv_SPTV5_col1={}
SPTV5_col1=[]
for i in PV1_SPTV5_col1:
    
    datapv_SPTV5_col1[i]=data['SPTV5'].copy()

    datapv_SPTV5_col1[i]['F2021']=datapv_SPTV5_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_SPTV5_col1[i]['W2021']=datapv_SPTV5_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    SPTV5_col1.append(datapv_SPTV5_col1[i])


# In[353]:


SPTV5_col1=pd.concat(SPTV5_col1)


# In[354]:


SPTV5_col1.F2021 = SPTV5_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[355]:



df_merge_SPTV5_col1= pd.merge(SPTV5_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[356]:


df_merge_SPTV5_col1['Shows_Name'] = df_merge_SPTV5_col1.apply(lambda x: x['Sec_List_Heading']+': '+x['Shows_Name']  if x['OneWave_Suppress']!='#' else x['Shows_Name'], axis=1)


# In[357]:


df_merge_SPTV5_col1['Shows_Name'] = df_merge_SPTV5_col1.apply(lambda x: x['Shows_Name'].lstrip("#")  if x['OneWave_Suppress']=='#' else x['Shows_Name'], axis=1)


# In[358]:


df_merge_SPTV5_col1['Shows_Name'] = df_merge_SPTV5_col1.apply(lambda x:'#'+ x['Sec_List_Heading']+': '+x['Shows_Name']  if x['OneWave_Suppress']=='#' else x['Shows_Name'], axis=1)


# ## TV5 

# In[282]:


PV1_TV5_col1=PV1['TV5']['PunchValue']


# In[283]:


datapv_TV5_col1={}
TV5_col1=[]
for i in PV1_TV5_col1:
    
    datapv_TV5_col1[i]=data['TV5'].copy()

    datapv_TV5_col1[i]['F2021']=datapv_TV5_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV5_col1[i]['W2021']=datapv_TV5_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV5_col1.append(datapv_TV5_col1[i])
	


# In[284]:


TV5_col1=pd.concat(TV5_col1)


# In[285]:


TV5_col1.F2021 = TV5_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[286]:


df_merge_TV5_col1= pd.merge(TV5_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[287]:


#df_merge_TV5_col1


# In[288]:


df_merge_TV5=df_merge_TV5_col1.copy()


# In[289]:


df_merge_TV5['LastDigit_PV']=df_merge_TV5['W2021'].str.strip().str[-1]


# In[290]:


df_merge_TV5=df_merge_TV5.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_TV5['Tmpl']=df_merge_TV5['Tmpl'].fillna(method='ffill')
df_merge_TV5['Super']=df_merge_TV5['Super'].fillna(method='ffill')
df_merge_TV5['Detail3']=df_merge_TV5['Detail3'].fillna(method='ffill')


# In[291]:


df_merge_TV5=df_merge_TV5.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_TV5['Category']=df_merge_TV5['Category'].fillna(method='ffill')
df_merge_TV5['QLevel']=df_merge_TV5['QLevel'].fillna(method='ffill')
#df_merge_TV5['Detail2']=df_merge_TV5['Detail2'].fillna(method='ffill')


# In[292]:


Listheading=df_merge_TV5['Sec_List_Heading'].unique()


# In[293]:


g=df_merge_TV5.groupby('Sec_List_Heading')


# In[294]:


i=0
n=0
df_merge_TV5_LH={}
for Sec_List_Heading, g_df in g:
    #print (Sec_List_Heading)
    df_merge_TV5_LH[i]=pd.DataFrame(g_df)
    i=i+1
    n=n+1
#converting each group in g to a pandas


# In[295]:



n=0
for values in Listheading:
    df_merge_TV5_LH[n]=df_merge_TV5_LH[n].sort_values(['LastDigit_PV'], 
               ascending=[True
                        ])
    df_merge_TV5_LH[n]['Detail2']=df_merge_TV5_LH[n]['Detail2'].fillna(method='ffill')
    n=n+1
#for each values List heading FFill the Detail2 values in each  DF


# In[296]:


df_merge_TV5_Frames=pd.DataFrame()


# In[297]:


df_merge_TV5_Frames = df_merge_TV5_Frames.append([df_merge_TV5_LH[i] for i in range(n)])


# ## TV6 

# In[299]:


PV1_TV6_col1=PV1['TV6']['PunchValue']


# In[300]:


datapv_TV6_col1={}
TV6_col1=[]
for i in PV1_TV6_col1:
    
    datapv_TV6_col1[i]=data['TV6'].copy()

    datapv_TV6_col1[i]['F2021']=datapv_TV6_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_TV6_col1[i]['W2021']=datapv_TV6_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    TV6_col1.append(datapv_TV6_col1[i])


# In[301]:


TV6_col1=pd.concat(TV6_col1)


# In[302]:



TV6_col1.F2021 = TV6_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[303]:


df_merge_TV6_col1= pd.merge(TV6_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[304]:


df_merge_TV6=df_merge_TV6_col1.copy()


# In[305]:


df_merge_TV6['LastDigit_PV']=df_merge_TV6['W2021'].str.strip().str[-1]


# In[306]:


df_merge_TV6=df_merge_TV6.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_TV6['Tmpl']=df_merge_TV6['Tmpl'].fillna(method='ffill')
df_merge_TV6['Super']=df_merge_TV6['Super'].fillna(method='ffill')
df_merge_TV6['Detail3']=df_merge_TV6['Detail3'].fillna(method='ffill')


# In[307]:



df_merge_TV6=df_merge_TV6.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_TV6['Category']=df_merge_TV6['Category'].fillna(method='ffill')
df_merge_TV6['QLevel']=df_merge_TV6['QLevel'].fillna(method='ffill')


# ## Movies 

# In[308]:


PV1_movies_col1=PV1['movies']['PunchValue']


# In[309]:


datapv_movies_col1={}
movies_col1=[]
for i in PV1_movies_col1:
    
    datapv_movies_col1[i]=data['Movie'].copy()

    datapv_movies_col1[i]['F2021']=datapv_movies_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_movies_col1[i]['W2021']=datapv_movies_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    movies_col1.append(datapv_movies_col1[i])
	


# In[310]:


movies_col1=pd.concat(movies_col1)


# In[311]:


movies_col1.F2021 = movies_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[312]:


df_merge_movies_col1= pd.merge(movies_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[313]:


df_merge_movies_col1['LastDigit_PV']=df_merge_movies_col1['W2021'].str.strip().str[-1]


# In[314]:


df_merge_movies_col1=df_merge_movies_col1.sort_values(['LastDigit_PV'],ascending=[True])
						  
df_merge_movies_col1['Tmpl']=df_merge_movies_col1['Tmpl'].fillna(method='ffill')
df_merge_movies_col1['Super']=df_merge_movies_col1['Super'].fillna(method='ffill')
df_merge_movies_col1['Detail3']=df_merge_movies_col1['Detail3'].fillna(method='ffill')


# In[315]:


df_merge_movies_col1=df_merge_movies_col1.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_movies_col1['Category']=df_merge_movies_col1['Category'].fillna(method='ffill')
df_merge_movies_col1['QLevel']=df_merge_movies_col1['QLevel'].fillna(method='ffill')
df_merge_movies_col1['Detail2']=df_merge_movies_col1['Detail2'].fillna(method='ffill')


# ## Cable

# In[316]:


PV1_cable_col1=PV1['cable']['PunchValue']


# In[317]:


datapv_cable_col1={}
cable_col1=[]
for i in PV1_cable_col1:
    
    datapv_cable_col1[i]=data['cable'].copy()

    datapv_cable_col1[i]['F2021']=datapv_cable_col1[i].apply(lambda x:x['F2021']+str(i), axis=1)
    datapv_cable_col1[i]['W2021']=datapv_cable_col1[i].apply(lambda x:x['W2021']+str(i), axis=1)
 
    cable_col1.append(datapv_cable_col1[i])


# In[318]:


cable_col1=pd.concat(cable_col1)


# In[319]:


cable_col1.F2021 = cable_col1.F2021.str.strip()
df_Fall_2021.CCP = df_Fall_2021.CCP.str.strip()


# In[320]:



df_merge_cable_col1= pd.merge(cable_col1, df_Fall_2021, left_on=['F2021'], right_on=['CCP'],suffixes=('_left','_right'),how='left')


# In[321]:


df_merge_cable_col1['LastDigit_PV']=df_merge_cable_col1['W2021'].str.strip().str[-1]


# In[322]:


df_merge_cable_col1=df_merge_cable_col1.sort_values(['LastDigit_PV'], 
               ascending=[True])
						  
df_merge_cable_col1['Tmpl']=df_merge_cable_col1['Tmpl'].fillna(method='ffill')
df_merge_cable_col1['Super']=df_merge_cable_col1['Super'].fillna(method='ffill')
df_merge_cable_col1['Detail3']=df_merge_cable_col1['Detail3'].fillna(method='ffill')


# In[323]:


df_merge_cable_col1=df_merge_cable_col1.sort_values(['Sec_List_Heading'], 
               ascending=[True])
df_merge_cable_col1['Category']=df_merge_cable_col1['Category'].fillna(method='ffill')
df_merge_cable_col1['QLevel']=df_merge_cable_col1['QLevel'].fillna(method='ffill')
#df_merge_cable_col1['Detail2']=df_merge_cable_col1['Detail2'].fillna(method='ffill')


# In[324]:


#df_merge_cable_col1.columns


# In[325]:


df_merge_cable_col1['Shows_Name'] = df_merge_cable_col1.apply(lambda x: x['Sec_List_Heading']+': '+x['Shows_Name']  if x['OneWave_Suppress']!='#' else x['Shows_Name'], axis=1)


# In[326]:


df_merge_cable_col1['Shows_Name'] = df_merge_cable_col1.apply(lambda x: x['Shows_Name'].lstrip("#")  if x['OneWave_Suppress']=='#' else x['Shows_Name'], axis=1)
#df_merge_cable_col1['Shows_Name'] = df_merge_cable_col1['Shows_Name'].lstrip("#")

#lambda x:x['Category'].replace(r'- Net','',regex=True)


# In[327]:


df_merge_cable_col1['Shows_Name'] = df_merge_cable_col1.apply(lambda x:'#'+ x['Sec_List_Heading']+': '+x['Shows_Name']  if x['OneWave_Suppress']=='#' else x['Shows_Name'], axis=1)


# ## Concat all DF

# In[568]:


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


# In[569]:


df_all=pd.concat(df_all)


# In[570]:


#display(df_all.head())


# In[571]:


df_all.drop(['StatisticID', 'CatSynID','NoteID','statusid'], axis=1, inplace=True)


# In[572]:


df_all['EditedBy']='codebookcreator'
df_all['EditedDate']=pd.to_datetime('today')
df_all['StudyEntryID']=434
df_all['VersionID']=0
df_all['SID']=1913


# In[573]:


df_all['Status']='Add'


# In[574]:


df_all['Definition'] = df_all.apply(lambda x: 0  if x['compare']==False else x['Definition'], axis=1)


# In[575]:


df_all['Definition']=df_all['Definition'].fillna('0')


# In[576]:


#df_all


# In[577]:


df_all['UCode']=df_all['UCode'].fillna('U0')
df_all['QuestionID']=df_all['QuestionID'].fillna(0)
df_all['QUESTID']=df_all['QUESTID'].fillna(0)
df_all['SDID']=df_all['SDID'].fillna(0)
df_all['Initial_wave']=df_all['Initial_wave'].replace(r'nan',np.nan, regex=True)
df_all['Initial_wave']=df_all['Initial_wave'].fillna(0)


# In[578]:


#df_all['Initial_wave'].unique()


# In[579]:


#df_all['Initial_wave']=df_all['Initial_wave'].replace(r'W', '', regex=True)


# In[580]:


df_all['StudyAnswerID']=0


# In[581]:


df_all['Full_Label']=''
df_all['ORD']=''


# In[582]:


#df_all['wave']=df_all['wave'].fillna(0)
df_all['AnswerID']=df_all['AnswerID'].fillna(0)


# In[583]:


df_all['Imported']=''
df_all['Min']=''
df_all['Max']=''


# In[584]:


df_all=df_all.sort_values(['Category','Detail1','Detail3'],ascending=[True,True,True])


# In[585]:


#df_all.isna().value_counts()


# In[586]:


#df_all = df_all.astype( {"QLevel":'int32', "QUESTID":'int32', "AnswerID":'int32',"QuestionID":'int32',"SID":'int64', "SDID":'int32', "VersionID":'int32', "Wave":'int32', "Min":'float',"Max":'float', "StudyEntryID":'int64',"Imported":'bool'} )


# In[587]:


df_all.to_csv(r"C:\Users\saraswathy.rajaman\Documents\df_all.csv",index=False,header=True,encoding='cp1252')


# In[588]:


df_all.drop(['clean_type', 'Detail1','F2021','compare','col2pv','LastDigit_PV','QID','CCP','Wave'], axis=1, inplace=True)


# In[589]:


df_all.rename(columns={'W2021':'CCP','Shows_Name':'Detail1','VersionID':'Version','Initial_wave':'Wave'},inplace=True)


# In[590]:


#df_all


# In[591]:


#df_all.Imported.isna().value_counts()


# In[592]:


df_all=df_all[["StudyEntryID","SID","Version","Category","Super","Tmpl","Time Period","Detail1","Detail2",
"Detail3","Detail4","UCode","Definition","CCP","ORD","Wave","Status","Full_Label","QLevel","QUESTID","AnswerID","EditedBy","EditedDate","SDID",
"StudyAnswerID","QuestionID","Imported","Min","Max"]]


# In[593]:


df_all['Max'] =df_all['Max'].apply(pd.to_numeric)
df_all['Min'] =df_all['Min'].apply(pd.to_numeric)


# In[594]:


#df_all.info()
df_all['Wave']=df_all['Wave'].fillna(0)
#df_all['Wave'].isna().value_counts()


# In[595]:


#df_all.shape


# #df_all.Wave.dtype()
# df_all['Wave'] = pd.to_numeric(df_all['Wave'], errors="coerce")

# df_all['Wave'] =df_all['Wave'].astype(int)

# In[596]:


#df_all.Tmpl.isna().value_counts()


# In[597]:


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


# In[598]:


#df_all.info()


# In[1]:


df_all=df_all.sort_values(['Category','Detail1','Detail3'],ascending=[True,True,True])


# In[599]:


df_all.to_csv('C:\\Users\\saraswathy.rajaman\\Documents\\Winter-2021.csv',index=False,header=True,encoding='cp1252')


# In[600]:


from sqlalchemy import create_engine
#engine = create_engine('sqlite://', echo=False)


# In[392]:


DB = {'server':'internalSQLdev.mridevops.com','database':'Codebook_Taxonomy','driver':'driver=SQL Server Native Client 11.0','pyodb_d':'SQL Server Native Client 11.0'}
#engine=create_engine('mssql+pyodbc://'+ DB['server']+'/'+ DB['database']+'?'+ DB['driver'])


# In[393]:



engine = create_engine('mssql+pyodbc://' + DB['server'] + '/' + DB['database'] + '?' + DB['driver'], fast_executemany = True)


# In[394]:


import pyodbc


# In[395]:


conn = pyodbc.connect('Driver={'+DB['pyodb_d']+'}; Server='+DB['server']+';Database='+DB['database']+'; Trusted_Connection=yes;')


# In[601]:


conn.commit()


# In[602]:


with engine.begin() as connection:
    df_all.to_sql(name="tmp_EditedRecords_Hold",con=engine,schema="dbo",if_exists='append', chunksize=1000,index=False)
#df.to_sql('db_table2', engine, if_exists='replace')


# In[ ]:




