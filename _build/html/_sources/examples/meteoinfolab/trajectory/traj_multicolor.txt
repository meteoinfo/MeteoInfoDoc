.. _examples-meteoinfolab-trajectory-traj_multicolor:

******************************
Trajectory multi-color plot
******************************

Only one color can be assigned to a line in MeteoInfo, so we have to create multi-line pieces to fullfill
multi-color trajectory plot function. Below is an example to plot a multi-color trajectory according
to it's height. Read the endpoints from the HYSPLIT output trajectory file, and create a layer with 
line shapes from each pair of the adjacent endpoints. Height values were put into the layer's attribute
table. Then we can display the trajectory layer using it's height field. 

::

    #Read trajectory data file
    fn = 'E:/Trajectory/RYO-to Yaqiang/05060306'
    f = open(fn)
    line = f.readline()
    mfn = int(line.split()[0])
    for i in range(mfn):
        f.readline()
    line = f.readline()
    sn = int(line.split()[0])
    for i in range(sn):
        f.readline()
    f.readline()
    lons = []
    lats = []
    alts = []
    for line in f:
        dd = line.split()
        lat = float(dd[9])
        lon = float(dd[10])
        alt = float(dd[11])
        lats.append(lat)
        lons.append(lon)
        alts.append(alt)
    alts = array(alts)
    f.close()
    
    #Create trajectory layer
    layer = MILayer(shapetype='line')
    layer.addfield('Height', 'float')
    lon1 = lons[0]
    lat1 = lats[0]
    for i in range(1, len(lons)):
        lon = lons[i]
        lat = lats[i]
        alt = alts[i]
        layer.addshape([lon1,lon], [lat1, lat], [alt])
        lon1 = lon
        lat1 = lat
    levs = arange(0, 1000, 100)
    cols = makecolors(len(levs) + 1)
    ls = makesymbolspec('line', levels=levs, colors=cols, field='Height', size=2)
    
    #Plot
    axesm()
    lworld = shaperead('D:/Temp/map/country1.shp')
    geoshow(lworld, edgecolor=(204,204,204), facecolor=(250,235,252))
    geoshow(layer, symbolspec=ls)
    scatterm(lons[0], lats[0], size=8, facecolor='r')
    text(lons[0], lats[0]-1, 'Fukushima')
    colorbar(layer)
    title('Multi-color line')
    yticks(arange(30, 51, 5))
    xlim(130, 160)
    ylim(30, 50)
    
.. image:: ../../../_static/multicolor_line.png