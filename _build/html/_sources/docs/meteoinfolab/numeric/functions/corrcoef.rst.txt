.. _docs-meteoinfolab-numeric-funcitons-corrcoef:


*******************
corrcoef
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: corrcoef(x, y)

    Return Pearson product-moment correlation coefficients.
    
    The relationship between the correlation coefficient matrix, `R`, and the
    covariance matrix, `C`, is
    
    .. math:: R_{ij} = \frac{C_{ij}} {\sqrt{C_{ii} * C_{jj}}}
    
    The values of `R` are between -1 and 1, inclusive.
    
    :param x: (*array_like*) A 1-D or 2-D array containing multiple variables and observations. 
        Each row of x represents a variable, and each column a single observation of all those 
        variables.
    :param y: (*array_like*) An additional set of variables and observations. y has the same 
        shape as x.
        
    :returns: The correlation coefficient matrix of the variables.
    
    **Examples**
    
    ::
    
        y = [29.81,30.04,41.7,43.71,28.75,37.73,52.25,32.41,25.67,28.17,25.71,36.05,37.62,34.28,38.82,40.15,35.69,28.36,39.56,52.56,54.14,50.76,39.35,43.16]
        x = [51.6,46,64.3,83.4,65.9,49.5,88.6,101.4,55.9,41.8,33.4,57.3,66.5,40.5,72.3,70,83.3,65.8,63.1,83.4,102,94,77,77]
        r = corrcoef(x, y)
        print r
        y1 = array(x) * 2
        r1 = corrcoef(x, y1)
        print r1
        
    Output:
    
    ::
    
        >>> run script...
        array([[1.0, 0.7007980346679688]
              [0.7007980346679688, 1.0]])
        array([[1.0, 1.0]
              [1.0, 1.0]])