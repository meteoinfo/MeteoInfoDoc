.. _docs-meteoinfolab-numeric-linalg-lstsq:


***********************
Least-squares
***********************

.. currentmodule:: numeric.linalg

.. function:: lstsq(a, b)

    Compute least-squares solution to equation Ax = b.

    Compute a vector x such that the 2-norm |b - A x| is minimized.
    
    ``Parameters``
    
    a : (M, N) array
        Left hand side matrix (2-D array).
    b : (M,) array
        Right hand side vector.
        
    ``Returns``
    
    x : (N,) array
        Least-squares solution. Return shape matches shape of b.
    residues : (0,) or () or (K,) ndarray
        Sums of residues, squared 2-norm for each column in b - a x.
    
    Examples::
    
        x = array([1, 2.5, 3.5, 4, 5, 7, 8.5])
        y = array([0.3, 1.1, 1.5, 2.0, 3.2, 6.6, 8.6])
        M = ones((len(x),2))
        M[:,1] = x**2
        p, res = linalg.lstsq(M, y)
        print p

        #Plot
        plot(x, y, 'bo', label='data')
        xx = linspace(0, 9, 101)
        yy = p[0] + p[1]*xx**2
        plot(xx, yy, label='least squares fit, $y = a + bx^2$')
        xlabel('x')
        ylabel('y')
        legend(loc='upper left')
        grid(alpha=0.25)
        
    Result::
    
        >>> run script...
        array([3.0, 2.23606797749979, 2.0, 0.0])
        
.. image:: ../../../../_static/lstsq.png