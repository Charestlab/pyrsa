#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from imagesAsTickMarks import imagesAtPositions


def MDSplot(rdm, pos, save=False):
    iconsAsLabels = True
    similarities = rdm.square
    fig = plt.figure(1)
    ax = plt.axes([0., 0., 1., 1.]) #

    
    plt.scatter(pos[:, 0], pos[:, 1], s=0)

    if not hasattr(rdm, 'images'):
        for s in range(len(rdm.labels)):
            plt.annotate(rdm.labels[s], xy = (pos[s, 0], pos[s, 1]), xytext = (-20, 20),
                textcoords = 'offset points')
    else:
        imagesAtPositions(ax, rdm.images, pos)
    ax.set_title(rdm.name)
    if save:
        fname = 'MDS_'+rdm.name.replace(' ','_')+'.png'
        print('Saving '+fname)
        plt.savefig(fname)
        plt.close()
    else:
        plt.show()


