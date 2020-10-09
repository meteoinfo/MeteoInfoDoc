.. _docs-meteoinfolab-numeric-interpolate-NearestNDInterpolator:


*********************
NearestNDInterpolator
*********************

.. currentmodule:: numeric.interpolate

.. class:: NearestNDInterpolator(object)

    NearestNDInterpolator(x, y)
    Nearest-neighbor interpolation in N dimensions.

    Methods
    -------
    __call__
    ----------
    x : (Npoints, Ndims) ndarray of floats
        Data point coordinates.
    y : (Npoints,) ndarray of float
        Data values.
    
    Examples::
    
        def func(x,y,z):
            return 0.5*(3)**(1./2)-((x-0.5)**2+(y-0.5)**2+(z-0.5)**2)**(1./2)

        x = random.rand(1000)
        y = random.rand(1000)
        z = random.rand(1000)
        v = func(x,y,z)

        f = interpolate.NearestNDInterpolator([x,y,z], v)

        gx = linspace(x.min(), x.max(), 50)
        gy = linspace(y.min(), y.max(), 50)
        gz = linspace(z.min(), z.max(), 50)
        xx,yy,zz = meshgrid(gx, gy, gz)
        gv = f([xx,yy,zz])

        levs = arange(0.1, 1.1, 0.1)
        scatter3(x, y, z, c=v, levels=levs)
        scatter3(xx, yy, zz, c=gv, s=2, levels=levs, alpha=0.5)
        colorbar()
        
.. image:: ../../../../_static/interp_3d_nearest.png