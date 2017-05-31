.. _docs-meteoinfolab-imagelib-filter-channel_mix:


*********************************
channel_mix
*********************************

.. currentmodule:: mipylib.imagelib.filter

.. function:: channel_mix(src, b_g=0, r_b=0, g_r=0, to_r=0, to_g=0, to_b=0)

    A filter which allows the red, green and blue channels of an image to be mixed into each other.
    
    :param src: (*image*) Source image.
    :param b_g: (*float*) Blue and green.
    :param r_b: (*float*) Red and blue.
    :param g_r: (*float*) Green and red.
    :param to_r: (*float*) Mix into red.
    :param to_g: (*float*) Mix into green.
    :param to_b: (*float*) Mix into blue.
    
    :returns: Destination image.