.. _docs-meteoinfolab-funcitons-statistics-corrcoef:


*******************
corrcoef
*******************

.. function:: corrcoef(x, y)

    Return Pearson product-moment correlation coefficients.
    
    :param x: (*array_like*) A 1-D or 2-D array containing multiple variables and observations. 
        Each row of x represents a variable, and each column a single observation of all those 
        variables.
    :param y: (*array_like*) An additional set of variables and observations. y has the same 
        shape as x.
        
    :returns: The correlation coefficient matrix of the variables.
    
    **Examples**
    
    ::
    
        >>> x = [0.6557,0.0357,0.8491,0.9340,0.6787]
        >>> y = [0.7315,0.1100,0.8884,0.9995,0.6959]
        >>> corrcoef(x, y)
        array([[1.0, 0.9976222515106201]
              [0.9976222515106201, 1.0]])
              
    Spatial correlation calculation script::
    
        f = addfile('D:/Temp/GrADS/model.ctl')
        t = f['T'][0,0,'10:60','60:140']
        q = f['Q'][0,0,'10:60','60:140']
        R = corrcoef(t, q)
        print R
        r = R[0,1]
        print r
    
    Output::
    
        >>> run script...
        array([[1.0, 0.9134382009506226]
              [0.9134382009506226, 1.0]])
        0.913438200951