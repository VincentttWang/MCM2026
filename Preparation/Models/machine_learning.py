import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
import matplotlib.pyplot as plt

class MLModels:
    @staticmethod
    def kmeans_clustering(X, n_clusters=3):
        """
        K-Means Clustering.
        Returns: labels, centers, model
        """
        model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = model.fit_predict(X)
        return labels, model.cluster_centers_, model
    
    @staticmethod
    def pca_reduction(X, n_components=2):
        """
        Principal Component Analysis (PCA) for dimensionality reduction.
        Returns: X_transformed, variance_ratio, model
        """
        model = PCA(n_components=n_components)
        X_pca = model.fit_transform(X)
        return X_pca, model.explained_variance_ratio_, model
    
    @staticmethod
    def random_forest_classification(X, y, test_size=0.2):
        """
        Random Forest Classification.
        Returns: model, accuracy, report
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        report = classification_report(y_test, preds)
        return model, acc, report

    @staticmethod
    def svm_classification(X, y, test_size=0.2):
        """
        Support Vector Machine Classification.
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        model = SVC(kernel='rbf', random_state=42)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        return model, acc

if __name__ == "__main__":
    from sklearn.datasets import make_blobs, make_classification
    
    print("--- K-Means Test ---")
    X, _ = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)
    labels, centers, _ = MLModels.kmeans_clustering(X, n_clusters=3)
    print("Cluster Centers:\n", centers)
    
    print("\n--- PCA Test ---")
    X_pca, var_ratio, _ = MLModels.pca_reduction(X, n_components=2)
    print("Explained Variance Ratio:", var_ratio)
    
    print("\n--- Random Forest Test ---")
    X_cls, y_cls = make_classification(n_samples=100, n_features=4, random_state=42)
    rf_model, acc, report = MLModels.random_forest_classification(X_cls, y_cls)
    print(f"Accuracy: {acc:.4f}")
    # print("Report:\n", report)
