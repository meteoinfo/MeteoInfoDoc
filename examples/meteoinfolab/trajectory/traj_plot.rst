.. _examples-meteoinfolab-trajectory-traj_plot:

*******************
Trajectory plot
*******************

Get a trajectory data file object using **addfile_hytraj** function from HYSPLIT trajectory
endpoint data file. It has two dimensions of ``trajectory`` (trajectory number) and ``obs``
(endpoint number in one trajectory. maximum number is given if the endpoint numbers are not
identical). The variables are ``time``, ``run_hour``, ``lat``, ``lon``, ``height``, ``PRESSURE``
and other output meteorological parameters. All variables have the two dimensions, so we can
get 2-D data arrays from the file object. The ``lat``, ``lon`` data can be used to plot trajectories.

::

    fn = os.path.join(migl.get_sample_folder(), 'HYSPLIT', 'tdump')
    f = addfile_hytraj(fn)
    lon = f['lon'][:,:]
    lat = f['lat'][:,:]

    #Plot
    figure(figsize=[526, 489], newfig=False)
    axesm(position=[0.12, 0.3, 0.85, 0.7])
    geoshow('country', edgecolor=(0,0,255), facecolor=(230,230,230))
    levs = arange(0, 101, 5)
    tlayer = plot(lon, lat, levels=levs)
    ls = tlayer.update_legend('unique', 'ID')
    scatter(lon[:,0], lat[:,0], size=6, color='r', marker='S')
    xlim(-92, -55)
    ylim(34, 54)
    yticks(arange(35, 54, 5))
    title('MeteoInfoLab script demo - Trajectory')

    axes(outerposition=[0, 0, 1, 0.3], yreverse=True, xaxistype='time')
    tt = f['time'][:,:]
    data = f['PRESSURE'][:,:]
    plot(tt, data, legend=tlayer.legend())
    xlabel('Time')
    ylabel('hPa')

.. image:: ../../../_static/traj_plot_1.png

Change the legend of the trajectory layer.

::

    from org.meteoinfo.geometry.legend import PointStyle

    fn = os.path.join(migl.get_sample_folder(), 'HYSPLIT', 'tdump')
    f = addfile_hytraj(fn)
    lon = f['lon'][:,:]
    lat = f['lat'][:,:]

    #Plot
    figure(figsize=[526, 489], newfig=False)
    axesm(position=[0.12, 0.3, 0.85, 0.7])
    geoshow('country', edgecolor=(0,0,255), facecolor=(230,230,230))
    cols = makecolors(len(lon))
    levs = arange(0, 101, 5)
    tlayer = plotm(lon, lat, levels=levs, isadd=False)
    ls = tlayer.update_legend('unique', 'ID')
    i = 0
    for lb in ls.getLegendBreaks():
        lb.setSize(2)
        lb.setDrawSymbol(True)
        lb.setSymbolInterval(6)
        if i == len(PointStyle.values()):
            i = 0
        lb.setSymbolStyle(PointStyle.values()[i])
        i += 1
    geoshow(tlayer)
    scatterm(lon[:,0], lat[:,0], size=6, color='r', marker='S')
    xlim(-92, -55)
    ylim(34, 54)
    yticks(arange(35, 54, 5))
    title('MeteoInfoLab script demo - Trajectory')

    axes(outerposition=[0, 0, 1, 0.3], yreverse=True, xaxistype='time')
    tt = f['time'][:,:]
    data = f['PRESSURE'][:,:]
    plot(tt, data, legend=tlayer.legend())
    xlabel('Time')
    ylabel('hPa')
    
.. image:: ../../../_static/traj_plot_2.png

Plot trajectories in a 3-D map colored by pressure values.

::

    fn = os.path.join(migl.get_sample_folder(), 'HYSPLIT', 'tdump')
    f = addfile_hytraj(fn)
    lon = f['lon'][:,:]
    lat = f['lat'][:,:]
    alt = f['height'][:,:]
    pres = f['PRESSURE'][:,:]

    #Plot
    ax = axes3d()
    geoshow('us_states', facecolor=(255,248,226), edgecolor='b')
    traj = plot3(lon, lat, alt, mvalues=pres, linewidth=2)
    scatter3(lon[:,0], lat[:,0], alt[:,0], marker='o', fill=False, \
        size=14, edgecolor='gray')
    colorbar(traj)
    xlim(-125, -55)
    ylim(25, 50)
    zlim(0, 1000)
    title('3D trajectory example')

.. image:: ../../../_static/traj_3d_color.png