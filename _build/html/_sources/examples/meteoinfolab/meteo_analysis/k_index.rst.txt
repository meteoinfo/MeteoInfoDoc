.. _examples-meteoinfolab-meteo_analysis-k_index:

*******************
K index
*******************

Calculate k index from FNL data.

::

    #Add file
    f = addfile('D:/Temp/grib/fnl_20110416_00_00')
    #Calculate K index
    #850hPa
    T850 = f['Temperature_isobaric'][0,'85000.0','10:35','90:125'] - 273.16
    rh = f['Relative_humidity_isobaric'][0,'85000.0','10:35','90:125']
    Td850 = T850-((14.55+0.114*T850)*(1-0.01*rh) + pow((2.5+0.007*T850)*(1-0.01*rh),3) + (15.9+0.117*T850)*pow((1-0.01*rh),14))
    #700hPa
    T700 = f['Temperature_isobaric'][0,'70000.0','10:35','90:125'] - 273.16
    rh = f['Relative_humidity_isobaric'][0,'70000.0','10:35','90:125']
    Td700 = T700-((14.55+0.114*T700)*(1-0.01*rh) + pow((2.5+0.007*T700)*(1-0.01*rh),3) + (15.9+0.117*T700)*pow((1-0.01*rh),14))
    #500hPa
    T500 = f['Temperature_isobaric'][0,[50000.0],[10,35],[90,125]] - 273.16
    K = T850-T500+Td850-(T700-Td700)
    #Plot
    axesm()
    geoshow('country', edgecolor='k')
    levs = arange(-40,36,2.5)
    layer = contour(K, levs)
    clabel(layer)
    colorbar(layer)
    t = f.gettime(0)
    title('K index (' + t.strftime('%Y-%m-%d %H:00') + ')')
    
.. image:: ../../../_static/k_index.png