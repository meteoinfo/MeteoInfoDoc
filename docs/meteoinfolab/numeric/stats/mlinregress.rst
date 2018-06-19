.. _docs-meteoinfolab-numeric-stats-mlinregress:


************
mlinregress
************

.. currentmodule:: numeric.stats

.. function:: mlinregress(y, x)

    Implements ordinary least squares (OLS) to estimate the parameters of a multiple linear 
    regression model.
    
    :param y: (*array_like*) Y sample data - one dimension array.
    :param x: (*array_like*) X sample data - two dimension array.
    
    :returns: Estimated regression parameters and residuals.
    
    Examples::
    
        y = array([11.0, 12.0, 13.0, 14.0, 15.0, 16.0])
        x = array([[0, 0, 0, 0, 0], [2.0, 0, 0, 0, 0], [0, 3.0, 0, 0, 0],
            [0, 0, 4.0, 0, 0], [0, 0, 0, 5.0, 0], [0, 0, 0, 0, 6.0]])
        byta, residuals = np.stats.mlinregress(y, x)
        print byta.astype('float')
        print residuals.astype('float')
        print 'y = %.2f + %.2fx1 + %.2fx2 + %.2fx3 + %.2fx4 + %.2fx5' % \
            (byta[0], byta[1], byta[2], byta[3], byta[4], byta[5])
            
    Result::
        
        >>> run script...
        array([11.0, 0.5, 0.6666667, 0.75, 0.8, 0.8333333])
        array([-3.5527137E-15, -1.7763568E-15, 0.0, 0.0, 0.0, 0.0])
        y = 11.00 + 0.50x1 + 0.67x2 + 0.75x3 + 0.80x4 + 0.83x5