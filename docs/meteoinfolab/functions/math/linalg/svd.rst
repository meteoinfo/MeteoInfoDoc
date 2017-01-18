.. _docs-meteoinfolab-funcitons-math-linalg-svd:


***********************
SVD decomposition
***********************

.. function:: svd(a)

    Singular Value Decomposition.
    
    Factorizes the matrix a into two unitary matrices U and Vh, and
    a 1-D array s of singular values (real, non-negative) such that
    ``a == U*S*Vh``, where S is a suitably shaped matrix of zeros with
    main diagonal s.
    
    ``Parameters``

    a : (M, N) array_like
        Matrix to decompose.
        
    ``Returns``

    U : ndarray
        Unitary matrix having left singular vectors as columns.
        Of shape ``(M,K)``.
    s : ndarray
        The singular values, sorted in non-increasing order.
        Of shape (K,), with ``K = min(M, N)``.
    Vh : ndarray
        Unitary matrix having right singular vectors as rows.
        Of shape ``(K,N)``.
    
    Examples::
    
        a = array([[1,0,0,0,2],[0,0,3,0,0],[0,0,0,0,0],[0,2,0,0,0]])
        U,s,Vh = linalg.svd(a)
        print s
        
    Result::
    
        >>> run script...
        array([3.0, 2.23606797749979, 2.0, 0.0])