.. _docs-meteoinfolab-funcitons-plot-savefig:


*******************
savefig
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: savefig(fname, width=None, height=None, dpi=None, sleep=None)

    Save the current figure.
    
    :param fname: (*string*) A string containing a path to a filename. The output format
        is deduced from the extention of the filename. Supported format: 'png', 'bmp',
        'jpg', 'eps' and 'pdf'.
    :param width: (*int*) Optional, width of the output figure with pixel units. Default
        is None, the output figure size is same as *figures* window.
    :param height: (*int*) Optional, height of the output figure with pixel units. Default
        is None, the output figure size is same as *figures* window.
    :param dpi: (*int*) Optional, figure resolution.
    :param sleep: (*int*) Optional, sleep seconds. For web map tiles loading.
      
    Examples::

        savefig('D:/Temp/test.png', width=800, height=600)