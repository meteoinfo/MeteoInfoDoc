.. _docs-meteoinfolab-funcitons-plot-boxplot:


*******************
boxplot
*******************

.. function:: boxplot(x, showmeans=False, meanline=False)

    Make a box and whisker plot.
    
    Make a box and whisker plot for each column of x or each vector in sequence x. The box extends from lower
    to upper quartile values of the data, with a line at the median. The whiskers extend from the box to show
    the range of the data. Flier points are those past the end of the whiskers.
    
    :param x: (*Array or a sequence of vectors*) The input data.
    :param showmeans: (*boolean*) Default is ``False``. Show the mean or not.
    :param meanline: (*boolean*) Default is ``False``. If ``True`` (and showmeans is ``True``), will try to render
        the mean as a line spanning. Otherwise, means will be shown as points.
    
    Examples:
    
    ::

        data = []
        for i in range(6):
            data.append(random.randn(500))
        boxplot(data)
        title('Box plot demo')
        
    .. image:: ../../../../_static/boxplot_1.png