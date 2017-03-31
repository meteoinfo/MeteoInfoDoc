.. _docs-meteoinfolab-funcitons-plot-text:


*******************
text
*******************

.. function:: text(x, y, s, fontname='Arial', fontsize=14, bold=False, color='black')

    Add text to the axes. Add text in string *s* to axis at location *x* , *y* , data
    coordinates.
    
    :param x: (*float*) Data x coordinate.
    :param y: (*float*) Data y coordinate.
    :param s: (*string*) Text.
    :param fontname: (*string*) Font name. Default is ``Arial`` .
    :param fontsize: (*int*) Font size. Default is ``14`` .
    :param bold: (*boolean*) Is bold font or not. Default is ``False`` .
    :param color: (*color*) Tick label string color. Default is ``black`` .
    
    **Example:**
    
    ::

        >>> text(15.5, 20.2, 'text', fontsize=12)