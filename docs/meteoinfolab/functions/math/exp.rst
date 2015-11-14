.. _docs-meteoinfolab-funcitons-math-exp:


*******************
exp
*******************

.. function:: exp(x)

    Calculate the exponential of all elements in the input array.
    
    :param x: (*array_like*) Input values.
    
    :returns: (*array_like*) Output array, element-wise exponential of *x* .
    
    Examples::
    
        >>> x = linspace(-2*pi, 2*pi, 10)
        >>> exp(x)
        array([0.0018674424051939472, 0.007544609964764651, 0.030480793298392952, 
            0.12314470389303135, 0.4975139510383202, 2.0099938864286777, 
            8.120527869949177, 32.80754507307142, 132.54495655444984, 535.4917491531113])