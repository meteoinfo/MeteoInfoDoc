.. docs-introduction-chinese-roadmap:


*************************
MeteoInfo开发历程
*************************

作者在做研究工作的时候需要自行开发一些算法完成特定的功能，针对气团轨迹统计分析功能（TrajStat）最早是用ArcView 3.x版本扩展
开发，后来改用开源的GIS控件MapWindows进行二次开发，能够结合长期大量后向轨迹和站点污染物浓度监测数据开展污染物传输路径和潜在
源区的分析，相关成果2009年发表在Environmental Modelling & Software上。同时由于绘图需要自行研发了等值线相关算法库
wContour。2009-2010年在西班牙Huelva大学做访问学者时萌生了开发气象GIS软件的想法并很快付诸实施，当时采用的计算机语言是
C#。wContour库2012年在Geoscience & Computers上发表，基于C#的气象GIS软件MeteoInfo 2014年在Meteorological
Applications上发表。

气象领域对Linux/Unix系统的应用很广泛，尤其是数值模式的运行，而C#语言开发的软件跨平台能力比较弱，因此考虑用跨平台能力很强的
Java语言重新开发MeteoInfo，而且Java拥有大量的开源科学计算库，特别是Unidata的NetCDF Java库能够支持大多数大气科学领域常
用的数据格式，对提升MeteoInfo的功能有很大帮助。同时由于气象GIS桌面软件的用途限制比较大，考虑开发基于Java和Jython的科学计
算软件，将MeteoInfo划分为同一框架下的MeteoInfoMap和MeteoInfoLab两大应用程序来满足更多的需求。MeteoInfo科学计算软件研
发的工作2019年在Journal of Open Research Software上发表。在新的MeteoInfo软件研发过程中，也在开发一些功能扩展模块，
TrajStat重新开发为MeteoInfoMap的一个插件，也开发了MeteoInfoLab的一些工具箱：IMEP（用于模式检验）、EMIPS（用于排放源
清单处理）、MIML（用于机器学习）。考虑到国外用户的使用，MeteoInfo的开发以英文为主，MeteoInfoMap的界面增加了中文支持。
MeteoInfo还需要不断的发展改进，相关的文档写作更是比较滞后，希望通过持续的努力工作让MeteoInfo能够更好地为项目科研和业务人
员服务。