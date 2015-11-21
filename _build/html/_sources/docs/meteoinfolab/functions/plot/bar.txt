.. _docs-meteoinfolab-funcitons-plot-bar:


*******************
bar
*******************

.. function:: bar(left, height, width=0.8, color=None, edgecolor='k')

    Make a bar plot.
    
    :param left: (*array_like*) The x coordinates of the left sides of the bars.
    :param height: (*array_like*) The height of the bars.
    :param width: (*array_like*) Optional, the widths of the bars default: 0.8.
    :param color: (*Color*) Optional, the color of the bar faces.
    :param edgecolor: (*Color*) Optional, the color of the bar edge.
    :param linewidth: (*int*) Optional, width of bar edge.
    :param label: (*string*) Label of the bar series.
    
    :returns: Bar legend break.
      
    Examples:
    
    The bar width in the chart was decided automatically
    according to data series number.

    ::

        menMeans = [20, 35, 30, 35, 27]
        bar(menMeans, color='r', label='Men')
        womenMeans = [25, 32, 34, 20, 25]
        bar(womenMeans, color='y', label='Women')
        ylim(0, 40)
        ylabel('Mean age')
        xticks(arange(1, len(menMeans) + 1), ['G1','G2','G3','G4','G5'])
        legend()
        title('Bar chart example')
        
    .. image:: ../../../../_static/bar_1.png

    The bar width and plot position could be set manually with x array and *width* argument.

    ::

        menMeans = [20, 35, 30, 35, 27]
        n = len(menMeans)
        ind = arange(n)
        width = 0.35
        gap = 0.06
        bar(ind, menMeans, width, color='r', label='Men')

        womenMeans = [25, 32, 34, 20, 25]
        bar(ind + width + gap, womenMeans, width, color='y', label='Women')
        
        xlim(-0.2, 5)
        ylim(0, 40)
        ylabel('Mean age')
        xticks(ind + width + gap / 2, ['G1','G2','G3','G4','G5'])
        legend()
        title('Bar chart example')
        
    .. image:: ../../../../_static/bar_2.png