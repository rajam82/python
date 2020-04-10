'''
Created on Jan 25, 2020

@author: rajam
'''
import com.cts.python.greetings as greetings
import com.cts.python.Employee as emp
e1=emp.Employee("raja",32)
sal=e1.calculate();
print("before")
print(sal)
greetings.greeting("ratan tata");
greetings.warning("misubalhag")
if __name__ == '__main__':
    pass

list1=["orange","apple","vinegar"]
print(list1[1:3])
list1.append("cutlet")
print(list1)
list1.remove("apple")
print(list1)

tuple1 = ("pope","stokes","wood")
x = list(tuple1)
x[0]="saqlain"
x.append("kohli")
tuple1 = tuple(x)
print(tuple1)

set1={"charless","soosai","pottuamman"};
set1.add("victor")
print(set1)
set1.remove("soosai")
print(set1)
dic={"india":"kohli","usa":"trump"}
dic["northkorea"]="kim"
print(dic)
for x in tuple1:
    print(x)
