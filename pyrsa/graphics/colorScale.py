"""
 linearly interpolates between a set of given 'anchor' colours to give
 nCols and displays them if monitor is set 

 Copyright (C) 2012 Medical Research Council
 Ported in Python from Matlab by Ian Charest

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def colorScale(nCols, anchorCols=None, monitor=None):

       
    if anchorCols is None:
        anchorCols = np.array([[1, 0, 0], [0, 0, 1]])

    # define color scale
    nAnchors=anchorCols.shape[0]

    fn = interp1d(
        range(nAnchors),
        anchorCols.T,         
    )
    
    cols = fn(np.linspace(0,nAnchors-1,nCols)).T

    # visualise
    if monitor:
        fig = plt.figure()
        reshapedCols = cols.reshape((nCols, 1, 3))
        width = int(nCols/2)
        mapping = np.tile(reshapedCols,(width,1))
        plt.imshow(mapping)
        plt.show()
    
    return cols
    #interp1d(self, x, y, kind='linear', axis=-1, copy=True, bounds_error=None, fill_value=nan, assume_sorted=False)

    
