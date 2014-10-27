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
        rankList, ranksFlat = numpy.unique(self.square, return_inverse=True)
        maxRank = rankList.size-1
        ranksFlat = ranksFlat/maxRank
        return ranksFlat.reshape(self.square.shape)


##### MATLAB
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

##### Javascript
#function rankTransform(RDM){
#    /*
#    transforms the matrix mat by replacing each element by its rank in the
#    distribution of all its elements. if scale01 is set the ranked elements
#    would be scaled between 0 to 1. One property of this function, as
#    indicated by its name, is that equal values would stay equal after
#    ranking and scaling. The way the function does this is by
#    assigning the mean scaled rank to all the equal entries of the input
#    matrix (mat). NaNs are ignored in this process.
#    __________________________________________________________________________
#    Copyright (C) 2014 Ian Charest @ Medical Research Council
#    */
#    // get the upper triangular vector
#    var utv = triu(RDM);
#    /*console.log(utv)*/

#    var sorted = utv.slice().sort(function(a,b){return b-a})
#    var rdmranks = utv.slice().map(function(v){ return sorted.indexOf(v)+1 });

#    var maxRank = utv.length;

#    for (var i =0; i < maxRank;i++){
#        rdmranks[i] = 1 - rdmranks[i]/maxRank;
#    }

#    return squareform(rdmranks)
#}
