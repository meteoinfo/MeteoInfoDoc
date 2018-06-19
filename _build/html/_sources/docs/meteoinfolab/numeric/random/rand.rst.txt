.. _docs-meteoinfolab-numeric-random-rand:


**********
rand
**********

.. currentmodule:: numeric.random

.. function:: rand(*args)

    Random values in a given shape.
    
    Create an array of the given shape and propagate it with random samples from a uniform 
        distribution over [0, 1).
    
    :param d0, d1, ..., dn: (*int*) optional. The dimensions of the returned array, should all
        be positive. If no argument is given a single Python float is returned.
        
    :returns: Random values array.
    
    Examples::
    
        >>> random.rand(3,2)
        array([[0.4696520873015779, 0.894834387530255]
              [0.032558348504158174, 0.23798858170392023]
              [0.3416176575753934, 0.8225067919346076]])