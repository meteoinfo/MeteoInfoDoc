.. _projects-emips_features:


*******************
EMIPS
*******************

Introduction:
------------------------------------
EMIPS (EMission Inventory Processing System) software was developed to create model used emission inventory (EI) 
data from two kinds of data sources: basic emission dataset (including activity levels, emission factors data 
and so on) and gridded emission dataset products. 

The basic emission dataset was organized using MySQL database, then the point and area sources EI can be calculated 
from it. The functions of chemical speciation, spatial allocation and temporal allocation are included in EMIPS to 
generate model used gridded EI data. EMIPS was developed using Java with cross-platform ability and friendly GUI. 
MeteoInfo library was used to implement GIS functions such as spatial allocation and projection transformation. 
Jython script was supported for automatic and batch run.


Main functions:
------------------------------
  - Create emission inventory: Database (MySQL): emission activity and emission factors; Data input, editing, inquiring and EI calculation (point, area and mobile sources).
  - Emission inventory data process:  Chemical speciation, Temporal allocation, Spatial allocation (projection conversion).

Characters：
--------------------------------
  - Developed using Java with cross-platform ability.
  - GUI, MySQL database. 
  - GIS functions based on MeteoInfo library for spatial allocation and projection conversion.
  - Jython script for batch running.
  

Screen shots:
-------------------
.. image:: emips_image/emips_frame.png
   :scale: 50
.. image:: emips_image/emips_gui.png
   :scale: 50
.. image:: emips_image/database_view.png
   :scale: 50
.. image:: emips_image/ei_cal.png
   :scale: 50
.. image:: emips_image/emips_run.png
   :scale: 50