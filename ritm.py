# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 11:55:31 2021

@author: muhammet.aydin
"""

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd 
import csv
import os 
from datetime import date, timedelta, datetime
import datetime


#### RES'lerin Toplam Güç Üretimi ve Tahmini ####

url2 = 'http://www.ritm.gov.tr/amline/data_file_ritm.txt'
response2 = requests.get(url2)
soup = BeautifulSoup(response2.text, "html.parser")
soup2 = str(soup)
file1 = open("ritm.txt","w")
file1.writelines(soup2) 
file1.close() 

df = pd.read_fwf('ritm.txt', header=None, skiprows=[0])
df2= df[1].str.split(',',expand=True)
df3 = pd.concat([df[0], df2], axis=1, ignore_index=True)

df3.columns = ['Tarih','Saat','Q1','Q2','Q3','Q4','Tahmin', 'Gerçekleşme']

df3['Tahmin'] = df3['Tahmin'].astype(float)
df3['Gerçekleşme'] = df3['Gerçekleşme'].astype(float)
df3['Q1'] = df3['Q1'].astype(float)
df3['Q2'] = df3['Q2'].astype(float)
df3['Q3'] = df3['Q3'].astype(float)
df3['Q4'] = df3['Q4'].astype(float)

name_df3 = 'RİTM' + '_' + date.today().strftime('%Y%m%d')+'.xlsx'
name_df3_path= os.getcwd() + '\\' + name_df3

#### RES'lerin Ölçeklenmiş Toplam Üretim Tahmini ####

url3 = 'http://www.ritm.gov.tr/amline/data_file_bolgesel.txt' 
response3 = requests.get(url3)
soup1 = BeautifulSoup(response3.text, "html.parser")
soup2_1 = str(soup1)
file2 = open("ritm(1).txt","w")
file2.writelines(soup2_1) 
file2.close()
        
df_1 = pd.read_fwf('ritm(1).txt', header=None)
df_2 = df_1[1].str.split(',',expand=True)
df_3 = pd.concat([df_1[0], df_2], axis=1, ignore_index=True)
df_3.columns=['Tarih', 'Saat', 'Tahmin']
df_3['Tahmin']=df_3['Tahmin'].astype(float)

        
#### CSV YE YAZMA ####

df3.to_csv("RES'lerin Toplam Güç Üretimi ve Tahmini.csv", encoding='utf-8-sig', index=False)  
df_3.to_csv("RES'lerin Ölçeklenmiş Toplam Üretim Tahmini.csv", encoding='utf-8-sig', index=False)





