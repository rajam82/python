'''
Created on Feb 29, 2020

@author: rajam
'''
import numpy
import matplotlib.pyplot as py

x=numpy.random.normal(5,1,50000);
y=numpy.random.normal(10,1,50000);

py.scatter(x, y);
py.show();