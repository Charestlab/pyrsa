#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from sklearn.manifold import MDS
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA


def mds(rdm):
    seed = np.random.RandomState(seed=3)

    mds = MDS(n_components=2, max_iter=3000, eps=1e-9, random_state=seed,
                   dissimilarity="precomputed", n_jobs=1)
    pos = mds.fit(rdm.square).embedding_

    #nmds = MDS(n_components=2, metric=False, max_iter=3000, eps=1e-12,
    #                    dissimilarity="precomputed", random_state=seed, n_jobs=1,
    #                    n_init=1)
    #npos = nmds.fit_transform(similarities, init=pos)

    # Rescale the data
#    if patterns:
#        pos *= np.sqrt((patterns ** 2).sum()) / np.sqrt((pos ** 2).sum())
    #npos *= np.sqrt((X_true ** 2).sum()) / np.sqrt((npos ** 2).sum())

    # Rotate the data
    clf = PCA(n_components=2)
    pos = clf.fit_transform(pos)
    #npos = clf.fit_transform(npos)
    return pos
