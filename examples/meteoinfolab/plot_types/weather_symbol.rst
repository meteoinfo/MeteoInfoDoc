.. _examples-meteoinfolab-plot_types-weather_symbol:

*******************
Weather symbol plot
*******************

Weather symbol plot was created by ``scatterm()`` function with weather specific legend
created by ``weatherspec()`` function.

::

    #Set data folders
    basedir = 'D:/MyProgram/Distribution/java/MeteoInfo/MeteoInfo'
    datadir = os.path.join(basedir, 'sample/MICAPS')
    mapdir = os.path.join(basedir, 'map')
    #Read shape files
    lworld = shaperead(os.path.join(mapdir, 'country1.shp'))
    lchina = shaperead(os.path.join(mapdir, 'bou2_4p.shp'))
    #Read station data
    f = addfile_micaps(os.path.join(datadir, '10101414.000'))
    data = f.stationdata('WeatherNow')
    #Plot
    axesm(bgcolor=(204,255,255))
    geoshow(lworld, edgecolor='k', facecolor=(255,251,195))
    geoshow(lchina, edgecolor='k')
    ls = weatherspec()
    layer = scatterm(data, symbolspec=ls)
    yticks([20,30,40,50])
    title('Weather symbol plot example')
    xlim(72, 136)
    ylim(16, 55)
    
.. image:: image/weather_symbol.png