from matplotlib.image import BboxImage,imread
from matplotlib.transforms import Bbox
import matplotlib.pyplot as plt
import numpy as np

#rename to "thumbnails" or "icons"

def imagesAsTickMarks(ax, images):
    TICKYPOS = -.6
    lowerCorner = ax.transData.transform((.8,TICKYPOS-.2))
    upperCorner = ax.transData.transform((1.2,TICKYPOS+.2))
    print(lowerCorner)
    print(upperCorner)
    bbox_image = BboxImage(Bbox([lowerCorner[0],
                                 lowerCorner[1],
                                 upperCorner[0],
                                 upperCorner[1],
                                 ]),
                           norm = None,
                           origin=None,
                           clip_on=False,
                           )

    image = imread(images[0])
    print('img loaded')
    bbox_image.set_data(image)
    ax.add_artist(bbox_image)

def imagesAtPositions(ax, images, positions):
    for s in range(len(positions)):
        #print(positions[s,:])
        bbox = Bbox(corners(ax, positions[s,:],20))
        bbox_image = BboxImage(bbox)
        image = imread(images[s])
        bbox_image.set_data(image)
        ax.add_artist(bbox_image)

def corners(ax, pos, size):
    tpos = ax.transData.transform((pos[0],pos[1]))
    return [[tpos[0], tpos[1]], [tpos[0]+size, tpos[1]+size]]

