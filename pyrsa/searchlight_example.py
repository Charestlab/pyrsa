import nibabel as nib
from searchlight import *

# load 3d binary brain mask
mask = nib.load('binary_mask.nii.gz').get_data()

# load 4d contrast data (different conditions on the last dim)
img = nib.load('contrast_data.nii.gz')
data = img.get_data()

conditionlabels = [1, 1, 1, 2, 2, 2] #...

# initiate searchlight class (radius is in voxels, so be mindful)
SL = RSASearchLight(mask, radius=2, thr=1.0)

# Get searchlight RDMs
SL.fit_rsa(data)

# Save RDM
RDM_img = nib.Nifti1Image(SL.RDM, img.affine, img.header)
nib.save(RDM_img, 'RDM_brain.nii.gz')

# Get searchlight decoding
SL.fit_mvpa(data, conditionlabels)
