.. docs-emips-meic_data-read_data:


**************************
Read data
**************************

These scripts( ``emission_meic_2015.py`` and ``emission_meic_2017.py`` ) are used to read meic emission data files.

**dir_emission**

It's corresponds to the path of the emission data file, you are supposed to change the path before use the script.

**emis_grid**

It describes the spatial distribution of the MEIC emission data.You can get more information about ``GridDesc`` function in the source code.

**grid_areas** 

The area(square meters) corresponding to the emission data.

**get_emis_fn**

The function uses four parameters ``sector``, ``month``, ``pollutant`` and ``dir_emission`` to get emission data files path. You can change the name of the parameters ``sector`` and ``pollutant`` through the judgment sentence.

**read_emis**

The function used to read emission data array and store in parameter ``data``.
