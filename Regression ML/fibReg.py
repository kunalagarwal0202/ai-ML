import numpy as np

import numpy as np

class HybridFibonacciFeatures:
    def __init__(self, n_terms=5, decay=0.5):
        self.n_terms = n_terms
        self.decay = decay

    def transform(self, X):
        X = np.asarray(X).reshape(-1, 1)
        n = X.shape[0]

        # Always include linear term
        features = [X[:, 0]]

        # Fibonacci sequence base
        f1 = X[:, 0]
        f2 = X[:, 0]

        for i in range(2, self.n_terms + 1):
            fk = f1 + f2
            alpha = self.decay ** (i - 1)
            features.append(alpha * fk)
            f1, f2 = f2, fk

        return np.column_stack(features)
    
class HybridFibonacciRegression:
    def __init__(self, n_terms=5, decay=0.5):
        self.n_terms = n_terms
        self.decay = decay
        self.feature_gen = HybridFibonacciFeatures(n_terms, decay)
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        X_feat = self.feature_gen.transform(X)
        y = np.asarray(y).reshape(-1)

        assert X_feat.shape[0] == y.shape[0], \
            f"X has {X_feat.shape[0]} rows, y has {y.shape[0]}"

        X_design = np.c_[np.ones(X_feat.shape[0]), X_feat]

        theta = np.linalg.pinv(X_design.T @ X_design) @ X_design.T @ y

        self.bias = theta[0]
        self.weights = theta[1:]
        return self

    def predict(self, X):
        X_feat = self.feature_gen.transform(X)
        return self.bias + X_feat @ self.weights

    def transform(self, X):
        return self.feature_gen.transform(X)
    
class HybridFibonacciFeatures:
    def __init__(self, n_terms=5, decay=0.5):
        self.n_terms = n_terms
        self.decay = decay

    def transform(self, X):
        X = np.asarray(X)

        # Force (n_samples, 1)
        if X.ndim == 2 and X.shape[1] != 1:
            X = X[:, 0]
        X = X.reshape(-1, 1)

        n_samples = X.shape[0]

        # First column: linear term
        features = np.zeros((n_samples, self.n_terms))

        features[:, 0] = X[:, 0]  # linear term

        if self.n_terms > 1:
            features[:, 1] = X[:, 0]  # second fib base

        for i in range(2, self.n_terms):
            features[:, i] = (
                self.decay * (features[:, i-1] + features[:, i-2])
            )

        return features
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataset=pd.read_csv('Mall_Customers.csv')
x=dataset.iloc[:,2:-1].values
y=dataset.iloc[:,-1].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

regressor= HybridFibonacciRegression(n_terms=6, decay=0.3)
regressor.fit(x_train, y_train)

y_pred=regressor.predict(x_test)
print(y_pred)
print("--")
print(y_test)
from sklearn.metrics import accuracy_score, confusion_matrix