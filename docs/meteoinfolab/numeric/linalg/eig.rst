.. _docs-meteoinfolab-numeric-linalg-eig:


***********************
Compute eigenvalues
***********************

.. currentmodule:: numeric.linalg

.. function:: eig(a)

    Compute the eigenvalues and right eigenvectors of a square array.
    
    ``Parameters``

    a : (M, M) array
        Matrices for which the eigenvalues and right eigenvectors will
        be computed
        
    ``Returns``

    w : (M) array
        The eigenvalues, each repeated according to its multiplicity.
        The eigenvalues are not necessarily ordered. The resulting
        array will be of complex type, unless the imaginary part is
        zero in which case it will be cast to a real type. When ``a``
        is real the resulting eigenvalues will be real (0 imaginary
        part) or occur in conjugate pairs
    v : (M, M) array
        The normalized (unit "length") eigenvectors, such that the
        column ``v[:,i]`` is the eigenvector corresponding to the
        eigenvalue ``w[i]``.
    
    Examples::
    
        a = np.diag((1,2,3))
        w, v = np.linalg.eig(a)
        print w
        print v
        
    Result::
    
        >>> run script...
        array([1.0, 2.0, 3.0])
        array([[1.0, 0.0, 0.0]
              [0.0, 1.0, 0.0]
              [0.0, 0.0, 1.0]])