'''
Created on Mar 1, 2020

@author: rajam
'''
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale=StandardScaler();
df=pandas.read_csv('C:\\Users\\rajam\\Documents\\car1.csv');
x=df[['Weight', 'Volume']];
y=df['CO2'];
scalex=scale.fit_transform(x);

regr=linear_model.LinearRegression();
regr.fit(scalex, y);
scaled=scale.transform([[2300,1.5]]);
print(regr.coef_);
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)