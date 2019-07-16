import scipy.spatial.distance
import matplotlib.pyplot as plt
import numpy
import pyrsa


def plot_rdm(utv, title, labels=None, ax=None):
    rdm = scipy.spatial.distance.squareform(utv)
    if ax is None:
        _, ax = plt.subplots()
    ax.set_title(title)
    if labels is not None:
        ax.set_xticks(numpy.arange(len(labels)))
        ax.set_yticks(numpy.arange(len(labels)))
        ax.set_yticklabels(labels, fontsize=6) 
        ax.set_xticklabels(labels, fontsize=6, rotation=90) 
    return ax.imshow(rdm)

def plot_mds(utv, title='', labels=None, ax=None):
    pos = pyrsa.mds(utv)
    ax.set_frame_on(False)
    ax.tick_params(left=False, bottom=False)
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.scatter(pos[:, 0], pos[:, 1], s=0)
    for i, label in enumerate(labels):
        ax.annotate(label, (pos[i, 0], pos[i, 1]), fontsize=6)