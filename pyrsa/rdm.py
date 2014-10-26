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

    def __init__(self, dissims=None):
        self.square = dissims

    @property
    def ranktransformed(self):
        ranks = numpy.arange(self.square.size)
        orderedIndices = numpy.argsort(self.square, None)
        rankVector = ranks[orderedIndices]
        return rankVector.reshape(self.square.shape)



#function rankArray=rankTransform(array,scale01)

#% transforms the array 'array' by replacing each element by its rank in the
#% distribution of all its elements



#if ~exist('scale01','var'), scale01=false; end;

#nonNan_LOG=~isnan(array);
#set=array(nonNan_LOG); % column vector

#[sortedSet, sortedIs]=sort(set);

#rankArray=nan(size(array));
#nonNan_IND=find(nonNan_LOG);
#rankArray(nonNan_IND(sortedIs))=1:numel(set);

#if scale01
#    rankArray=rankArray/numel(set);
#end
