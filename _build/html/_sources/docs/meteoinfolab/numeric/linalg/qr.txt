.. _docs-meteoinfolab-numeric-linalg-qr:


***********************
QR decomposition
***********************

.. currentmodule:: numeric.linalg

.. function:: qr(a)

    Compute QR decomposition of a matrix.
    
    Calculate the decomposition ``A = Q R`` where Q is unitary/orthogonal and R upper triangular.
    
    ``Parameters``

    a : (M, N) array_like
        Matrix to be decomposed
    
    ``Returns``

    Q : float or complex ndarray
        Of shape (M, M), or (M, K) for ``mode='economic'``.  Not returned
        if ``mode='r'``.
    R : float or complex ndarray
        Of shape (M, N), or (K, N) for ``mode='economic'``.  ``K = min(M, N)``.
    
    Examples::
    
        a = array([[12, -51,   4],[6, 167, -68],[-4,  24, -41]])
        q,r = np.linalg.qr(a)
        print q
        print r
        
    Result::
    
        >>> run script...
        array([[-0.857142857142857, 0.3942857142857143, -0.3314285714285714]
              [-0.42857142857142855, -0.9028571428571428, 0.03428571428571431]
              [0.2857142857142857, -0.17142857142857143, -0.9428571428571428]])
        array([[-14.0, -21.000000000000004, 14.0]
              [0.0, -175.0, 69.99999999999999]
              [0.0, 0.0, 35.0]])