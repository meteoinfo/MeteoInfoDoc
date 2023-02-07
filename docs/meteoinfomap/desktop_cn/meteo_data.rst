.. docs-meteoinfomap-desktop_cn-meteo_data:


************************
MeteoInfoMap气象数据分析
************************

气象数据通常是多维的，包含空间三维以及时间维，来表示大气的时空变化状态。而GIS图层是二维的，且是地理坐标（经纬度或者投影后的
坐标），因此需要将多维的气象数据通过设置转变为GIS图层的维度，从而生成GIS图层和地理图层一起显示、分析。但是GIS图层仅限于地理
坐标，难以对多维的气象数据进行充分展示，因此需要剖面图、一维图等功能进行扩充。

气象数据根据其数据空间分布特征可以主要分为三种类型：（1）格点数据，数据在地理空间上是以规则网格形式分布，气象再分析以及模式输
出数据是典型的格点数据；（2）站点数据，数据在地理空间上是以不规则点状形式分布，多气象站点的观测数据是典型的站点数据；（3）轨
迹数据，数据在地理空间上是以线条形状分布，气团轨迹、台风路径等是典型的轨迹数据。


.. toctree::
   :maxdepth: 2

   meteo_data/meteo_data_dialog.rst
   meteo_data/grid_data.rst
   meteo_data/station_data.rst
   meteo_data/traj_data.rst
   meteo_data/cross_section.rst
   meteo_data/one_dimension.rst