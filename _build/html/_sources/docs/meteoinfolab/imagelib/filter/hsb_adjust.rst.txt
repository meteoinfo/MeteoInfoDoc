.. _docs-meteoinfolab-imagelib-filter-hsb_adjust:


*********************************
hsb_adjust
*********************************

.. currentmodule:: mipylib.imagelib.filter

.. function:: hsb_adjust(src, h=0, s=0, b=0)

    This filter adds or subtracts a given amount from each of the hue, saturation and brightness 
    channels of an image.
    
    :param src: (*image*) Source image.
    :param h: (*float*) Hue.
    :param s: (*float*) Saturation.
    :param b: (*float*) brightness.
    
    :returns: Destination image.
    
    **Example:**

    ::

        #Add data file
        fn = r'C:\Temp\himawari8\NC_H08_20170508_0040_r14_FLDK.02701_02601.nc'
        f = addfile(fn)
        #Read data
        bdata = f['albedo_01'][:,:]
        gdata = f['albedo_02'][:,:]
        rdata = f['albedo_03'][:,:]
        bdata[bdata>1] = 1
        gdata[gdata>1] = 1
        rdata[rdata>1] = 1
        #Plot
        axesm()
        mlayer = shaperead('D:/Temp/map/country1.shp')
        geoshow(mlayer, edgecolor='g')
        layer = imshowm([rdata,gdata,bdata])
        #Adjust image
        imagelib.hsb_adjust(layer, h=0, s=0.1, b=0.2)
        title('Himarari 8 true color image example')

    .. image:: ../../../../_static/himawari8_true_color.png