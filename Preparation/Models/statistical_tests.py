import numpy as np
import pandas as pd
from scipy import stats

class StatisticalTests:
    @staticmethod
    def correlation(df, method='pearson'):
        """
        Calculate correlation matrix.
        method: 'pearson', 'kendall', 'spearman'
        """
        return df.corr(method=method)
    
    @staticmethod
    def normality_test(data):
        """
        Shapiro-Wilk test for normality.
        Returns: statistic, p-value
        """
        stat, p = stats.shapiro(data)
        return stat, p
    
    @staticmethod
    def t_test_ind(group1, group2):
        """
        Independent T-test.
        Returns: statistic, p-value
        """
        stat, p = stats.ttest_ind(group1, group2)
        return stat, p

    @staticmethod
    def check_significance(p_value, alpha=0.05):
        """
        Helper to interpret p-value.
        """
        if p_value < alpha:
            return "Significant (Reject H0)"
        else:
            return "Not Significant (Fail to reject H0)"

if __name__ == "__main__":
    print("--- Statistical Tests ---")
    
    # 1. Correlation
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [2, 4, 6, 8, 10],
        'C': [5, 4, 3, 2, 1]
    })
    print("Correlation:\n", StatisticalTests.correlation(df))
    
    # 2. Normality
    data = np.random.randn(100)
    stat, p = StatisticalTests.normality_test(data)
    print(f"\nNormality (Shapiro) p={p:.4f}: {StatisticalTests.check_significance(p)}")
    
    # 3. T-Test
    g1 = np.random.normal(0, 1, 100)
    g2 = np.random.normal(1, 1, 100)
    stat, p = StatisticalTests.t_test_ind(g1, g2)
    print(f"\nT-Test (Ind) p={p:.4f}: {StatisticalTests.check_significance(p)}")
