.. _docs-meteoinfolab-funcitons-plot-scatter:


*******************
scatter
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: scatter(x, y, s=8, c='b', marker='o', label='S_0')

    Make a scatter plot of x vs y, where x and y are sequence like objects of the same lengths.
    
    :param x: (*array_like*) Input x data.
    :param y: (*array_like*) Input y data.
    :param s: (*int*) Size of points.
    :param c: (*Color*) Color of the points.
    :param marker: (*string*) Marker of the points.
    :param label: (*string*) Label of the points series.
    
    :returns: Points legend break.
      
    Examples::

        x = [1,2,3,4]
        y = [1,4,9,16]
        scatter(x, y, marker='S', s=14, color='r')
        ylabel('Y Axis')
        xlabel('X Axis')
        axis([0,5,0,20])
        title('Scatter plot example', color='b')
        
    .. image:: ../../../../_static/scatter.png