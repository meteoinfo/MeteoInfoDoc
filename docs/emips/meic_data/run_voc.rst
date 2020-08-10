.. docs-emips-meic_data-run_voc:


******************************
Process emission data of VOC
******************************

This script is used to process VOC emission data by spatial allocation, temporal allocation and chemical speciation. The main part of the script is ``run()`` function with five parameters ``year``, ``month`` , ``dir_inter`` , ``emission`` and ``model_grid`` . You are supposed to check these parameters before running the script.

**year, month**

Year and month in file name.

**dir_inter**

Data output directory.

**emission**

You need to import the appropriate ``read_data`` module as ``emission``.

**model_grid**

Grid describe of the output emission data.

**temp_profile_fn**

Temporal allocation profile file

**temp_ref_fn**

Temporal allocation reference file

**dims**

It describes the spatial and temporal distribution of the output emission data.

**sectors**

Enumeration of all sectors, including industry, agriculture, energy, residential and transport.

**fn_sectors**

Abbreviation sectors in file name

**pollutant**

NMVOC pollutants

**scc**

Source classification code

**emis_data**

Emission data

**outfn**

Output file name

**gattrs**

Global attribute

**proj**
Projection method

