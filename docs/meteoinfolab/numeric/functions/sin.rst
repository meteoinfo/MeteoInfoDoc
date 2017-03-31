.. _docs-meteoinfolab-numeric-funcitons-sin:


*******************
sin
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: sin(x)

    Trigonometric sine, element-wise.
    
    :param x: (*array_like*) Angle, in radians.
    
    :returns: (*array_like*) The sine of each element of x.
    
    Examples::
    
        >>> sin(pi/2.)
        1.0
        >>> sin(array([0., 30., 45., 60., 90.]) * pi / 180)
        array([0.0, 0.49999999999999994, 0.7071067811865475, 0.8660254037844386, 1.0])