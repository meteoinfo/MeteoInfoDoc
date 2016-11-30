.. _examples-meteoinfolab-plot_types-pie:

*******************
Pie chart
*******************

Pie chart was created by ``pie()`` function.

::

    x = [1, 3, 0.5, 2.5, 2]
    pie(x, explode=[0,1,0,1,0], startangle=90, autopct='%.1f%%')
    title('Pie chart')
    
.. image:: ../../../_static/pie_1.png