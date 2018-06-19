.. _docs-meteoinfolab-numeric-funcitons-atan2:


*******************
atan2
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: atan2(x1, x2)

    Element-wise arc tangent of ``x1/x2`` choosing the quadrant correctly.

    The quadrant (i.e., branch) is chosen so that ``arctan2(x1, x2)`` is the signed angle in
    radians between the ray ending at the origin and passing through the point (1,0), and 
    the ray ending at the origin and passing through the point (*x2, x1*). (Note the role 
    reversal: the “*y*-coordinate” is the first function parameter, the “*x*-coordinate” is 
    the second.) By IEEE convention, this function is defined for *x2* = +/-0 and for either 
    or both of *x1* and *x2* = +/-inf (see Notes for specific values).

    This function is not defined for complex-valued arguments; for the so-called argument 
    of complex values, use angle.

    :param x1: (*array_like*) *y*-coordinates.
    :param x2: (*array_like*) *x*-coordinates. *x2* must be broadcastable to match the 
        shape of *x1* or vice versa.
        
    :returns: (*array_like*) Array of angles in radians, in the range ``[-pi, pi]`` .
    
    Examples::
    
        >>> x = array([-1, +1, +1, -1])
        >>> y = array([-1, -1, +1, +1])
        >>> atan2(y, x) * 180 / pi
        array([-135.00000398439022, -45.000001328130075, 45.000001328130075, 135.00000398439022])