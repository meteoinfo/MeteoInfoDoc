.. _examples-meteoinfolab-plot_types-latex:

*******************
LaTeX
*******************

LaTeX string is supported with ``$`` at start and end, which is specific useful for writing mathematical 
formula::

    def  f(x, c):
        m1 = sin(2*pi*x)
        m2 = exp(-c*x)
        return m1 * m2
        
    x = linspace(0, 4, 100)
    sigma = 0.5
    plot(x, f(x, sigma), 'r', linewidth=2)
    xlabel(r'$\rm{time}  \  t$', fontsize=16)
    ylabel(r'$\rm{Amplitude} \ f(x)$', fontsize=16)
    title(r'$f(x) \ \rm{is \ damping  \ with} \ x$', fontsize=16)
    grid(True)
    text(2.0, 0.6, r'$f(x) = \rm{sin}(2 \pi  x^2) e^{\sigma x}$', fontsize=20)
    
.. image:: image/latex_1.png

One more example::

    x = arange(0.01, 1, 0.01)
    y = 0.5*log((1-x)/x)
    scatter(x,y,s=4,label=r'$\alpha =\frac{1}{2}\ln(\frac{1-\varepsilon}{\varepsilon })$')
    #scatter(x,y,s=4,label='Test')
    xlabel(r'$\varepsilon$',fontsize=20)
    ylabel(r'$\alpha$',fontsize=20)
    xlim(0,1)    
    legend()
    
.. image:: image/latex_2.png