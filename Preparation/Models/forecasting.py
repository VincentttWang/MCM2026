import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing

class GM11:
    """
    Grey Prediction Model GM(1,1)
    Suitable for small datasets with uncertain information.
    """
    def __init__(self, x0):
        self.x0 = np.array(x0)
        self.n = len(self.x0)
        
    def predict(self, k=1):
        """
        Predict k steps ahead.
        """
        # 1. Accumulate
        x1 = np.cumsum(self.x0)
        
        # 2. Mean generation
        z1 = (x1[:-1] + x1[1:]) / 2.0
        
        # 3. Least Squares
        B = np.vstack([-z1, np.ones(self.n - 1)]).T
        Y = self.x0[1:]
        
        # u = [a, b]
        u = np.linalg.inv(B.T @ B) @ B.T @ Y
        a, b = u
        
        # 4. Prediction functionality
        def f(k):
            return (self.x0[0] - b/a) * np.exp(-a * k) + b/a

        # 5. Restore
        # x1_hat(k+1) = f(k)
        # x0_hat(k) = x1_hat(k) - x1_hat(k-1)
        
        predicted_x1 = np.array([f(i) for i in range(self.n + k)])
        predicted_x0 = np.concatenate(([predicted_x1[0]], np.diff(predicted_x1)))
        
        return predicted_x0

class TimeSeries:
    """
    Wrapper for ARIMA and Exponential Smoothing
    """
    @staticmethod
    def arima_predict(data, order=(1,1,1), steps=5):
        """
        ARIMA model.
        order: (p, d, q)
        """
        model = ARIMA(data, order=order)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=steps)
        return forecast
    
    @staticmethod
    def exp_smoothing_predict(data, seasonal='add', seasonal_periods=4, steps=5):
        """
        Exponential Smoothing (Holt-Winters)
        """
        model = ExponentialSmoothing(data, seasonal=seasonal, seasonal_periods=seasonal_periods)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps)
        return forecast

if __name__ == "__main__":
    print("--- GM(1,1) Test ---")
    data = [71.1, 72.4, 72.4, 72.1, 71.4, 72.0, 71.6]
    gm = GM11(data)
    pred = gm.predict(k=3)
    print("Original:", data)
    print("Prediction (including history + 3 future):", pred)
    
    print("\n--- ARIMA Test ---")
    # Generate random walk
    np.random.seed(42)
    ts_data = np.cumsum(np.random.randn(50)) + 100
    pred_arima = TimeSeries.arima_predict(ts_data, steps=3)
    print("ARIMA Forecast:", pred_arima)
