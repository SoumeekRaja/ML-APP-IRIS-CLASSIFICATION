import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test , y_train, y_test = train_test_split(X, y)

model = SVC(kernel="poly", degree=2)

model.fit(X_train, y_train)

#saving model to disk
pickle.dump(model, open('model.pkl', 'wb'))

#Loading model to check accuracy
y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))