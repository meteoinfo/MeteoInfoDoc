.. _docs-meteoinfolab-funcitons-math-log:


*******************
log
*******************

.. function:: log(x)

    Natural logarithm, element-wise.
    
    The natural logarithm log is the inverse of the exponential function, so that 
    *log(exp(x))* = *x* . The natural logarithm is logarithm in base e.
    
    :param x: (*array_like*) Input values.
    
    :returns: (*array_like*) The natural logarithm of *x* , element-wise.
    
    Examples::
    
        >>> log([1, e, e**2, 0])
        array([0.0, 1.0, 2.0, -Infinity])