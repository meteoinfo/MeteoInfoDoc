.. _news-wcontour_1.6.1:


******************************************
wContour 1.6.1 was released (2017-11-2)
******************************************

Fixed a bug tracing contour polygon from inner border line. In this situation, the polygon may have been traced
from outter border line, so need to check and stop tracing and reduce the using time number of the traced
border points.

**The bug**

.. image:: ../_static/news/wcontour_1.6.1_bug.png

**Bug fixed**

.. image:: ../_static/news/wcontour_1.6.1_bugfixed.png