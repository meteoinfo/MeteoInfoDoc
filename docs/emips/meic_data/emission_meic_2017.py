from emips.chem_spec import Pollutant, PollutantEnum
from emips.utils import Sector, SectorEnum
from emips.spatial_alloc import GridDesc
import os
from mipylib.dataset import addfile
from mipylib import geolib

__all__ = ['dir_emission', 'emis_grid', 'grid_areas', 'get_emis_fn', 'read_emis']

dir_emission = 'D:/KeyData/Emission/MEIC/2017/nc'

emis_grid = GridDesc(geolib.projinfo(), x_orig=70.05, x_cell=0.1, x_num=800,
    y_orig=10.05, y_cell=0.1, y_num=500)

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
        pollutant_name = 'PM25'
    elif pollutant == PollutantEnum.NMVOC:
        pollutant_name = 'VOC'
    fn = 'meic-2017_%i_%s-%s.nc' % (month, sector_name, pollutant_name)
    return os.path.join(dir_emission, fn)

def read_emis(sector, pollutant, month):
    """
    Read emission data array.

    :param sector: (*Sector*) The sector.
    :param pollutant: (*Pollutant*) The pollutant.
    :param month: (*int*) The month.
    :returns: (*array*) Emission data array.
    """
    fn = get_emis_fn(sector, pollutant, month)
    f = addfile(fn)
    data = f['z'][:]
    nx = 800
    ny = 500
    data = data.reshape(ny, nx)
    data = data[::-1,:]
    return data