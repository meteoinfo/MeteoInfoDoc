.. _docs-meteoinfolab-funcitons-plot-figure:


*******************
figure
*******************

.. function:: figure(bgcolor=None, figsize=None, newfig=True)

    Creates a figure.
    
    :param bgcolor: (*Color*) Optional, background color of the figure. Default is ``None`` .
    :param figsize: (*list*) Optional, width and height of the figure such as ``[600, 400]`` .
        Default is ``None`` with changable size same as *Figures* window.
    :param newfig: (*boolean*) Optional, if creates a new figure. Default is ``True`` .
      
    Examples::

        figure()    # Create a new figure
        figure(bgcolor='y')    # Create a new figure with yellow background
        figure(figsize=[700,550], newfig=False)    # Create/set a figure with width and height
        
    Notes:
        The ``width`` and ``height`` arguments shoud not be given in ``savefig()`` function
        if ``figsize`` arguments was given in ``figure()`` function.