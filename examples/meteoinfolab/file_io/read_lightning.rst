.. _examples-meteoinfolab-file_io-read_lightning:

*********************
Read lightning data
*********************

Python ASCII file read functions could be used if the data can not be read by ``asciiread``
or ``DataFrame.read_table`` functions. Read data into several Python lists and create arrays from them
for plotting.

::

    fn = 'D:/Temp/ascii/lightning/2009_06_06.txt'
    tf = open(fn)
    lats = []
    lons = []
    vs = []
    for aline in tf:    
        datalist = aline.split()
        lat = float(datalist[3].split('=')[1])
        lon = float(datalist[4].split('=')[1])
        v = float(datalist[5].split('=')[1])
        lats.append(lat)
        lons.append(lon)
        vs.append(v)
    lon = array(lons)
    lat = array(lats)  
    v = array(vs)
    axesm()
    geoshow('cn_province')
    ss = makesymbolspec('point', {'value':(-10000,0), 'color':'b', 'marker':'m', 'size':6, 'caption':'Negative'}, \
        {'value':(0,10000), 'color':'r', 'marker':'+', 'size':6, 'caption':'Positive'})
    layer = scatter(lon, lat, v, symbolspec=ss)
    legend(legend=layer.legend(), loc='lower left')
    xlim(90, 130)
    ylim(20, 50) 
    title('Lightning locations')
    
.. image:: image/ascii_lightning.png