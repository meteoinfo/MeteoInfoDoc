.. _docs-meteoinfolab-numeric-fitting-expfit:


**********
expfit
**********

.. currentmodule:: numeric.fitting

.. function:: expfit(x, y, func=False)

    Exponent fitting.
    
    :param x: (*array_like*) x data array.
    :param y: (*array_like*) y data array.
    :param func: (*boolean*) Return fit function (for predict function) or not. Default is ``False``.
    
    :returns: Fitting parameters and function (optional).
    
    Examples::
    
        from mipylib.numeric import fitting

        x = linspace(0.1, 10, 200)
        y = 20*pow(e, 3*x)
        plot(x, y, 'ro', fill=False, size=1)
        r = np.fitting.expfit(x, y, func=True)
        f = r[3]
        py = fitting.predict(f, 0.2)
        print py
        print 20*pow(e, 3*0.2)

        #Plot fitting line
        xx = linspace(x.min(), x.max(), 100)
        yy = r[0]*pow(e, r[1]*xx)
        plot(xx, yy, '-b', linewidth=2)
        title('Exponent fitting example')
        
.. image:: ../../../../_static/expfit.png