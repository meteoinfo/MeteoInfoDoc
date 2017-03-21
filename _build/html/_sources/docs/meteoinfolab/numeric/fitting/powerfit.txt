.. _docs-meteoinfolab-numeric-fitting-powerfit:


**********
powerfit
**********

.. currentmodule:: numeric.fitting

.. function:: powerfit(x, y, func=False)

    Power law fitting.
    
    :param x: (*array_like*) x data array.
    :param y: (*array_like*) y data array.
    :param func: (*boolean*) Return fit function (for predict function) or not. Default is ``False``.
    
    :returns: Fitting parameters and function (optional).
    
    Examples::
    
        from mipylib.numeric import fitting

        fn = 'D:/Temp/ascii/PM&vis-1.txt'
        ncol = numasciicol(fn)
        nrow = numasciirow(fn)
        a = asciiread(fn,shape=(nrow,ncol))
        x=a[:,0]
        y=a[:,1]
        z=a[:,2]
        axes(tickfontsize=17)
        ls=scatter(x,y,s=8,c=z,cmap='NCV_jet',edgecolor=None,cnum=20)
        xlim(0,450)
        ylim(0,30)
        xlabel(r'$\rm{PM_{2.5}} \ (\mu g \ m^{-3})$',fontsize=17)
        ylabel(r'$\rm{Visibility (km)}$',fontname='Arial',fontsize=17) 
        colorbar(ls,fontsize=17,label='RH(%)')

        #Pow law fitting
        a,b,r,f = fitting.powerfit(x, y, func=True)

        #Plot fitting line
        xx = linspace(x.min(), x.max(), 100)
        #yy = a*pow(xx, b)
        yy = fitting.predict(f, xx)
        plot(xx, yy, '-b', linewidth=2)
        text(250, 20, r'$y = ' + '%.4f' % a + 'x^{%.4f' % b + '}$', fontsize=16)
        text(250, 18, r'$r^2=%.4f' % r + '$', fontsize=16)
        
.. image:: ../../../../_static/powerfit.png