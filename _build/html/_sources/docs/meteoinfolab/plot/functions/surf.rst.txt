.. _docs-meteoinfolab-funcitons-plot-surf:


*******************
surf
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: surf(ax)

    creates a three-dimensional surface plot

    :param x: (*array_like*) Optional. X coordinate array.
    :param y: (*array_like*) Optional. Y coordinate array.
    :param z: (*array_like*) 2-D z value array.
    :param c: (*array_like*) Optional. Additionally specifies the surface color.
    :param cmap: (*string*) Color map string.
    :param lighting: (*bool*) Using light or not.

    :returns: 3D surface graphic
    
    **Examples:**

    Create surface plot
    --------------------

    Create three matrices of the same size. Then plot them as a surface. The surface plot uses Z for both
    height and color.
    
    ::

        [X,Y] = meshgrid(arange(1,10.5,0.5), arange(1,20.1))
        Z = sin(X) + cos(Y)
        surf(X, Y, Z)

    .. image:: ./image/surf_1.png

    Specify Colormap Colors for Surface Plot
    ----------------------------------------

    Specify the colors for a surface plot by including a fourth matrix input, C. The surface plot uses Z for
    height and C for color. Specify the colors using a colormap, which uses single numbers to stand for
    colors on a spectrum. When you use a colormap, C is the same size as Z. Add a color bar to the graph to
    show how the data values in C correspond to the colors in the colormap.

    ::

        [X,Y] = meshgrid(arange(1,10.5,0.5), arange(1,20.1))
        Z = sin(X) + cos(Y)
        C = X * Y
        surf(X, Y, Z, C)
        colorbar()
        
    .. image:: ./image/surf_color_1.png

    Specify True Colors for Surface Plot
    ------------------------------------

    Specify the colors for a surface plot by including a fourth matrix input, CO. The surface plot uses Z for
    height and CO for color. Specify the colors using truecolor, which uses triplets of numbers to stand for
    all possible colors. When you use truecolor, if Z is m-by-n, then CO is m-by-n-by-3. The first page of
    the array indicates the red component for each color, the second page indicates the green component, and
    the third page indicates the blue component.

    ::

        [X,Y,Z] = peaks(25)
        ny, nx = Z.shape
        CO = zeros([ny, nx, 3])
        CO[:,:,0] = zeros(25) # red
        CO[:,:,1] = ones(25)*linspace(0.5,0.6,25) # green
        CO[:,:,2] = ones(25)*linspace(0,1,25) # blue
        surf(X,Y,Z,CO)

    .. image:: ./image/surf_color_2.png

    Modify Surface Plot Appearance
    ------------------------------

    Create a semitransparent surface by specifying the FaceAlpha name-value pair with 0.5 as the value. To
    allow further modifications, assign the surface object to the variable s.

    ::

        x, y = meshgrid(arange(-5,5.5,0.5))
        z = y * sin(x) + x * cos(y)
        s = surf(x, y, z, 20, facealpha=0.5)

    .. image:: ./image/surf_alpha_1.png