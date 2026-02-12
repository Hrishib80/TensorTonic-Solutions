import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X = np.array(X)
    if(X.ndim < 2):
        return None
    X = X.T
    return np.corrcoef(X)