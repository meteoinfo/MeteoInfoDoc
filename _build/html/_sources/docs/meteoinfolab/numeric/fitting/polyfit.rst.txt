.. _docs-meteoinfolab-numeric-fitting-polyfit:


**********
polyfit
**********

.. currentmodule:: numeric.fitting

.. function:: polyfit(x, y, degree, func=False)

    Polynomail fitting.
    
    :param x: (*array_like*) x data array.
    :param y: (*array_like*) y data array.
    :param degree: (*int*) Degree of the fitting polynomial.
    :param func: (*boolean*) Return fit function (for predict function) or not. Default is ``False``.
    
    :returns: Fitting parameters and function (optional).
    
    Examples::
    
        from mipylib.numeric import fitting

        x = linspace(0, 4*pi, 10)
        y = sin(x)

        #Plot data points
        plot(x, y, 'ro', fill=False, size=1)

        #Use polyfit to fit a 7th-degree polynomial to the points
        r = fitting.polyfit(x, y, 7)

        #Plot fitting line
        xx = linspace(0, 4*pi, 100)
        p = r[0]
        yy = fitting.polyval(p, xx)
        plot(xx, yy, '-b')
        title('Polynomial fitting example')
        
.. image:: ../../../../_static/news/mi_1.4.1_lab_polyfit.png