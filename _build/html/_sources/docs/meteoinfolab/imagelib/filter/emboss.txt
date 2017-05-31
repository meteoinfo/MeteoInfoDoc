.. _docs-meteoinfolab-imagelib-filter-emboss:


*********************************
emboss
*********************************

.. currentmodule:: mipylib.imagelib.filter

.. function:: emboss(src, azimuth=135, elevation=30, emboss=False, bh=1)

    This filter will emboss an image. 
    
    :param src: (*image*) Source image.
    :param azimuth: (*float*) Azimuth of the light source.
    :param elevation: (*float*) Elevation of the light source.
    :param emboss: (*boolean*) Emboss or not.
    :param bh: (*float*) Bump height.
    
    :returns: Destination image.
    
    **Example:**
    
    Image emboss:

    ::

        fn = 'D:/Temp/image/Lenna.png'
        lena = image.imread(fn)
        subplot(1, 2, 1,aspect='equal', tickline=False)
        imshow(lena)
        subplot(1, 2, 2, aspect='equal', tickline=False)
        lena_1 = imfilter.emboss(lena)
        imshow(lena_1)

    .. image:: ../../../../_static/image_emboss.png