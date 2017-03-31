.. _docs-meteoinfolab-numeric-funcitons-dot:


*******************
dot
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: dot(a, b)

    Matrix multiplication.
    
    :param a: (*2D Array*) Matrix a.
    :param b: (*2D Array*) Matrix b.
    
    :returns: Result Matrix.
    
    Examples::
    
        >>> a = [[1, 0], [0, 1]]
        >>> b = [[4, 1], [2, 2]]
        >>> dot(a, b)
        array([[4, 1]
              [2, 2]])