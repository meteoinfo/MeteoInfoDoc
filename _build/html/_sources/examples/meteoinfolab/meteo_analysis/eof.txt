.. _examples-meteoinfolab-meteo_analysis-eof:

*******************
EOF analysis
*******************

Empirical Orthogonal Function (EOF) analysis is often used to study possible spatial
modes (ie, patterns) of variability and how they change with time. In statistics, EOF
analysis is known as Principal Component Analysis (PCA). To get localized EOF structures,
rotated EOF analysis can be applied. Varimax rotation method is commonly used. The 
following script does EOF and REOF analysis from a dataset including the 62-year globle 
temperature of a certain month with dimensions of 71 * 144 * 62.

::

    fn = 'C:/Temp/EOF/test.txt'
    ny = 71
    nx = 144
    m = ny * nx
    n = 62
    ss1 = asciiread(fn, shape=(71,144,n))
    ss1 = ss1[::-1,::1,:]
    X = ss1.reshape(ny * nx, n)

    #EOF calculation - Time-space transform
    EOF, E, PC = meteo.eof(X, transform=True)
    eof1 = EOF[:,0].reshape(ny, nx)

    #REOF calculation using varimax rotation
    REOF = meteo.varimax(EOF[:,:5])[0]
    reof1 = REOF[:,0].reshape(ny, nx)

    #Plot
    lon = linspace(0, 360, nx)
    lat = linspace(-90, 90, ny)
    #EOF mode 1
    subplot(2,1,1)
    axesm(newaxes=False)
    geoshow('country', edgecolor='k')
    levs = arange(-0.02, 0.021, 0.002)
    layer = contourfm(lon, lat, eof1, levs, smooth=False)
    colorbar(layer)
    title('EOF mode 1')
    #REOF mode 1
    subplot(2,1,2)
    axesm(newaxes=False)
    geoshow('country', edgecolor='k')
    levs = arange(-0.02, 0.021, 0.002)
    layer = contourfm(lon, lat, reof1, levs, smooth=False)
    colorbar(layer)
    title('REOF mode 1')
    
.. image:: ../../../_static/eof_reof_1.png