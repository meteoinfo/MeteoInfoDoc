.. _examples-meteoinfolab-trajectory-traj_plot:

*******************
Trajectory plot
*******************

Get a trajectory data file object using **addfile_hytraj** function from HYSPLIT trajectory
endpoint data file, and then get trajectory polyline and start point layers using 
**trajlayer** and **trajsplayer** functions of the file object. The layers can be plotted 
in a map axes. The height or pressure variationdata along trajectories can be obtained 
by **trajvardata** function of the file object. The parameter is the column index of the
HYSPLIT trajectory endpoint data file. **trajvardata(12)** means to get trajectory pressure
data, while **trajvardata(11)** is used to get trajectory height data.

::

    fn = 'D:/MyProgram/Distribution/java/MeteoInfo/MeteoInfo/sample/HYSPLIT/tdump'
    f = addfile_hytraj(fn)
    tlayer = f.trajlayer()
    stlayer = f.trajsplayer()

    #Plot
    figure(figsize=[526, 489], newfig=False)
    axesm(position=[0.12, 0.3, 0.9, 0.7])
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer, edgecolor=(0,0,255), facecolor=(230,230,230))
    geoshow(tlayer)
    ss = makesymbolspec('point', {'marker':'S'})
    geoshow(stlayer, symbolspec=ss)
    xlim(-92, -55)
    ylim(34, 54)
    yticks(arange(35, 54, 5))
    title('MeteoInfoLab script demo - Trajectory')

    axes(outerposition=[0, 0, 1, 0.3], yreverse=True, xaxistype='time')
    data = f.trajvardata(12)
    plot(data, legend=tlayer.legend())
    xlabel('Time')
    ylabel('hPa')
    
.. image:: image/traj_plot.png