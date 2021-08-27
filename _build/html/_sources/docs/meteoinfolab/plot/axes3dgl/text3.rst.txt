.. _docs-meteoinfolab-plotlib-_axes3dgl-Axes3DGL-text3:


*******************
text3
*******************

.. method:: Axes3DGL.text(x, y, z, s, zdir=None, **kwargs):

    Add text to the plot. kwargs will be passed on to text, except for the zdir
    keyword, which sets the direction to be used as the z direction.

    :param x: (*float*) X coordinate.
    :param y: (*float*) Y coordinate.
    :param z: (*float*) Z coordinate.
    :param s: (*string*) Text string.
    :param zdir: Z direction.

    :return: 3D text graphics

    Example of ``text3`` function ::

        ax = axes3d()
        geoshow('continent', color='c', edgecolor='b')
        text3(0, 0, 0, 'Text in 3D', fontsize=30, zdir='x', ha='center')
        text3(0, 20, 0.5, 'Text in 3D', color='r', fontsize=20)
        zlim(0, 1)

    .. image:: ../../../../_static/text3_1.png