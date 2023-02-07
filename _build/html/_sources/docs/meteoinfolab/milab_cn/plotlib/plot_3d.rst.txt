.. _dos-meteoinfolab-milab_cn-plotlib-plot_3d:


*******************************
三维图形
*******************************

MeteoInfoLab三维图绘制在三维坐标系中，axes3d函数可以生成一个三维坐标系（OpenGL绘图引擎），通过三维绘图函数绘制相应的三维图形。
绘制三维线图的函数是plot3，前三个参数是数据的x、y、z坐标数组，如果有cdata参数可以绘制随该参数数据变化的多颜色线。

::

    z = linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)

    plot3(x, y, z, cdata=z, linewidth=5)
    colorbar()
    title('3D plot example')

.. image:: ./image/axes3d_plot3.png

绘制三维点图的函数是scatter3，前三个参数是数据的x、y、z坐标数组，c参数可以设置用于绘制颜色的数组。

::

    z = linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)
    c = x + y

    #Plot
    points = scatter3(x, y, z, c=c)
    scatter3(x, y, 0.5, fill=False)
    colorbar(points, shrink=0.8)
    title('Point 3D plot example')

.. image:: ./image/axes3d_scatter3.png

三维针状图用stem3函数绘制，edgecolor函数设置针状图上点轮廓线颜色，samestemcolor参数设置针状图线段是否和点颜色一致。

::

    z = linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)
    c = x + y

    stem3(x, y, z, c=c, edge=False, samestemcolor=True)
    colorbar(shrink=0.8)
    title('Stem 3D plot example')

.. image:: ./image/axes3d_stem3.png

三维条形图用bar3函数绘制，width参数指定条形图的宽度，color参数指定条形图颜色，linewidth参数指定条形图边框线宽。

::

    z = linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)
    c = x + y

    cols = makecolors(len(x))
    bar3(x, y, z, width=0.05, color=cols, linewidth=1)
    title('Bar 3D plot example')

.. image:: ./image/axes3d_bar3.png

在三维坐标系中可以用contour或contourf函数绘制二维等值线，需要zdir参数确定等值线平面的垂直方向（zdir缺省为”z”），offset
参数设置等值线平面在zdir轴的位置（offset缺省为0）。mesh函数用来绘制网格曲面图。

::

    alpha = 0.7
    phi_ext = 2 * pi * 0.5
    N = 25
    x1 = linspace(0, 2*pi, N)
    y1 = linspace(0, 2*pi, N)
    x,y = meshgrid(x1, y1)
    z = 2 + alpha - 2 * cos(y) * cos(x) - alpha * cos(phi_ext - 2 * y)
    z = z.T

    mesh(x, y, z, edgecolor='b', facecolor=None)
    contourf(x1, y1, z, 10, alpha=0.8, offset=-2)
    colorbar()
    grid(False)

.. image:: ./image/axes3d_mesh_contourf.png

mesh函数缺省的facecolor参数是白色，edgecolor参数设置为“interp”则会用彩色绘制网格曲面线条。

::

    tx = ty = linspace(-8, 8, 33)
    xx, yy = meshgrid(tx, ty)
    r = sqrt(xx ** 2 + yy ** 2) + 2.2204e-16
    tz = sin(r) / r

    mesh(xx, yy, tz, edgecolor='interp')
    title('Mesh 3D plot example')
    colorbar()

.. image:: ./image/axes3d_mesh_interp.png

三维坐标系中也可以用geoshow函数绘制地理底图。imshow函数可以绘制二维图像，和二维等值线类似，可以设置offset和zdir参数。

::

    fn = os.path.join(migl.get_sample_folder(), 'GrADS', 'model.ctl')
    f = addfile(fn)
    ps = f['T'][0,:,'20','0:180']
    yy = linspace(0, 1., ps.shape[0])
    ps.setdimvalue(0, yy)

    ax = axes3d()
    geoshow('continent', color='c', edgecolor='b')
    imshow(ps, 10, offset=20, zdir='y', alpha=0.8)
    colorbar()
    zlim(0, 1)
    xlim(0, 180)

.. image:: ./image/axes3d_geoshow_imshow.png

绘制三维曲面图的函数是surf，曲面颜色缺省会根据Z数据填充，facecolor参数设为“interp”则颜色填充有渐变效果。

::

    tx = ty = linspace(-8, 8, 41)
    xx, yy = meshgrid(tx, ty)
    r = sqrt(xx ** 2 + yy ** 2) + 2.2204e-16
    tz = sin(r) / r

    surf(xx, yy, tz, edgesize=1)
    title('3-D Sombrero plot')

.. image:: ./image/axes3d_surf_sombrero.png

对于三维曲面图可以通过设置光照增强立体效果，lighting函数用来设置光照，第一个参数设置是否打开光照，还可以设置光源的位置、环境光、
散射光、镜面光等光照属性。

::

    tx = ty = linspace(-8, 8, 81)
    xx, yy = meshgrid(tx, ty)
    r = sqrt(xx ** 2 + yy ** 2) + 2.2204e-16
    tz = sin(r) / r

    lighting(True, position=[-1,-1,1,1], mat_specular=1)
    surf(xx, yy, tz, edgecolor=None, facecolor='g')
    title('3-D Sombrero plot')
    zlim(-0.4, 1)

.. image:: ./image/axes3d_surf_lighting.png

三维切片图绘制的函数是slice3，下面的例子绘制在值-1.2、0.8和2处与x轴正交的切片平面，在值0处与y轴正交的切片平面，以及在值0处
与z轴正交的切片平面。

::

    X=Y=Z = arange(-2, 2.1, 0.2)
    X,Y,Z = meshgrid(X, Y, Z)
    V = X*exp(-X**2-Y**2-Z**2)

    xslice = [-1.2,0.8,2]
    yslice = [0]
    zslice = 0

    slice3(X, Y, Z, V, xslice=xslice, yslice=yslice, zslice=zslice)
    colorbar()

.. image:: ./image/axes3d_slice3.png

isosurface函数用来绘制三维等值面图，需要设置三维坐标系和三维数组的值以及等值面的值，nthread参数设置用几个线程并行计算等值面。
三维等值面也可以设置光照效果。

::

    a = linspace(-3, 3, 100)
    x,y,z = meshgrid(a, a, a)
    p = (x**2+(9/4.)*y**2+z**2-1)**3-x**2*z**3-(9/80.)*y**2*z**3

    axes3d(aspect='equal', axes_zoom=True)
    grid(False)
    lighting(mat_specular=1)
    isosurface(x, y, z, p, 0, facecolor='r', edgecolor=None)

.. image:: ./image/axes3d_isosurface_heart.png

三位风场箭头图绘制的函数是quiver3，需要x、y、z坐标和风场的三维分量u、v、w数据。

::

    x, y, z = meshgrid(arange(-0.8, 1, 0.2),
                   arange(-0.8, 1, 0.2),
                   arange(-0.8, 1, 0.8))

    u = sin(pi * x) * cos(pi * y) * cos(pi * z)
    v = -cos(pi * x) * sin(pi * y) * cos(pi * z)
    w = (sqrt(2.0 / 3.0) * cos(pi * x) * cos(pi * y) *
         sin(pi * z))
    w = w * 3

    quiver3(x, y, z, u, v, w, color='b', length=0.2, linewidth=2)
    xlim(-0.8, 1)
    ylim(-0.8, 1)
    zlim(-1, 1)

.. image:: ./image/axes3d_quiver3.png

对于三维格点数据也可以用点的密度和透明度结合显示出数值的变化，particles函数需要输出x、y、z坐标和相应的三维格点数据，s
参数设置点的大小，vmin和vmax参数设置要绘制的数据最小值和最大值区间，alpha_min和alpha_max设置最小和最大透明度，density
设置点的密度。

::

    x = y = z = arange(-3, 3.1, 0.1)
    xx,yy,zz = meshgrid(x, y, z)
    v = xx*exp(-xx**2 - yy**2 - zz**2)

    ax = axes3d()
    ax.set_elevation(-50)
    ax.set_rotation(30)
    particles(x, y, z, v, 3, vmin=0.01, s=3, cmap='matlab_jet')
    colorbar()
    xlim(-1, 3)

.. image:: ./image/axes3d_particles.png

三维体绘制能够体现所有三维格点值的贡献，具有丰富的表现力。三维体绘制用到了射线追踪算法（Ray casting），在计算某条射线颜色时可以
选择三种不同的算法：max_value，basic和specular，其中max_value是用射线中格点最大值颜色，basic和specular用到射线穿过的所有
格点颜色叠加（不同距离有不同的透明度设置），specular是带光照效果的。此外还有 opacity_nodes 和 opacity_levels 参数来控制
重点显示哪些数值。

::

    fn = 'D:/Temp/image/sagittal.png'
    data1 = imagelib.imread(fn)
    data1 = data1[:,:,0]
    data1 = data1.reshape(88,300,600)
    data = zeros([176,300,300], dtype='int')
    data[:88] = data1[::-1,:,:300]
    data[88:] = data1[::-1,:,300:]
    data = data.swapaxes(0, 1)

    print('Plot...')
    figure(facecolor='c')
    ax = axes3d(aspect='equal', clip_plane=False, axis=False)
    volumeplot(data, cmap='NCV_bright', ray_casting='specular', brightness=1.5)

.. image:: ./image/axes3d_volumeplot.png