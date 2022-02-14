.. _examples-meteoinfolab-meteo_analysis-hcurl_hdivg:

************************
Vorticity and divergence
************************

Calculate vorticity and divergence from u and v wind components using ``vorticity()`` and
``divergence()`` functions.

::

    fn = os.path.join(migl.get_sample_folder(), 'GrADS', 'model.ctl')
    f = addfile(fn)
    u = f['U'][0,0,:,:]
    v = f['V'][0,0,:,:]
    lat = u.dimvalue(0)
    lon = u.dimvalue(1)
    glon, glat = np.meshgrid(lon, lat)
    dx, dy = meteolib.lat_lon_grid_deltas(glon, glat)
    vort = meteolib.vorticity(u, v, dx, dy)
    divg = meteolib.divergence(u, v, dx, dy)

    levs = arange(-3e-5, 3e-5, 1e-6)
    subplot(2,1,1,axestype='map')
    geoshow('continent')
    contourf(lon, lat, vort, levs)
    title('Vorticity')
    colorbar(orientation='horizontal', aspect=50)
    subplot(2,1,2,axestype='map')
    geoshow('continent')
    contourf(lon, lat, divg, levs)
    title('Divergence')
    colorbar(orientation='horizontal', aspect=50)
    
.. image:: ../../../_static/vorticity_divergence.png