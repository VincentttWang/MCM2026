# MCM Models Library

This folder contains common algorithms, models, and plotting scripts for the Mathematical Contest in Modeling (MCM/ICM).

## Contents

### 1. Data Preprocessing & Visualization
- **`plot_templates.py`**: High-quality plotting functions (Line, Multi-line, Scatter, Heatmap, Bar, 3D Surface).
- **`data_preprocessing.py`**: Missing value handling, outlier detection (Z-score, IQR), normalization (Min-Max, Z-score).

### 2. Evaluation & Decision Making
- **`evaluation_methods.py`**:
    - **AHP**: Analytic Hierarchy Process for weighting.
    - **TOPSIS**: Technique for Order of Preference by Similarity to Ideal Solution.
    - **EntropyWeight**: Entropy Weight Method (EWM).
    - **CRITIC**: Criteria Importance Through Intercriteria Correlation.

### 3. Prediction & Forecasting
- **`forecasting.py`**:
    - **GM11**: Grey Prediction Model (GM(1,1)).
    - **TimeSeries**: Wrapper for ARIMA and Exponential Smoothing.
- **`regression.py`**: Linear, Polynomial, Logistic, Ridge, and Lasso regression wrappers.

### 4. Optimization
- **`optimization.py`**: Wrappers for Linear Programming and Non-linear Optimization using `scipy.optimize`.

### 5. Differential Equations
- **`differential_equations.py`**: `ODESolver` class and templates for Logistic Growth, SEIR, and Lotka-Volterra models.

### 6. Graph Theory
- **`graph_algorithms.py`**: Shortest Path, Minimum Spanning Tree (MST), Centrality measures, and Efficiency using `networkx`.

### 7. Machine Learning & Statistics
- **`machine_learning.py`**: K-Means Clustering, PCA, Random Forest, SVM.
- **`statistical_tests.py`**: Correlation, Normality tests, T-tests.

## Usage

Each script contains a `if __name__ == "__main__":` block with example usage. You can run any file directly to see a demo:

```bash
python Models/plot_templates.py
python Models/evaluation_methods.py
# etc.
```

To use in your notebook or script:

```python
import sys
sys.path.append('Models') # Add folder to path if needed, or just import if in same dir

from Models.plot_templates import plot_line
from Models.evaluation_methods import AHP

# Use functions...
```
