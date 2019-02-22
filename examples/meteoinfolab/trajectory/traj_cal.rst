.. _examples-meteoinfolab-trajectory-traj_cal:

************************
Trajectory calculation
************************

`HYSPLIT <http://ready.arl.noaa.gov/HYSPLIT.php>`_ or TrajStat is needed for air mass 
trajectory calculation in this example. The following code not includes any MeteoInfoLab
function, thus they are pure Python code.

Calculate one day back trajectories:

::

    # Set working directory
    metDir = 'D:/Temp/arl'
    outDir = 'D:/Temp/HYSPLIT'
    workingDir = 'C:/hysplit4/working'
    os.chdir(workingDir)
    print 'Current directory: ' + os.getcwd()

    # Set parameters
    lon = '115.2'
    lat = '40.1'
    shour = '06'
    heights = ['100.0','500.0','1000.0']
    hnum = len(heights)
    hours = '-48'
    vertical = '0'
    top = '10000.0'

    # Set meteorological data files
    fns = []
    fn = 'gdas1.jul09.w5'
    fns.append(fn)

    # Set start/end time
    stime = datetime.datetime(2009,7,31)

    # Write CONTROL file
    ctFile = './CONTROL'
    print stime.strftime('%Y-%m-%d ') + shour + ':00'
    ctf = open(ctFile, 'w')
    ctf.write(stime.strftime('%y %m %d ') + shour + "\n")
    ctf.write(str(hnum) + '\n')
    for i in range(0,hnum):
      ctf.write(lat + ' ' + lon + ' ' + heights[i] + '\n')
    ctf.write(hours + '\n')
    ctf.write(vertical + '\n')
    ctf.write(top + '\n')
    fnnum = len(fns)
    ctf.write(str(fnnum) + '\n')
    for i in range(0,fnnum):
        ctf.write(metDir + '/' + '\n')
        ctf.write(fns[i] + '\n')
    ctf.write(outDir + '/' + '\n')
    outfn = stime.strftime('traj_%Y%m%d')
    ctf.write(outfn)
    ctf.close()

    # Calculate trajectories
    os.system('c:/hysplit4/exec/hyts_std.exe')

    print 'Finish...'

Calculate multiple days back trajectories:
        
::

    import calendar

    # Set working directory
    metDir = 'U:/data/ARL'
    outDir = 'D:/Temp/HYSPLIT'
    workingDir = 'C:/hysplit4/working'
    os.chdir(workingDir)
    print 'Current directory: ' + os.getcwd()

    # Set parameters
    lon = '115.2'
    lat = '40.1'
    shour = '06'
    heights = ['100.0','500.0','1000.0']
    hnum = len(heights)
    hours = '-48'
    vertical = '0'
    top = '10000.0'

    # Get GDAS1 meteorological data files by time
    def getmeteofiles(t):
        ystr = t.strftime('%y')
        mdir = metDir + '/%s' % t.strftime('%Y')
        mmm = miutil.dateformat(t, 'MMM', 'us_en').lower()
        mdirs = []
        fns = []
        # The meteo files of this month
        for i in range(1,6):
            fn = 'gdas1.' + mmm + ystr + '.w' + str(i)
            if os.path.exists(os.path.join(mdir, fn)):
                mdirs.append(mdir)
                fns.append(fn)

        # The last two meteo files of last month  
        days = calendar.monthrange(t.year, t.month)[1]
        t = t - datetime.timedelta(days=days)
        ystr = t.strftime('%y')
        mdir = metDir + '/%s' % t.strftime('%Y')
        mmm = miutil.dateformat(t, 'MMM', 'us_en').lower()
        fn = 'gdas1.' + mmm + ystr + '.w4'
        mdirs.append(mdir)
        fns.append(fn)
        fn = 'gdas1.' + mmm + ystr + '.w5'
        if os.path.exists(os.path.join(mdir, fn)):
            mdirs.append(mdir)
            fns.append(fn)
        else:
            mdirs.append(mdir)
            fns.append('gdas1.' + mmm + ystr + '.w3')
         
        return mdirs, fns

    # Set start/end time
    stime = datetime.datetime(2014,9,1)
    etime = datetime.datetime(2014,10,1)

    # Loop
    ctFile = './CONTROL'
    while stime < etime:
        print stime.strftime('%Y-%m-%d ') + shour + ':00'
        ctf = open(ctFile, 'w')
        ctf.write(stime.strftime('%y %m %d ') + shour + "\n")
        ctf.write(str(hnum) + '\n')
        for j in range(0,hnum):
            ctf.write(lat + ' ' + lon + ' ' + heights[j] + '\n')
        ctf.write(hours + '\n')
        ctf.write(vertical + '\n')
        ctf.write(top + '\n')
        mdirs, fns = getmeteofiles(stime)
        fnnum = len(fns)
        ctf.write(str(fnnum) + '\n')
        for mdir,fn in zip(mdirs,fns):
            ctf.write(mdir + '/' + '\n')
            ctf.write(fn + '\n')
        ctf.write(outDir + '/' + '\n')
        outfn = stime.strftime('traj_%Y%m%d')
        ctf.write(outfn)
        ctf.close()
        os.system('c:/hysplit4/exec/hyts_std.exe')
      
        stime = stime + datetime.timedelta(days=1)

    print 'Finish...'