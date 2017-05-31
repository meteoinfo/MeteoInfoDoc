.. _docs-meteoinfolab-imagelib-filter-gray_scale:


*********************************
gray_scale
*********************************

.. currentmodule:: mipylib.imagelib.filter

.. function:: gray_scale(src)

    A filter which converts an image to grayscale using the NTSC brightness calculation.
    
    :param src: (*image*) Source image.
    
    :returns: Destination image.
    
    **Example:**
    
    Image gray scale:

    ::

        fn = 'D:/Temp/image/Lenna.png'
        lena = image.imread(fn)
        subplot(1, 2, 1,aspect='equal', tickline=False)
        imshow(lena)
        subplot(1, 2, 2, aspect='equal', tickline=False)
        lena_1 = imfilter.gray_scale(lena)
        imshow(lena_1)

    .. image:: ../../../../_static/image_gray_scale.png