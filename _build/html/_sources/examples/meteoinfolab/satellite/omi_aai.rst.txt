.. _examples-meteoinfolab-satellite-omi_aai:

****************************
OMI Absorbing Aerosol Index
****************************

This example code illustrates how to access and visualize OMI absorbing aerosol index data, which can be
downloaded from this webpage: http://www.temis.nl/airpollution/absaai/#OMI_AAI

::

    #Read data from file
    tt = datetime.datetime(2016,4,6)
    fn = 'W:/SDS_Asian/SDS_obs/aai_omi/' + tt.strftime('%y%m%d') + '.esr'
    f = open(fn)
    for i in range(3):
        f.readline()
    data = []
    for line in f:
        line = line.strip('\n').split(' lat')[0][1:]
        #print line
        for m in range(0, len(line), 3):
            d = line[m:m+3]
            data.append(float(d))
    f.close()
    #Reshape data
    xn = 288
    yn = 180
    data = array(data)
    data = data.reshape([yn,xn])
    data[data>=996.0] = nan
    data = (data - 450) * 0.1
    #Set lon/lat
    lon = arange1(-179.375, xn, 1.25)
    lat = arange1(-89.5, yn, 1.0)
    #Plot
    axesm()
    geoshow('country', edgecolor=[50,50,50])
    levs = arange(0, 3.1, 0.1)
    layer = imshow(lon, lat, data, levs, cmap='wh-bl-gr-ye-re', fill_color='lightgray')
    colorbar(layer)
    title('Absorbing Aerosol Index (' + tt.strftime('%Y-%m-%d') + ')')
    
.. image:: ../../../_static/omi_aai.png