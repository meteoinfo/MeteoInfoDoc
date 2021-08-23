.. _docs-meteoinfolab-plotlib-_axes3dgl-Axes3DGL-contourslice:


*******************
contourslice
*******************

.. method:: Axes3DGL.contourslice(*args, **kwargs):

    Volume slice contours.

    :param x: (*array_like*) Optional. X coordinate array.
    :param y: (*array_like*) Optional. Y coordinate array.
    :param z: (*array_like*) Optional. Z coordinate array.
    :param data: (*array_like*) 3D data array.
    :param xslice: (*list*) X slice locations.
    :param yslice: (*list*) Y slice locations.
    :param zslice: (*list*) Z slice locations.
    :param cmap: (*string*) Color map string.
    :param smooth: (*bool*) Smooth contour lines or not.

    :return: Contour slice graphics

    Example of ``contourslice`` ::

        X=Y=Z = arange(-2, 2.1, 0.2)
        X,Y,Z = meshgrid(X, Y, Z)
        V = X*exp(-X**2-Y**2-Z**2)

        xslice = [-1.2,0.8,2]
        yslice = []
        zslice = []

        levs = arange(-0.2, 0.4, 0.01)
        contourslice(X, Y, Z, V, levs, xslice=xslice, yslice=yslice, zslice=zslice)
        colorbar()
        xlim(-2, 2)
        ylim(-2, 2)

    .. image:: ../../../../_static/contourslice_1.png