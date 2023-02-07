.. docs-meteoinfo-desktop-geo_map_data:


************************
Geographic Map Data
************************

The following geographic map data were supported by MeteoInfo.

- ESRI shape file with point, polyline or polygon shape type.
- Geographic map data of GrADS.
- wmf map data. (Can be created by ‘Output Map Data’ function in MeteoInfo)
- Web map tile images.

A shapefile is a digital vector storage format for storing geometric location and associated 
attribute information. This format lacks the capacity to store topological information. 
Shapefiles are simple because they store primitive geometrical data types of points, lines, 
and polygons. These primitives are of limited use without any attributes to specify what they 
represent. Therefore, a table of records will store properties/attributes for each primitive 
shape in the shapefile. Shapes (points/lines/polygons) together with data attributes can create 
infinitely many representations about geographical data. Representation provides the ability 
for powerful and accurate computations.

While the term "shapefile" is quite common, a "shapefile" is actually a set of several files. 
Three individual files are mandatory to store the core data that comprises a shapefile: ".shp", 
".shx", ".dbf", and other extensions on a common prefix name (e.g., "lakes.*"). The actual 
shapefile relates specifically to files with the ".shp" extension, but alone is incomplete for 
distribution, as the other supporting files are required.

Some resources for freely available shapefiles are: 

- `National Weather Service Shapefile Database <http://www.weather.gov/geodata/>`_
- `National Atlas <http://www.nationalatlas.gov/atlasftp.html>`_
- `DIVA-GIS <http://www.diva-gis.org/Data>`_