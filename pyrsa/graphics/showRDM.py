#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def showRDM(rdm, save=False):
    plt.matshow(rdm.square)
    plt.title(rdm.name)
    plt.yticks(np.arange(len(rdm.labels)), rdm.labels, size=8)
    plt.xticks(np.arange(len(rdm.labels)), rdm.labels, size=8, rotation=90)
    if save:
        plt.savefig(rdm.name.replace(' ','_')+'.png')
        plt.close()
    else:
        show()
