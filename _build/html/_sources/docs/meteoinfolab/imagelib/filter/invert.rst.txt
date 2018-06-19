.. _docs-meteoinfolab-imagelib-filter-invert:


*********************************
invert
*********************************

.. currentmodule:: mipylib.imagelib.filter

.. function:: invert(src)

    A filter which inverts the RGB channels of an image.
    
    :param src: (*image*) Source image.
    
    :returns: Destination image.
    
    **Example:**
    
    Image invert:

    ::

        fn = 'D:/Temp/image/Lenna.png'
        lena = imagelib.imread(fn)
        subplot(1, 2, 1,aspect='equal', tickline=False)
        imshow(lena)
        subplot(1, 2, 2, aspect='equal', tickline=False)
        lena_1 = imagelib.invert(lena)
        imshow(lena_1)

    .. image:: ../../../../_static/image_invert.png