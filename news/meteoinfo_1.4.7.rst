.. _news-meteoinfo_1.4.7:


******************************************
MeteoInfo 1.4.7 was released (2017-11-2)
******************************************

  - ``Difference`` and ``Symmetrical Difference`` functions were added in GeoProcessing menu of MeteoInfoMap.
  - Update wContour library to version 1.6.1.
  - Add ``eof`` and ``varimax`` functions in ``meteo`` module for EOF and REOF analysis.
  - Add ``inv`` method in ``MIArray`` and ``DimArray`` class to calculate inverse matrix array.
  - Add ``lonflip`` and ``lonpivot`` methods in ``DimArray`` class to reorder the array with global longitude dimension.
  - Add ``month_to_season`` method in ``DimArray`` class to compute a user-specified three-month seasonal mean from monthly mean array.
  - Add ``select`` method in ``MILayer`` class to select shapes using a specified expression.
  - Add ``argmin`` and ``argmax`` methods in ``minum`` module to get the indices of the minimum/maximum values along an axis.
  - Add ``text`` and ``fill_between`` plot method in ``Axes3D`` class.
  - Add ``step`` plot function in ``miplot`` module to make a step plot.
  - Some bug fix and existing functions update.

**Symmetrical difference analysis**

.. image:: ../_static/news/mi_1.4.7_symdif_1.png

.. image:: ../_static/news/mi_1.4.7_symdif_2.png

.. image:: ../_static/news/mi_1.4.7_symdif_3.png