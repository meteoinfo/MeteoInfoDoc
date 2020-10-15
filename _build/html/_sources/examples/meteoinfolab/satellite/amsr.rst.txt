.. _examples-meteoinfolab-satellite-amsr:

*******************
AMSR-E Land3 data
*******************

This example code illustrates how to access and visualize a AMSR-E land3 data.

::

    #Add data file
    fn = 'AMSR_E_L3_DailyLand_V06_20091231.hdf'
    f = addfile(os.path.join('D:/Temp/hdf', fn))
    #vname = 'D_Soil_Moisture'
    vname = 'A_TB36.5H_(Res_1)'
    data = f[vname][::-1,:]
    data = data * 0.1
    data[data==0] = nan
    yn, xn = data.shape

    #Project data
    toproj = projinfo()    #longlat projection
    x = linspace(-180, 180, xn)
    y = linspace(-90, 90, yn)
    lon, lat = meshgrid(x, y)
    data = data.project(lon, lat, toproj=toproj)

    #Plot
    axesm(tickfontsize=12)
    geoshow('country', edgecolor='k')
    levs = arange(140, 320, 10)
    layer = imshow(x, y, data, levs)
    colorbar(layer, fontsize=12)
    xticks(arange(-180, 181, 30))
    yticks(arange(-90, 91, 30))
    title([fn, vname])
    
.. image:: ../../../_static/amsr_2.png