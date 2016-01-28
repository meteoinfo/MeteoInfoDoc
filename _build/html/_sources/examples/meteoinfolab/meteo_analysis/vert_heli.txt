.. _examples-meteoinfolab-meteo_analysis-vert_heli:

*******************
Vertical helicity
*******************

The example to calcluate vertical helicity.

::

    print 'Open data files...'
    f_uwnd = addfile('D:/Temp/nc/uwnd.2011.nc')
    f_vwnd = addfile('D:/Temp/nc/vwnd.2011.nc')
    f_omega = addfile('D:/Temp/nc/omega.2011.nc')

    print 'Calculate vertical helicity...'
    tidx = 173    # Jun 23, 2011
    t = f_uwnd.gettime(tidx)
    level = [1000, 100]
    lat = [15,55]
    lon = [70,135]
    uwnd = f_uwnd['uwnd'][tidx,level,lat,lon]
    vwnd = f_vwnd['vwnd'][tidx,level,lat,lon]
    omega = f_omega['omega'][tidx,level,lat,lon]
    wd = hcurl(uwnd, vwnd)
    lx = -(wd*omega*10.)/12.64*1e6
    lx1 = lx[:,[40],:]
    lev1 = lx1.dimvalue(0)
    #lev2 = 1000 - lev1
    lev2 = p2h(lev1)
    levels = []
    for i in range(0, len(lev1)):
        levels.append('%i' % lev1[i])
    lx1.setdimvalue(0, lev2)

    print 'Plot...'
    layer = contourf(lx1, 20)
    title('Vertical helicity (' + t.strftime('%Y-%m-%d') + ')')
    yticks(lev2, levels)
    xlabel('Longitude')
    ylabel('Pressure (hPa)')
    colorbar(layer)
    
.. image:: image/vert_heli.png