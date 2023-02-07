.. docs-introduction-index_chinese:


*******************
MeteoInfo总体介绍
*******************

MeteoInfo是中国气象科学院王亚强博士开发的开源软件，是融合GIS和科学数据分析及可视化为一体的软件平台，可以作为工具软件用于
地学尤其是大气科学领域的科学研究和业务工作中。MeteoInfo具有很好的跨平台能力，可以在Windows、Linux/Unix和Mac OS等操作
系统中运行。

地球科学数据通常具有鲜明的三维空间特征，其中大气圈状态快速变化，时间维度也很重要，加上描述各种物理、化学状态的变量，共同构成了
地球科学多维数据集。科学研究需要从数据中发现规律，功能强大、使用便利的科学数据分析和可视化工具是科研工作的重要助力。

科学计算和GIS功能对于大气科学数据分析都十分重要，将这些功能放入一个软件框架里更有利于交叉融合并满足不同需求。从2010年开始作
者开发的MeteoInfo软件致力于实现这个目标。目前MeteoInfo框架中包含GIS桌面软件MeteoInfoMap和科学计算、可视化软件
MeteoInfoLab，以及可用于二次开发的MeteoInfo Java库。MeteoInfo是免费和开源的软件，源代码代管在GitHub网站上。软件支持
国内外常用的大气科学数据格式，MeteoInfoMap可以快速、方便地以GIS图层方式浏览各类气象数据，并包含空间数据编辑、投影和分析等
功能；MeteoInfoLab包含了多维数组计算、线性代数等科学计算以及2维/3维绘图等功能，适合完成科研和业务中大气科学数据分析和可视
化的任务；MeteoInfo的Java库功能丰富，在其基础上可以方便、快捷地开发相关科研、业务软件。随着软件功能的不断丰富，其复杂性不
断提高，作为开源软件，也欢迎有兴趣的读者参与软件的开发、测试和文档编写等工作。

.. toctree::
   :maxdepth: 2
   
   chinese/framework.rst
   chinese/website_code.rst
   chinese/download_run.rst
   chinese/data_formats.rst
   chinese/roadmap.rst