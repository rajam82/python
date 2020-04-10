'''
Created on Mar 1, 2020

@author: rajam
'''
import pandas
from sklearn import linear_model
df=pandas.read_csv('C:\\Users\\rajam\\Documents\\car.csv');
x=df[['Weight', 'Volume']];
y=df['CO2'];

regr=linear_model.LinearRegression();
regr.fit(x, y);

predco2=regr.predict([[1200,1200]]);
print(predco2);
print(regr.coef_);