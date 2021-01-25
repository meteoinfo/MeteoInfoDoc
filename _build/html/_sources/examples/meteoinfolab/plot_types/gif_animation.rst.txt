.. _examples-meteoinfolab-plot_types-gif_animation:

*******************
Gif animation
*******************

Gif animation image can be created using :ref:`gifanimation() <docs-meteoinfolab-funcitons-plot-gifanimation>`, 
:ref:`gifaddframe() <docs-meteoinfolab-funcitons-plot-gifaddframe>` and :ref:`giffinish() <docs-meteoinfolab-funcitons-plot-giffinish>`
functions.

::

    #Set data folders
    fcstdir = 'W:/CUACE_out/haze_54'
    obsdir = 'U:/data/micaps'
    mapdir = 'T:/verification/map'
    outdir = 'T:/verification/cases/cuace_54km/result'

    #Set time
    st = datetime.datetime(2015,11,1,0)
    sbjt = st + datetime.timedelta(hours=8)

    #Get forecasting data files
    fcstfn = os.path.join(fcstdir, str(st.year) + '/' + st.strftime('%Y%m') + '/' + \
        st.strftime('%Y%m%d%H') + '/produce/haze_post_aero_' + st.strftime('%Y%m%d%H') + '.ctl')
    print 'Forecasting data file: ' + fcstfn
    fcstf = addfile(fcstfn)
    fcstf.bigendian(True)

    #Plot
    figure(figsize=[768,480], newfig=False)
    axesm(position=[0,0,1,1], xyscale=1.2, tickfontsize=12)
    geoshow('cn_province')
    geoshow('country', edgecolor='k')
    levs = [0.1, 0.5, 1, 5, 10, 20, 30, 50]
    cols = [(192,0,0),(255,69,0),(255,105,180),(255,128,0),(255,192,128),(51,255,255), \
        (153,255,153),(204,255,204),(255,255,255)]
    #Set weather list - haze, mist and fog
    weathers = [5,10,11,12,40,41,42,43,44,45,46,47,48,49]
    ls = weatherspec(weathers)
    #Add south China Sea
    axesm(position=[0.76,0.09,0.16,0.22], axison=False, xyscale=1.2)
    geoshow('cn_border', facecolor=(0,0,255))
    xlim(106, 123)
    ylim(2, 23)
    #Set current plot to 1
    currentplot(1)

    #Create gif animation
    giffn = os.path.join(outdir, 'V_vis_' + st.strftime('%Y%m%d') + '--loop-.gif')
    print giffn
    animation = gifanimation(giffn)

    #Loop
    tnum = fcstf.timenum()
    nn = 0
    for t in range(1, 25):
        if nn > 0:
            cll()
            cll()
        tt = fcstf.gettime(t)
        bjt = tt + datetime.timedelta(hours=8)
        obsfn = os.path.join(obsdir,  str(bjt.year) + '/plot/' + bjt.strftime('%y%m%d%H.000'))
        if os.path.exists(obsfn):
            print 'Observation data file: ' + obsfn    
            obsf = addfile_micaps(obsfn)
            fdata = fcstf['VIS'][t,:,:]
            lfcst = contourf(fdata, levs, colors=cols, proj=fcstf.proj)
            odata = obsf.stationdata('WeatherNow')
            lobs = scatter(odata, symbolspec=ls)
            title('CUACE/Haze-Fog visibility (km) ' + sbjt.strftime('%Y-%m-%d %H:00') + \
                    ' +' + str(t*3) + ' (' + bjt.strftime('%Y-%m-%d %H:00') + ')', \
                    bold=False)
            xlim(68.6, 140.5)
            ylim(17.3, 54)
            colorbar(lfcst, extendrect=False, shrink=0.6)
            #Add frame to gif animation
            gifaddframe(animation)
            nn += 1

    #Finish gif animation
    animation.finish()
    print 'Finished...'
    
.. image:: ../../../_static/gif_animation.gif