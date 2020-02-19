.. _examples-meteoinfolab-trajectory-grib2arl:

********************************
Convert GRIB data to ARL data
********************************

ARL meteorological data format is specified using in HYSPLIT model. This is an example script
for converting GRIB data to ARL data.

::
                                         
    # Convert GRIB data to ARL data  

    #---- Set data folder
    datadir = 'D:/Temp/grib'
    #---- Set output data file
    outfn = os.path.join(datadir, 'test_grib.arl')
    #if os.path.exists(outfn):
    #    os.remove(outfn)
    #---- Read a GRIB data file
    infn = os.path.join(datadir, 'INGVC_2802_00_024')
    print infn
    inf = addfile(infn)
    print 'GRIB data file has been opened...'
    #---- Set output ARL data file
    arlf = addfile(outfn, 'c', dtype='arl')
    #---- Set variable and level list
    gvar2d = ['Pressure_surface','Temperature_surface','u-component_of_wind_height_above_ground',\
        'v-component_of_wind_height_above_ground']
    gvar3d = ['Geopotential_isobaric','Temperature_isobaric','Pressure_Vertical_velocity_isobaric',\
        'u-component_of_wind_isobaric','v-component_of_wind_isobaric','Specific_humidity_isobaric']
    avar2d = ['PRSS','T02M','U10M','V10M']
    avar3d = ['HGTS','TEMP','WWND','UWND','VWND','SPHU']
    gv = inf['Geopotential_isobaric']
    nx = gv.dimlen(gv.ndim - 1)
    ny = gv.dimlen(gv.ndim - 2)
    levels = gv.dimvalue(gv.ndim - 3)[::-1]
    nz = len(levels)
    arlf.setlevels(levels)
    arlf.set2dvar(avar2d)
    for l in levels:
        arlf.set3dvar(avar3d)

    #---- Write ARL data file
    arlf.setx(gv.dimvalue(gv.ndim - 1))
    arlf.sety(gv.dimvalue(gv.ndim - 2))
    tNum = inf.timenum()
    fhour = 0
    for t in range(0, tNum):
        print 'Time index: ' + str(t)
        atime = inf.gettime(t)   
        print atime.strftime('%Y-%m-%d %H:00') 
        dhead = arlf.getdatahead(inf.proj, 'RSMC', 2, fhour)  
        #Pre-write index record without checksum - will be over-write latter
        arlf.writeindexrec(atime, dhead)
        #Checksum list
        ksumlist = []
        # Write 2d variables
        ksums = []
        for avname,gvname in zip(avar2d, gvar2d):        
            print avname + ' ' + gvname
            if avname == 'U10M' or avname == 'V10M':
                gdata = inf[gvname][t,0,:,:]
            else:
                gdata = inf[gvname][t,:,:]
            if avname == 'PRSS':
                gdata = gdata * 0.01
            ksum = arlf.writedatarec(atime, 0, avname, fhour, 99, gdata)
            ksums.append(ksum)
        ksumlist.append(ksums)
        # Write 3d variables
        for lidx in range(0, nz):
            ksums = []
            llidx = nz - lidx - 1
            print lidx
            print llidx
            for avname,gvname in zip(avar3d, gvar3d):
                print avname + ' ' + gvname
                gdata = inf[gvname][t,llidx,:,:]
                if avname == 'WWND':
                    gdata = gdata * 0.01
                elif avname == 'SPHU':
                    gdata = gdata * 1000.
                ksum = arlf.writedatarec(atime, lidx + 1, avname, fhour, 99, gdata)
                ksums.append(ksum)
            ksumlist.append(ksums)
        #Re-write index record with checksum
        arlf.writeindexrec(atime, dhead, ksumlist)
        fhour += 1
    arlf.close()
    print 'Finished!'
	
Convert ERA5 grib data to ARL data.

::

    # Convert ERA5 GRIB data to ARL data

    #---- Set data folder
    datadir = r'D:/Temp/grib'
    #---- Set output data file
    outfn = os.path.join(datadir, 'test_era5_grib-1.arl')
    #---- Read a GRIB data file
    infn3d = addfile('{}/ERA5_2017.Aug22.3dpl.grib'.format(datadir))
    infn2d = addfile('{}/ERA5_2017.Aug22.2dpl.all.grib  '.format(datadir))

    print 'GRIB data file has been opened...'
    #---- Set output ARL data file
    arlf = addfile(outfn, 'c', dtype='arl')
    ##---- Set variable and level list
    gvar2d = ['Surface_pressure_surface','2_metre_temperature_surface','10_metre_U_wind_component_surface',\
        '10_metre_V_wind_component_surface','Boundary_layer_height_surface','Convective_available_potential_energy_surface',\
        'Instantaneous_eastward_turbulent_surface_stress_surface','Instantaneous_northward_turbulent_surface_stress_surface']

    gvar3d = ['Geopotential_isobaric','Temperature_isobaric','Vertical_velocity_isobaric',\
        'U_component_of_wind_isobaric','V_component_of_wind_isobaric','Relative_humidity_isobaric']
    #
    avar2d = ['PRSS','T02M','U10M','V10M','PBLH','CAPE','UMOF','VMOF',]
    avar3d = ['HGTS','TEMP','WWND','UWND','VWND','RELH']

    gv = infn3d['Geopotential_isobaric']
    nx = gv.dimlen(gv.ndim - 1)
    ny = gv.dimlen(gv.ndim - 2)
    levels = gv.dimvalue(gv.ndim - 3)[::-1]
    nz = len(levels)
    arlf.setlevels(levels)
    arlf.set2dvar(avar2d)
    for l in levels:
        arlf.set3dvar(avar3d)

    #---- Write ARL data file
    arlf.setx(gv.dimvalue(gv.ndim - 1))
    arlf.sety(gv.dimvalue(gv.ndim - 2))
    tNum = infn3d.timenum()
    fhour = 0
    for t in range(0, tNum):
        print 'Time index: ' + str(t)
        atime = infn3d.gettime(t)
        print atime.strftime('%Y-%m-%d %H:00')
        dhead = arlf.getdatahead(infn3d.proj, 'RSMC', 2, fhour)
        #Pre-write index record without checksum - will be over-write latter
        arlf.writeindexrec(atime, dhead)
        #Checksum list
        ksumlist = []
        # Write 2d variables
        ksums = []
        for avname,gvname in zip(avar2d, gvar2d):
            gdata = infn2d[gvname][t,:,:]
            if avname == 'PRSS':
                gdata = gdata * 0.01
            ksum = arlf.writedatarec(atime, 0, avname, fhour, 99, gdata)
            ksums.append(ksum)
        ksumlist.append(ksums)
        # Write 3d variables
        for lidx in range(0, nz):
            ksums = []
            llidx = nz - lidx - 1
            print(lidx,llidx)
            for avname,gvname in zip(avar3d, gvar3d):
                gdata = infn3d[gvname][t,llidx,:,:]
                if avname == 'WWND':
                    gdata = gdata * 0.01
                elif avname == 'SPHU':
                    gdata = gdata * 1000.
                elif avname == 'HGTS':
                    gdata = gdata / 9.80665
                ksum = arlf.writedatarec(atime, lidx + 1, avname, fhour, 99, gdata)
                ksums.append(ksum)
            ksumlist.append(ksums)
        #Re-write index record with checksum
        arlf.writeindexrec(atime, dhead, ksumlist)
        fhour += 1
    arlf.close()
    print 'Finished!'
	
Comparing ERA5 data with converted ARL data. The two data array are not exactly consistant due
to the lossy compression algorithm of ARL data format.

::

    ddir = 'D:/Temp/grib'
    f_era5_3d = addfile(os.path.join(ddir, 'ERA5_2017.Aug22.3dpl.grib'))
    w1 = f_era5_3d['Vertical_velocity_isobaric'][0,-1]
    f = addfile(os.path.join(ddir, 'test_era5_grib-1.arl'))
    vname = 'WWND'
    w = f[vname][0,0]
    w = w * 100

    subplot(2,2,1,axestype='map')
    geoshow('country', edgecolor='k')
    levs = arange(-1, 1, 0.02)
    layer = imshowm(w, levs)
    colorbar(layer)
    title('ARL ({})'.format(vname))

    subplot(2,2,2,axestype='map')
    geoshow('country', edgecolor='k')
    layer1 = imshowm(w1, levs)
    colorbar(layer1)
    title('ERA5 ({})'.format(vname))

    subplot(2,2,3,axestype='map')
    geoshow('country', edgecolor='k')
    layer2 = imshowm(w1 - w, 20)
    colorbar(layer2)
    title('ERA5 - ARL ({})'.format(vname))
	
.. image:: ../../../_static/era5_arl.png