from math import sqrt
import numpy as np
def prod_non_zero_diag(x):
    res = 1
    for i in range(min(len(x), len(x[0]))):
        if(x[i][i]):
            res *= x[i][i]
    return res
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """

    pass


def are_multisets_equal(x, y):

    return sorted(x) == sorted(y)
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """

    pass


def max_after_zero(x):
    res = 0
    for i in range(1, len(x)):
        if(x[i-1] == 0):
            res = max(res, x[i])
    return res
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """

    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """
    res = [[0] * len(img[0]) for _ in range(len(img))]
  
    for hi in range(len(img)):

        for wi in range(len(img[0])):
            res[hi][wi] = img[hi][wi][0] * coefs[0] +img[hi][wi][1]  * coefs[1] + img[hi][wi][2] * coefs[2]   
            
    return res



def run_length_encoding(x):
    ct = {}
    el = []
    counter = []
    for i in x:
        i = int(i)
        ct[i] = ct.get(i, 0) + 1
        if(ct[i] == 1):
            el.append(i)
    for i in el:
        counter.append(ct[i])
        
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """

    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array(

    Non Vctorized implementation.
    """
    res = [[0]*len(x)]*len(x)
    for i in range(len(x)):
        for j in range(len(y)):
            res[i][j] = sqrt((x[i][0] - y[j][0])**2 + (x[i][1] - y[j][1])**2)


    return res
