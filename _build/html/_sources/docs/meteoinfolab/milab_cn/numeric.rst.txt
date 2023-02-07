.. _dos-meteoinfolab-milab_cn-numeric:


***************************
numeric包
***************************

Python或者Jython作为动态语言运行速度很慢，并不适合完成高强度的数值运算任务，Python的numpy包中数值运行是由
C、C++、Fortran等语言写的代码完成的，Python再对这些由低级语言编写的外部库进行封装和调用。MeteoInfoLab中数值
运算是由高效的Java代码完成的，Jython再进行封装和调用，达到能够简单编写数值运算程序并高效率运行的目的。

numeric包的核心是多维数组NDArray，封装了MeteoInfoLib Java库中org.meteoinfo.ndarray.Array多维数组对象，
对MeteoInfoLab中Jython多维数组的操作实际上就是对封装的Java多维数组的操作，主要使用
org.meteoinfo.ndarray.math.ArrayMath和org.meteoinfo.ndarray.math.ArrayUtil类中的相关静态方法实现。
有一个原则是在MeteoInfoLab的Jython代码中不要用循环来对数组进行运算，而是利用数组整体的运算函数进行数值运算，这
样就能利用底层Java代码极大提高运算效率。

.. toctree::
   :maxdepth: 2

   numeric/create_array.rst
   numeric/array_operation.rst
   numeric/array_slice.rst
   numeric/dimarray.rst
   numeric/linalg.rst
   numeric/random.rst
   numeric/stats.rst
   numeric/fitting.rst
   numeric/interpolate.rst