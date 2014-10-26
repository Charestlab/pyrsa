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
        #all integers
        self.assertEqual(list(range(dissims.size)), 
            numpy.sort(numpy.ravel(rdmR)).tolist())



if __name__ == '__main__':
    unittest.main()
