.. _examples-meteoinfolab-plot_types-image_process:

*******************
Image process
*******************

Some image processing functions are included in ``imagelib`` package.

Image flip:

::

    fn = 'D:/Temp/image/Lenna.png'
    lena = imagelib.imread(fn)
    subplot(1, 2, 1,aspect='equal', tickline=False)
    imshow(lena)
    subplot(1, 2, 2, aspect='equal', tickline=False)
    lena_1 = imagelib.flip(lena)
    imshow(lena_1)

.. image:: ../../../_static/image_flip.png

Image gray scale:

::

    fn = 'D:/Temp/image/Lenna.png'
    lena = imagelib.imread(fn)
    subplot(1, 2, 1,aspect='equal', tickline=False)
    imshow(lena)
    subplot(1, 2, 2, aspect='equal', tickline=False)
    lena_1 = imagelib.gray_scale(lena)
    imshow(lena_1)
    
.. image:: ../../../_static/image_gray_scale.png

Image emboss:

::

    fn = 'D:/Temp/image/Lenna.png'
    lena = imagelib.imread(fn)
    subplot(1, 2, 1,aspect='equal', tickline=False)
    imshow(lena)
    subplot(1, 2, 2, aspect='equal', tickline=False)
    lena_1 = imagelib.emboss(lena)
    imshow(lena_1)
    
.. image:: ../../../_static/image_emboss.png