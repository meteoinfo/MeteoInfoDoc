.. docs-meteoinfo-desktop_cn-map_layer:


************************
图层操作
************************

MeteoInfoMap中的一个基本显示和操作单元是图层，目前支持四种类型的图层：矢量图层（Vector Layer）、图像图层
（Image Layer）、栅格图层（Raster Layer）和网络地图图层（Web Map Layer）。矢量图层由相同类型的空间要素
组成，包含了空间要素的坐标和属性信息，可以和Shapefile文件相对应。图像图层是将一个图像作为地理图层，图像的显示
是固定的。栅格图层是图像图层的扩展，图层包含一个二维格点数组，可以进行相应的数组计算。网络地图图层也是图像图层的
扩展，其图像来自网络地图切片图的实施加载。

所有项目包含的图层都显示在图层管理区，图层名最左边显示为方框内加号（图层的图例隐藏）或者减号（图层的图例显示）。
右边紧跟一个方框内如果有对勾表明该图层显示在地图视图中，否则不显示。可以用鼠标点击的方式切换上述图层状态。

图层在地图视图中显示是按照图层管理区的顺序从下往上一层一层显示，这就意味着上面的图层内容可能压盖下面的图层内容。
因此通常图像图层（包括栅格图层和网络地图图层）放在最下面，往上是多边形填色图层、线图层和点图层。图层的顺序可以
通过鼠标拖动来调整。

.. toctree::
   :maxdepth: 2

   map_layer/add_remove_layer.rst
   map_layer/vector_layer.rst
   map_layer/image_layer.rst
   map_layer/raster_layer.rst
   map_layer/web_layer.rst
   map_layer/map_frame_layer_group.rst