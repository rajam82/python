'''
Created on Feb 29, 2020

@author: rajam
'''
import numpy
import matplotlib.pyplot as py

x=numpy.random.normal(.5,.1,10000);
py.hist(x,5);
py.show();