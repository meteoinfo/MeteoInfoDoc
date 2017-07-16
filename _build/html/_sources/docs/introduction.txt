.. _docs-instroduction:


*******************
Introduction
*******************

MeteoInfoMap is a GIS application which enables the user to visualize and analyze
the spatial and meteorological data with multiple data formats.
  
MeteoInfoLab is a scientific Jython development environment with the ability of 
multiple array calculation and 2D plotting.

It requires that Java 7 be installed on your computer. See the
http://www.java.com website for a free download of Java if you do not have it
already installed.
  
Publication
======================
  
- Wang, Y.Q., 2014. MeteoInfo: GIS software for meteorological data visualization and analysis. Meteorological Applications, 21: 360-368.
  
Downloading
======================

The current version of MeteoInfo, along with other information about the
application, may always be found at http://www.meteothinker.com

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

On Windows paltform, you can launch MeteoInfoMap by double-clicking "MeteoInfoMap.exe" file, 
or by run the batch command file "mimap.bat". The batch command file with parameters will
run a Jython script ("mimap.bat test.py").

On other platforms, you should run MeteoInfoMap from the shell command line; 'cd' into
the directory where the above files are located and then type:

``./mimap.sh``

This will execute a one-line command in the shell file which starts
MeteoInfoMap and requests that it be allocated 1 GB of memory. To run the script, type:

``./mimap.sh test.py``

To run the script with headless model, a system configuration in which the display device is lacking, type:
``./mimap.sh -b test.py``
It is specially useful in Unix/Linux crontab.

Run MeteoInfoLab:
On Windows paltform, you can launch MeteoInfoLab by double-clicking "MeteoInfoLab.exe" file, 
or by run the batch command file "milab.bat". The batch command file with parameters will
run a Jython script.

On other platforms, you should run MeteoInfoLab from the shell command line; 'cd' into
the directory where the above files are located and then type:

``./milab.sh``

This will execute a one-line command in the shell file which starts
MeteoInfoLab and requests that it be allocated 1 GB of memory. To run the script, type:

``./milab.sh test.py``

To run the script with headless model, a system configuration in which the display device is lacking, type:
``./milab.sh -b test.py``
It is specially useful in Unix/Linux crontab.

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
- Apache common Imaging: Available at http://commons.apache.org/proper/commons-imaging
- Groovy: Available at http://groovy.codehaus.org
- Jython: Available at http://www.jython.org
- wContour: Available at http://www.meteothinker.com
- L2FProd: Available at http://common.L2FProd.com
- RSyntaxTextArea: Available at http://bobbylight.github.io/RSyntaxTextArea
- JavaHelp: Available at https://javahelp.java.net
- BeanShell: Available at http://www.beanshell.org
- FreeHEP VectorGraphics: Available at http://java.freehep.org/vectorgraphics
- Docking Frames: Available at http://www.docking-frames.org
- JLaTeXMath: Available at https://github.com/opencollab/jlatexmath
- JTS Topology Suite: Available at https://www.locationtech.org/projects/technology.jts
- Jerry's Java Image Processing: Available at http://www.jhlabs.com/ip/index.html
- SurfacePlotter: Available at https://github.com/ericaro/surfaceplotter