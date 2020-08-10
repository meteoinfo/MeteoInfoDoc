from emips.chem_spec import Pollutant, PollutantEnum
from emips.utils import Sector, SectorEnum
from emips.spatial_alloc import GridDesc
import os
from mipylib import dataset
from mipylib import geolib

__all__ = ['dir_emission', 'emis_grid', 'grid_areas', 'get_emis_fn', 'read_emis']

dir_emission = r'S:\Data\Emission\MEIC\MEIC_2015\asc'

emis_grid = GridDesc(geolib.projinfo(), x_orig=70.125, x_cell=0.25, x_num=320,
    y_orig=10.125, y_cell=0.25, y_num=200)

#Calculate emission grid areas
grid_areas = emis_grid.grid_areas()    #square meters

def get_emis_fn(sector, pollutant, month):
    """
    Get emission file path.

    :param sector: (*Sector*) The emission sector.
    :param pollutant: (*Pollutant*) The pollutant.
    :param month: (*int*) The month.
    :returns: (*string*) Emission file path.
    """
    sector_name = sector.name.lower()
    if sector == SectorEnum.ENERGY:
        sector_name = 'power'
    elif sector == SectorEnum.TRANSPORT:
        sector_name = 'transportation'
    pollutant_name = pollutant.name.upper()
    if pollutant == PollutantEnum.PM2_5:
        pollutant_name = 'PM2.5'
    elif pollutant == PollutantEnum.NMVOC:
        pollutant_name = 'VOC'
    fn = '2015_{:0>2d}__{}__{}.asc'.format(month, sector_name, pollutant_name)
    return os.path.join(dir_emission, str(month), fn)

def read_emis(sector, pollutant, month):
    """
    Read emission data array.

    :param sector: (*Sector*) The sector.
    :param pollutant: (*Pollutant*) The pollutant.
    :param month: (*int*) The month.
    :returns: (*array*) Emission data array.
    """
    fn = get_emis_fn(sector, pollutant, month)
    f = dataset.addfile_ascii_grid(fn)
    data = f['var'][:]
    return data