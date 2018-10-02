"""
 linearly interpolates between a set of given 'anchor' colours to give
 nCols and displays them if monitor is set 

 Copyright (C) 2012 Medical Research Council
 Ported in Python from Matlab by Ian Charest

"""

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
def rankTransformRDM(rdm):
    shape = rdm.shape
    rdm_ranks = rankdata(rdm)
    return scaler.fit_transform(rdm_ranks.reshape(-1, 1)).reshape(shape)