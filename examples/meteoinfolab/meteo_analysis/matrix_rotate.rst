.. _examples-meteoinfolab-meteo_analysis-matrix_rotate:

*******************
Matrix rotate
*******************

The example for matrix rotate.

::

    #Plot
    axesm(tickfontsize=12)
    lworld = shaperead('D:/Temp/map/country1.shp')
    geoshow(lworld, edgecolor='k')

    #Original matrix
    lat = arange(10, 41, 5)
    lon = arange(70, 131, 5)
    lon, lat = meshgrid(lon, lat)
    scatterm(lon, lat, facecolor='b', size=8, edge=False)

    #Rotate matrix
    angle = 20 * pi / 180
    rotate = array([[cos(angle),sin(angle)], [-sin(angle),cos(angle)]])
    n = len(lon)
    xy = zeros([n, 2])
    xy[:,0] = lon - 70
    xy[:,1] = lat - 10
    xy = dot(xy, rotate)    #Matrix multiplication
    xy[:,0] = xy[:,0] + 70
    xy[:,1] = xy[:,1] + 10
    scatterm(xy[:,0], xy[:,1], facecolor='r', size=8, edge=False)

    xticks(arange(0, 361, 10))
    yticks(arange(-90, 91, 10))
    title('Matrix rotate sample')
    xlim(50, 150)
    ylim(0, 70)
    
.. image:: ../../../_static/matrix_rotate.png