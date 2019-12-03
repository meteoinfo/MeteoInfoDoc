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
    lon = f['Longitude'][:,0]
    lat = f['Latitude'][:,0]
    lon = lon[::10]
    lat = lat[::10]
    data = data[::10]

    # Extract Feature Type only through bitmask.
    data = data & 7

    # Plot
    axesm()
    geoshow('country', edgecolor='k')
    levs = arange(8)
    cols = [(0,0,0),(0,0,255),(255,255,0),(0,255,0),(255,0,0), \
        (200,100,255),(100,50,255),(127,127,127)]
    ls = makesymbolspec('point', levels=levs, colors=cols)
    layer = scatterm(lon, lat, data, size=5, edge=False, symbolspec=ls)
    colorbar(layer, ticklabels=['invalid', 'clear', 'cloud', 'aerosol', \
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
    lat = f['Latitude'][:,0]

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
    layer = imshow(rot90(data, 3), symbolspec=ls, extent=[lat[0],lat[-1],alt[0],alt[-1])
    colorbar(layer, ticklabels=['Others','Cloud'])
    basename = os.path.basename(fn)
    title([basename, 'Feature Type (Bits 1-3) in Feature Classification Flag'])
    xlabel('Latitude (degrees north)')
    ylabel('Altitude (km)')

.. image:: ../../../_static/calipso_cloud.png

Vertical feature types.

::

    # Add file
    fn = 'D:/Temp/hdf/CAL_LID_L2_VFM-Standard-V4-10.2013-12-08T04-46-10ZD.hdf'
    f = addfile(fn)

    # Read data
    vname = 'Feature_Classification_Flags'
    var = f[vname]
    data = var[:,:]
    lat = f['Latitude'][:,0]

    # Extract Feature Type only through bitmask.
    data = data & 7

    # Subset latitude values for the region of interest (40N to 62N).
    lat = lat[3000:4000]
    size = lat.shape[0]

    data2d = data[3000:4000, 1165:]  # -0.5km to  8.2km
    data3d = reshape(data2d, (size, 15, 290))
    data = data3d[:,0,:]

    # Generate altitude data according to file specification [1].
    alt = zeros(290)
    # -0.5km to 8.2km
    for i in range (0, 290):
        alt[i] = -0.5 + i*0.03

    # Plot
    levs = arange(8)
    cols = [(255,255,255),(0,0,255),(51,255,255),(255,153,0),(255,255,0),(0,255,0),(127,127,127),(0,0,0)]
    ls = makesymbolspec('image', levels=levs, colors=cols)
    layer = imshow(rot90(data, 1), symbolspec=ls, extent=[lat[0],lat[-1],alt[0],alt[-1])
    colorbar(layer, ticklabels=['Invalid', 'Clear Air', 'Cloud', 'Aerosol', 'Strato Feature', 'Surface', 'Subsurface', 'No Signal'])
    basename = os.path.basename(fn)
    title([basename, 'Feature Type (Bits 1-3) in Feature Classification Flag'])
    xlabel('Latitude (degrees north)')
    ylabel('Altitude (km)')
    xaxis(tickin=False)
    yaxis(tickin=False)
    
.. image:: ../../../_static/calipso_featuretype-vertical.png

Aerosol types.

::

    # Add file
    fn = 'D:/Temp/hdf/CAL_LID_L2_VFM-Standard-V4-10.2013-12-08T04-46-10ZD.hdf'
    f = addfile(fn)

    # Read data
    vname = 'Feature_Classification_Flags'
    var = f[vname]
    data = var[:,:]
    lat = f['Latitude'][:,0]
    lon = f['Longitude'][:,0]

    # Subset latitude values for the region of interest.
    lidx1 = 3176
    lidx2 = 3313
    lat = lat[lidx1:lidx2]
    lon = lon[lidx1:lidx2]
    size = lat.shape[0]

    N = 290    # 290 is sample numbe of low hight data: -0.5km to 8.2km
    sidx = data.shape[1] - N * 15
    data2d = data[lidx1:lidx2, sidx:]
    data3d = reshape(data2d, (size, 15, N))
    data_l = data3d[:,0,:]
    #data_l = rot90(data_1, 1)

    sidx1 = sidx - 200 * 5
    data2d = data[lidx1:lidx2, sidx1:sidx]
    data3d = reshape(data2d, (size, 5, 200))
    data_m = data3d[:,0,:]
    data_m1 = zeros([data_m.shape[0], data_m.shape[1]*2])
    for i in range(data_m.shape[1]):
        data_m1[:,i*2] = data_m[:,i]
        data_m1[:,i*2+1] = data_m[:,i]
    #data_m = rot90(data_1, 1)

    data = concatenate([data_m1, data_l], axis=1)
    data = rot90(data, 1)

    # Aerosol type
    a = data >> 9
    temp = a & 7
    type2 = data & 7
    tmask = (type2 == 3)
    temp1 = (temp!=0)
    temp2 = (temp1 & tmask)
    atype = temp * temp2

    # Generate altitude data according to file specification [1].
    alt = zeros(N + 200*2)
    # -0.5km to 20.2km
    for i in range (0, N+200*2):
        alt[i] = -0.5 + i * 0.03

    # Plot
    levs = arange(8)
    cols = [(204,204,204),(0,0,255),(153,51,0),(0,204,0),(255,241,85),(0,255,255),\
        (102,102,255),(0,0,0)]
    ls = makesymbolspec('image', levels=levs, colors=cols)
    layer = imshow(atype, symbolspec=ls, extent=[lat[0],lat[-1],alt[0],alt[-1])
    colorbar(layer, ticklabels=['Not Determined','Clean Marine','Dust','Polluted Cont.','Clean Cont.',\
        'Polluted Dust','Smoke','Other'])
    basename = os.path.basename(fn)
    title([basename, 'Aerosol types'])
    xlabel('Latitude (degrees north)')
    ylabel('Altitude (km)')
    ylim(-0.5, 12.1)
    
.. image:: ../../../_static/calipso_aerosol_type.png

Plot total attenuated backscatter.

::

    sys.path.append('D:/Working/MIScript/Jython/mis/hdf')
    import CALIPSO_colors

    # Add file
    fn = 'D:/Temp/hdf/CAL_LID_L1-ValStage1-V3-01.2007-06-12T03-42-18ZN.hdf'
    f = addfile(fn)

    # Read data
    x1 = 0
    x2 = 1001
    nx = x2 - x1
    h1 = 0  # km
    h2 = 20  # km
    nz = 500  # Number of pixels in the vertical
    vname = 'Total_Attenuated_Backscatter_532'
    var = f[vname]
    data = var[x1:x2,:]
    data = rot90(data)
    lats = f['Latitude'][x1:x2,0]
    lons = f['Longitude'][x1:x2,0]
    height = f['metadata']['Lidar_Data_Altitudes']
    height = height[::-1]
    data.setdimvalue(0, height)

    # Interpolate data on a regular grid
    x = arange(x1, x2)
    h = linspace(h1, h2, nz)
    data = np.linint2(data, x, h)

    # X axis ticks
    xvals = []
    xstrs = []
    for i in range(0, nx, 200):
        xvals.append(i + x1)
        if i == 0:
            xstrs.append('Lat: %.2f\nLon: %.2f' % (lats[i],lons[i]))
        else:
            xstrs.append('%.2f\n%.2f' % (lats[i],lons[i]))

    # Plot
    levs = [0.0001,0.0002,0.0003,0.0004,0.0005,0.0006,0.0007,0.0008,0.0009,\
        0.001,0.0015,0.002,0.0025,0.003,0.0035,0.004,0.0045,0.005,0.0055,0.006,\
        0.0065,0.007,0.0075,0.008,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]
    colors = CALIPSO_colors.makecolors()
    layer = imshow(x, h, data, levs, colors=colors)
    xaxis(tickin=False)
    yaxis(tickin=False)
    xticks(xvals, xstrs)
    ylabel('Altitude (km)')
    colorbar(layer, extendrect=False, label=r'$\rm{km}^{-1}$ \rm{sr}$^{-1}$')
    basename = os.path.basename(fn)
    title('{0}\n{1}'.format(basename, vname))
    
The script to make colors (CALIPSO_colors.py)::

    import mipylib.numeric as np

    def makecolors(gray=True):
        """
        Return colors for CAPLIPSO backscatter data plot.

        :param gray: Using gray scale colors or not.

        :returns: Colors.

        Acknowledgements: This is mostly copied from Kathy Powells IDL routine(s) to generate a
            color map and colorbar for plotting CALIPSO lidar data. Thank you Kathy!
        """
        red_c=[0.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,\
            0.0,42.5,85.0,127.5,170.0,212.5,255.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,\
            0.0,42.5,85.0,127.5,170.0,212.5,255.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,\
            0.0,42.5,85.0,127.5,170.0,212.5,255.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,\ 
            0.0,42.5,85.0,127.5,170.0,212.5,255.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,\ 
            0.0,42.5,85.0,127.5,170.0,212.5,255.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,\ 
            0.0,42.5,85.0,127.5,170.0,212.5,255.0,\
            0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,255.0,255.0,255.0,255.0,255.0,\
            0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,255.0,255.0,255.0,255.0,255.0,\
            0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            42.5,85.0,127.5,170.0,212.5,42.5,85.0,127.5,170.0,212.5,\ 
            42.5,85.0,127.5,170.0,212.5,42.5,85.0,127.5,170.0,212.5,42.5,85.0,127.5,170.0,212.5]
        
        green_c=[0.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            255.0,255.0,255.0,255.0,255.0,255.0,255.0,212.5,212.5,212.5,212.5,212.5,212.5,212.5,\ 
            170.0,170.0,170.0,170.0,170.0,170.0,170.0,127.5,127.5,127.5,127.5,127.5,127.5,127.5,\ 
            85.0,85.0,85.0,85.0,85.0,85.0,85.0,42.5,42.5,42.5,42.5,42.5,42.5,42.5,\ 
            0.0,0.0,0.0,0.0,0.0,0.0,0.0,\ 
            212.5,170.0,127.5,85.0,42.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,\ 
            212.5,170.0,127.5,85.0,42.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,\ 
            212.5,170.0,127.5,85.0,42.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,\ 
            212.5,170.0,127.5,85.0,42.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,\ 
            212.5,170.0,127.5,85.0,42.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,\ 
            212.5,170.0,127.5,85.0,42.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,42.5,85.0,127.5,170.0,212.5,\ 
            42.5,42.5,42.5,42.5,42.5,85.0,85.0,85.0,85.0,85.0,\ 
            127.5,127.5,127.5,127.5,127.5,170.0,170.0,170.0,170.0,170.0,212.5,212.5,212.5,212.5,212.5]
        
        blue_c=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,42.5,42.5,42.5,42.5,42.5,42.5,42.5,\ 
            85.0,85.0,85.0,85.0,85.0,85.0,85.0,127.5,127.5,127.5,127.5,127.5,127.5,127.5,\ 
            170.0,170.0,170.0,170.0,170.0,170.0,170.0,212.5,212.5,212.5,212.5,212.5,212.5,212.5,\ 
            255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            255.0,255.0,255.0,255.0,255.0,255.0,255.0,\ 
            212.5,212.5,212.5,212.5,212.5,212.5,212.5,212.5,212.5,212.5,212.5,212.5,212.5,212.5,212.5,212.5,212.5,\ 
            170.0,170.0,170.0,170.0,170.0,170.0,170.0,170.0,170.0,170.0,170.0,170.0,170.0,170.0,170.0,170.0,170.0,\ 
            127.5,127.5,127.5,127.5,127.5,127.5,127.5,127.5,127.5,127.5,127.5,127.5,127.5,127.5,127.5,127.5,127.5,\ 
            85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,\ 
            42.5,42.5,42.5,42.5,42.5,42.5,42.5,42.5,42.5,42.5,42.5,42.5,42.5,42.5,42.5,42.5,42.5,\ 
            0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,\ 
            0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,\ 
            0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

        if gray:
            g_scale = [70,100,130,155,180,200,225,235,240,242,245,249,253]
            ix1 = 10
            ix2 = 23
            red_c[ix1:ix2] = g_scale[0:13];
            green_c[ix1:ix2] = g_scale[0:13];
            blue_c[ix1:ix2] = g_scale[0:13];

        red_c[0] = red_c[49]
        green_c[0] = green_c[49]
        blue_c[0] = blue_c[49]
        
        color_bar = np.array([130,113,113, 64, 57, 50, 43, 36, 29,128,144,  7,  7,193,192,191,190,188,155,139,123, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 49])
        #color_bar = color_bar + 1
        colors = []
        for j in color_bar:
            r = red_c[j]
            g = green_c[j]
            b = blue_c[j]
            colors.append([int(r),int(g),int(b)])
        return colors

.. image:: ../../../_static/calipso_l1.png