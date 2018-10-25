.. _examples-meteoinfolab-meteo_analysis-oblique_section_plot:

****************************
Oblique section plot
****************************

The example to plot cross section with oblique direction.

::

    figure(figsize=[1500,400],newfig=False)
    fig,((ax1,ax2)) = subplots(1,2,position=[0,0.08,1,0.89])
    f = addfile(r'H:\test\data\test.nc')
    fn1 = addfile(r'H:\alldata\dixing/elev.0.5-deg.nc')
    lev1 = f['level'][:]
    lev2 = meteo.pressure_to_height_std(lev1)
    lev2 = lev2[::-1]/1000

    lon1 = 80
    lon2 = 120
    lat1 = 32
    lat2 = 40
    lon = lon1
    lat_c = []
    tdata = []
    tdata_terrain = []
    while lon<=lon2:
        lat = lat1+(lat2-lat1)*(lon-lon1)/(lon2-lon1)
        lat_c.append(lat)
        print lat
        tdata.append(f['w'][0,:,'%f'%lat,'%f'%lon])
        tdata_terrain.append(fn1['data']['%f'%lat,'%f'%lon])
        lon = lon+1
        
    tdata_terrain=array(tdata_terrain)    
    tdata_terrain=tdata_terrain/1000.0
    alldata=concatenate(tdata,axis=0)
    alldata=reshape(alldata,(len(tdata),len(lev1)))    
    alldata=alldata.T
    alldata = alldata[::-1,:]

    axes(newaxes=False)    
    x=arange(lon1,lon2+1,1) 
    levs = arange(-0.2,0.22,0.02)
    yaxis(tickin=False,tickfontsize=17)
    xaxis(tickin=False,tickfontsize=17)
    yaxis(location='right',tickin=True,tickfontsize=18)
    layer = contourf(x,lev2,alldata,levs,cmap='BlRe')
    fill_between(x,tdata_terrain,color='gray')
    plot(x,tdata_terrain,color='k')
    ylabel('Hight(km)',fontsize=18,bold=False)
    xlabel('Longitude',fontsize=18)
    ylim(lev2.min(),12.001)
    colorbar(layer,aspect=25)

    caxes(ax2)
    axesm(newaxes=False,tickfontsize=17)
    lat = [32, 40]
    lon = [100, 120]
    geoshow(lat, lon, size=2, color='b')
    lchina = shaperead('D:/Temp/map/bou2_4p.shp')
    geoshow(lchina,edgecolor='k',size=1)
    xlim(70,140)
    ylim(15,55)
    antialias(True)
    
.. image:: ../../../_static/oblique_section_plot.png

Plot oblique cross section in 3-D coordinate.

::

    f = addfile(r'H:\test\data\test.nc')
    fn1 = addfile(r'H:\alldata\dixing/elev.0.5-deg.nc')
    lev1 = f['level'][:]
    lev2 = meteo.pressure_to_height_std(lev1)
    lev2 = lev2[::-1]/1000

    lon1 = 80
    lon2 = 120
    lat1 = 32
    lat2 = 40
    lon = lon1
    x = []
    y = []
    tdata = []
    tdata_terrain = []
    while lon<=lon2:
        lat = lat1+(lat2-lat1)*(lon-lon1)/(lon2-lon1)
        print lon
        tdata.append(f['w'][0,:,'%f'%lat,'%f'%lon])  
        tdata_terrain.append(fn1['data']['%f'%lat,'%f'%lon])
        x.append(lon)
        y.append(lat)
        lon = lon+1
        
    tdata_terrain=array(tdata_terrain)    
    tdata_terrain[tdata_terrain<0] = 0
    tdata_terrain=tdata_terrain/1000.0

    alldata=concatenate(tdata,axis=0)
    alldata=reshape(alldata,(len(tdata),len(lev1)))   
    alldata=alldata.T
    alldata = alldata[::-1,:]
    x=array(x)
    y=array(y)

    ax = axes3d(position=[0.11, 0.11, 0.775, 0.815],tickfontsize=17,bbox=False) 
    levs = arange(-0.2,0.22,0.02)
    china = shaperead('D:/Temp/map/china.shp')
    world = shaperead('D:/Temp/map/country1.shp')
    ax.plot_layer(china,edgecolor='gray')
    ax.plot_layer(world,edgecolor='gray')
    layer=ax.contourf(x,lev2,alldata,levs,zdir='xy',alpha=0.8,sepoint=[lon1,lat1,lon2,lat2],cmap='BlRe')
    k =(lat2-lat1)/float((lon2-lon1))
    y1=k*(x-lon1)+lat1
    ax.plot(x,y1,tdata_terrain,'-k',linewidth=1)
    ax.fill_between(x,tdata_terrain, zdir='xy',color='gray',y=y1)

    xlim(70,140)
    ylim(15,55)
    zlim(0,12)
    colorbar(layer,aspect=30)
    ylabel('Latitude (degrees)',fontsize=17)
    xlabel('Longitude (degrees)',fontsize=17)
    zlabel(label='Altitude (km)',fontsize=17)
    antialias(True)
    
.. image:: ../../../_static/oblique_section_plot_3d.png