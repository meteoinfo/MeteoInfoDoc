.. _examples-meteoinfolab-meteo_analysis-moisture_potential_vorticity:

*****************************
Moisture potential vorticity
*****************************

The example to calcluate moisture potential vorticity.

::

    # Calculate moisture potential vorticity
    # Set working directory
    trajDir = 'D:/Temp/HYSPLIT'
    meteoDir = r'U:\data\ARL\2015'

    # Open meteorological data file
    print 'Open meteorological data file...'
    meteofn = os.path.join(meteoDir, 'gdas1.mar15.w5')
    print 'Meteorological file: ' + meteofn
    meteof = addfile(meteofn)

    # Read data
    print 'Read data...'
    latlim = '10:60'
    lonlim = '60:140'
    rh = meteof['RELH'][:,:,latlim,lonlim]
    nt,nz,ny,nx = rh.shape
    lat = rh.dimvalue(2)
    lev = rh.dimvalue(1)
    t0 = meteof['TEMP'][:,:nz-1,latlim,lonlim]
    uwnd = meteof['UWND'][:,:nz-1,latlim,lonlim]
    vwnd = meteof['VWND'][:,:nz-1,latlim,lonlim]
    vort = hcurl(uwnd, vwnd)
    prs = zeros([nt,nz,ny,nx])
    prs = dim_array(prs, rh.dims)
    for i in range(nz):
        prs[:,i,:,:] = lev[i]

    # Calculate pseudo-equivalent potential temperature
    print 'Clalulate pseudo-equivalent potential temperature...'
    es = 6.1078*exp(17.2693882*(t0-273.16)/(t0-35.86))
    qq = rh*(0.62197*es/(prs-0.378*es))/100.
    e = prs*qq/(0.62197+qq)+1e-10
    tlcl = 55.0+2840.0/(3.5*log(t0)-log(e)-4.805)
    theta = t0*pow((1000/prs),(0.2854*(1.0-0.28*qq)))
    eqt = theta*exp(((3376./tlcl)-2.54)*qq*(1.0+0.81*qq))
    thse = eqt-273.15

    # Calculate moisture potential vorticity
    print 'Calculate moisture potential vorticity...'
    mpv = zeros([nt,nz,ny,nx], dtype='double')
    mpv = dim_array(mpv, rh.dims)
    mpv.setdimvalue(1, lev[1:nz-1])
    for t in range(nt):
        tt = meteof.gettime(t)
        print tt.strftime('%Y-%m-%d %H:00')
        for z in range(1, nz-1):
            #print '\tLevel: %i' % z
            f = zeros([ny,nx])
            f1 = 2*7.292*sin(lat*3.14159/180.0)*0.00001
            for i in range(nx):
                f[:,i] = f1
            g = 9.8
            dp = 100*(lev[z-1]-lev[z+1]) 
            deqt = eqt[t,z-1,:,:]-eqt[t,z+1,:,:]
            du = uwnd[t,z-1,:,:]-uwnd[t,z+1,:,:]
            dv = vwnd[t,z-1,:,:]-vwnd[t,z+1,:,:]
            dx1 = 2.0*6370949.0*cos(lat*3.14159/180.0)*3.14159/180.0
            dx = zeros([ny,nx])
            for i in range(nx):
                dx[:,i] = dx1
            dy = 2.0*6370949.0*3.14159/180.0
            dtx = cdiff(eqt[t,z,:,:], 1)
            dty = cdiff(eqt[t,z,:,:], 0)
            pv1 = -g*(vort[t,z,:,:]+f)*deqt/dp  
            pv2 = g*((dv/dp)*(dtx/dx)-(du/dp)*(dty/dy))
            pv = pv1+pv2
            mpv[t,z-1,:,:] = pv.array

    #Plot
    axesm()
    lworld = shaperead('D:/Temp/Map/country1.shp')
    geoshow(lworld, edgecolor='k')
    t = 0
    tt = meteof.gettime(t)
    z = 5
    clevs = arange(-3,3.1,0.5)
    layer = contourfm(mpv[t,z,:,:]*1e6, clevs)
    colorbar(layer)
    title('Moisture potential vorticity (%i hPa)\n' % lev[z] + \
        tt.strftime('%Y-%m-%d %H:00'))

    print 'Finish...'
    
.. image:: ../../../_static/moisture_potential_vorticity.png