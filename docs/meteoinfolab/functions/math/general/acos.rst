.. _docs-meteoinfolab-funcitons-math-acos:


*******************
acos
*******************

.. function:: acos(x)

    Trigonometric inverse cosine, element-wise.
    
    :param x: (*array_like*) *x*-coordinate on the unit circle. For real arguments, the domain
        is ``[-1, 1]``.
    
    :returns: (*array_like*) The inverse cosine of each element of *x*, in radians and in the
        closed interval ``[0, pi]``.
    
    Examples::
    
        >>> acos([1, -1])
        array([0.0, 3.1415927])