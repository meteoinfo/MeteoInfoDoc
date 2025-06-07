.. _examples-meteoinfolab-trajectory-wrfout2arl:

********************************
Convert WRF out data to ARL data
********************************

ARL meteorological data format is specified using in HYSPLIT model. This is an example script
for converting WRF out netCDF data to ARL data.

::

    #---- Set data folder
    datadir = 'D:/Temp/nc/wrf'
    #---- Set output data file
    outfn = os.path.join(datadir, 'test1_wrfout1.arl')
    if os.path.exists(outfn):
        os.remove(outfn)
    #---- Read a netCDF data file
    infn = os.path.join(datadir, 'wrfout_d01_1984-05-30_12_00_00-subset')
    print(infn)
    inf = addfile(infn)
    print('NetCDF file has been opened...')
    #---- Set output ARL data file
    arlf = addfile(outfn, 'c', dtype='arl')
    #---- Set variable and level list
    wvar2d = ['HGT','PSFC','PBLH','UST','SWDOWN','HFX','LH','T2','U10','V10','RAINNC']
    wvar3d = ['P','T','U','V','W','QVAPOR']
    avar2d = ['SHGT','PRSS','PBLH','USTR','DSWF','SHTF','LHTF','T02M','U10M','V10M','TPPA']
    avar3d = ['PRES','TEMP','UWND','VWND','WWND','SPHU']
    wv = inf['P']
    nx = wv.dimlen(wv.ndim - 1)
    ny = wv.dimlen(wv.ndim - 2)
    levels = wv.dimvalue(wv.ndim - 3)
    nz = len(levels)
    arlf.setlevels(levels)
    arlf.set2dvar(avar2d)
    for l in levels:
        arlf.set3dvar(avar3d)
    #---- Constant for poisson's equation
    cp = 1004.0         # J/kg/K; specific heat
    grav = 9.81         # m/s**2; gravity
    rdry = 287.04       # J/kg/K; gas constant
    rovcp = rdry / cp   # constant for poisson's equation
    #---- Write ARL data file
    arlf.setx(wv.dimvalue(wv.ndim - 1))
    arlf.sety(wv.dimvalue(wv.ndim - 2))
    tNum = inf.timenum()
    fhour = 0
    for t in range(0, tNum):
        print 'Time index: ' + str(t)
        atime = inf.gettime(t)
        print atime.strftime('%Y-%m-%d %H:00')
        dhead = arlf.getdatahead(inf.proj, 'AWRF', 1, fhour, atime.minute)
        #Pre-write index record without checksum - will be over-write latter
        arlf.writeindexrec(atime, dhead)
        #Checksum list
        ksumlist = []
        #Write 2d variables
        ksums = []
        for avname,wvname in zip(avar2d, wvar2d):
            print(avname + ' ' + wvname)
            gdata = inf[wvname][t,:,:]
            if avname == 'PRSS':
                gdata = gdata * 0.01
            elif avname == 'TPPA':
                gdata = gdata * 0.001
            ksum = arlf.writedatarec(atime, 0, avname, fhour, 99, gdata)
            ksums.append(ksum)
        ksumlist.append(ksums)
        #Write 3d variables
        wwnd_l = inf['W'][t]
        wwnd_l = meteo.wrf.destagger(wwnd_l, -3)
        for lidx in range(0, nz):
            ksums = []
            print(lidx)
            pp = inf['P'][t,lidx,:,:]
            pb = inf['PB'][t,lidx,:,:]
            pres = pp + pb
            uwnd = inf['U'][t,lidx,:,:]
            uwnd = meteo.wrf.destagger(uwnd, -1)
            vwnd = inf['V'][t,lidx,:,:]
            vwnd = meteo.wrf.destagger(vwnd, -2)
            temp = inf['T'][t,lidx,:,:]
            #potential to ambient temperature
            temp = (temp + 300.) * (pres / 100000.) ** rovcp
            sphu = inf['QVAPOR'][t,lidx,:,:]
            #convert mixing ratio to specific humidity
            sphu = sphu / (1. + sphu)
            wwnd = wwnd_l[lidx]
            #convert vertical velocity from m/s to hPa/s using omega = -W g rho
            wwnd = -wwnd * grav * pres * 0.01 / (rdry * temp * (1.0 + 0.6077 * sphu))

            pres = pres * 0.01
            ksum = arlf.writedatarec(atime, lidx + 1, 'PRES', fhour, 99, pres)
            ksums.append(ksum)
            ksum = arlf.writedatarec(atime, lidx + 1, 'TEMP', fhour, 99, temp)
            ksums.append(ksum)
            ksum = arlf.writedatarec(atime, lidx + 1, 'UWND', fhour, 99, uwnd)
            ksums.append(ksum)
            ksum = arlf.writedatarec(atime, lidx + 1, 'VWND', fhour, 99, vwnd)
            ksums.append(ksum)
            ksum = arlf.writedatarec(atime, lidx + 1, 'WWND', fhour, 99, wwnd)
            ksums.append(ksum)
            ksum = arlf.writedatarec(atime, lidx + 1, 'SPHU', fhour, 99, sphu)
            ksums.append(ksum)
            ksumlist.append(ksums)
        #Re-write index record with checksum
        arlf.writeindexrec(atime, dhead, ksumlist)
        fhour += 6
    arlf.close()
    print('Finished!')

Comparing WRF netCDF data with converted ARL data.

::

    ddir = 'D:/Temp/nc/wrf'
    f1 = addfile(os.path.join(ddir, 'wrfout_d01_1984-05-30_12_00_00-subset'))
    w1 = f1['U'][0,10]
    w1 = meteo.wrf.destagger(w1, -1)

    f = addfile(os.path.join(ddir, 'test1_wrfout1.arl'))
    vname = 'UWND'
    w = f[vname][0,10]

    subplot(2,2,1, axestype='map', projection=f1.projection)
    geoshow('country')
    levs = arange(-10, 10, 0.2)
    imshow(w1, levs, transform=f1.projection)
    colorbar()
    title('wrf ({})'.format(vname))

    subplot(2,2,2, axestype='map', projection=f.projection)
    geoshow('country')
    imshow(w, levs, transform=f.projection)
    colorbar()
    title('ARL  ({})'.format(vname))

    subplot(2,2,3)
    imshow(w1 - w, 20)
    colorbar()
    title('wrf - ARL ({})'.format(vname))

.. image:: image/wrf_arl.png