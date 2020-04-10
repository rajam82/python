'''
Created on Mar 1, 2020

@author: rajam
'''
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))

print(r2)


mymodel1 = numpy.poly1d(numpy.polyfit(test_x, test_y, 4))

r21 = r2_score(test_y, mymodel1(test_x))

print(r21)
