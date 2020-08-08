.. docs-emips-meic_data-merge_sector:


********************************************************
Merge emission data according sectors
********************************************************

This script is used to merge all pollutant emission files in one file for each sector. The main part of the script is ``run()`` function with four parameters ``year``, ``month``, ``dir_inter`` and ``model_grid``. You are supposed to check these parameters before running the script.

**year, month**

Year and month in file name.

**dir_inter**

Data input and output directory.

**model_grid**

Grid describe of the output emission data.

**sectors**

Enumeration of all sectors, including industry, agriculture, energy, residential and transport.

**pollutants**

Enumeration of all pollutants.

**dims**

It describes the spatial and temporal distribution of the output emission data.

**outfn**

Output sector emission file name

**gattrs**

Global attribute

**proj**

Projection method
