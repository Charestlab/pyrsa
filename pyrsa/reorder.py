import numpy
from scipy.spatial.distance import squareform


def reorder_rdm(utv, newOrder):
    ax, bx = numpy.ix_(newOrder, newOrder)
    newOrderRDM = squareform(utv)[ax, bx]
    return squareform(newOrderRDM, 'tovector', 0)

def reorder_rdms(utvs, newOrder):
    newOrderUTVs = utvs.copy()
    for m in range(utvs.shape[0]):
        newOrderUTVs[m, :] = reorder_rdm(utvs[m, :], newOrder)
    return newOrderUTVs
