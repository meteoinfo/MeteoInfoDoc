.. docs-introduction-chinese-download_run:


********************
MeteoInfo下载与运行
********************

MeteoInfo下载
======================

MeteoInfo可以在其网站上的Download页面中下载，下载的文件是zip压缩文件，可以解压在计算机某个目录中，解压后的主目录是
MeteoInfo，里面包含了MeteoInfoMap和MeteoInfoLab的运行文件、依赖的库和一些配置文件，子目录sample里有一些各类格式
的示例数据文件，子目录map中包含了世界地图和中国地图等常用的地图数据，plugins和toolbox子目录中是扩展MeteoInfoMap和
MeteoInfoLab功能的插件和工具箱。MeteoInfo软件解压后可以直接使用，没有安装过程。

MeteoInfo运行
====================

MeteoInfo的运行需要Java 8或者更高版本的支持（必须是64位），建议使用Java 11 64位版本，Java可以在网上免费下载安装。
MeteoInfo是跨平台软件，所有平台都使用一个软件包，但启动文件不同。

启动MeteoInfoMap和MeteoInfoLab用户界面程序：

  -	Windows： MeteoInfoMap.exe和MeteoInfoLab.exe。也可以在命令行中运行mimap.bat和milab.bat。
  -	Linux/Unix： mimap.sh和milab.sh（需要注意这两个文件要将权限设置为可执行）。
  -	Mac OS：mimap_mac.sh和milab_mac.sh（需要注意这两个文件要将权限设置为可执行）。

运行Jython脚本程序也可以不启动MeteoInfoLab用户界面，直接在命令行环境中运行：

  -	Windows：milab.bat test.py（可以在任务计划中定时自动运行）。
  -	Linux/Unix：milab.sh test.py（可以在crontab中定时自动运行 ）。
  -	Mac OS: milab_mac.sh test.py（可以在crontab中定时自动运行 ）。

如果在远程登录Linux/Unix系统机器是没有启动Xwindos图形环境，可以在定时加 -b 参数：milab.sh -b test.py（无需图形环境）。

设置MeteoInfo运行内存
=====================

在利用MeteoInfo软件处理超大数据时由于内存限制可能会出现java.lang.OutOfMemoryError: Java heap space，error之类
的错误信息，这时可以尝试修改MeteoInfo启动文件中最大内存设置。比如在Windows中可以用文本编辑软件修改MeteoInfoLab.l4j.ini
（或MeteoInfoMap.l4j.ini）文件中-Xmx参数，例如从-Xmx2G改为-Xmx4G来增大MeteoInfoLab运行可用的最大内存。文件中还有-Xms
参数是用来设置可用内存的初始大小。

在Linux/Unix中修改milab.sh文件中的-Xmx参数，Mac OS中修改milab_mac.sh文件。