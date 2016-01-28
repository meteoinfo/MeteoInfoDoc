.. _examples-meteoinfolab-satellite-calipso:

*******************
CALIPSO data
*******************

NASA launched the CloudSat and the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation 
(CALIPSO) spacecraft to study the role that clouds and aerosols play in regulating Earth's weather, 
climate and air quality. On April 28, 2006. This example illustrates how to access and visualize a
LaRC CALIPSO data file.

::

    # Add file
    fn = 'CAL_LID_L2_VFM-ValStage1-V3-02.2011-12-31T23-18-11ZD.hdf'
    f = addfile('D:/Temp/hdf/' + fn)

    # Read data
    vname = 'Feature_Classification_Flags'
    var = f[vname]
    data = var[:,1256]
    lon = f['longitude'][:,0]
    lat = f['latitude'][:,0]
    lon = lon[::10]
    lat = lat[::10]
    data = data[::10]

    # Extract Feature Type only through bitmask.
    data = data & 7

    # Plot
    axesm()
    lworld = shaperead('D:/Temp/map/country1.shp')
    geoshow(lworld, edgecolor='k')
    levs = arange(8)
    cols = [(0,0,0),(0,0,255),(255,255,0),(0,255,0),(255,0,0), \
        (200,100,255),(100,50,255),(127,127,127)]
    ls = makesymbolspec('point', levels=levs, colors=cols)
    layer = scatterm(lon, lat, data, size=5, edge=False, symbolspec=ls)
    colorbar(layer, ticks=['invalid', 'clear', 'cloud', 'aerosol', \
        'strato', 'surface', 'subsurf', 'no signal'])
    xlim(-180, 180)
    ylim(-90, 90)
    title([fn, 'Feature Type at Altitude = 2500m'])
    
.. image:: ../../../_static/calipso_featuretype.png

::

    # Add file
    fn = 'D:/Temp/hdf/CAL_LID_L2_VFM-ValStage1-V3-02.2011-12-31T23-18-11ZD.hdf'
    f = addfile(fn)

    # Read data
    vname = 'Feature_Classification_Flags'
    var = f[vname]
    data = var[:,:]
    lat = f['latitude'][:,0]

    # Extract Feature Type only through bitmask.
    data = data & 7

    # Subset latitude values for the region of interest (40N to 62N).
    lat = lat[3500:4000]
    size = lat.shape[0]

    data2d = data[3500:4000, 1165:]  # -0.5km to  8.2km
    data3d = reshape(data2d, (size, 15, 290))
    data = data3d[:,0,:]

    # Focus on cloud (=2) data only.
    data[data > 2] = 0
    data[data < 2] = 0
    data[data == 2] = 1

    # Generate altitude data according to file specification [1].
    alt = zeros(290)
    # -0.5km to 8.2km
    for i in range (0, 290):
        alt[i] = -0.5 + i*0.03

    # Plot
    levs = arange(2)
    cols = ['w','b']
    ls = makesymbolspec('image', levels=levs, colors=cols)
    layer = imshow(lat, alt, rot90(data, 3), symbolspec=ls)
    colorbar(layer, ticks=['Others','Cloud'])
    basename = os.path.basename(fn)
    title([basename, 'Feature Type (Bits 1-3) in Feature Classification Flag'])
    xlabel('Latitude (degrees north)')
    ylabel('Altitude (km)')

.. image:: ../../../_static/calipso_cloud.png