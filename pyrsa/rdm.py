#!/usr/bin/python
# -*- coding: UTF-8 -*-
from scipy.spatial.distance import pdist, squareform
import numpy

def create(patterns):
    rdm = RDM()
    rdm.utv = pdist(patterns,'correlation')
    rdm.square = squareform(rdm.utv)
    return rdm

def secondorder(rdmlist):
    utvs = numpy.array([r.utv for r in rdmlist])
    rdm = RDM()
    rdm.utv = pdist(utvs,'correlation')
    rdm.square = squareform(rdm.utv)
    rdm.labels = [r.name for r in rdmlist]
    return rdm


class RDM(object):
    pass
