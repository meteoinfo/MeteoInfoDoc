.. _docs-meteoinfolab-funcitons-math-asin:


*******************
asin
*******************

.. function:: asin(x)

    Trigonometric inverse sine, element-wise.
    
    :param x: (*array_like*) *y*-coordinate on the unit circle.
    
    :returns: (*array_like*) The inverse sine of each element of *x*, in radians and in the
        closed interval ``[-pi/2, pi/2]``.
    
    Examples::
    
        >>> asin(array([1,-1,0]))
        array([1.5707964, -1.5707964, 0.0])