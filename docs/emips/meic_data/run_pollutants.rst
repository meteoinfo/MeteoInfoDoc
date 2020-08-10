.. docs-emips-meic_data-run_pollutants:


************************************
Process emission data except VOC
************************************

This script is used to process emission data (except VOC) by spatial allocation, temporal allocation and chemical speciation. The main part of the script is ``run()`` function with five parameters ``year``, ``month``, ``dir_inter`` , ``emission``  and ``model_grid`` .You are supposed to check these parameters before running the script.

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

**spec_profile_fn**

Species allocation profile file

**spec_ref_fn**

Species allocation reference file

**dims**

It describes the spatial and temporal distribution of the output emission data.

**sectors**

Enumeration of all sectors, including industry, agriculture, energy, residential and transport.

**pollutant**

Enumeration of all pollutants except VOC.

**out_species**

Output sepcies

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
