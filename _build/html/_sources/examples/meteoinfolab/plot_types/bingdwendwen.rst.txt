.. _examples-meteoinfolab-plot_types-bingdwendwen:

*******************
Plot Bing Dwen Dwen
*******************

Plot Bing Dwen Dwen.

::

    # Ellipse data calculation function, enter the covariance matrix, center point,
    # radius to generate ellipse data
    def getEllipse(Mu, Sigma, S, pntNum):
        # (X-Mu)*inv(Sigma)*(X-Mu) = S
        Mu = array(Mu)
        Sigma = array(Sigma)
        invSig = linalg.inv(Sigma)

        D, V = linalg.eig(invSig)
        aa = sqrt(S / D[0])
        bb = sqrt(S / D[1])

        t = linspace(0, 2*pi, pntNum)
        XY = dot(V, vstack([aa*cos(t), bb*sin(t)]))
        X=(XY[0,:] + Mu[0]).T
        Y=(XY[1,:] + Mu[1]).T
        return X, Y

    ############################################################
    antialias(True)
    ax = axes(aspect='equal', axis=False)
    xlim(-5, 5)
    ylim(-5, 5)

    # Draw the rock sugar shell
    X, Y = getEllipse([0,0], [[1,0],[0,1.3]], 3.17**2, 200)
    plot(X, Y, color=[57,57,57], linewidth=1.8)

    X, Y = getEllipse([1.7,2.6], [[1.2,0],[0,1.8]], .65**2, 200)
    plot(X, Y, color=[57,57,57], linewidth=1.8)
    plot(-X, Y, color=[57,57,57], linewidth=1.8)
    X, Y = getEllipse([1.7,2.6], [[1.2,0],[0,1.8]], .6**2, 200)
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)
    fill(-X, Y, facecolor='w', edgecolor='w', linewidth=1.8)

    X, Y = getEllipse([-3.5,-1], [[1.1,.3],[.3,1.1]], .75**2, 200)
    plot(X, Y, color=[57,57,57], linewidth=1.8)
    X, Y = getEllipse([-3.5,-1], [[1.1,.3],[.3,1.1]], .68**2, 200)
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)
    X, Y = getEllipse([3.5,1], [[1.1,.3],[.3,1.1]], .75**2, 200)
    plot(X, Y, color=[57,57,57], linewidth=1.8)
    X, Y = getEllipse([3.5,1], [[1.1,.3],[.3,1.1]], .68**2, 200)
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)

    X = array([-3.8,-2,-3])
    Y = array([-.51+.13,1+.13,-1])
    plot(X, Y, color=[57,57,57], linewidth=1.8)
    plot(-X, -Y, color=[57,57,57], linewidth=1.8)
    X = array([-3.8,-2,-3])
    Y = array([-.51+.03,1+.03,-1])
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)
    fill(-X, -Y, facecolor='w', edgecolor='w', linewidth=1.8)

    X, Y = getEllipse([0,-.1], [[1,0],[0,1.6]], .9**2, 200)
    Y[Y<0] = Y[Y<0]*.2
    Y = Y - 4.2
    X = X - 1.2
    plot(X, Y, color=[57,57,57], linewidth=2)
    plot(-X, Y, color=[57,57,57], linewidth=2)
    rectangle([-2.1, -4.2, 1.7, 3], curvature=0.4, facecolor='w',
        edgecolor=[57,57,57], linewidth=1.8)
    rectangle([2.1-1.7, -4.2, 1.7, 3], curvature=0.4, facecolor='w',
        edgecolor=[57,57,57], linewidth=1.8)
    X, Y = getEllipse([0,-.1], [[1,0],[0,1.6]], .8**2, 200)
    Y[Y<0] = Y[Y<0] * .2
    Y = Y - 4.1
    X = X - 1.2
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)
    fill(-X, Y, facecolor='w', edgecolor='w', linewidth=1.8)

    X, Y = getEllipse([0,0], [[1,0],[0,1.3]], 3.1**2, 200)
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)

    ######################################################
    # Ears
    X, Y = getEllipse([1.7,2.6], [[1.2,0],[0,1.8]], .5**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    fill(-X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)

    # Arms
    X, Y = getEllipse([-3.5,-1], [[1.1,.3],[.3,1.1]], .6**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    X, Y = getEllipse([3.5,1], [[1.1,.3],[.3,1.1]], .6**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    X = array([-3.8,-2,-3])
    Y = array([-.51,1,-1])
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57])
    fill(-X, -Y, facecolor=[57,57,57], edgecolor=[57,57,57])
    tt = linspace(-2.9, 2.9, 1000)
    X = 16*(sin(tt))**3
    Y = 13*cos(tt)-5*cos(2*tt)-2*cos(3*tt)-cos(4*tt)
    X = X*.018+3.6
    Y = Y*.018+1.1
    fill(X, Y, facecolor=[180,39,45], edgecolor=[180,39,45], linewidth=2)

    # Legs
    X, Y = getEllipse([0,-.1], [[1,0],[0,1.6]], .7**2, 200)
    Y[Y<0] = Y[Y<0] * .2
    Y = Y - 4.1
    X = X - 1.2
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    fill(-X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    rectangle([-1.95, -4.3, 1.4, 3], curvature=0.4, facecolor=[57,57,57],
        edgecolor=[57,57,57])
    rectangle([1.95-1.4, -4.3, 1.4, 3],curvature=0.4, facecolor=[57,57,57],
        edgecolor=[57,57,57])

    # Body
    X, Y = getEllipse([0,0], [[1,0],[0,1.3]], 3**2, 200)
    fill(X, Y, facecolor='w', edgecolor=[57,57,57], linewidth=2.5)

    # Five rings
    cList = [[132,199,114],[251,184,77],[89,120,177],[158,48,87],[98,205,247]]
    for i in range(5):
        X, Y = getEllipse([0,0], [[1.6,0],[0,1.3]], (2.05-0.05*(i+1))**2, 200)
        Y[Y<0] = Y[Y<0] * .8
        Y = Y + .5
        fill(X, Y, facecolor='w', edgecolor=cList[i], linewidth=2.5)

    # Eyes
    X, Y = getEllipse([1.2,1.2], [[1.2,-.5],[-.5,1.1]], .65**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    fill(-X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    X, Y = getEllipse([.95,1.3], [[1,0],[0,1]], .35**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor='w', linewidth=1.6)
    fill(-X, Y, facecolor=[57,57,57], edgecolor='w', linewidth=1.6)
    X, Y = getEllipse([.95,1.3], [[1,0],[0,1]], .1**2, 200)
    fill(X + .18, Y, facecolor='w', edgecolor=[57,57,57], linewidth=.5)
    fill(-X + .18, Y, facecolor='w', edgecolor=[57,57,57], linewidth=.5)

    # Mouth
    X, Y = getEllipse([0.05,.2], [[1.2,.15],[.15,.8]], .69**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    X, Y = getEllipse([0,.75], [[1,0.2],[0.2,.3]], .4**2, 200)
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=2)
    X, Y = getEllipse([0,0], [[.8,0],[0,.2]], .6**2, 200)
    fill(X, Y, facecolor=[180,39,45], edgecolor=[180,39,45], linewidth=2)

    # Nose
    X, Y = getEllipse([0,-.1], [[1,0],[0,1.6]], .2**2, 200)
    Y[Y<0] = Y[Y<0] * .2
    Y = -Y + .9
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)

    ##################################################################
    # Winter Olympic symbol and five rings
    # Five rings
    tt = linspace(0, 2*pi, 100)
    X = cos(tt) * .14
    Y = sin(tt) * .14
    plot(X, Y-2.8, color=[57,57,57], linewidth=1.2)
    plot(X-.3, Y-2.8, color=[106,201,245], linewidth=1.2)
    plot(X+.3, Y-2.8, color=[155,79,87], linewidth=1.2)
    plot(X-.15, Y-2.9, color=[236,197,107], linewidth=1.2)
    plot(X+.15, Y-2.9, color=[126,159,101], linewidth=1.2)

    # Text
    text(0, -2.4, 'BEIJING 2022', xalign='center', fontsize=8,
        fontname='Comic Sans MS')

    # Symbol
    fill([.1,-.12,-.08], array([0,0-0.05,-0.15])-1.5, facecolor=[98,118,163], edgecolor=[98,118,163])
    fill([-.08,-.35,.1], array([-0.1,-.2,-.1])-1.6, facecolor=[98,118,163], edgecolor=[98,118,163])
    fill([-.08,-.08,.1,.1], array([-0.1,-0.15,-.2,-.15])-1.5, facecolor=[192,15,45], edgecolor=[192,15,45])
    plot(array([-.35,-.3,-.25,-.2,-.15,-.1,-.05,.1])+.02,
         array([0,.02,.04,.06,.04,.02,0,.02])-1.82, color=[120,196,219], lLinewidth=1.8)
    plot(array([-.33,.05])+.02, array([0,-.08])-1.82, color=[190,215,84], linewidth=1.8)
    plot(array([.05,-.2])+.02, array([-.08,-.15])-1.82, color=[32,162,218], linewidth=1.8)
    plot(array([-.2,.05])+.02, array([-.15,-.2])-1.82, color=[99,118,151], linewidth=1.8)
    
.. image:: ../../../_static/bingdwendwen.png

Plot Bing Dwen Dwen with animation.

::

    import time

    # Ellipse data calculation function, enter the covariance matrix, center point,
    # radius to generate ellipse data
    def getEllipse(Mu, Sigma, S, pntNum):
        # (X-Mu)*inv(Sigma)*(X-Mu) = S
        Mu = array(Mu)
        Sigma = array(Sigma)
        invSig = linalg.inv(Sigma)

        D, V = linalg.eig(invSig)
        aa = sqrt(S / D[0])
        bb = sqrt(S / D[1])

        t = linspace(0, 2*pi, pntNum)
        XY = dot(V, vstack([aa*cos(t), bb*sin(t)]))
        X=(XY[0,:] + Mu[0]).T
        Y=(XY[1,:] + Mu[1]).T
        return X, Y

    ############################################################
    mipylib.plotlib.miplot.isinteractive = True
    clf()
    antialias(True)
    ax = axes(aspect='equal', axis=False)
    xlim(-4.5, 4.5)
    ylim(-4.5, 4.5)

    # Draw the rock sugar shell
    X, Y = getEllipse([0,0], [[1,0],[0,1.3]], 3.17**2, 200)
    plot(X, Y, color=[57,57,57], linewidth=1.8)

    X, Y = getEllipse([1.7,2.6], [[1.2,0],[0,1.8]], .65**2, 200)
    plot(X, Y, color=[57,57,57], linewidth=1.8)
    plot(-X, Y, color=[57,57,57], linewidth=1.8)
    X, Y = getEllipse([1.7,2.6], [[1.2,0],[0,1.8]], .6**2, 200)
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)
    fill(-X, Y, facecolor='w', edgecolor='w', linewidth=1.8)

    X, Y = getEllipse([-3.5,-1], [[1.1,.3],[.3,1.1]], .75**2, 200)
    plot(X, Y, color=[57,57,57], linewidth=1.8)
    X, Y = getEllipse([-3.5,-1], [[1.1,.3],[.3,1.1]], .68**2, 200)
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)
    X, Y = getEllipse([3.5,1], [[1.1,.3],[.3,1.1]], .75**2, 200)
    plot(X, Y, color=[57,57,57], linewidth=1.8)
    X, Y = getEllipse([3.5,1], [[1.1,.3],[.3,1.1]], .68**2, 200)
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)

    X = array([-3.8,-2,-3])
    Y = array([-.51+.13,1+.13,-1])
    plot(X, Y, color=[57,57,57], linewidth=1.8)
    plot(-X, -Y, color=[57,57,57], linewidth=1.8)
    X = array([-3.8,-2,-3])
    Y = array([-.51+.03,1+.03,-1])
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)
    fill(-X, -Y, facecolor='w', edgecolor='w', linewidth=1.8)

    X, Y = getEllipse([0,-.1], [[1,0],[0,1.6]], .9**2, 200)
    Y[Y<0] = Y[Y<0]*.2
    Y = Y - 4.2
    X = X - 1.2
    plot(X, Y, color=[57,57,57], linewidth=2)
    plot(-X, Y, color=[57,57,57], linewidth=2)
    rectangle([-2.1, -4.2, 1.7, 3], curvature=0.4, facecolor='w',
        edgecolor=[57,57,57], linewidth=1.8)
    rectangle([2.1-1.7, -4.2, 1.7, 3], curvature=0.4, facecolor='w',
        edgecolor=[57,57,57], linewidth=1.8)
    X, Y = getEllipse([0,-.1], [[1,0],[0,1.6]], .8**2, 200)
    Y[Y<0] = Y[Y<0] * .2
    Y = Y - 4.1
    X = X - 1.2
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)
    fill(-X, Y, facecolor='w', edgecolor='w', linewidth=1.8)

    X, Y = getEllipse([0,0], [[1,0],[0,1.3]], 3.1**2, 200)
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=1.8)
    time.sleep(.5)

    ######################################################
    # Ears
    X, Y = getEllipse([1.7,2.6], [[1.2,0],[0,1.8]], .5**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    fill(-X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    time.sleep(.5)

    # Arms
    X, Y = getEllipse([-3.5,-1], [[1.1,.3],[.3,1.1]], .6**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    X, Y = getEllipse([3.5,1], [[1.1,.3],[.3,1.1]], .6**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    X = array([-3.8,-2,-3])
    Y = array([-.51,1,-1])
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57])
    fill(-X, -Y, facecolor=[57,57,57], edgecolor=[57,57,57])
    time.sleep(.5)
    tt = linspace(-2.9, 2.9, 1000)
    X = 16*(sin(tt))**3
    Y = 13*cos(tt)-5*cos(2*tt)-2*cos(3*tt)-cos(4*tt)
    X = X*.018+3.6
    Y = Y*.018+1.1
    fill(X, Y, facecolor=[180,39,45], edgecolor=[180,39,45], linewidth=2)
    time.sleep(.5)

    # Legs
    X, Y = getEllipse([0,-.1], [[1,0],[0,1.6]], .7**2, 200)
    Y[Y<0] = Y[Y<0] * .2
    Y = Y - 4.1
    X = X - 1.2
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    fill(-X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    rectangle([-1.95, -4.3, 1.4, 3], curvature=0.4, facecolor=[57,57,57],
        edgecolor=[57,57,57])
    rectangle([1.95-1.4, -4.3, 1.4, 3],curvature=0.4, facecolor=[57,57,57],
        edgecolor=[57,57,57])
    time.sleep(.5)

    # Body
    X, Y = getEllipse([0,0], [[1,0],[0,1.3]], 3**2, 200)
    fill(X, Y, facecolor='w', edgecolor=[57,57,57], linewidth=2.5)
    time.sleep(.5)

    # Five rings
    cList = [[132,199,114],[251,184,77],[89,120,177],[158,48,87],[98,205,247]]
    for i in range(5):
        X, Y = getEllipse([0,0], [[1.6,0],[0,1.3]], (2.05-0.05*(i+1))**2, 200)
        Y[Y<0] = Y[Y<0] * .8
        Y = Y + .5
        fill(X, Y, facecolor='w', edgecolor=cList[i], linewidth=2.5)
        time.sleep(.5)

    # Eyes
    X, Y = getEllipse([1.2,1.2], [[1.2,-.5],[-.5,1.1]], .65**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    time.sleep(.5)
    fill(-X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    time.sleep(.5)
    X, Y = getEllipse([.95,1.3], [[1,0],[0,1]], .35**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor='w', linewidth=1.6)
    time.sleep(.5)
    fill(-X, Y, facecolor=[57,57,57], edgecolor='w', linewidth=1.6)
    time.sleep(.5)
    X, Y = getEllipse([.95,1.3], [[1,0],[0,1]], .1**2, 200)
    fill(X + .18, Y, facecolor='w', edgecolor=[57,57,57], linewidth=.5)
    time.sleep(.5)
    fill(-X + .18, Y, facecolor='w', edgecolor=[57,57,57], linewidth=.5)
    time.sleep(.5)

    # Mouth
    X, Y = getEllipse([0.05,.2], [[1.2,.15],[.15,.8]], .69**2, 200)
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    X, Y = getEllipse([0,.75], [[1,0.2],[0.2,.3]], .4**2, 200)
    fill(X, Y, facecolor='w', edgecolor='w', linewidth=2)
    time.sleep(.5)
    X, Y = getEllipse([0,0], [[.8,0],[0,.2]], .6**2, 200)
    fill(X, Y, facecolor=[180,39,45], edgecolor=[180,39,45], linewidth=2)
    time.sleep(.5)

    # Nose
    X, Y = getEllipse([0,-.1], [[1,0],[0,1.6]], .2**2, 200)
    Y[Y<0] = Y[Y<0] * .2
    Y = -Y + .9
    fill(X, Y, facecolor=[57,57,57], edgecolor=[57,57,57], linewidth=2)
    time.sleep(.5)

    ##################################################################
    # Winter Olympic symbol and five rings
    # Five rings
    tt = linspace(0, 2*pi, 100)
    X = cos(tt) * .14
    Y = sin(tt) * .14
    plot(X, Y-2.8, color=[57,57,57], linewidth=1.2)
    time.sleep(.5)
    plot(X-.3, Y-2.8, color=[106,201,245], linewidth=1.2)
    time.sleep(.5)
    plot(X+.3, Y-2.8, color=[155,79,87], linewidth=1.2)
    time.sleep(.5)
    plot(X-.15, Y-2.9, color=[236,197,107], linewidth=1.2)
    time.sleep(.5)
    plot(X+.15, Y-2.9, color=[126,159,101], linewidth=1.2)
    time.sleep(.5)

    # Text
    text(0, -2.4, 'BEIJING 2022', xalign='center', fontsize=8,
        fontname='Comic Sans MS')
    time.sleep(.5)

    # Symbol
    fill([.1,-.12,-.08], array([0,0-0.05,-0.15])-1.5, facecolor=[98,118,163], edgecolor=[98,118,163])
    fill([-.08,-.35,.1], array([-0.1,-.2,-.1])-1.6, facecolor=[98,118,163], edgecolor=[98,118,163])
    fill([-.08,-.08,.1,.1], array([-0.1,-0.15,-.2,-.15])-1.5, facecolor=[192,15,45], edgecolor=[192,15,45])
    plot(array([-.35,-.3,-.25,-.2,-.15,-.1,-.05,.1])+.02,
         array([0,.02,.04,.06,.04,.02,0,.02])-1.82, color=[120,196,219], lLinewidth=1.8)
    plot(array([-.33,.05])+.02, array([0,-.08])-1.82, color=[190,215,84], linewidth=1.8)
    plot(array([.05,-.2])+.02, array([-.08,-.15])-1.82, color=[32,162,218], linewidth=1.8)
    plot(array([-.2,.05])+.02, array([-.15,-.2])-1.82, color=[99,118,151], linewidth=1.8)