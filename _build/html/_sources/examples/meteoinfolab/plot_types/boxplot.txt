.. _examples-meteoinfolab-plot_types-boxplot:

*******************
Box chart
*******************

Box chart was created by ``boxplot()`` function.

::

    data = []
    for i in range(6):
        data.append(random.randn(500))
    boxplot(data)
    title('Box plot demo')
    
.. image:: ../../../_static/boxplot_1.png