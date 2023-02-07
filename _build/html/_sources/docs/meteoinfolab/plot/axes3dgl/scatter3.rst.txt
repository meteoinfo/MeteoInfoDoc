.. _docs-meteoinfolab-plotlib-_axes3dgl-Axes3DGL-scatter3:


*******************
scatter3
*******************

.. method:: Axes3DGL.scatter(x, y, z, s=8, c='b', marker='o', **kwargs):

    Make a 3D scatter plot of x, y and z, where x, y and z are sequence like objects of the same lengths.

    :param x: (*array_like*) Input x data.
    :param y: (*array_like*) Input y data.
    :param z: (*array_like*) Input z data.
    :param s: (*int*) Size of points.
    :param c: (*Color*) Color of the points. Or z vlaues.
    :param alpha: (*int*) The alpha blending value, between 0 (transparent) and 1 (opaque).
    :param marker: (*string*) Marker of the points.
    :param label: (*string*) Label of the points series.
    :param levels: (*array_like*) Optional. A list of floating point numbers indicating the level
        points to draw, in increasing order.

    :returns: Point 3D graphics.

    Example of 3D point plot ::

        z = linspace(0, 1, 100)
        x = z * np.sin(20 * z)
        y = z * np.cos(20 * z)
        c = x + y

        #Plot
        scatter3(x, y, z, c=c)
        colorbar(shrink=0.8)
        title('Point 3D plot example')

    .. image:: ../../../../_static/scatter3_1.png