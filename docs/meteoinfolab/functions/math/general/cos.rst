.. _docs-meteoinfolab-funcitons-math-cos:


*******************
cos
*******************

.. function:: cos(x)

    Trigonometric cosine, element-wise.
    
    :param x: (*array_like*) Angle, in radians.
    
    :returns: (*array_like*) The cosine of each element of x.
    
    Examples::
    
        >>> cos(array([0, pi/2, pi]))
        array([1.0, 6.123233995736766E-17, -1.0])