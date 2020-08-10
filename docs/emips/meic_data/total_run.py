"""
Process emission data by spatial allocation, temporal allocation
and chemical speciation.
"""

#Set current working directory
from inspect import getsourcefile
dir_run = os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))
if not dir_run in sys.path:
    sys.path.append(dir_run)

import emission_meic_2015 as emission
from emips.spatial_alloc import GridDesc

#Set year month and data path
year = 2015
month = 2
dir_inter = r'D:\run_data\emips\run_meic\inter_data\{}{:>02d}'.format(year, month)
if not os.path.exists(dir_inter):
    os.mkdir(dir_inter)

#Set emission and model grids
proj = geolib.projinfo()
model_grid = GridDesc(proj, x_orig=70., x_cell=0.15, x_num=502,
    y_orig=15., y_cell=0.15, y_num=330)

#Process emission data except VOC
print('Process emission data except VOC...')
import run_pollutants
run_pollutants.run(year, month, dir_inter, emission, model_grid)

#Process emission data of VOC
print('\n#####################################')
print('Process emission data of VOC...')
import run_VOC
run_VOC.run(year, month, dir_inter, emission, model_grid)

#Lump voc according chemical mechanism
print('\n#####################################')
print('Lump voc according chemical mechanism...')
#Using RADM2 chemical mechanism
from emips.chem_spec import RADM2
import lump_VOC
lump_VOC.run(year, month, dir_inter, RADM2(), model_grid)

#Merge all pollutant emission files in one file for each sector
print('\n#####################################')
print('merge all pollutant emission files in one file for each sector...')
import merge_sector
merge_sector.run(year, month, dir_inter, model_grid)