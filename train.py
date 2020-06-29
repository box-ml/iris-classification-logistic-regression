import pickle
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# Load dataset
iris_dataset = datasets.load_iris()
X = iris_dataset.data
y = iris_dataset.target

# Train the machine learning model
log_reg = LogisticRegression()
log_reg.fit(X, y)

# Test prediction
print(log_reg.predict([[6.4,2.9,4.3,1.3]]))

# Export the trained model
f = open('iris_logistic_regression.pkl','wb')
pickle.dump(log_reg, f)
f.close()

# Deploy in box.ml
# Drag & Drop the file iris_logistic_regression.pkl in box.ml
# Read the README.md file for more details.
