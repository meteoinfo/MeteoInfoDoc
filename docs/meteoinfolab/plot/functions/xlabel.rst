.. _docs-meteoinfolab-plot-functions-xlabel:


*******************
xlabel
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: xlabel(label, fontname='Arial', fontsize=14, bold=True, color='black')

    Set the x axis label of the current axes.
    
    :param label: (*string*) Label string.
    :param fontname: (*string*) Font name. Default is ``Arial`` .
    :param fontsize: (*int*) Font size. Default is ``14`` .
    :param bold: (*boolean*) Is bold font or not. Default is ``True`` .
    :param color: (*color*) Label string color. Default is ``black`` .
    
    **Example:**
    
    ::

        x = [1,2,3,4]
        y = [1,4,9,16]
        scatter(x, y, marker='S', s=14, color='r')
        ylabel('Y Axis')
        xlabel('X Axis')
        axis([0,5,0,20])
        title('Scatter plot example', color='b')
        
    .. image:: ../../../../_static/scatter.png