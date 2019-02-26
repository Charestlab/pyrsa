import numpy as np
from scipy.spatial.distance import cdist
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn import svm
from tqdm import tqdm
from joblib import Parallel, delayed


def upper_tri_indexing(A):
    # returns the upper triangle
    m = A.shape[0]
    r, c = np.triu_indices(m, 1)
    return A[r, c]


def run_per_center(data, c, labels):
    svc = svm.LinearSVC()
    clf = make_pipeline(StandardScaler(), svc)

    # Get indices from center
    ind = np.array(c)
    X = np.array(data[ind, :]).T
    # pdb.set_trace()
    score = np.mean(cross_val_score(clf, X, labels, cv=9, n_jobs=1))
    return score


def get_distance(data, c):
    ind = np.array(c)
    X = np.array(data[ind, :]).T
    return upper_tri_indexing(cdist(X, X, 'correlation'))


class RSASearchLight():
    def __init__(self, mask, radius=1, thr=.7, njobs=1, verbose=False):
        """
        Parameters:
            mask:    3d spatial mask (of usable voxels set to 1)
            radius:  radius around each center (in voxels)
            thr :    proportion of usable voxels necessary
                     thr = 1 means we don't accept centers with voxels outside
                     the brain
        """
        self.verbose = verbose
        self.mask = mask
        self.njobs = njobs
        self.radius = radius
        self.thr = thr
        self.centers = self._findCenters()
        self.centerIndices = self._findCenterIndices()
        self.allIndices = self._allSphereIndices()
        self.RDM = None
        self.NaNs = []

    def _findCenters(self):
        """
        Find all indices from centers with usable voxels over threshold.
        """
        # make centers a list of 3-tuple coords
        centers = zip(*np.nonzero(self.mask))

        good_center = []
        for center in centers:
            ind = self.searchlightInd(center)
            if self.mask[ind].mean() >= self.thr:
                good_center.append(center)
        return np.array(good_center)

    def _findCenterIndices(self):
        """
        Find all subspace indices from centers
        """
        centerIndices = []
        dims = self.mask.shape
        for i, cen in enumerate(self.centers):
            n_done = i/len(self.centers)*100
            if i % 50 == 0 and self.verbose is True:
                print('Converting voxel coordinates of centers to subspace'
                      f'indices {n_done:.0f}% done!', end='\r')
            centerIndices.append(np.ravel_multi_index(np.array(cen), dims))
        print('\n')
        return np.array(centerIndices)

    def _allSphereIndices(self):
        allIndices = []
        dims = self.mask.shape
        for i, cen in enumerate(self.centers):
            n_done = i/len(self.centers)*100
            if i % 50 == 0 and self.verbose is True:
                print(f'Finding SearchLights {n_done:.0f}% done!', end='\r')

            # Get indices from center
            ind = np.array(self.searchlightInd(cen))           
            allIndices.append(np.ravel_multi_index(np.array(ind), dims))
        print('\n')
        return allIndices

    def searchlightInd(self, center):
        """Return indices for searchlight where distance < radius

        Parameters:
            center: point around which to make searchlight sphere
        Sets RDM variable to:
            numpy array of shape (3, N_comparisons) for subsetting data
        """
        center = np.array(center)
        shape = self.mask.shape
        cx, cy, cz = np.array(center)
        x = np.arange(shape[0])
        y = np.arange(shape[1])
        z = np.arange(shape[2])

        # First mask the obvious points
        # - may actually slow down your calculation depending.
        x = x[abs(x-cx) < self.radius]
        y = y[abs(y-cy) < self.radius]
        z = z[abs(z-cz) < self.radius]

        # Generate grid of points
        X, Y, Z = np.meshgrid(x, y, z)
        data = np.vstack((X.ravel(), Y.ravel(), Z.ravel())).T
        distance = cdist(data, center.reshape(1, -1), 'euclidean').ravel()

        return data[distance < self.radius].T.tolist()

    def checkNaNs(X):
        """
        TODO - this function
        """
        pass
        # nans = np.all(np.isnan(X), axis=0)[0]
        # return X[:,~nans]

    def fit_rsa(self, data, metric='correlation'):
        """
        Fit Searchlight for RDM
        Parameters:
            data:       4D numpy array - (x, y, z, condition vols)
            metric :    str or callable, optional
                        The distance metric to use.  If a string, the distance function can be
                        'braycurtis', 'canberra', 'chebyshev', 'cityblock', 'correlation',
                        'cosine', 'dice', 'euclidean', 'hamming', 'jaccard', 'kulsinski',
                        'mahalanobis', 'matching', 'minkowski', 'rogerstanimoto', 'russellrao',
                        'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean',
                        'wminkowski', 'yule'.
        """
        print('Running searchlight RSA')

        # reshape the data to squish the first three dimensions
        x, y, z, nobjects = data.shape

        # now the first dimension of data is directly indexable by
        # subspace index of the searchlight centers
        data = data.reshape((x*y*z, nobjects))

        # test get_distance()
        # for x in self.allIndices:
        #    t = get_distance(data, x)
        # test passed.

        # brain = np.zeros((x, y, z, rdm_size, rdm_size))
        if self.verbose is True:
            distances = Parallel(n_jobs=self.njobs)(
                delayed(get_distance)(
                    data, x) for x in tqdm(self.allIndices))
        else:
            distances = Parallel(n_jobs=self.njobs)(
                delayed(get_distance)(
                    data, x) for x in self.allIndices)
        # number of pairwise comparisons
        n_combs = nobjects*(nobjects-1) // 2
        self.RDM = np.zeros((x*y*z, n_combs))
        self.RDM[list(self.centerIndices), :] = distances
        self.RDM = self.RDM.reshape((x, y, z, n_combs))

    def fit_mvpa(self, data, labels):
            """
            Fit Searchlight for MVPA
            Parameters:
                data:       4D numpy array - (x, y, z, condition vols)
                labels:     classifier labels

            """
            print('Running searchlight Decoding')
            x, y, z, nobjects = data.shape
            # now the first dimension of data is directly indexable by
            # subspace index of the searchlight centers
            data = data.reshape((x*y*z, nobjects))

            # test run_per_center
            # for x in self.allIndices:
            #     t = run_per_center(data, x, labels)

            if self.verbose is True:
                scores = Parallel(n_jobs=self.njobs)(
                    delayed(run_per_center)(
                        data, x, labels) for x in tqdm(self.allIndices))
            else:
                scores = Parallel(n_jobs=self.njobs)(
                    delayed(run_per_center)(
                        data, x, labels) for x in self.allIndices)

            print('\n')

            self.MVPA = np.zeros((x*y*z))
            self.MVPA[list(self.centerIndices)] = scores
            self.MVPA = self.MVPA.reshape((x, y, z))
