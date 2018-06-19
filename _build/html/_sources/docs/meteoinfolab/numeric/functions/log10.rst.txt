.. _docs-meteoinfolab-numeric-funcitons-log10:


*******************
log10
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: log10(x)

    Return the base 10 logarithm of the input array, element-wise.
    
    :param x: (*array_like*) Input values.
    
    :returns: (*array_like*) The logarithm to the base 10 of *x* , element-wise.
    
    Examples::
    
        >>> log10([1e-15, -3.])
        array([-15.,  NaN])