import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import os

os.environ['PATH'] = os.environ['PATH']+";C:\\Program Files (x86)\\Graphviz2.38\\bin\\graphviz"
df = pandas.read_csv("C:\\Users\\rajam\\Documents\\show.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('C:\\Users\\rajam\\Documents\\mydecisiontree.png')
img=pltimg.imread('C:\\Users\\rajam\\Documents\\mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()