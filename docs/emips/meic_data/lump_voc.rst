.. docs-emips-meic_data-lump_voc:


****************************************
Lump VOC according chemical mechanism
****************************************

This script is used to lump VOC species according RADM2 chemical mechanism. The main part of the script is ``run()`` function with five parameters ``year``, ``month``, ``dir_inter``, ``chem_mech`` and ``model_grid``. You are supposed to check these parameters before running the script.

**year, month**

Year and month in file name.

**dir_inter**

Data input and output directory.

**chem_mech**

Chemical mechanism module, RADM2 is used in this script.

**model_grid**

Grid describe of the output emission data.

**sectors**

Enumeration of all sectors, including industry, agriculture, energy, residential and transport.

**pollutant**

NMVOC pollutants

**dims**

It describes the spatial and temporal distribution of the output emission data.

**infn**

Input files name

**outfn**

Output file name

**gattrs**

Global attribute

**RADM2**

Chemical mechanism used in script processing.

**proj**
Projection method

