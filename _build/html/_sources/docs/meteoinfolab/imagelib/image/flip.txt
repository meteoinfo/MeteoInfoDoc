.. _docs-meteoinfolab-imagelib-image-flip:


*********************************
flip
*********************************

.. currentmodule:: mipylib.imagelib.image

.. function:: flip(src, operation=1)

    A filter which flips images or rotates by multiples of 90 degrees.
    
    :param src: (*image*) Source image.
    :param operation: (*int*) Operation. 1: Flip the image horizontally; 2: Flip the image 
        vertically; 3: Flip the image horizontally and vertically; 4: Rotate the image 90 
        degrees clockwise; 5: Rotate the image 90 degrees counter-clockwise; 6: Rotate the 
        image 180 degrees.
    
    :returns: Destination image.
    
    **Example:**
    
    Image flip:

    ::

        fn = 'D:/Temp/image/Lenna.png'
        lena = image.imread(fn)
        subplot(1, 2, 1,aspect='equal', tickline=False)
        imshow(lena)
        subplot(1, 2, 2, aspect='equal', tickline=False)
        lena_1 = image.flip(lena)
        imshow(lena_1)

    .. image:: ../../../../_static/image_flip.png