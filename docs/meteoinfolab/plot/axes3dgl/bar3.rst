.. _docs-meteoinfolab-plotlib-_axes3dgl-Axes3DGL-bar3:


*******************
bar3
*******************

.. method:: Axes3DGL.bar(x, y, z, width=0.8, bottom=None, cylinder=False, **kwargs):

    Make a 3D bar plot of x, y and z, where x, y and z are sequence like objects of the same lengths.

    :param x: (*array_like*) Input x data.
    :param y: (*array_like*) Input y data.
    :param z: (*array_like*) Input z data.
    :param width: (*float*) Bar width.
    :param cylinder: (*bool*) Is cylinder bar or rectangle bar.
    :param bottom: (*bool*) Color of the points. Or z values.
    :param color: (*Color*) Optional, the color of the bar faces.
    :param edgecolor: (*Color*) Optional, the color of the bar edge. Default is black color.
        Edge line will not be plotted if ``edgecolor`` is ``None``.
    :param linewidth: (*int*) Optional, width of bar edge.
    :param label: (*string*) Label of the bar series.
    :param hatch: (*string*) Hatch string.
    :param hatchsize: (*int*) Hatch size. Default is None (8).
    :param bgcolor: (*Color*) Background color, only valid with hatch.
    :param barswidth: (*float*) Bars width (0 - 1), only used for automatic bar with plot
        (only one argument without ``width`` argument). Default is 0.8.

    :returns: Bar 3D graphics.

    Example of 3D bar plot ::

        z = linspace(0, 1, 100)
        x = z * np.sin(20 * z)
        y = z * np.cos(20 * z)
        c = x + y

        lighting(True)
        cols = makecolors(len(x))
        bar3(x, y, z, width=0.05, color=cols, edgecolor=None, linewidth=1)
        title('Bar 3D plot example')

    .. image:: ../../../../_static/bar_3d_1.png

    Example of 3D cylinder bar plot ::

        z = linspace(0, 1, 100)
        x = z * np.sin(20 * z)
        y = z * np.cos(20 * z)
        c = x + y

        #Plot
        lighting(True)
        cols = makecolors(len(x))
        bar3(x, y, z, width=0.08, color=cols, linewidth=1.5, cylinder=True)
        title('Bar 3D plot example')

    .. image:: ../../../../_static/bar_3d_cylinder.png