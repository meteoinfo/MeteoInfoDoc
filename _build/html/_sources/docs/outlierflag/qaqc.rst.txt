.. _docs-outlierflag-qaqc:


*******************
qaqc Jython module
*******************

.. function:: timeorder(data, stime, etime, tdelta, tunit)

    Time order of the table data.
    
    :param data: (*TimeTableData*) Original data.
    :param stime: (*datetime*) Start datetime.
    :param etime: (*datetime*) End datetime.
    :param tdelta: (*int*) Time delta value.
    :param tunit: (*string*) Time delta unit. [year|month|day|hour|minute].
    
    :returns: Result table data.
    
.. function:: flagset(minlim=-10000, maxlim=50000, errornum=11, quantilenum=21, quantil=0.9, factor=2.3, stdnum=29, stdfactor=3)

    Create flag setting object.
    
    :param minlim: (*float*) Minimum limitation.
    :param maxlim: (*float*) Maximum limitation.
    :param errornum: (*int*) Error point number.
    :param quantilenum: (*int*) Quantile point number.
    :param quantil: (*float*) Quantile value.
    :param factor: (*float*) Factor value.
    :param stdnum: (*int*) Standard deviation point number.
    :param stdfactor: (*float*) Standard deviation factor value.
    
    :returns: Flag setting object.
    
.. function:: check_lim(data, fset)

    Check limitation - Get flag code list according to min/max limitation setting.
    
    :param data: (*array*) Input data array.
    :param fset: (*FlagSetting*) FlagSetting.
    
    :returns: (*list of string*) Flag code list.
    
.. function:: check_error(data, fset, fcodes)

    Check error - Set flag code list according to error setting.
    
    :param data: (*array*) Input data array.
    :param fset: (*FlagSetting*) FlagSetting.
    :param fcodes: (*list of sting*) Flag code list.
    
.. function:: check_std(data, fset, fcodes)

    Check 3 times of standard deviation - Set flag code list according to standard deviation setting.
    
    :param data: (*array*) Input data array.
    :param fset: (*FlagSetting*) FlagSetting.
    :param fcodes: (*list of sting*) Flag code list.
    
.. function:: check_all(data, fset)

    Check all 3 steps.
    
    :param data: (*array*) Input data array.
    :param fset: (*FlagSetting*) FlagSetting.
    
    :returns: (*list of string*) Flag code list.
    
.. function:: makecolors(fcodes, c=None)

    Make colors according to flag codes.
    
    :param fcodes: (*list of string*) Flag code list.
    :param c: (*list of color*) Option colors for flag types.
    
    :returns: (*list of color*) Colors with the length as same as fcodes.
    
.. function:: makearray(fcodes, v=None)

    Make array according to flag codes.
    
    :param fcodes: (*list of string*) Flag code list.
    :param v: (*list of float*) Option values for flag types.
    
    :returns: (*array_like*) Array with the length as same as fcodes.
    
.. function:: flagchart(data, fcodes, dates=None, title='Flag chart')

    Open a flag chart form for mannual flagging.
    
    :param data: (*array_like*) Data array.
    :param fcodes: (*list of string*) Flag code list.
    :param dates: (*list of datetime*) X datetime data.
    :param title: (*string*) Chart title.
    
    :returns: (*list of string*) Result flag code list.
    
.. function:: bc_loading_effect(bc, atn, avenum=4, refine=True, smooth=True, smoothnum=10)

    Black carbon loading effect compensation.
    
    :param bc: (*array*) Black carbon data array.
    :param atn: (*array*) Attenuation data array.
    :param avenum: (*int*) Point number used for average in compensation parameter calculation.
        Default is `4`.
    :param refine: (*boolean*) Is refine compensation paramter or not. Default is `True`.
    :param smooth: (*boolean*) Is smooth compensation paramter or not. Default is `True`.
    :param smoothnum: (*int*) Point number used for smooth. Default is `10`.
    
    :returns: Compensated BC data array and compensation parameters