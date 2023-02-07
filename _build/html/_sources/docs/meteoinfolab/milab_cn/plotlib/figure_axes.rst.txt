.. _dos-meteoinfolab-milab_cn-plotlib-figure_axes:


***************************
Figure和Axes
***************************

图形的绘制需要一块画布，也就是Figure对象。figure函数可以生成一个Figure对象，缺省其绘图区域是大小可变的，即随着用户拖动
MeteoInfLab中Figures窗体大小Figure绘图区域大小也随之变化。可以通过设置figure函数中的figsize参数对Figure的绘图区域
进行固定，如figure(figsize=[600, 400])即生成一个固定绘图区域为宽600像素、高400像素的Figure对象。还可以通过facecolor
参数设置Figure对象的背景色，缺省是白色，facecolor=None则Figure对象背景是透明的。

每个Figure对象可以包含一个或多个坐标系（Axes），每个Axes对象都是一个拥有自己坐标系统的绘图区域。Axes对象包含两个或三个
坐标轴，分别对应二维或三维坐标系，坐标轴内部是真正的数据绘制区域，由点、线、面、文字等组成数据图形，坐标轴外部还可能有坐标
轴标注、图题、图例等图形和文字信息。Axes的位置和大小是由其position参数确定的，缺省值是position=[0.13, 0.11, 0.775, 0.815]，
四个数字分别代表左下角的x、y坐标以及宽度和高度，都是归一化的数字，也就是Figure的绘图区域是[0, 0, 1, 1]。plotlib包中有以下
几种坐标系类：

  -	Axes：普通二维坐标系，也是其它坐标系类的基类，可以用axes()函数生成Axes对象；
  -	PolarAxes：极坐标系，可以用axes(polar=True)函数生成PolarAxes对象；
  -	MapAxes：地图坐标系，此坐标系可以有不同的地图投影设置，可以用axesm()函数生成MapAxes对象；
  -	Axes3D：三维坐标系，此坐标系中绘制三维图形时将三维坐标投影到二维平面，然后再用Java2D的绘图函数来绘制，没有硬件加速。可以用axes3d(opengl=False)函数生成Axes3D对象；
  -	Axes3DGL：带OpenGL硬件加速的三维坐标系，低层采用了JOGL（OpenGL的Java绑定）来绘制三维图形，由于有GPU加速，绘图速度快且有光照、图形深度探测等功能，能够绘制复杂的三维图形。可以用axes3d()函数生成Axes3DGL。