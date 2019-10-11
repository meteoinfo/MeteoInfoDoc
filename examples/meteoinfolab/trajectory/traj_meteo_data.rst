.. _examples-meteoinfolab-trajectory-traj_meteo_data:

*******************
Get meteorological data along trajectory
*******************

Read trajectory data array from the endpoint data file. Read meteorological data arrays from 
corresponding meteorological data file. Then interpolate the meteorological data to the endpoint 
location using **interpn** function of the data array.

::

    # Set working directory
    trajDir = 'D:/Temp/HYSPLIT'
    meteoDir = 'D:/Temp/arl'

    # Open trjactory data file
    print 'Open trajectory data file ...'
    trajfn = os.path.join(trajDir, 'traj_20090731')
    print 'Trajectory file: ' + trajfn
    trajf = addfile_hytraj(trajfn)
    # Read coordinates
    lons = trajf['lon'][:,:]
    lats = trajf['lat'][:,:]
    press = trajf['PRESSURE'][:,:]
    heights = trajf['height'][:,:]
    tt = trajf['time'][:,:]
    ntraj, np = lons.shape

    # Open meteorological data file
    print 'Open meteorological data file...'
    meteofn = os.path.join(meteoDir, 'gdas1.jul09.w5')
    print 'Meteorological file: ' + meteofn
    meteof = addfile(meteofn)

    # Get meteorological data along trajectory
    print 'Get meteorological data along trajectory...'
    outfn = os.path.join(trajDir, 'pblh_traj-1.txt')
    outf = open(outfn, 'w')
    outf.write('TrajID,Lon,Lat,Time,Heigh,PBLH,UWND\n')
    pbldata = meteof['PBLH'][:]
    udata = meteof['UWND'][:]
    idx = 0
    for i in range(ntraj):
        for j in range(np):
            lon = lons[i,j]
            lat = lats[i,j]
            pres = press[i,j]
            z = heights[i,j]
            t = tt[i,j]
            pbl = pbldata.interpn([t, lat, lon])
            uwnd = udata.interpn([t, pres, lat, lon])
            t = miutil.num2date(t)
            print 'TrajID: %i; lon: %.2f; lat: %.2f; time: %s; height: %.2f; PBLH: %.2f; UWND: %.2f' \
                % (i, lon, lat, t.strftime('%Y%m%d_%H:%M'), z, pbl, uwnd)
            line = '%i,%.4f,%.4f,%s,%.2f,%.2f,%.2f' % (i,lon,lat,t.strftime('%Y%m%d_%H:%M'),z,pbl,uwnd)
            outf.write(line + '\n')
            t = t + datetime.timedelta(hours=-1)
        idx += 1

    outf.close()
    print 'Finish...'
    
.. image:: image/traj_meteo_data.png