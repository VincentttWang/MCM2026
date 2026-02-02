import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score, mean_squared_error

class RegressionModel:
    def __init__(self):
        self.model = None
        
    def fit_predict_linear(self, X, y, X_new=None):
        self.model = LinearRegression()
        self.model.fit(X, y)
        if X_new is None: X_new = X
        return self.model.predict(X_new), self.model.coef_, self.model.intercept_
    
    def fit_predict_polynomial(self, X, y, degree=2, X_new=None):
        self.model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        self.model.fit(X, y)
        if X_new is None: X_new = X
        return self.model.predict(X_new)

    def fit_predict_logistic(self, X, y, X_new=None):
        """
        For classification (y is categorical/binary)
        """
        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(X, y)
        if X_new is None: X_new = X
        return self.model.predict(X_new), self.model.predict_proba(X_new)
        
    def fit_predict_ridge(self, X, y, alpha=1.0, X_new=None):
        self.model = Ridge(alpha=alpha)
        self.model.fit(X, y)
        if X_new is None: X_new = X
        return self.model.predict(X_new)

if __name__ == "__main__":
    print("--- Linear Regression Test ---")
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 5, 4, 5])
    reg = RegressionModel()
    pred, coef, intercept = reg.fit_predict_linear(X, y)
    print(f"Coef: {coef}, Intercept: {intercept}")
    print("Prediction:", pred)
    
    print("\n--- Polynomial Regression Test ---")
    pred_poly = reg.fit_predict_polynomial(X, y, degree=2)
    print("Poly Prediction:", pred_poly)
