.. _docs-meteoinfolab-funcitons-plot-title:


*******************
title
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: title(title, fontname='Arial', fontsize=14, bold=True, color='black')

    Set a title of the current axes.
    
    :param title: (*string or list*) Title string.
    :param fontname: (*string*) Font name. Default is ``Arial`` .
    :param fontsize: (*int*) Font size. Default is ``14`` .
    :param bold: (*boolean*) Is bold font or not. Default is ``True`` .
    :param color: (*color*) Title string color. Default is ``black`` . 
    
    **Example:**
    
    ::

        t = arange(0., 5., 0.2)
        plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
        legend(loc='upper left')
        title('Multiple lines')
        
    .. image:: ../../../../_static/title.png
    
    Multiple rows title can be added using string list:
    
    ::
    
        t = arange(0., 5., 0.2)
        plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
        legend(loc='upper left')
        title(['Multiple lines', 'Title test'])
        
    .. image:: ../../../../_static/titles.png