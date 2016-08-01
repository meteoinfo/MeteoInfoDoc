.. _examples-meteoinfolab-trajectory-traj_meteo_data:

*******************
Get meteorological data along trajectory
*******************

Read trajectory endpoint data file and create trajectory polyline layer. Then read endpoint 
from the layer and interpolate the meteorological data to the endpoint location using
**tostation** function of the data file object.

::

    # Set working directory
    trajDir = 'D:/Temp/HYSPLIT'
    meteoDir = 'D:/Temp/arl'

    # Open trjactory data file
    print 'Open trajectory data file ...'
    trajfn = os.path.join(trajDir, 'traj_20090731')
    print 'Trajectory file: ' + trajfn
    trajf = addfile_hytraj(trajfn)
    # Create trajectory layer
    trajLayer = trajf.trajlayer()

    # Open meteorological data file
    print 'Open meteorological data file...'
    meteofn = os.path.join(meteoDir, 'gdas1.jul09.w5')
    print 'Meteorological file: ' + meteofn
    meteof = addfile(meteofn)

    # Get meteorological data along trajectory
    print 'Get meteorological data along trajectory...'
    outfn = os.path.join(trajDir, 'pblh_traj.txt')
    outf = open(outfn, 'w')
    outf.write('Lon,Lat,Time,Heigh,PBLH,UWND\n')
    pblvar = 'PBLH'
    uvar = 'UWND'
    idx = 0
    for tline in trajLayer.shapes():
        t = trajLayer.cellvalue('Date', idx)
        h = trajLayer.cellvalue('Hour', idx)    
        t.replace(hour=h)
        for ps in tline.getPoints():
            lon = ps.X
            lat = ps.Y 
            z = ps.M
            pres = ps.Z
            pbl = meteof.tostation(pblvar, lon, lat, None, t)
            uwnd = meteof.tostation(uvar, lon, lat, pres, t)
            print 'lon: %.2f; lat: %.2f; time: %s; height: %.2f; PBLH: %.2f; UWND: %.2f' % (lon, lat, t.strftime('%Y%m%d_%H:%M'), z, pbl, uwnd)
            line = '%.4f,%.4f,%s,%.2f,%.2f,%.2f' % (lon,lat,t.strftime('%Y%m%d_%H:%M'),z,pbl,uwnd)
            outf.write(line + '\n')
            t = t + datetime.timedelta(hours=-1)
        idx += 1

    outf.close()
    print 'Finish...'
    
.. image:: image/traj_meteo_data.png