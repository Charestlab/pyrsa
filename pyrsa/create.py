import numpy
import itertools
from tqdm import trange

def rdm(x, labels, metric='correlation'):
    rdm_lda_kfold(x, labels)

def rdms(x, labels, metric='correlation'):
    nsamples, nfeatures, nmeasures = x.shape
    objects = numpy.unique(labels)
    pairs = list(itertools.combinations(objects, 2))
    npairs = len(pairs)
    utvs = numpy.full([nmeasures, npairs], numpy.nan)
    for m in trange(nmeasures, desc='RDMs', ascii=True):
        utvs[m, :] = rdm(x[:, :, m], labels)
    return utvs

def rdm_lda_kfold(x, labels):
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.model_selection import RepeatedStratifiedKFold
    from sklearn.model_selection import cross_val_score
    lda = LinearDiscriminantAnalysis(solver='lsqr', shrinkage='auto')
    folding = RepeatedStratifiedKFold(n_splits=3, n_repeats=3)

    objects = numpy.unique(labels)
    pairs = list(itertools.combinations(objects, 2))
    npairs = len(pairs)
    utv = numpy.full([npairs,], numpy.nan)
    for p in trange(npairs, desc='pairs', leave=False, ascii=True):
        pair = pairs[p]
        pair_mask = numpy.isin(labels, pair)
        x_pair = x[pair_mask, :]
        labels_pair = labels[pair_mask]
        scores = cross_val_score(lda, x_pair, labels_pair, cv=folding)
        utv[p] = scores.mean()
    return utv