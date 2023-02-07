.. _dos-meteoinfolab-milab_cn-plotlib-plot_functions:


***************************
常用绘图函数
***************************

使用plotlib包绘图有两种模式：一种是面向对象的模式，先创建Figure和Axes对象，然后用Axes对象中的绘图方法来绘图；另一种是利用
plotlib.miplot模块中的绘图函数，如果没有Figure和Axes对象会自动生成，绘图函数会自动调用生成的Figure和Axes对象。极坐标系
（PolarAxes）和地图坐标系（MapAxes）需要用相关函数创建坐标系对象，然后再使用plotlib.miplot模块中的绘图函数。

对于二维坐标系，常用的绘图函数包括：

  -	plot(x, y, ...) – 绘制线条图
  -	scatter(x, y, ...) – 绘制散点图
  -	step(x, y, ...) – 绘制阶梯线图
  -	bar(x, y, ...) – 绘制条形图
  -	hist(x, ...) – 绘制直方图
  -	stem(x, y, ...) – 绘制针状图
  -	fill_between(x, y1, y2, ...) – 绘制曲线填充图
  -	semilogx(x, y, ...), semilogy(), loglog() – 绘制对数坐标线条图
  -	boxplot(x, ...) – 绘制箱形图
  -	violinplot(x, ...) – 绘制小提琴图
  -	imshow(x, y, ...) – 绘制二维图像
  -	contour(x, y, z, ...) – 绘制等值线图
  -	contourf(x, y, z, ...) – 绘制等值线填色图
  -	quiver(x, y, u, v, z, ...) – 绘制风场箭头图
  -	babs(x, y, u, v, z, ...) – 绘制风向杆图
  -	streamplot(x, y, u, v, z, ...) – 绘制流场图
  - text(x, y, s, ...) - 绘制文字
  - geoshow(map, ...) - 绘制地图图形

对于三维坐标系，常用的绘图函数包括：

  -	plot3(x, y, z, ...) – 绘制三维线条图
  -	scatter3(x, y, z, ...) – 绘制三维散点图
  -	bar3(x, y, z, ...) – 绘制三维条形图
  - stem3(x, y, z, ...) - 绘制三维针状图
  - text3(x, y, z, s, ...) - 绘制三维文字
  -	quiver3(x, y, z, u, v, w, ...) – 绘制三维风场箭头图
  - streamplot3(x, y, z, u, v, w, ...) - 绘制三维流场图
  - streamslice(x, y, z, u, v, w, ...) - 绘制三维流场切片图
  - contourslice(x, y, z, data, ...) - 绘制三维等值线切片图
  - contourfslice(x, y, z, data, ...) - 绘制三维等值线天色切片图
  - imshow(x, y, z, ...) - 在三维坐标系中绘制图像
  - geoshow(map, ...) - 在三维坐标系中绘制地图图形
  -	mesh(x, y, z, ...) – 绘制三维曲面网格图
  -	surf(x, y, z, ...) – 绘制三维曲面图
  -	slice3(x, y, z, ...) – 绘制三维体切片平面图
  -	isosurface(x, y, z, ...) – 绘制三维等值面图
  -	particles(x, y, z, ...) – 绘制三维颗粒图
  - volumeplot(x, y, z, data, ...) - 三维体绘制