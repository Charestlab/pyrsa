#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy
from numpy import sqrt
import scipy.spatial.distance
from sklearn.manifold import MDS
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA


def mds(utv):
    rdm = scipy.spatial.distance.squareform(utv)
    seed = numpy.random.RandomState(seed=3)
    mds = MDS(n_components=2, max_iter=3000, eps=1e-9, random_state=seed,
                   dissimilarity="precomputed", n_jobs=1)
    pos = mds.fit_transform(rdm)

    # rescale
    #pos *= sqrt((X_true ** 2).sum()) / sqrt((pos ** 2).sum())


   # Y = mds.fit_transform(RDM)
#    if itime == 0:
#        Y = mds.fit_transform(RDM)
#    else:
#        d, Y, _ = procrustes(
#            Y, mds.fit_transform(RDM), scaling=False)

    # Rotate the data
    # clf = PCA(n_components=2)
    # pos = clf.fit_transform(pos)
    return pos
