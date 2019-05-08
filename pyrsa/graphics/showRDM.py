#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
#from pyrsa.graphics.imagesAsTickMarks import imagesAsTickMarks


def showRDM(rdm, save=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.matshow(rdm.square)
    #ax.set_title(rdm.name, y=-.2)
    #imagesAsTickMarks(ax, rdm.images)
    plt.yticks(np.arange(len(rdm.labels)), rdm.labels, size=8)
    plt.xticks(np.arange(len(rdm.labels)), rdm.labels, size=8, rotation=90)
    if save:
        fname = rdm.name.replace(' ', '_')+'.png'
        print('Saving '+fname)
        plt.savefig(fname)
        plt.close()
    else:
        plt.show()
