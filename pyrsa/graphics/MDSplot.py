#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection


def MDSplot(rdm, pos):
	similarities = rdm.square
	fig = plt.figure(1)
	ax = plt.axes([0., 0., 1., 1.])

	plt.scatter(pos[:, 0], pos[:, 1], s=20, c='g')

	similarities = similarities.max() / similarities * 100
	similarities[np.isinf(similarities)] = 0

#	# Plot the edges
#	start_idx, end_idx = np.where(pos)
#	#a sequence of (*line0*, *line1*, *line2*), where::
#	#            linen = (x0, y0), (x1, y1), ... (xm, ym)
#	segments = [[X_true[i, :], X_true[j, :]]
#		    for i in range(len(pos)) for j in range(len(pos))]
#	values = np.abs(similarities)
#	lc = LineCollection(segments,
#		            zorder=0, cmap=plt.cm.hot_r,
#		            norm=plt.Normalize(0, values.max()))
#	lc.set_array(similarities.flatten())
#	lc.set_linewidths(0.5 * np.ones(len(segments)))
#	ax.add_collection(lc)
	for s in range(len(rdm.labels)):
		plt.annotate(rdm.labels[s], xy = (pos[s, 0], pos[s, 1]), xytext = (-20, 20),
			textcoords = 'offset points')
	plt.show()
