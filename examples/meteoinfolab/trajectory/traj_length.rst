.. _examples-meteoinfolab-trajectory-traj_length:

*****************************
Trajectory length calculation
*****************************

`distance` function in `migeo` module of `geolib` package can be used to get length of `LineString` object.
So it can be used to get the length of each trajectory in a trajectory layer.

::

    # Open trjactory shape file
    print 'Open trajectory shape file ...'
    trajfn = r'D:\Temp\traj\2011_MAM\201103.shp'
    trajLayer = shaperead(trajfn)

    # Chek length of each trajectory
    print 'Chek length of each trajectory...'
    idx = 0
    for tline in trajLayer.shapes:
        d = distance(tline, islonlat=True)
        t = trajLayer.cellvalue('Date', idx)
        h = trajLayer.cellvalue('Hour', idx)    
        t.replace(hour=h)
        print t.strftime('%Y-%m-%d %H') + ': %.2fkm' % (d / 1000)
        idx += 1

    print 'Finish...'
    
The output from the print code in above script:

::

    >>> run script...
    Open trajectory shape file ...
    Chek length of each trajectory...
    2011-03-01 00: 51.13km
    2011-03-02 00: 691.60km
    2011-03-03 00: 456.37km
    2011-03-04 00: 1533.14km
    2011-03-05 00: 1683.81km
    2011-03-06 00: 944.17km
    2011-03-07 00: 501.29km
    2011-03-08 00: 1400.35km
    2011-03-09 00: 1468.49km
    2011-03-10 00: 2138.57km
    2011-03-11 00: 2143.41km
    2011-03-12 00: 762.63km
    2011-03-13 00: 548.47km
    2011-03-14 00: 629.21km
    2011-03-15 00: 535.15km
    2011-03-16 00: 666.08km
    2011-03-17 00: 623.15km
    2011-03-18 00: 1297.56km
    2011-03-19 00: 966.95km
    2011-03-20 00: 998.49km
    2011-03-21 00: 512.22km
    2011-03-22 00: 398.51km
    2011-03-23 00: 1534.89km
    2011-03-24 00: 843.08km
    2011-03-25 00: 1403.16km
    2011-03-26 00: 1956.59km
    2011-03-27 00: 537.35km
    2011-03-28 00: 1760.05km
    2011-03-29 00: 570.91km
    2011-03-30 00: 1386.61km
    2011-03-31 00: 1141.01km
    Finish...


`distance` function also suport x/y coordinate vlaues:
        
::

    fn = 'D:/MyProgram/Distribution/java/MeteoInfo/MeteoInfo/sample/HYSPLIT/tdump'
    f = addfile_hytraj(fn)
    lons = f['lon'][:,:]
    lats = f['lat'][:,:]
    tn = lon.shape[0]
    for i in range(tn):
        lon = lons[i,:]
        lat = lats[i,:]
        wlon = where(lon==nan)
        if not wlon is None:
            lon = lon[:wlon[0]]
            lat = lat[:wlon[0]]
        d = distance(lon, lat, islonlat=True)
        print 'Length: %.2fkm' % (d / 1000)