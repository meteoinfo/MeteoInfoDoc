.. _docs-meteoinfolab-plot-funcitons-yticks:


*******************
yticks
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: yticks(locs, labels, rotation=0)

    Set the y-limits of the current tick locations and labels.
    
    :param locs: (*array_like*) Tick locations.
    :param labels: (*string list*) Tick labels.
    :param fontname: (*string*) Font name. Default is ``Arial`` .
    :param fontsize: (*int*) Font size. Default is ``14`` .
    :param bold: (*boolean*) Is bold font or not. Default is ``True`` .
    :param color: (*color*) Tick label string color. Default is ``black`` .
    :param rotation: (*float*) Tick label rotation angle. Default is 0.
    
    **Example:**
    
    ::

        # set the locations of the yticks
        yticks( arange(6) )

        # set the locations and labels of the yticks
        yticks( arange(5), ['Tom', 'Dick', 'Harry', 'Sally', 'Sue'])