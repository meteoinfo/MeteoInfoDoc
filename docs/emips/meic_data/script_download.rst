.. docs-emips-meic_data-script_download:


************************************
Scripts download and Introduction
************************************

In this example, we convert Network Common Data Form (NetCDF) and ASCII format data files to GrADS format files, to achieve the input requirements of the CMA Unified Atmospheric Chemistry Environment (CUACE) model. The processiong scripts and related information are below (Scripts need to be run in the MeteoInfolab) .

- `read_data(asc) <emission_meic_2015.py>`_
- `read_data(NetCDF) <emission_meic_2017.py>`_
 Read emission data in asc and nc formats respectively.

- `run_pollutants <run_pollutants.py>`_
 Process pollutants emission data by spatial allocation, temporal allocation and chemical speciation (VOC is not included in this script) .

- `run_VOC <run_VOC.py>`_
 Process VOC emission data by spatial allocation, temporal allocation and chemical speciation (No consideration of chemical mechanism) .

- `lump_VOC <lump_VOC.py>`_
 Lump VOC species according chemical mechanism.

- `merge_sector <merge_sector.py>`_
 Merge all pollutants emission files in one file for each sector.

- `total_run <total_run.py>`_
 Import and run the scripts above.

- `convert_grads <convert_grads.py>`_
 Convert NetCDF model-ready emission data files to GrADS format data files for CUACE model.

**Attention: The file paths in scripts should be modified correctly before use.**
