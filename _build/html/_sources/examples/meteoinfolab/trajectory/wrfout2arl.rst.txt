.. _examples-meteoinfolab-trajectory-wrfout2arl:

*******************
Convert WRF out data to ARL data
*******************

ARL meteorological data format is specified using in HYSPLIT model. This is an example script
for converting WRF out netCDF data to ARL data.

::

    #--------------------------------------------------------        
    # Author: Yaqiang Wang                                           
    # Date: 2015-12-2                                            
    # Purpose: Convert WRF out netCDF data to ARL data  
    # Note: Sample                                                   
    #-----------------------------------------------------------
    #---- Set data folder
    datadir = 'E:/Temp/Yaqiang'
    #---- Set output data file
    outfn = os.path.join(datadir, 'test_wrfout1.arl')
    #---- Read a netCDF data file
    infn = os.path.join(datadir, 'wrfout_d01_1984-05-30_12_00_00-subset')
    print infn
    inf = addfile(infn)
    print 'NetCDF file has been opened...'
    #---- Set output ARL data file
    arlf = addfile(outfn, 'c', dtype='arl')
    #---- Set variable and level list
    wvar2d = ['PSFC','HGT','T2','U10','V10','PBLH','RAINNC']
    wvar3d = ['P','U','V','W','T','QVAPOR']
    avar2d = ['PRSS','SHGT','T02M','U10M','V10M','PBLH','TPPA']
    avar3d = ['PRES','UWND','VWND','WWND','TEMP','SPHU']
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
    fhour = 6
    for t in range(0, tNum):
        print 'Time index: ' + str(t)
        atime = inf.gettime(t)    
        dhead = arlf.getdatahead(inf.proj, 'AWRF', 1, fhour)  
        #Pre-write index record without checksum - will be over-write latter
        arlf.writeindexrec(atime, dhead)
        #Checksum list
        ksumlist = []
        # Write 2d variables
        ksums = []
        for avname,wvname in zip(avar2d, wvar2d):        
            print avname
            gdata = inf[wvname][t,:,:]
            if avname == 'PRSS':
                gdata = gdata * 0.01
            elif avname == 'TPPA':
                gdata = gdata * 0.001
            ksum = arlf.writedatarec(atime, 0, avname, fhour, 99, gdata)
            ksums.append(ksum)
        ksumlist.append(ksums)
        # Write 3d variables
        for lidx in range(0, nz):
            ksums = []
            print lidx
            pp = inf['P'][t,lidx,:,:]
            pb = inf['PB'][t,lidx,:,:]
            pres = pp + pb        
            uwnd = inf['U'][t,lidx,:,:]               
            vwnd = inf['V'][t,lidx,:,:]        
            temp = inf['T'][t,lidx,:,:]
            #potential to ambient temperature
            temp = (temp + 300.) * (pres / 100000.) ** rovcp        
            sphu = inf['QVAPOR'][t,lidx,:,:]
            #convert mixing ratio to specific humidity
            sphu = sphu / (1. + sphu) 
            wwnd = inf['W'][t,lidx+1,:,:]
            #convert vertical velocity from m/s to hPa/s using omega = -W g rho
            wwnd = -wwnd * grav * pres * 0.01 / (rdry * temp * (1.0 + 0.6077 * sphu))

            pres = pres * 0.01
            ksum = arlf.writedatarec(atime, lidx + 1, 'PRES', fhour, 99, pres)
            ksums.append(ksum)
            ksum = arlf.writedatarec(atime, lidx + 1, 'UWND', fhour, 99, uwnd[:,:nx])
            ksums.append(ksum)
            ksum = arlf.writedatarec(atime, lidx + 1, 'VWND', fhour, 99, vwnd[:ny,:])
            ksums.append(ksum)
            ksum = arlf.writedatarec(atime, lidx + 1, 'WWND', fhour, 99, wwnd)
            ksums.append(ksum)
            ksum = arlf.writedatarec(atime, lidx + 1, 'TEMP', fhour, 99, temp)
            ksums.append(ksum)
            ksum = arlf.writedatarec(atime, lidx + 1, 'SPHU', fhour, 99, sphu)
            ksums.append(ksum)
            ksumlist.append(ksums)
        #Re-write index record with checksum
        arlf.writeindexrec(atime, dhead, ksumlist)
        fhour += 1
    arlf.close()
    print 'Finished!'