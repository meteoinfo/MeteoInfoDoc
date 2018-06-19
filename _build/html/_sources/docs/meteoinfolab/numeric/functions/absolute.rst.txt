.. _docs-meteoinfolab-numeric-funcitons-absolute:


*******************
absolute
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: absolute(x)

    Calculate the absolute value element-wise.
    
    :param x: (*array_like*) Input array.
    
    :returns: An array containing the absolute value of each element in x. 
        For complex input, a + ib, the absolute value is \sqrt{ a^2 + b^2 }.
    
    Examples
    
    ::
    
        >>> x = array([-1.2, 1.2])
        >>> absolute(x)
        array([1.2, 1.2])
        >>> absolute(1.2 + 1j)
        1.5620499351813308