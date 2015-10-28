.. _examples-meteoinfolab-trajectory-tropical_cyclone:

*******************
Tropical cyclone plot
*******************

One tropical cyclone
====================

Read an ASCII data file with tropical cyclone data, and extract longitude and latitude data.
Then plot the cyclone line and points.

::

    # Read tropical cyclone data file
    fn = 'D:/Temp/ascii/198214track.dat'
    tf = open(fn)
    tf.readline()
    aline = tf.readline()
    id = aline.split()[1]
    tf.readline()
    lon = []
    lat = []
    ws = []
    for aline in tf:
        print aline
        datalist = aline.split()
        lat.append(float(datalist[1]))
        lon.append(float(datalist[2]))
        t = datalist[3]
        ws.append(int(datalist[4]))
        stat = datalist[6]
        if len(datalist) == 8:
            stat = stat + ' ' + datalist[7]

    # Plot
    axesm()
    lworld = shaperead('D:/Temp/map/country1.shp')
    geoshow(lworld, facecolor=[200,200,200])
    plotm(lon, lat, linewidth=2)
    layer = scatterm(lon, lat, ws)
    colorbar(layer, shrink=0.8)
    xlim(110, 140)
    ylim(15, 45)
    title('Typhoon pathway')
    
.. image:: image/typhoon_pathway.png

Multiple tropical cyclones
===========================

Read mutiple tropical cyclones longitude/latitude data from a netCDF data file
(https://climatedataguide.ucar.edu/climate-data/ibtracs-tropical-cyclone-best-track-data)
and plot them.

::

    fn = 'D:/Temp/nc/Allstorms.ibtracs_wmo.v03r06.nc'
    f = addfile(fn)
    lons = f['lon_wmo'][:200,:]
    lats = f['lat_wmo'][:200,:]
    data = MIXYListData()
    for i in range(0, lons.dimlen(0)):
        data.addseries(lons[i,:], lats[i,:])

    # Plot
    axesm()
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer)
    layer = plotm(data)
    #layer = scatterm(lons[:,0], lats[:,0], facecolor='b', size=2)
    title('IBTrACS')
    xlim(-180, 180)
    ylim(-90, 90)
    
.. image:: image/tropical_cyclone.png