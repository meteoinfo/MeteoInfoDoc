.. _docs-meteoinfolab-funcitons-math-trapz:


*******************
trapz
*******************

.. function:: trapz(y, x=None, dx=1.0, axis=-1)

    Integrate along the given axis using the composite trapezoidal rule.
    
    :param y: (*array_like*) Input array to integrate.
    :param x: (*array_like*) Optional, If x is None, then spacing between all y elements is dx.
    :param dx: (*scalar*) Optional, If x is None, spacing given by dx is assumed. Default is 1.
    :param axis: (*int*) Optional, Specify the axis.
    
    :returns: Definite integral as approximated by trapezoidal rule.
    
    **Notes**
    
    Trapezoidal rule: y-axis locations of points
    will be taken from `y` array, by default x-axis distances between
    points will be 1.0, alternatively they can be provided with `x` array
    or with `dx` scalar.
    
    **References**
    
    Wikipedia page: http://en.wikipedia.org/wiki/Trapezoidal_rule
    
    **Examples**
    
    ::
    
        >>> trapz([1,2,3])
        4.0
        >>> trapz([1,2,3], x=[4,6,8])
        8.0
        >>> trapz([1,2,3], dx=2)
        8.0
        >>> a = arange(6).reshape(2, 3)
        >>> a
        array([[0, 1, 2]
              [3, 4, 5]])
        >>> trapz(a, axis=0)
        array([1.5, 2.5, 3.5])
        >>> trapz(a, axis=1)
        array([2.0, 8.0])