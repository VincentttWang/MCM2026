import numpy as np
import pandas as pd

class AHP:
    """
    Analytic Hierarchy Process (AHP)
    """
    def __init__(self, criteria_matrix):
        """
        criteria_matrix: square matrix (n x n)
        """
        self.matrix = np.array(criteria_matrix)
        self.n = self.matrix.shape[0]
        
    def get_weights(self):
        """
        Calculate weights using the eigenvector method.
        Returns: weights array, consistency ratio (CR)
        """
        eig_val, eig_vec = np.linalg.eig(self.matrix)
        max_eig_val = np.max(eig_val).real
        eig_vec = eig_vec[:, np.argmax(eig_val)].real
        weights = eig_vec / np.sum(eig_vec)
        
        # Consistency Index (CI)
        CI = (max_eig_val - self.n) / (self.n - 1)
        # Random Consistency Index (RI) lookup (up to n=9)
        RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
        RI = RI_dict.get(self.n, 1.49) # Default for larger n
        
        CR = CI / RI if RI != 0 else 0
        return weights, CR

class TOPSIS:
    """
    Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)
    """
    def __init__(self, data, weights=None, beneficial_indices=None):
        """
        data: n x m matrix (n alternatives, m criteria)
        weights: array of length m (weights for criteria)
        beneficial_indices: list of indices for beneficial criteria (higher is better). 
                            Others are assumed to be cost criteria (lower is better).
        """
        self.data = np.array(data)
        self.n, self.m = self.data.shape
        if weights is None:
            self.weights = np.ones(self.m) / self.m
        else:
            self.weights = np.array(weights)
        self.beneficial_indices = beneficial_indices if beneficial_indices is not None else list(range(self.m))

    def calculate(self):
        # 1. Normalize
        norm_data = self.data / np.sqrt(np.sum(self.data**2, axis=0))
        
        # 2. Weighted Normalize
        weighted_data = norm_data * self.weights
        
        # 3. Ideal and Negative Ideal Solutions
        ideal = np.zeros(self.m)
        neg_ideal = np.zeros(self.m)
        
        for i in range(self.m):
            if i in self.beneficial_indices:
                ideal[i] = np.max(weighted_data[:, i])
                neg_ideal[i] = np.min(weighted_data[:, i])
            else:
                ideal[i] = np.min(weighted_data[:, i])
                neg_ideal[i] = np.max(weighted_data[:, i])
                
        # 4. Euclidean Distance
        dist_pos = np.sqrt(np.sum((weighted_data - ideal)**2, axis=1))
        dist_neg = np.sqrt(np.sum((weighted_data - neg_ideal)**2, axis=1))
        
        # 5. Score
        scores = dist_neg / (dist_pos + dist_neg)
        return scores

class EntropyWeight:
    """
    Entropy Weight Method (EWM)
    """
    def __init__(self, data):
        """
        data: n x m matrix (n samples, m features)
        """
        self.data = np.array(data)
        self.n, self.m = self.data.shape
        
    def get_weights(self):
        # 1. Normalize (Min-Max to avoid negatives and div by zero)
        # Using simple proportion here assuming positive data, or use MinMax externally.
        # Here we assume data is already positive.
        # Standard normalization: p_ij = x_ij / sum(x_ij)
        p = self.data / self.data.sum(axis=0)
        
        # 2. Entropy
        # Handle log(0)
        p[p == 0] = 1e-10
        k = 1 / np.log(self.n)
        e = -k * np.sum(p * np.log(p), axis=0)
        
        # 3. Weights
        d = 1 - e
        weights = d / np.sum(d)
        return weights

class CRITIC:
    """
    CRITIC Method (Criteria Importance Through Intercriteria Correlation)
    """
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        
    def get_weights(self):
        # 1. Normalize (Min-Max)
        df_norm = (self.data - self.data.min()) / (self.data.max() - self.data.min())
        
        # 2. Standard Deviation
        std = df_norm.std()
        
        # 3. Correlation
        corr = df_norm.corr().abs()
        
        # 4. Information content
        # C_j = sigma_j * sum(1 - r_ij)
        C = std * (1 - corr).sum()
        
        # 5. Weights
        weights = C / C.sum()
        return weights.values

if __name__ == "__main__":
    print("--- AHP Test ---")
    matrix = [
        [1, 3, 5],
        [1/3, 1, 2],
        [1/5, 1/2, 1]
    ]
    ahp = AHP(matrix)
    w, cr = ahp.get_weights()
    print("Weights:", w)
    print("CR:", cr)
    
    print("\n--- TOPSIS Test ---")
    data = [
        [250, 16, 12, 5],
        [200, 16, 8, 3],
        [300, 32, 16, 4],
        [275, 32, 8, 2] # 4 alternatives, 4 criteria
    ]
    # Assume: 1st beneficial, 2nd beneficial, 3rd cost, 4th cost (indices 0, 1, 2, 3)
    # Correcting assumption for beneficial_indices
    topsis = TOPSIS(data, beneficial_indices=[0, 1]) 
    scores = topsis.calculate()
    print("Scores:", scores)
    
    print("\n--- Entropy Weight Test ---")
    ew = EntropyWeight(data)
    print("Weights:", ew.get_weights())
    
    print("\n--- CRITIC Test ---")
    critic = CRITIC(data)
    print("Weights:", critic.get_weights())
