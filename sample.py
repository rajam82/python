'''
Created on Jan 18, 2020

@author: rajam
'''
import pymysql
print("helloworld")
e=90
u=90
h=e+u
print(h)
word="sample"
print(word.replace("sa","sasasa",-1))
# Open database connection
db1 = pymysql.connect('localhost','root','root','world')
cur = db1.cursor();

data=cur.execute("select * from Emp")
data1 = cur.fetchall();
for row in data1:
  name=row[1]
  id=row[0]
  print(name,id)
  
  
print(data)
db1.commit();

db1.close()