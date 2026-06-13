# Libraries import
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Dataset Load
iris = load_iris()
X = iris.data
y = iris.target

# Dataset Understand
print("Features: ")
print(iris.feature_names)
print("\nTarget classes: ")
print(iris.target_names)
print("\nDataset shape: ")
print(X.shape)

# Train-test-split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 42
)

# Model Create
model = DecisionTreeClassifier()

# Model Training
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: ", accuracy)

