.. _docs-meteoinfolab-numeric-fitting-predict:


**********
predict
**********

.. currentmodule:: numeric.fitting

.. function:: predict(func, x)

    Predict y value using fitting function and x value.
    
    :param func: (*Fitting function object*) Fitting function.
    :param x: (*float*) x value.
    
    :returns: (*float*) y value.
    
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
        
    Result::
    
        >>> run script...
        36.4423757947
        36.4423760078