.. _docs-meteoinfolab-funcitons-array-array:


*******************
array
*******************

.. function:: array(object)
    Create an array.
    
    :param object: (*array_like*) A Jython list or number object.
                        
    :returns: (*MIArray*) An array object satisfying the specified requirements.
                    
    Examples
    
    ::
    
        >>> array([1,2,3])
        array([1, 2, 3])
        >>> array(25.6)
        array([25.6])
        
    More than one dimensions:
    
    ::
    
        >>> array([[1,2], [3,4]])
        array([[1.0, 2.0]
              [3.0, 4.0]])