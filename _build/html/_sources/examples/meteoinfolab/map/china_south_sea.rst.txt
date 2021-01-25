.. _examples-meteoinfolab-map-china_south_sea:

*******************
Add China South Sea
*******************

This example demonstrate how to add China South Sea sum-map using multiple map axes.

::

    #Plot
    axesm()
    geoshow('cn_province', edgecolor='lightgray')
    geoshow('cn_border', facecolor=(0,0,255))
    ss = makesymbolspec('line', {'value':'Yangtze', 'color':(0,255,255), 'size':1}, \
        {'value':'Huang He', 'color':(0,255,255), 'size':1}, field='NAME')
    geoshow('rivers', symbolspec=ss)
    geoshow('cn_cities', facecolor='r', size=4, labelfield='NAME', fontname=u'楷体', fontsize=16, yoffset=15)
    xlim(72, 136)
    ylim(16, 55)
    #Add south China Sea
    axesm(position=[0.14,0.18,0.15,0.2], axison=False)
    geoshow('cn_border', facecolor=(0,0,255))
    xlim(106, 123)
    ylim(2, 23)
        
.. image:: ../../../_static/china_south_sea.png