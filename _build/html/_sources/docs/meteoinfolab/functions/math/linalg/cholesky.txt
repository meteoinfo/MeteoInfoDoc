.. _docs-meteoinfolab-funcitons-math-linalg-cholesky:


***********************
Cholesky decomposition
***********************

.. function:: cholesky(a)

    Cholesky decomposition.
    
    Return the Cholesky decomposition, ``L * L.H``, of the square matrix ``a``,
    where ``L`` is lower-triangular and .H is the conjugate transpose operator
    (which is the ordinary transpose if ``a`` is real-valued).  ``a`` must be
    Hermitian (symmetric if real-valued) and positive-definite.  Only ``L`` is
    actually returned.
    
    ``Parameters``
    
    a : (M, M) array_like
        Hermitian (symmetric if all elements are real), positive-definite
        input matrix.
        
    ``Returns``
    
    L : (M, M) array_like
        Upper or lower-triangular Cholesky factor of ``a``.  Returns a
        matrix object if ``a`` is a matrix object.
    
    Examples::
    
        a1 = array([[25,15,-5],[15,18,0],[-5,0,11]])
        r1 = np.linalg.cholesky(a1)
        print r1

        a2 = array([[18,22,54,42],[22,70,86,62],[54,86,174,134],[42,62,134,106]])
        r2 = np.linalg.cholesky(a2)
        print r2
        
    Result::
    
        >>> run script...
        array([[5.0, 0.0, 0.0]
              [3.0, 3.0, 0.0]
              [-1.0, 1.0, 3.0]])
        array([[4.242640687119285, 0.0, 0.0, 0.0]
              [5.185449728701349, 6.565905201197403, 0.0, 0.0]
              [12.727922061357857, 3.0460384954008553, 1.6497422479090682, 0.0]
              [9.899494936611667, 1.624553864213788, 1.8497110052313714, 1.3926212476455935]])