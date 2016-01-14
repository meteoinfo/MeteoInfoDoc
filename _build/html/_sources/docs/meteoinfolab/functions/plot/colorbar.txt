.. _docs-meteoinfolab-funcitons-plot-colorbar:


*******************
colorbar
*******************

.. function:: colorbar(layer, **kwargs)

    Add a colorbar to a plot.
    
    :param layer: (*MapLayer*) The layer in plot.
    :param cmap: (*string*) Color map name. Default is None.
    :param shrink: (*float*) Fraction by which to shrink the colorbar. Default is 1.0.
    :param orientation: (*string*) Colorbar orientation: ``vertical`` or ``horizontal``.
    :param aspect: (*int*) Ratio of long to short dimensions.
    :param fontname: (*string*) Font name. Default is ``Arial`` .
    :param fontsize: (*int*) Font size. Default is ``14`` .
    :param bold: (*boolean*) Is bold font or not. Default is ``False`` .
    :param extendrect: (*boolean*) If ``True`` the minimum and maximum colorbar extensions will be
        rectangular (the default). If ``False`` the extensions will be triangular.
    :param extendfrac: [None | 'auto' | length] If set to *None*, both the minimum and maximum triangular
        colorbar extensions with have a length of 5% of the interior colorbar length (the default). If
        set to 'auto', makes the triangular colorbar extensions the same lengths as the interior boxes
        . If a scalar, indicates the length of both the minimum and maximum triangle colorbar extensions
        as a fraction of the interior colorbar length.
    :param ticks: [None | list of ticks] If None, ticks are determined automatically from the input.
    
    **Example:**
    
    ::

        f = addfile('D:/Temp/GrADS/model.ctl')
        psv = f['PS']
        ps = psv[0,[10,60],[60,140]]
        axesm()
        mlayer = shaperead('D:/Temp/map/country1.shp')
        geoshow(mlayer, edgecolor=(0,0,255))
        #layer = contourm(ps, 20)
        layer = contourfm(ps, 20)
        title('Pressure')
        yticks(arange(20, 61, 20))
        grid()
        colorbar(layer, orientation='horizontal', extendrect=False, shrink=0.8, aspect=12)
        
    .. image:: ../../../../_static/contourm.png