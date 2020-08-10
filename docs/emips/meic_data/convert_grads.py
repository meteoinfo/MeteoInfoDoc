"""
Convert netcdf model-ready emission file to GrADS data format for
GRAPES/CUACE model
"""

#Import from emips package
import emips
from emips.utils import Sector, SectorEnum
from emips.spatial_alloc import GridDesc
from emips.chem_spec import RADM2

#Set emission low, poi, pow
emis_cuace = {}
emis_cuace['low'] = [SectorEnum.AGRICULTURE, SectorEnum.RESIDENTIAL, \
    SectorEnum.TRANSPORT, SectorEnum.SHIPS]
emis_cuace['poi'] = [SectorEnum.INDUSTRY]
emis_cuace['pow'] = [SectorEnum.ENERGY]
emis_cuace['air'] = [SectorEnum.AIR]

#Get RADM2 emission species
all_species = [RADM2.CO, RADM2.NO, RADM2.NO2, RADM2.ALD, RADM2.CH4, \
    RADM2.CSL, RADM2.ETH, RADM2.HC3, RADM2.HC5, RADM2.HC8, RADM2.HCHO, \
    RADM2.ISOP, RADM2.KET, RADM2.NR, RADM2.OL2, RADM2.OLE, RADM2.OLI, \
    RADM2.OLT, RADM2.ORA2, RADM2.PAR, RADM2.TERP, RADM2.TOL, RADM2.XYL, \
    RADM2.NH3, RADM2.SO2, RADM2.SULF, RADM2.PEC, RADM2.PMFINE, \
    RADM2.PNO3, RADM2.POA, RADM2.PSO4, RADM2.PMC]

#Set year month
year = 2015
month = 2
#Set directory
dir_data = r'D:\run_data\emips\run_merge\output'
dir_data = os.path.join(dir_data, '{}{:>02d}'.format(year, month))

#Set dimension length
xn = 502
yn = 330
tn = 25    # 0 - 24 hour

#Loop
for emis_type, sectors in emis_cuace.iteritems():
    print(emis_type)
    
    #set output binary dta file
    outfn = os.path.join(dir_data, 'emis_{}_{}_{}.grd'.format(year, \
        month, emis_type))
    outer = bincreate(outfn)

    #Loop time number
    for t in range(tn):
        print('Time number: {}'.format(t))
        if t == tn - 1:
            t = 0
        #Loop species
        for species in all_species:
            #print(species)
            data = None
            #Loop sectors
            for sector in sectors:
                fn = os.path.join(dir_data, 'emis_{}_{}_{}_hour.nc'.format(sector.name, year, month))
                #print('\t{}'.format(fn))
                f = addfile(fn)
                if species.name in f.varnames():
                    dd = f[species.name][t]
                    if dd.sum() == 0:
                        continue
                    if data is None:
                        data = dd
                    else:
                        data = data + dd
            if data is None:
                #print('Is None: {}'.format(species))
                data = zeros((yn, xn))
            else:
                data[data==np.nan] = 0    #turn nan to 0
            binwrite(outer, data.astype('float'), byteorder='big_endian', sequential=True)
    outer.close()

print('Finish!')
