.. _dos-meteoinfolab-milab_cn-plotlib-vector_plot:


*******************************
向量场图
*******************************

气象领域里的风场是典型的向量场，通常用U、V分量或风向、风速来表示。quiver函数可以将向量绘制成箭头，箭头方向指示向量的方向，
箭头长度指示向量的大小。size参数用来调整箭头的大小，color参数指定箭头颜色。

::

    X, Y = meshgrid(arange(-pi, pi, pi/8),arange(-pi ,pi, pi/8))
    U = sin(Y) * 10
    V = cos(X) * 10
    q = quiver(X, Y, U, V, size=15, color='b')

.. image:: ./image/plotlib_quiver.png

barbs函数可以将向量绘制为风向杆，U、V变量参数后如果还有非关键字参数会被当做用于颜色分级显示的变量，比如从U、V分量计算出风速，
将其作为颜色分级变量绘制彩色风向杆图。quiver函数也可以类似处理绘制彩色箭头图。

::

    X, Y = meshgrid(arange(-pi, pi, pi/8),arange(-pi ,pi, pi/8))
    U = sin(Y) * 10
    V = cos(X) * 10
    speed = sqrt(U * U + V * V)
    q = barbs(X, Y, U, V, speed, size=10)
    colorbar(shrink=0.8)

.. image:: ./image/plotlib_barbs.png

向量场还可以用streamplot绘制流线图，density参数指定流线的密度。

::

    x = y = linspace(-3, 3, 20)
    X, Y = meshgrid(y, x)
    U = -1 - X**2 + Y
    V = 1 + X - Y**2
    streamplot(x, y, U, V, color='b', density=3)

.. image:: ./image/plotlib_streamplot.png