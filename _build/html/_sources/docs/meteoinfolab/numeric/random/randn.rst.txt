.. _docs-meteoinfolab-numeric-random-randn:


**********
randn
**********

.. currentmodule:: numeric.random

.. function:: randn(*args)

    Return a sample (or samples) from the “standard normal” distribution.
    
    Create an array of the given shape and propagate it with random samples from a "normal" 
        (Gaussian) distribution of mean 0 and variance 1.
    
    :param d0, d1, ..., dn: (*int*) optional. The dimensions of the returned array, should all
        be positive. If no argument is given a single Python float is returned.
        
    :returns: Random values array.
    
    Examples::
    
        >>> random.randn(3,2)
        array([[-0.16930188565311702, 0.14022386771529866]
              [-0.8445258136512078, 0.20906704358209086]
              [-1.157825603461335, -2.441255068283659]])