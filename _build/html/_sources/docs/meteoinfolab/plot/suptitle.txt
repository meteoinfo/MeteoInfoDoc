.. _docs-meteoinfolab-funcitons-plot-suptitle:


*******************
suptitle
*******************

.. function:: title(title, fontname='Arial', fontsize=14, bold=True, color='black')

    Add a centered title to the figure.
    
    :param title: (*string or list*) Title string.
    :param fontname: (*string*) Font name. Default is ``Arial`` .
    :param fontsize: (*int*) Font size. Default is ``14`` .
    :param bold: (*boolean*) Is bold font or not. Default is ``True`` .
    :param color: (*color*) Title string color. Default is ``black`` . 
    
    **Example:**
    
    ::

        x = linspace(0, 5, 10)
        y = x ** 2
        subplot(1,2,1)
        plot(x, y, 'r--')
        title('Subplot 1', bold=False)
        subplot(1,2,2)
        plot(y, x, 'g*-')
        title('Subplot 2', bold=False)
        suptitle('Supper title')
        
    .. image:: ../../../../_static/suptitle.png