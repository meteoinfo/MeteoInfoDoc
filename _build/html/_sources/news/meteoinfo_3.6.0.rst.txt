.. _news-meteoinfo_3.6.0:


******************************************
MeteoInfo 3.6.0 was released (2023-6-2)
******************************************

  - Add `meshc` and `surfc` plot functions
  - Add `fill3` function
  - Add Arc patch
  - Add `trisurf` function and a simple wavefront object file loader function
  - Add `odeint` function
  - Add `pinv` function
  - Add `multivariate_normal` function
  - Add `isscalar` function in numeric module
  - Add `airy` function
  - Add `polygonindex` function
  - Add jenks nature breaks module
  - Add enum package
  - Add MultiIndex class in DataFrame package
  - Add field of view parameter in 3D axes for perspective projection
  - Add reindex method in DataFrame class
  - update netcdfAll to version 5.5.4-SNAPSHOT to support Grib2 template 4.60
  - Update `hist` function to support multiple arrays
  - Update FlatLaf to version 3.1.1
  - Update JOGL to version 2.4.0
  - Update rsyntaxtextarea to version 3.3.2
  - Some other bugs fixed

**Read and plot 3D model object**::

    fn = 'D:/Temp/3d/15994_Multi-Purpose_Utility_Helicopter_v1.obj'
    T, x, y, z, normal = plt.load_obj_model(fn)

    figure(facecolor='k', newfig=False)
    axes3d(aspect='equal', axis=False, clip_plane=False)
    lighting(mat_specular=1)
    trisurf(T, x, y, z, facecolor='c')

.. image:: ../_static/model3d_helicopter.png

**surfc function example**::

    [X,Y] = meshgrid(arange(-3, 3, .125))
    Z = peaks(X,Y)[2]
    C = X*Y
    axes3d()
    surfc(X, Y, Z, C, 20)
    colorbar()

.. image:: ../_static/surfc_1.png