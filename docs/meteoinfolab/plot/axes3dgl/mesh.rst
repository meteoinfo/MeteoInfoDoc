.. _docs-meteoinfolab-plotlib-_axes3dgl-Axes3DGL-mesh:


*******************
mesh
*******************

.. method:: Axes3DGL.mesh(*args, **kwargs):

    creates a three-dimensional wireframe plot

    :param x: (*array_like*) Optional. X coordinate array.
    :param y: (*array_like*) Optional. Y coordinate array.
    :param z: (*array_like*) 2-D z value array.
    :param cmap: (*string*) Color map string.
    :param xyaxis: (*boolean*) Draw x and y axis or not.
    :param zaxis: (*boolean*) Draw z axis or not.
    :param grid: (*boolean*) Draw grid or not.
    :param boxed: (*boolean*) Draw boxed or not.
    :param mesh: (*boolean*) Draw mesh line or not.

    :returns: Mesh graphics

    Example of 3D ``mesh`` function ::

        x = y = arange(-5, 5, 0.5)
        x, y = meshgrid(x, y)
        z = y * sin(x) + x * cos(y)

        # Plot
        axes3d()
        grid(False)
        mesh(x, y, z, 20, cmap='MPL_gist_rainbow')
        colorbar(shrink=0.8, ticklen=2)
        zlim(-10, 10)

    .. image:: ../../../../_static/mesh_1.png