.. _docs-meteoinfolab-numeric-interpolate-interp1d:


**********
interp1d
**********

.. currentmodule:: numeric.interpolate

.. class:: interp1d(object)

    Interpolate a 1-D function.
    
    :param x: (*array_like*) A 1-D array of real values.
    :param y: (*array_like*) A 1-D array of real values. The length of y must be equal to the length of x.
    :param kind: (*boolean*) Specifies the kind of interpolation as a string (‘linear’, 
        ‘cubic’,‘akima’,‘divided’,‘loess’,‘neville’). Default is ‘linear’.
    
    Examples::
    
        from mipylib.numeric import interpolate

        x = linspace(0, 10, num=11, endpoint=True)
        y = cos(-x**2/9.0)
        f = interpolate.interp1d(x, y)
        f2 = interpolate.interp1d(x, y, kind='cubic')

        xnew = linspace(0, 10, num=100, endpoint=True)
        plot(x, y, 'bo', xnew, f(xnew), 'g-', xnew, f2(xnew), 'r--')
        ylim(-1.5, 1.2)
        legend(['data','linear','cubic'], loc='lower left')
        title('Interpolation example')
        
.. image:: ../../../../_static/interp1d.png