.. _news-meteoinfo_1.9:


******************************************
MeteoInfo 1.9 was released (2019-8-27)
******************************************

  - Add org.meteoinfo.ndarray package for multiple dimensional array implementation replace ucar.ma2 package.
  - Add ``interplate_1d`` function to support vertical coordinate conversion such as sigma to isobaric.
  - Support violin and nested pie plots.
  - Add position capibility to Axis.
  - Add qucksort algorithm and improve 3D plot.
  - Update gif animation with dpi setting.
  - Speed up interpolation functions using KDTree.
  - Replace Apache Sanselan 0.97-incubator with Apache Commons Imaging 1.0-alpha.
  - Add ``reproject`` function in ``migeo`` module of geolib package.
  - Add percentile and quantile functions to groupby DataFrame.
  - Add ``loc`` and ``iloc`` in Series class.
  - Distinguish between corner and center when reading ESRI ASCII grid data.

.. toctree::

   ../examples/meteoinfolab/meteo_analysis/sigma2pressure.rst
   ../examples/meteoinfolab/plot_types/violinplot.rst