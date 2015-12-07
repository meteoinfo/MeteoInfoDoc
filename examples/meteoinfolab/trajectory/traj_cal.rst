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

    # Get month abstract string
    def getmonthstr(m):  
        mmm = 'jan'
        if m == 1:
            mmm = 'jan'
        elif m == 2:
            mmm = 'feb'
        elif m == 3:
            mmm = 'mar'
        elif m == 4:
            mmm = 'apr'
        elif m == 5:
            mmm = 'may'
        elif m == 6:
            mmm = 'jun'
        elif m == 7:
            mmm = 'jul'
        elif m == 8:
            mmm = 'aug'
        elif m == 9:
            mmm = 'sep'
        elif m == 10:
            mmm = 'oct'
        elif m == 11:
            mmm = 'nov'
        elif m == 12:
            mmm = 'dec'

        return mmm

    # Get GDAS1 meteorological data files by time
    def getmeteofiles(t):
        y = t.year
        ystr = t.strftime('%y')
        m = t.month
        mmm = getmonthstr(m)
        fns = []
        # The meteo files of this month
        for i in range(1,6):
            fn = 'gdas1.' + mmm + ystr + '.w' + str(i)
            if os.path.exists(os.path.join(metDir, fn)):
                fns.append(fn)

        # The last two meteo files of last month  
        m = m - 1
        if m == 0:
            m = 12
            ystr = str(y - 1)[2:]
        mmm = getmonthstr(m)
        fn = 'gdas1.' + mmm + ystr + '.w4'
        fns.append(fn)
        fn = 'gdas1.' + mmm + ystr + '.w5'
        if os.path.exists(os.path.join(metDir, fn)):
            fns.append(fn)
        else:
            fns.append('gdas1.' + mmm + ystr + '.w3')

        return fns

    # Set start/end time
    stime = datetime.datetime(2012,2,1)
    etime = datetime.datetime(2012,3,10)

    # Loop
    ctFile = './CONTROL'
    while stime <= etime:
        print stime.strftime('%Y-%m-%d ') + shour + ':00'
        ctf = open(ctFile, 'w')
        ctf.write(stime.strftime('%y %m %d ') + shour + "\n")
        ctf.write(str(hnum) + '\n')
        for i in range(0,hnum):
            ctf.write(lat + ' ' + lon + ' ' + heights[i] + '\n')
        ctf.write(hours + '\n')
        ctf.write(vertical + '\n')
        ctf.write(top + '\n')
        fns = getmeteofiles(stime)
        fnnum = len(fns)
        ctf.write(str(fnnum) + '\n')
        for i in range(0,fnnum):
            ctf.write(metDir + '/' + '\n')
            ctf.write(fns[i] + '\n')
        ctf.write(outDir + '/' + '\n')
        outfn = stime.strftime('traj_%Y%m%d')
        ctf.write(outfn)
        ctf.close()
        os.system('c:/hysplit4/exec/hyts_std.exe')

        stime = stime + datetime.timedelta(days=1)

    print 'Finish...'