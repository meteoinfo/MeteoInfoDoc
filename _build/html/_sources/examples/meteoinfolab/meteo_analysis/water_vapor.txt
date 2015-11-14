.. _examples-meteoinfolab-meteo_analysis-water_vapor:

*******************
Water vapor flux divergency
*******************

The example to calcluate water vapor flux divergency.

::

    print 'Open data files...'
    f_air = addfile('D:/Temp/nc/air.2011.nc')
    f_uwnd = addfile('D:/Temp/nc/uwnd.2011.nc')
    f_vwnd = addfile('D:/Temp/nc/vwnd.2011.nc')
    f_rhum = addfile('D:/Temp/nc/rhum.2011.nc')

    print 'Read data array...'
    tidx = 173    # Jun 23, 2011
    t = f_air.gettime(tidx)
    lidx = 3    # 700 hPa
    air = f_air['air'][tidx,lidx,::-1,:]
    uwnd = f_uwnd['uwnd'][tidx,lidx,::-1,:]
    vwnd = f_vwnd['vwnd'][tidx,lidx,::-1,:]
    rhum = f_rhum['rhum'][tidx,lidx,::-1,:]

    # Calculate
    print 'Calculate...'
    prs = 700
    g = 9.8
    es = 6.112*exp(17.67*(air-273.16)/(air-29.65))
    qs = 0.62197*es/(prs-0.378*es)
    q = qs*rhum/100
    test = cdiff(q, True)
    qhdivg = hdivg(q*uwnd/g,q*vwnd/g)
    qv = rhum*es/100
    uv = magnitude(uwnd, vwnd)
    uvq = uv*qv/(9.8*1000)

    #Plot
    print 'Plot...'
    axesm()
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer, edgecolor='black')
    #layer = contourfm(qhdivg, 20)
    layer = contourfm(qhdivg, cmap='grads_rainbow')
    title('Water Vapor Flux Divergency (' + t.strftime('%Y-%m-%d') + ')')
    colorbar(layer)
    xlim(0, 360)
    ylim(-90, 90)
    
.. image:: image/water_vapor.png