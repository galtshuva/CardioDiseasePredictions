# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd

#BMI - DISC
def transformation(value):
    if value < 18.5:
        return 1
    elif value < 24.9:
        return 2
    elif value < 29.9:
        return 3
    else:
        return 4
()

data = pd.read_csv ('datasets\data.csv') 
dataset=data.iloc[:,0]
min_value=dataset.min()
max_value=dataset.max()
bins=np.linspace(min_value,max_value,4)
labels = [1,2,3]
dataset = pd.cut(dataset, bins=bins,labels=labels, include_lowest=True)
dataset.to_csv ("data_agebins", sep='\t', encoding='utf-8')

#AGE - disc by width
def transformation2(value):
    if value > 29.99 and value<=41.667:
        return 1
    elif  value>41.667 and value<= 53.33:
        return 2
    else:
        return 3
()

#MBP
def transformation3(value):
    if value <70:
        return 1
    elif  value< 103.33 and value>=70:
        return 2
    else:
        return 3
()

#ap_high
#def transformation4(value):
#    if value <120:
 #       return 1
  #  elif  value<= 130 and value>=120:
   #     return 2
   # else:
    #    return 3
#()

#ap_low
#def transformation5(value):
 #   if value <80:
  #      return 1
  #  elif  value< 90 and value>=80:
  #      return 2
  #  else:
   #     return 3
#()
   
data = pd.read_csv('datasets/data.csv')
#deleting the columns id & age_days
data = data.drop(['id','age_days'], axis = 1)
#inserting a new bmi column and its values
x = (data.height)/100
bmi = (data.weight)/x**2
data.insert(2,"BMI", bmi)
data = data.drop(['height','weight'], axis = 1)
data["BMI"] = data["BMI"].apply(transformation)
#rounding the age
data.age_year = round(data.age_year)

data = data[data.ap_hi>data.ap_lo]

data = data.drop(data[data.ap_hi<70].index)
data = data.drop(data[data.ap_hi>200].index)
data = data.drop(data[data.ap_lo<40].index)
data = data.drop(data[data.ap_lo>120].index)

#calculating the mean blood pressure
y = (data.ap_hi)/3
z = ((data.ap_lo)*2)/3
mbp = y+z
data.insert(3,"MBP", mbp)
data = data.drop(['ap_hi','ap_lo'], axis = 1)

#data["ap_hi"] = data["ap_hi"].apply(transformation4)
#data["ap_lo"] = data["ap_lo"].apply(transformation5)
data["MBP"] = data["MBP"].apply(transformation3)
data["age_year"] = data["age_year"].apply(transformation2)
data.to_csv("data_sofi2", sep='\t', encoding='utf-8')


