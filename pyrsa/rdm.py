#!/usr/bin/python
# -*- coding: UTF-8 -*-
from scipy.spatial.distance import pdist, squareform

def create(patterns):
    rdm = RDM()
    rdm.utv = pdist(patterns,'correlation')
    rdm.square = squareform(rdm.utv)
    return rdm


class RDM(object):
    pass
