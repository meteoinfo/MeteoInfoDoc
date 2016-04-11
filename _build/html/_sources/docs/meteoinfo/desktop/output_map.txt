.. docs-meteoinfo-desktop-tools-output_map:


************************
Output Map Data
************************

This function is designed to convert selected shapes in a map layer to other format files 
which contains border data of the shapes. Following example is to create an ASCII wmf file 
with latitude/longitude border data of Xinjiang province of China.

Add and select ‘bou2_4p.shp’ layer, then select the Xinjiang shape with ‘Select Feature by 
Rectangle’ tool button.

.. image:: ../../../_static/meteoinfo/select_feature.png

Click ‘Output Map Data’ sub-menu item under ‘Tools’ menu item to open ‘Output Map Data’ dialog.

.. image:: ../../../_static/meteoinfo/output_mapdata.png

Select ‘Map Layer’ as ‘bou2_4p.shp’ and select shape index 2 (Xinjiang province). Set ‘Output 
Format’ as ‘ASCII wmp File’ and then press ‘Output’ button. Set output file name ‘Xinjiang.wmp’ 
in ‘Save As’ dialog then the border longitude/latitude data will be saved in the file.

.. image:: ../../../_static/meteoinfo/wmp_file.jpg

In the ASCII wmp file, first line is the shape type (Point, Polyline or Polygon). Second line 
is total shape number. The data of each shape were written with point number and 
longitude/latitude pairs. Longitude and latitude data were separated with comma.

wmp file could be opened in MeteoInfo as a layer.

.. image:: ../../../_static/meteoinfo/open_wmp_file.png

Because ‘Xinjiang.wmp’ is a polygon layer, it can be the mask layer.

.. image:: ../../../_static/meteoinfo/maskout_wmp_xinjiang.png