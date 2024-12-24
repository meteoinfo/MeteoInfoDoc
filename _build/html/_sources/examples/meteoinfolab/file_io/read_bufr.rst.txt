.. _examples-meteoinfolab-file_io-read_bufr:

***********************************
Read BURF data
***********************************

BURF data file can be opened using ``addfile()`` function. A ``obs`` variable or several root variables with ``sequence`` data type
exists in the file.

``keepopen=True`` argument should be added in ``addfile()`` function so the data could be read from the opened
file. The file object should be closed after data reading.

For sequence variable, ``variables`` and ``varnames`` properties could be used to identify internal variables.

::

    >>> obs.varnames
    [u'BYTCNT-5', u'SID-5', u'XOB-5', u'YOB-5', u'DHR-5', u'ELV-5', u'TYP-5', u'T29-5', u'TSB-5', u'ITP-5', u'SQN-5', u'PROCN-5', u'RPT-5', u'TCOR-5', u'RSRD_SEQ_RESTRICTIONS_ON_REDISTRIBUTION_SEQUENCE', u'CAT-5', u'P___INFO_PRESSURE_INFORMATION', u'Q___INFO_SPECIFIC_HUMIDITY_INFORMATION', u'T___INFO_TEMPERATURE_INFORMATION', u'Z___INFO_HEIGHT_INFORMATION', u'W___INFO_WIND_INFORMATION', u'W2_EVENT_WIND_{DIRECTION-SPEEDm-s}_EVENT_SEQUENCE', u'PMSL_SEQ_MEAN_SEA_LEVEL_PRESSURE_SEQUENCE', u'ALTIMSEQ_ALTIMETER_SETTING_SEQUENCE', u'SST_INFO_SEA_TEMPERATURE_INFORMATION', u'TOPC_SEQ_TOTAL_PRECIPITATION-TOTAL_WATER_EQUIVALENT_SEQUENCE', u'PREWXSEQ_PRESENT_WEATHER_SEQUENCE', u'CLOUDSEQ_OBSERVED_CLOUD_SEQUENCE_#_1', u'TMXMNSEQ_MAXIMUM-MINIMUM_TEMPERATURE_SEQUENCE', u'SWELLSEQ_SWELL_WAVE_SEQUENCE', u'VISB1SEQ_VISIBILITY_SEQUENCE_#_1', u'PSTWXSEQ_PAST_WEATHER_SEQUENCE', u'PKWNDSEQ_PEAK_WIND_SEQUENCE', u'GUST1SEQ_MAXIMUM_WIND_GUST_SEQUENCE_#_1', u'TPRECSEQ_TOTAL_PRECIPITATION_SEQUENCE', u'SUNSHSEQ_TOTAL_SUNSHINE_SEQUENCE', u'CLOU2SEQ_OBSERVED_CLOUD_SEQUENCE_#_2', u'SNOW_SEQ_SNOW_DEPTH_SEQUENCE', u'WAVE_SEQ_WAVE_SEQUENCE', u'PTENDSEQ_PRESSURE_TENDENCY_SEQUENCE', u'CLOU3SEQ_OBSERVED_CLOUD_SEQUENCE_#_3_CEILING', u'seq5']

Example script for reading ADPSFC station longitude, latitude and temperature data.

::

    fn = 'D:/Temp/bufr/prepbufr.gdas.20230325.t00z.nr'
    f = addfile(fn, keepopen=True)
    obs = f['ADPSFC']
    print(obs.varnames)
    lon = obs['XOB-5'][:]
    lat = obs['YOB-5'][:]
    sid = obs['SID-5'][:]
    typ = obs['TYP-5'][:]
    v = obs['T___INFO_TEMPERATURE_INFORMATION']
    vv = v['T__EVENT_TEMPERATURE_EVENT_SEQUENCE']
    vvv = vv['TOB-5']
    data = vvv[0]
    f.close()

    #Plot
    axesm()
    geoshow('country')
    levs = arange(-20, 41, 5)
    layer = scatter(lon, lat, data, levs, size=2, edgecolor=None, zorder=0)
    colorbar(layer)
    title('Bufr data example')
    
.. image:: ../../../_static/prepbufr_adpsfc.png

Example script for reading SATWND station longitude, latitude and pressure data.

::

    fn = 'D:/Temp/bufr/prepbufr.gdas.20230325.t00z.nr'
    f = addfile(fn, keepopen=True)
    obs = f['SATWND']
    print(obs.varnames)
    lon = obs['XOB-3'][:]
    lat = obs['YOB-3'][:]
    sid = obs['SID-3'][:]
    typ = obs['TYP-3'][:]
    v = obs['P___INFO_PRESSURE_INFORMATION']
    vv = v['P__EVENT_PRESSURE_EVENT_SEQUENCE']
    vvv = vv['POB-3']
    data = vvv[0]
    f.close()

    #Plot
    axesm()
    geoshow('country')
    layer = scatter(lon, lat, data, size=2, edgecolor=None, zorder=0)
    colorbar(layer)
    title('Bufr data example')

.. image:: ../../../_static/prepbufr_satwnd.png