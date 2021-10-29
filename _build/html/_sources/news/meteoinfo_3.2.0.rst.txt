.. _news-meteoinfo_3.2.0:


******************************************
MeteoInfo 3.2.0 was released (2021-10-15)
******************************************

  - Update pro4j to 1.1.3
  - Update FlatLaf to version 1.6
  - Remove jchardet library
  - Add ``contourslice`` and ``contourfslice`` functions in 3D axes
  - Enable lighting to support double sides normal in 3D axes
  - Support 3D pipe line plot
  - Add vertex normal calculation functions
  - Support equal aspect in 3D axes
  - Add ``sphere`` and ``cylinder`` functions
  - Add MICAPS MDFS type 3 data support
  - Support unicode path of MeteoInfo
  - Add ``erf`` and ``erfc`` functions
  - Add ``arctan`` and ``arctan2`` functions for numpy compatible
  - Add ``peaks`` function
  - Add ``patches`` package in plotlib
  - Add lines ``module`` and ``Line2D`` class
  - Add ``supxlabel`` and ``supylabel`` functions
  - Add ``copy`` and ``move`` functions in MILayer class
  - Support CAMx output nc data file
  - Some bug fixed

**sphere plot**::

    x, y, z = sphere()
    axes3d(aspect='equal')
    surf(x, y, z)
    antialias()

.. image:: ../_static/sphere_surf.png

**cylinder plot**::

    t = arange(0, 2*pi+0.001, pi/10)
    r = 2 + cos(t)
    x, y, z = cylinder(r)
    surf(x, y, z)
    antialias()

.. image:: ../_static/cylinder_surf.png

**peaks plot**::

    x, y, z = peaks(25)
    mesh(x, y, z, cmap='GMT_drywet_r')
    antialias()

.. image:: ../_static/peaks_mesh.png