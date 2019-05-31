import numpy
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import rankdata


def rank_transform(rdm):
    scaler = MinMaxScaler()
    shape = rdm.shape
    rdm_ranks = rankdata(rdm)
    return scaler.fit_transform(rdm_ranks.reshape(-1, 1)).reshape(shape)


def triu_vector(A):
    # returns the upper triangle
    m = A.shape[0]
    r, c = numpy.triu_indices(m, 1)
    return A[r, c]