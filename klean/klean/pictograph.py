# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:23:17 2022

@author: CTTC
"""
import numpy as np
a=np.random.randint(100)
print(a)

b=np.random.randint(100, size=(5,5))
print(b)

c=np.random.rand(50)
print(c)

d=np.random.rand(3,5)
print(d)

e=np.random.choice([3,6,8,5])
print(e)

f=np.random.choice([3,6,4,6],size=(3,5))
print(f)

z=np.random.rand(20)
print(z)

y=np.random.rand(80)
print(y)

b=np.random.rand(100,size=(3,5))
print(b)
print(b.dtype)
print(b.shape)
print(b.ndim)
print(b.astype(float))
b1=b.reshape(5,3)
print(b1)

import numpy as np
import matplotlib.pyplot as plt

x=np.array([2017,2018,2019,2020])
shirt = [200,250,310,230]
cap =[100,220,220,210]


plt.bar(x+0.25,shirt,width=0.5,label='shirt sales')
plt.bar(x,cap,width=0.5,label='cap sales')
plt.legend()
plt.xticks(x,('2017','2018','2019','2022'))
plt.show()

import numpy as num
import matplotlib.pyplot as plt

bins=[10,20,30,40,50]

x=np.random.randint(0,50,100)

plt.hist(x, bins, histtype='bar')
plt.show()


plt.his(x,bins, histtype='bar', r
plt.grid()
plt.show()


img = plt.imread(r"C:\Users\CTTC\Pictures\thor.jpg")
plt.imshow(img)
plt.axis('off')
plt.show()

import pandas as pd


data = pd.read_excel(r"C:\Users\CTTC\Desktop\Datasets\ENB2012_data.xlsx")
df2= pd.read_csv(r"C:\Users\CTTC\Desktop\Datasets\Churn_Modelling.csv")
df3= pd.read_csv(r"C:\Users\CTTC\Desktop\Datasets\movie_metadata.csv")

data.isnull().sum()
df.isnull().sum()
df3.isnull().sum()

df3.dropna(axis=0,inplace=True)
df3.dropna(axis=1,inplace=True)
df3= pd.read_csv(r"C:\Users\CTTC\Desktop\Datasets\movie_metadata.csv")
df3.fillna('x',inplace=True)



df4= pd.read_csv(r"C:\Users\CTTC\Desktop\Datasets\auto-mpg.csv")
df4.isnull().sum()

df4.columns = ['a','b','c','d','e','f','g','h','i']

import numpy as np
df4.replace('?',np.nan,inplace=True)
df4.isnull().sum()
df4.dropna(axis=0,inplace=True)

#linear regression
import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.linespace(0,10,n)

y = x+2 +np.random.uniform(-1,1,n)

plt.scatter(x,y)
plt.show()
