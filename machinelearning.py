'''
Created on Feb 29, 2020

@author: rajam
'''
import numpy as numpy1
import matplotlib.pyplot as pyplot

x = numpy1.random.uniform(0.0,0.5,250);
pyplot.hist(x,1000);
pyplot.show();