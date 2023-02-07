.. _docs-meteoinfolab-plotlib-_axes3dgl-Axes3DGL-contourfslice:


*******************
contourfslice
*******************

.. method:: Axes3DGL.contourfslice(*args, **kwargs):

    Volume slice contour polygons

    :param x: (*array_like*) Optional. X coordinate array.
    :param y: (*array_like*) Optional. Y coordinate array.
    :param z: (*array_like*) Optional. Z coordinate array.
    :param data: (*array_like*) 3D data array.
    :param xslice: (*list*) X slice locations.
    :param yslice: (*list*) Y slice locations.
    :param zslice: (*list*) Z slice locations.
    :param cmap: (*string*) Color map string.
    :param smooth: (*bool*) Smooth contour lines or not.

    :return: Contour polygon slice graphics

    Example of ``contourfslice`` ::

        fn = os.path.join(migl.get_sample_folder(), 'GrADS', 'model.ctl')
        f = addfile(fn)
        data = f['U'][0,:,:,'0:180']
        pres = data.dimvalue(0)
        z = meteolib.pressure_to_height_std(pres)
        y = data.dimvalue(1)
        x = data.dimvalue(2)

        #Plot
        ax = axes3d()
        geoshow('continent', facecolor=[255,231,177], edgecolor='b')
        levs = arange(-16, 57, 8)
        contourfslice(x, y, z, data, levs, edgecolor='lightgray', alpha=0.8,
            xslice=[120], yslice=[40], zslice=[z[3]])
        colorbar()
        xlim(0, 180)
        title('contourfslice example')

    .. image:: ../../../../_static/contourfslice_1.png

    Vertical cross section contour fill slice with start and end x/y points ::

        fn = os.path.join(migl.get_sample_folder(), 'GrADS', 'model.ctl')
        f = addfile(fn)
        data = f['U'][0,:,:,'0:180']
        pres = data.dimvalue(0)
        z = meteolib.pressure_to_height_std(pres)
        y = data.dimvalue(1)
        x = data.dimvalue(2)

        #Plot
        ax = axes3d()
        geoshow('continent', facecolor=[255,231,177], edgecolor='b')
        levs = arange(-16, 57, 8)
        contourfslice(x, y, z, data, levs, edgecolor='lightgray', alpha=0.8,
            xyslice=[20,-40,160,40])
        colorbar(aspect=30)
        xlim(0, 180)
        title('contourfslice example')

    .. image:: ../../../../_static/contourfslice_xyslice.png