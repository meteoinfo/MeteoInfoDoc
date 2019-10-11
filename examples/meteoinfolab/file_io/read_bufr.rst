.. _examples-meteoinfolab-file_io-read_bufr:

***********************************
Read BURF data
***********************************

BURF data file can be opened using ``addfile()`` function. Only ``obs`` variable exists in the file.
The variable can be read as ArraySequence, then StructureDataIterator was used to read the data
from its StructureMembers. The members can viewed in console.

``keepopen=True`` argument should be added in ``addfile()`` function so the data could be read from opened
file. The file object should be closed after data reading.

::

    >>> data.members
    [CLOUD_INDEX, CLOUD_AMOUNT_IN_SEGMENT-2, CLOUD_PHASE, TEMPERATURE_AIR_TEMPERATURE, PRESSURE]

Example script

::

    fn = 'D:/Temp/bufr/MSG3-SEVI-MSGCLAP-0000-0000-20150101004500.000000000Z-20150101005935-1187380.bfr'
    f = addfile(fn, keepopen=True)
    d = f['obs'].read().array
    iter1 = d.getStructureDataIterator()
    if iter1.hasNext():
        data = iter1.next()
    iter1.finish()
    mlon = data.findMember('LONGITUDE_(HIGH_ACCURACY)')
    mlat = data.findMember('LATITUDE_(HIGH_ACCURACY)')
    lon = (array(mlon.dataArray).astype('float') - 1.8E7) * 1.E-5
    lat = (array(mlat.dataArray).astype('float') - 9.E6) * 1.E-5
    struct1 = data.getArray('struct1')
    iter1 = struct1.getStructureDataIterator()
    if iter1.hasNext():
        data = iter1.next()
    iter1.finish()
    mtemp = data.findMember('TEMPERATURE_AIR_TEMPERATURE')
    temp = array(mtemp.dataArray).astype('float') * 0.1
    temp = temp[:,0]
    f.close()

    #Plot
    axesm()
    geoshow('country', edgecolor='k', facecolor=(204,255,204))
    layer = scatterm(lon, lat, temp, size=4, edge=False)
    colorbar(layer)
    xlim(-50, 0)
    ylim(10, 40)
    title('Bufr data example')
    
.. image:: ../../../_static/bufr_1.png