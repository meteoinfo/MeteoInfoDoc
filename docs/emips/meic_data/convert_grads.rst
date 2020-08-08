.. docs-emips-meic_data-convert_grads:


**********************************************
Convert NetCDF data to GrADS data 
**********************************************

This script is used to convert NetCDF model-ready emission files to GrADS format files for
CUACE model.

**emis_cuace**

Sectors are divided into four categories including ``low`` (agriculture, residential, transport, ships), ``poi`` (industry), ``pow`` (energy) and ``air`` (air), you are supposed to check the sectors in emission inventory files and add sector included in the four emission categories(or remove sector that are not included). 

**all_species**

All species included in RADM2 chemical mechanism.

**year, month**

Year and month in file name.

**dir_data**

File input and output directory.

**xn, yn, tn**

Dimension length of nc files. In this script, we loop ``tn`` and accumulate emissions data to convert hourly data to daily data.

**outfn**

Output file's name

**outer**

Output file

**data**

Daily data of a certain specie


