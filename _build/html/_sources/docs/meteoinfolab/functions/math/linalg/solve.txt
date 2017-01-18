.. _docs-meteoinfolab-funcitons-math-linalg-solve:


*******************************
Solve a linear matrix equation
*******************************

.. function:: solve(a, b)

    Solve a linear matrix equation, or system of linear scalar equations.
    
    Computes the "exact" solution, ``x``, of the well-determined, i.e., full
    rank, linear matrix equation ``ax = b``.
    
    ``Parameters``

    a : (M, M) array_like
        Coefficient matrix.
    b : {(M), (M, K)}, array_like
        Ordinate or "dependent variable" values.
        
    ``Returns``

    x : {(M), (M, K)} ndarray
        Solution to the system a x = b.  Returned shape is identical to ``b``.
    
    Examples::
    
        a = np.array([[3,1], [1,2]])
        b = np.array([9,8])
        x = np.linalg.solve(a, b)
        print x
        
    Result::
    
        >>> run script...
        array([2.0, 3.0])