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

class MDSTests(unittest.TestCase):

    def test_Input_rdm_object_and_returns_positions(self):
        from pyrsa import RDM, mds
        rdm = RDM(dissims)
        # Can call mds() on RDM object
        pos = mds(rdm)
        # MDS positions has a column for x and y coordinates, 
        #   one row for each item
        self.assertEqual(pos.shape, (6, 2))



if __name__ == '__main__':
    unittest.main()
