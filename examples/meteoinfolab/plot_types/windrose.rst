.. _examples-meteoinfolab-plot_types-windrose:

*******************
Windrose plot
*******************

Windrose can be plotted using ``windrose`` function with wind direction and wind speed data.

::

    fn = r'D:\Temp\ascii\windrose.txt'
    ncol = numasciicol(fn)
    nrow = numasciirow(fn)
    a = asciiread(fn,shape=(nrow,ncol))
    ws=a[:,0]
    wd=a[:,1]

    n = 16
    wsbins = arange(0., 21.1, 4)
    cols = makecolors(['k','y','r','b','g'], alpha=0.7)
    rtickloc = [0.05,0.1,0.15,0.18]
    ax, bars = windrose(wd, ws, n, wsbins, rmax=0.18, colors=cols, rtickloc=rtickloc)
    colorbar(bars, shrink=0.6, vmintick=True, vmaxtick=True, xshift=10, \
        label='m/s', labelloc='bottom')
    title('Windrose example')
    
.. image:: ../../../_static/news/mi_1.4.2_lab_windrose.png