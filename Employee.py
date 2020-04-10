'''
Created on Jan 25, 2020

@author: rajam
'''

class Employee:
    '''
    classdocs
    '''


    def __init__(self, name, age):
        '''
        Constructor
        '''
        self.name=name;
        self.age=age;
        
    def calculate(self):
        return self.age*100
    
        