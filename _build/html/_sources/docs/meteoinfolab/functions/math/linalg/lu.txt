.. _docs-meteoinfolab-funcitons-math-linalg-lu:


***********************
LU decomposition
***********************

.. function:: lu(a)

    Compute pivoted LU decomposition of a matrix.
    
    The decomposition is::
    
        A = P L U
        
    where P is a permutation matrix, L lower triangular with unit
    diagonal elements, and U upper triangular.
    
    ``Parameters``

    a : (M, M) array_like
        Array to decompose
    permute_l : bool, optional
        Perform the multiplication P*L  (Default: do not permute)
    overwrite_a : bool, optional
        Whether to overwrite data in a (may improve performance)
    check_finite : bool, optional
        Whether to check that the input matrix contains only finite numbers.
        Disabling may give a performance gain, but may result in problems
        (crashes, non-termination) if the inputs do contain infinities or NaNs.
        
    ``Returns``

    p : (M, M) ndarray
        Permutation matrix
    l : (M, M) ndarray
        Lower triangular or trapezoidal matrix with unit diagonal.
    u : (M, M) ndarray
        Upper triangular or trapezoidal matrix
    
    Examples::
    
        a = array([[1,3,5],[2,4,7],[1,1,0]])
        p,l,u = np.linalg.lu(a)
        print p
        print l
        print u
        
    Result::
    
        >>> run script...
        array([[0.0, 1.0, 0.0]
              [1.0, 0.0, 0.0]
              [0.0, 0.0, 1.0]])
        array([[1.0, 0.0, 0.0]
              [0.5, 1.0, 0.0]
              [0.5, -1.0, 1.0]])
        array([[2.0, 4.0, 7.0]
              [0.0, 1.0, 1.5]
              [0.0, 0.0, -2.0]])