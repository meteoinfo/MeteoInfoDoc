.. _docs-meteoinfolab-imagelib-image-invert:


*********************************
invert
*********************************

.. currentmodule:: mipylib.imagelib.image

.. function:: invert(src)

    A filter which inverts the RGB channels of an image.
    
    :param src: (*image*) Source image.
    
    :returns: Destination image.
    
    **Example:**
    
    Image invert:

    ::

        fn = 'D:/Temp/image/Lenna.png'
        lena = image.imread(fn)
        subplot(1, 2, 1,aspect='equal', tickline=False)
        imshow(lena)
        subplot(1, 2, 2, aspect='equal', tickline=False)
        lena_1 = image.invert(lena)
        imshow(lena_1)

    .. image:: ../../../../_static/image_invert.png