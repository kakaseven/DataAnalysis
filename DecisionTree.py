from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier #引入决策树算法包
import numpy as np

np.random.seed(0)
iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target
indices = np.random.permutation(len(iris_x))
iris_x_train = iris_x[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_x_test = iris_x[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]

#设置树的最大深度为4
clf = DecisionTreeClassifier(max_depth=4)
clf.fit(iris_x_train, iris_y_train)
#引入画图相关的包
from IPython.display import Image
from sklearn import tree
#dot是一个程序化生成流程图的简单语言
import pydotplus

# dot_data = tree.export_graphviz(clf, out_file=None, feature_names=iris.feature_names, class_names=iris.target_names
#                                 , filled=True, rounded=True, special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data)
# Image(graph.create_png())

iris_y_predict = clf.predict(iris_x_test)
score = clf.score(iris_x_test, iris_y_test, sample_weight=None)
print('iris_y_predict=')
print(iris_y_predict)
print('iris_y_test=')
print(iris_y_test)
print('Accurary:', score)