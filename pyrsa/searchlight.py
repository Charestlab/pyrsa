import numpy as np
import pandas as pd
import os
from scipy.spatial.distance import cdist
from scipy.stats import spearmanr
from itertools import combinations
def upper_tri_indexing(A):
    # returns the upper triangle
    m = A.shape[0]
    r,c = np.triu_indices(m,1)
    return A[r,c]

class RSASearchLight():
    def __init__(self, mask, radius=1, thr=.7):
        """
        Parameters:
            mask:    3d spatial mask (of usable voxels set to 1)
            radius:  radius around each center (in voxels)
            thr :    proportion of usable voxels necessary
                     thr = 1 means we don't accept centers with voxels outside
                     the brain
        """
        self.mask = mask
        self.radius = radius
        self.thr = thr
        self.centers = self._findCenters()
        self.RDM = None
        self.NaNs = []

    def _findCenters(self):
        """
        Find all indices from centers with usable voxels over threshold.
        """
        # make centers a list of 3-tuple coords if not given
        centers = zip(*np.nonzero(self.mask))

        good_center = []
        for center in centers:
            ind = self.searchlightInd(center)
            if self.mask[ind].mean() >= self.thr:
                good_center.append(center)
        return good_center

    def searchlightInd(self, center):
        """Return indices for searchlight where distance < radius

        Parameters:
            center: point around which to make searchlight sphere
        Sets RDM variable to:
            numpy array of shape (3, N_comparisons) for subsetting data
        """
        center = np.array(center)
        shape = self.mask.shape
        cx, cy, cz = np.array(center)
        x = np.arange(shape[0])
        y = np.arange(shape[1])
        z = np.arange(shape[2])

        #First mask the obvious points
        # - may actually slow down your calculation depending.
        x = x[abs(x-cx)<self.radius]
        y = y[abs(y-cy)<self.radius]
        z = z[abs(z-cz)<self.radius]

        #Generate grid of points
        X,Y,Z = np.meshgrid(x,y,z)
        data = np.vstack((X.ravel(),Y.ravel(),Z.ravel())).T
        distance = cdist(data, center.reshape(1,-1), 'euclidean').ravel()

        return data[distance<self.radius].T.tolist()

    def checkNaNs(X):
        """
        TODO - this function
        """
        pass
        # nans = np.all(np.isnan(X), axis=0)[0]
        # return X[:,~nans]

    def fit(self, data, metric='correlation'):
        """
        Fit Searchlight for RDM
        Parameters:
            data:       4D numpy array - (x, y, z, condition vols)
            metric :    str or callable, optional
                        The distance metric to use.  If a string, the distance function can be
                        'braycurtis', 'canberra', 'chebyshev', 'cityblock', 'correlation',
                        'cosine', 'dice', 'euclidean', 'hamming', 'jaccard', 'kulsinski',
                        'mahalanobis', 'matching', 'minkowski', 'rogerstanimoto', 'russellrao',
                        'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean',
                        'wminkowski', 'yule'.
        """
        #brain = np.zeros((x, y, z, rdm_size, rdm_size))
        distances = []
        print('Runnning searchlight\n')
        for i, c in enumerate(self.centers):
            n_done = i/len(self.centers)*100
            if i % 50 == 0:
                print(f'{n_done:.0f}% done!', end='\r')

            # Get indices from center
            ind = np.array(self.searchlightInd(c))
            X = np.array([data[f[0], f[1], f[2], :] for f in ind.T]).T

            dist = upper_tri_indexing(cdist(X, X, 'correlation'))
            distances.append(dist)
        print('\n')

        x, y, z = data.shape[:-1]
        rdm_size = data.shape[-1]
        n_combs = len(list(combinations(np.arange(rdm_size), 2)))
        self.RDM = np.zeros((x, y, z, n_combs))
        self.RDM[centers[:, 0], centers[:, 1], centers[:, 2], :] = distances
