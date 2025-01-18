import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d=pd.read_csv('dataset11.csv',index_col=0)

print(d)


#print("--------------------------------------------------------------")

#print the info of data frame
# print(d.info())
#print(d.dtypes)

#now  remove the fault or noisy data
c=pd.read_csv('dataset11.csv',index_col=0,na_values=['??','????'])


#check the type
# print(c.dtypes)
# print("--------------------------------------------------------------")

#check the null counts
# print(c.isnull().sum())


#fill the null count according to the datatype 
  #if int type then use mean()
    # if object type then use mode()
c['Rank'].fillna(c['Rank'].mean(),inplace=True)
c['1980'].fillna(c['1980'].mean(),inplace=True)
c['2000'].fillna(c['2000'].mean(),inplace=True)
c['2010'].fillna(c['2010'].mean(),inplace=True)
c['2021'].fillna(c['2021'].mean(),inplace=True)
c['2022'].fillna(c['2022'].mean(),inplace=True)
c['2030'].fillna(c['2030'].mean(),inplace=True)
c['2050'].fillna(c['2050'].mean(),inplace=True)
c['area'].fillna(c['area'].mean(),inplace=True)
c['landAreaKm'].fillna(c['landAreaKm'].mean(),inplace=True)
c['growthRate'].fillna(c['growthRate'].mean(),inplace=True)
c['landAreaKm'].fillna(c['landAreaKm'].mean(),inplace=True)
c['worldPercentage'].fillna(c['worldPercentage'].mean(),inplace=True)
c['density'].fillna(c['density'].mean(),inplace=True)
#print("--------------------------------------------------------------")

#check the null value count
# print(c.isnull().sum())

#print("--------------------------------------------------------------")
# print(c.info())
#print("--------------------------------------------------------------")

#convert the data types according to the respective data
c['Rank']=c['Rank'].astype('int64')
c['1980']=c['1980'].astype('int64')
c['2000']=c['2000'].astype('int64')
c['2010']=c['2010'].astype('int64')
c['2021']=c['2021'].astype('int64')
c['2022']=c['2022'].astype('int64')
c['2030']=c['2030'].astype('int64')
c['2050']=c['2050'].astype('int64')
c['area']=c['area'].astype('int64')
c['landAreaKm']=c['landAreaKm'].astype('int64')

# print(c.describe(include=float,exclude=[object,int]))

# finally print the types and info
# print(c.dtypes)
# print(c.info())

# 1
# Retrieve the population data for a specific country for the years 1980, 2000, 2010, 2021, and observe the growth trends
country_data = c[c["country"] == "India"]
# Select the population data for the years 1980, 2000, 2010, and 2021
population_years = country_data[["1980", "2000", "2010", "2021"]]
print(population_years)


# 2Top 10 Most Populous Countries in 2030:
  #  - Identify the top 10 countries with the highest projected populations in the year 2030.

# sorted_data = c.sort_values(by=["2030"], ascending=False)
# print(sorted_data)
# # Select the top 10 countries with the highest projected populations in the year 2030
# top_10_countries = sorted_data.head(10)
# # Display the top 10 countries
# print(top_10_countries[["country", "2030"]])




