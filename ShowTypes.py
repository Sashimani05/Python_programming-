#import openpyxl as oxl
from asyncio.windows_events import NULL
from datetime import datetime
from numpy import int32
import pandas as pd
import pyodbc
import re 
import numpy as np
from sqlalchemy import create_engine
import time
import sys 

startTime = time.time()

inFile = "C:\\Users\\saraswathy.rajaman\\Documents\\w84_Media_ShowTypes.txt"


print(sys.argv[0])
df_ShowTypes = pd.read_csv(inFile, sep='\t', skiprows=1)
print(df_ShowTypes.dtypes)
#Card-Col
df_ShowTypes['CC'] = df_ShowTypes.Spring2021_Client.str.replace('*', '')
df_ShowTypes['CC'] =  df_ShowTypes['CC'].str.split("-", 1).str[0].str[1:]

#Get the column values to get the number of columns the defintion spans
df_ShowTypes['Min'] = df_ShowTypes['W84_MRI'].str.split("-", 1).str[0]
df_ShowTypes['Max'] = df_ShowTypes['W84_MRI'].str.split("-", 1).str[1]
df_ShowTypes['Max'] = df_ShowTypes['Max'].fillna(0)
df_ShowTypes = df_ShowTypes.astype({"Min":'int64', "Max":'int64'})
df_ShowTypes.loc[(df_ShowTypes['Max'] != 0), ['NumberColumns']] = df_ShowTypes['Max'] - df_ShowTypes['Min'] + 1
#if the there is no max then the number of columns will be 1
df_ShowTypes['NumberColumns'] = df_ShowTypes['NumberColumns'].fillna(1)
df_ShowTypes = df_ShowTypes.astype({"NumberColumns":'int64'})

df_ShowTypes['IsACodeChange'] = df_ShowTypes['Spring2021_Client'].equals(df_ShowTypes['Fall2020_Client'])
#Handle the case when they are different
df_ShowTypes['Old_Code'] = "quotient(rvol(" + df_ShowTypes['CC'] + "," + df_ShowTypes['NumberColumns'].astype(str) + ")," + df_ShowTypes['Fall2020_Divide'].astype(str) + ")"
df_ShowTypes['New_Code'] = "quotient(rvol(" + df_ShowTypes['CC'] + "," + df_ShowTypes['NumberColumns'].astype(str) + ")," + df_ShowTypes['Spring2021_Divide'].astype(str) + ")"

DB = {  'server': 'internalSQLdev.mridevops.com', 'database': 'Codebook_Taxonomy', 
    'driver': 'driver=SQL Server Native Client 11.0', 'pyodb_d': 'ODBC Driver 17 for SQL Server' }

conn = pyodbc.connect('Driver={'+DB['pyodb_d']+'}; Server='+DB['server']+';Database='+DB['database']+'; Trusted_Connection=yes;')
#+'; Trusted_Connection=no; UID=CodebookCreator_aws; PWD=6kmcbLwm6TXc;')

#Get previous dictionary info
Prev_Dict_StudyEntryID = '323'
Prev_Dict_VersionID = '17'
query = "EXEC [app_Codebook_Read] @VersionID = {0}, @StudyEntryID = {1}".format(Prev_Dict_VersionID, Prev_Dict_StudyEntryID)

df_LastDictionary = pd.read_sql_query(query, conn)
#print (df_LastDictionary)

df_AlignedData = pd.merge(df_ShowTypes, df_LastDictionary, how='left', left_on=df_ShowTypes['Old_Code'].str.lower(), right_on=df_LastDictionary['CCP'].str.lower())
print ("post-megre")
df_ReleaseData = df_AlignedData.copy(deep=True)
df_ReleaseData = df_ReleaseData[df_ReleaseData.Rel.str.upper() != 'X']

#print(df_ReleaseData.dtypes)
df_ToBePublished = df_ReleaseData[['Category', 'Super', 'Time Period', 'Detail1', 'Detail2', 'Detail3', 'Detail4', 'UCode', 'AnswerID', 'QLevel', 'QUESTID', 'SDID', 'QuestionID']].copy()
df_ToBePublished['CCP'] = df_ReleaseData[['New_Code']].copy()
df_ToBePublished['SID'] = 1952

df_ToBePublished = df_ToBePublished.assign(StudyEntryID=0, Version=0,Tmpl=3,ORD="",Wave=0,Full_Label="",Definition=np.nan,Status="Add",EditedBy="codebookcreator", EditedDate=datetime.now(),StudyAnswerID=0, Imported=False,Min=0,Max=0)
df_ToBePublished = df_ToBePublished.astype( {"QLevel":'int32', "QUESTID":'int32', "AnswerID":'int32',"QuestionID":'int32', "SDID":'int32', "Version":'int32',"Definition":'object',  "Wave":'int32', "Min":'float',"Max":'float', "StudyAnswerID":'int32'} )

engine = create_engine('mssql+pyodbc://' + DB['server'] + '/' + DB['database'] + '?' + DB['driver'], fast_executemany = True)

cursor = conn.cursor()
cursor.execute('DROP TABLE dbo.tmp_EditedRecords_Hold_Test')
conn.commit()

with engine.begin() as connection:
    df_ToBePublished.to_sql(name="tmp_EditedRecords_Hold_Test", con=engine, schema="dbo", if_exists = 'append',index=False)

EndTime = time.time() - startTime
print ('Done: ' + str(EndTime))