import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X = np.array(X)
    if(X.ndim < 2):
        return None
    cov = np.cov(X, ddof = 1, rowvar = False)
    stds = np.std(X, ddof = 1, axis = 0).reshape(-1, 1)
    prod_stds = np.matmul(stds, stds.T)
    return (cov/prod_stds)