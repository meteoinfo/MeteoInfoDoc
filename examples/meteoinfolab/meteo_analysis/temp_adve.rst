.. _examples-meteoinfolab-meteo_analysis-temp_adve:

*******************
Temperature advection
*******************

Calculate temperature advection from u and v wind components. The mainly used function is
``cdiff()`` .

::

    print 'Open data files...'
    f_air = addfile('D:/Temp/nc/air.2011.nc')
    f_uwnd = addfile('D:/Temp/nc/uwnd.2011.nc')
    f_vwnd = addfile('D:/Temp/nc/vwnd.2011.nc')

    print 'Read data array...'
    tidx = 173    # Jun 23, 2011
    t = f_air.gettime(tidx)
    lidx = 0    # 1000 hPa
    air = f_air['air'][tidx,lidx,::-1,:]
    uwnd = f_uwnd['uwnd'][tidx,lidx,::-1,:]
    vwnd = f_vwnd['vwnd'][tidx,lidx,::-1,:]
    lon = f_air['lon'][:]
    lat = f_air['lat'][::-1]
    lon, lat = meshgrid(lon, lat)

    # Calculate
    print 'Calculate...'
    dtx = cdiff(air, 1)
    dty = cdiff(air, 0)
    dx = cdiff(lon, 1) * pi / 180
    dy = cdiff(lat, 0) * pi / 180
    tadv = -1*((uwnd*dtx)/(cos(lat*pi/180)*dx)+vwnd*dty/dy)/6.37e6

    #Plot
    print 'Plot...'
    axesm()
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer, edgecolor='black')
    layer = contourfm(tadv, cmap='grads_rainbow')
    title('Temperature advection (' + t.strftime('%Y-%m-%d') + ')')
    colorbar(layer)
    xlim(0, 360)
    ylim(-90, 90)
    xticks(arange(0, 361, 30))
    yticks(arange(-90, 91, 30))
    
.. image:: image/temp_adve.png