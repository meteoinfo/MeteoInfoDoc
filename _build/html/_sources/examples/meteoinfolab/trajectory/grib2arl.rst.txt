.. _examples-meteoinfolab-trajectory-grib2arl:

********************************
Convert GRIB data to ARL data
********************************

ARL meteorological data format is specified using in HYSPLIT model. This is an example script
for converting GRIB data to ARL data.

::

    #--------------------------------------------------------        
    # Author: Yaqiang Wang                                           
    # Date: 2016-2-4                                            
    # Purpose: Convert GRIB data to ARL data  
    # Note: Sample                                                   
    #-----------------------------------------------------------
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