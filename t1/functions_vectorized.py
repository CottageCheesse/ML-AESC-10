import numpy as np

def prod_non_zero_diag(x):
    """
    Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number
    """
    diag = np.diag(x)
    ne_z = diag[diag != 0]
    return np.prod(ne_z) if ne_z.size > 0 else 0

def are_multisets_equal(x, y):
    """
    Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean
    """

    return (np.sort(x), np.sort(y))

def max_after_zero(x):
    """
    Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number
    """
    zero_indices = np.where(x == 0)[0]
    if zero_indices.size == 0:
        return None
    return np.max(x[zero_indices])

def convert_image(img, coefs):
    """
    Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array
    """
    return np.tensordot(img, coefs, axes=([-1], [0]))

def run_length_encoding(x):
    """
    Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables
    """
    elements, counts = np.unique(x, return_counts=True)
    return elements, counts

def pairwise_distance(x, y):
    """
    Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array
    """
    return np.sqrt(((x[:, np.newaxis, :] - y[np.newaxis, :, :])**2).sum(axis=2))
