.. _docs-meteoinfolab-meteolib-meteo-qair2rh:


*********************************
qair2rh
*********************************

.. currentmodule:: mipylib.meteolib.meteo

.. function:: qair2rh(qair, temp, press=1013.25)

    Specific humidity to relative humidity
        
    qair: DimArray or MIArray or number 
        Specific humidity - dimensionless (e.g. kg/kg) ratio of water mass / total air mass
    temp: DimArray or MIArray or number
        Temperature - degree c
    press: DimArray or MIArray or number
        Pressure - hPa (mb)
    
    return: DimArray or MIArray or number
        Relative humidity - %