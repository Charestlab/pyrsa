import scipy.spatial.distance
import numpy

x = numpy.arange(10)
utv = scipy.spatial.distance.pdist(numpy.atleast_2d(x).T)
rdm = scipy.spatial.distance.squareform(utv)

utvs = numpy.stack([utv, 9-utv])