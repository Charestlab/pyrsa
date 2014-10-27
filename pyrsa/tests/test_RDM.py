import unittest
from mock import Mock, sentinel, patch
import numpy

dissims = numpy.array([ [0,   0.1, 0.1, 0.9, 0.9, 0.9], 
                    [0.1, 0,   0.1, 0.9, 0.9, 0.9], 
                    [0.1, 0.1, 0,   0.9, 0.9, 0.9], 
                    [0.9, 0.9, 0.9, 0,   0.1, 0.1], 
                    [0.9, 0.9, 0.9, 0.1, 0,   0.1], 
                    [0.9, 0.9, 0.9, 0.1, 0.1, 0  ], 
                    ])

class RDMTests(unittest.TestCase):

    def test_Ranktransform(self):
        from pyrsa import RDM
        rdm = RDM(dissims)
        rdmR = rdm.ranktransformed
        # same dimensions
        self.assertEqual(rdmR.shape, rdm.square.shape)
        # rank preserved
        self.assertGreater(rdmR[0,1], rdmR[0,0])
        self.assertGreater(rdmR[0,3], rdmR[0,1])
        # same values stay same
        self.assertEqual(rdmR[0,1], rdmR[0,2])
        # max 1 min 0
        self.assertEqual(rdmR.max(), 1)
        self.assertEqual(rdmR.min(), 0)



if __name__ == '__main__':
    unittest.main()




#dissims = numpy.array([ [0,   0.1, 0.1, 0.9, 0.9, 0.9], 
#                    [0.1, 0,   0.1, 0.9, 0.9, 0.9], 
#                    [0.1, 0.1, 0,   0.9, 0.9, 0.9], 
#                    [0.9, 0.9, 0.9, 0,   0.1, 0.1], 
#                    [0.9, 0.9, 0.9, 0.1, 0,   0.1], 
#                    [0.9, 0.9, 0.9, 0.1, 0.1, 0  ], 
#                    ])


#In [6]: numpy.arange(36).reshape([6,6])
#Out[6]: 
#array([[ 0,  1,  2,  3,  4,  5],
#       [ 6,  7,  8,  9, 10, 11],
#       [12, 13, 14, 15, 16, 17],
#       [18, 19, 20, 21, 22, 23],
#       [24, 25, 26, 27, 28, 29],
#       [30, 31, 32, 33, 34, 35]])

