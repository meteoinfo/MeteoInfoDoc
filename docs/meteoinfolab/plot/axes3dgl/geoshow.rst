.. _docs-meteoinfolab-plotlib-_axes3dgl-Axes3DGL-geoshow:


*******************
geoshow 3D
*******************

.. method:: Axes3DGL.geoshow(layer, **kwargs):

    Plot a layer map in 3D axes.

    :param layer: (*str or MILayer*) The layer to be plotted.
    :param offset: (*float*) Location on z axis.
    :param xshift: (*float*) X coordinate shift.
    :param facecolor: (*color*) Face color.
    :param edgecolor: (*color*) Edge color.
    :param linewidth: (*float*) Line width.

    :returns: Graphics.

    Example of 3D ``geoshow`` ::

        ax = axes3d()
        geoshow('continent', facecolor='c', edgecolor='b')
        zlim(0, 1)
        title('geoshow in 3D plot')
        xlabel('Longitude')
        ylabel('Latitude')
        zlabel('Altitude')

    .. image:: ../../../../_static/geoshow_3d.png

    Plot geo-located image using ``geoshow`` function ::

        ax = axes3d()
        grid(False)
        layer = georead('global_shade.jpg')
        geoshow(layer)
        geoshow('continent', edgecolor='b', offset=1)
        zlim(0, 1000)
        xlabel('Longitude')
        ylabel('Latitude')
        zlabel('Altitude (m)')

    .. image:: ../../../../_static/geoshow_3d_image.png