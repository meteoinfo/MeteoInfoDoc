.. _docs-instroduction:


*******************
Introduction
*******************

**MeteoInfo** is an intergrated framework both for GIS application and scientific computation environment, 
especially for meteorological community.

**MeteoInfoMap** is a GIS application which enables the user to visualize and analyze
the spatial and meteorological data with multiple data formats.
  
**MeteoInfoLab** is a scientific computation and visualization environment using Jython scripting with the 
ability of multiple dimensional array calculation and 2D/3D plotting.

It requires that Java 8 or greater be installed on your computer. See the
http://www.java.com website for a free download of Java if you do not have it
already installed.
  
Publication
======================
  
- Wang, Y.Q., 2014. MeteoInfo: GIS software for meteorological data visualization and analysis. Meteorological Applications, 21: 360-368.
- Wang, Y.Q., 2019. An Open Source Software Suite for Multi-Dimensional Meteorological Data Computation and Visualisation. Journal of Open Research Software, 7(1), p.21. DOI: http://doi.org/10.5334/jors.267
  
Presentation
======================

- MeteoInfo introduction in 2018 HYSPLIT workshop: `PPT <../downloads/files/MeteoInfo_and_HYSPLIT.pptx>`_ ; `Video <../downloads/files/ARLHysplitWorkshop2018-0614_MeteoInfo.zip>`_
  
Downloading
======================

The current version of MeteoInfo, along with other information about the
application, may always be found at http://www.meteothink.org

Installing MeteoInfoMap/MeteoInfoLab
==============================================

There is no specified installation file, just unzip the downloaded MeteoInfo file. The 
complete MeteoInfo Java "Generic" package should, after uncompression, include
the following items:
  
- MeteoInfo launcher in a shell command files called "mimap.sh" and "milab.sh" for MAC OS, Linux, Unix system.
- MeteoInfo launcher in a batch command files called "mimap.bat" and "milab.bat" for Windows system.
- MeteoInfo executable files called "MeteoInfoMap.exe" and "MeteoInfoLab.exe" for Windows system.
- MeteoInfo jar files called "MeteoInfoMap.jar" and "MeteoInfoLab.jar".
- Default MeteoInfo project file called "default.mip".
- Configure file called "config.xml" for MeteoInfo and "milconfig.xml" for MeteoInfoLab.
- Splash file called "splash.png' for MeteoInfo and "splash_mil.png" for MeteoInfoLab.
- Color map files in a folder called "colormaps".
- Image data files in a folder called "image".
- Library files in a folder called "lib".
- Map data files in a folder called "map".
- Plugin files in a folder called "plugins" for MeteoInfo.
- Jython program files in a folder called "pylib" for MeteoInfoLab.
- Sample data files in a folder called "sample".
- Synop and METAR station files in a folder called "station".
- A README file.

Running MeteoInfoMap/MeteoInfoLab
=================================

Run MeteoInfoMap:
-----------------

On Windows paltform, you can launch MeteoInfoMap by double-clicking ``MeteoInfoMap.exe`` file, 
or by run the batch command file ``mimap.bat``.

On Linux/Unix platforms, you should run MeteoInfoMap from the shell command line; 'cd' into
the directory where the above files are located and then type:

``./mimap.sh``

This will execute a one-line command in the shell file which starts
MeteoInfoMap and requests that it be allocated 1 GB of memory.

On Mac OS platform, you can launch MeteoInfoMap similar with Linux paltform but using:

``./mimap_mac.sh``

Run MeteoInfoLab:
-----------------

On Windows paltform, you can launch MeteoInfoLab by double-clicking ``MeteoInfoLab.exe`` file, 
or by run the batch command file ``milab.bat``. The batch command file with parameters will
run a Jython script:

``milab.bat test.py``

On Linux/Unix platforms, you should run MeteoInfoLab from the shell command line; 'cd' into
the directory where the above files are located and then type:

``./milab.sh``

This will execute a one-line command in the shell file which starts
MeteoInfoLab and requests that it be allocated 1 GB of memory. To run the script, type:

``./milab.sh test.py``

To run the script with headless model, a system configuration in which the display device is lacking, type:
``./milab.sh -b test.py``
It is specially useful in Unix/Linux crontab.

On Mac OS platform, you can launch MeteoInfoLab similar with Linux paltform but using:

``./milab_mac.sh``

Run MeteoInfo with more memory:
_______________________________

JVM will be started with ``Xms`` amount of memory and will be able to use a maximum of ``Xmx`` amount of memory.
For example, starting a JVM like below will start it with 128 MB of memory and will allow the process to use
up to 1 GB of memory:

``java -Xmx1G -Xms128m``

Try to increase ``Xmx`` value in the ``MeteoInfoMap`` and ``MeteoInfoLab`` starting files when you encounter
a ``java.lang.OutOfMemoryError``. In windows, you can change ``MeteoInfoMap.l4j.ini`` and ``MeteoInfoLab.l4j.ini``
files, when you staring the applications using ``MeteoInfoMap.exe`` and ``MeteoInfoLab.exe`` files.

Also the starting files of ``mimap.bat`` and ``milab.bat`` can be edited in Windows.
The corresponding files are ``mimap.sh`` and ``milab.sh`` in Linux and Unix, ``mimap_mac.sh`` and ``milab_mac.sh`` in Mac OS.

Lib files
======================

The folder called lib must remain in the same directory as the
mimap.sh application, and all the "jar" files it holds must remain
in the lib folder. These file contain the MeteoInfo application code
and (re)moving any of them will break MeteoInfo.

Contact
===================

MeteoInfo was written by Dr. Yaqiang Wang. 
Please send bug reports, etc., to:
  
  Yaqiang Wang
  
  email: yaqiang.wang@gmail.com
  
  Chinese Academy of Meteorological Sciences
  
  46 Zhong-Guan-Cun South Avenue, Beijing, China


Acknowledgment
=====================

MeteoInfo uses Java classes and libraries written by several third-party organizations.

- NetCDF Java and its dependence libraries: Available at http://www.unidata.ucar.edu/software/thredds/current/netcdf-java
- Proj4J: Available at http://trac.osgeo.org/proj4j/wiki
- Apache Common Math: Available at http://commons.apache.org/proper/commons-math
- Efficient Java Matrix Library (EJML): Available at http://ejml.org/wiki/index.php?title=Main_Page
- Apache common Imaging: Available at http://commons.apache.org/proper/commons-imaging
- Groovy: Available at http://groovy.codehaus.org
- Jython: Available at http://www.jython.org
- wContour: Available at http://www.meteothink.org
- L2FProd: Available at http://common.L2FProd.com
- RSyntaxTextArea: Available at http://bobbylight.github.io/RSyntaxTextArea
- JavaHelp: Available at https://javahelp.java.net
- BeanShell: Available at http://www.beanshell.org
- FreeHEP VectorGraphics: Available at http://java.freehep.org/vectorgraphics
- Docking Frames: Available at http://www.docking-frames.org
- JLaTeXMath: Available at https://github.com/opencollab/jlatexmath
- JTS Topology Suite: Available at https://www.locationtech.org/projects/technology.jts
- Jerry's Java Image Processing: Available at http://www.jhlabs.com/ip/index.html
- JXMapViewer: Available at https://github.com/msteiger/jxmapviewer2
- SurfacePlotter: Available at https://github.com/ericaro/surfaceplotter
- Joinery: Available at http://cardillo.github.io/joinery/v1.8/api/reference/joinery/DataFrame.html
- JOGL: Available at https://jogamp.org/jogl/www/
- FlatLaf: Available at https://www.formdev.com/flatlaf/