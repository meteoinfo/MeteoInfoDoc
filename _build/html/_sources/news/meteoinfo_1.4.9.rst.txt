.. _news-meteoinfo_1.4.9:


******************************************
MeteoInfo 1.4.9 was released (2018-4-13)
******************************************

  - Add figure, mapaxes and axes3d modules in plotlib package.
  - Add boolean array.
  - Add left and right title.
  - Update micaps data reading functions.
  - Add pcolor and pcolorm functions.
  - Default read/write encoding of dBase file (part of shape file) changed to utf-8. Add .cpg file support for encoding.
  - Add T test and Chisquare test functions. Add normal, beta and many other distributions.
  - Add mouse wheel moved event for figure zooming.
  - Add add_bil function in midata module to open .bil data file.
  - Some bug fix and existing functions update.

**Bata distribution**::

    from mipylib.numeric import stats

    x = arange(0.01, 1, 0.01)
    aa = [0.5, 5, 1, 2,2]
    bb = [0.5, 1, 3, 2 ,5]
    ss = ['-b', '-r', '-c', '-g', '-m']

    #PDF
    subplot(1,2,1)
    for a,b,s in zip(aa,bb,ss):
        y = stats.beta.pdf(x, a, b)
        plot(x, y, s, label=r'$\alpha = %.1f, \beta = %.1f$' % (a, b))
    legend(loc='upper left', facecolor='w')
    ylim(0, 5)
    xlim(0, 1)
    title('PDF')

    #CDF
    subplot(1,2,2)
    for a,b,s in zip(aa,bb,ss):
        y = stats.beta.cdf(x, a, b)
        plot(x, y, s, label=r'$\alpha = %.1f, \beta = %.1f$' % (a, b))
    legend(loc='lower right', facecolor='w')
    ylim(0, 1)
    xlim(0, 1)
    title('CDF')

    suptitle('Beta distribution')

.. image:: ../_static/beta_distribution.png

**GUI map script**::

    # coding=utf-8

    import java.awt as awt
    import javax.swing as swing
    from java.awt.event import KeyEvent
    from java.io import File
    from javax.swing.filechooser import FileNameExtensionFilter
    from javax.imageio import ImageIO
    import inspect
    import os
    import sys
    import mipylib.miutil as miutil
    import mipylib.geolib as geolib
    from mipylib.plotlib.figure import Figure

    class MainGUI(swing.JFrame):

        def __init__(self):
            super(MainGUI, self).__init__()

            this_file = inspect.getfile(inspect.currentframe())
            self.currentPath = os.path.abspath(os.path.dirname(this_file))
            print self.currentPath

            self.initUI()
            
        def initUI(self):
            #Add menu bar
            menubar = swing.JMenuBar()
            menu_file = swing.JMenu('File')
            menu_file.setMnemonic(KeyEvent.VK_F)
            menuItem_fileExit = swing.JMenuItem('Exit', None,
                actionPerformed=self.onClick_exit)
            menuItem_fileExit.setMnemonic(KeyEvent.VK_C)
            menu_file.add(menuItem_fileExit)
            menubar.add(menu_file)        
            self.setJMenuBar(menubar)   

             #Add tool bar
            toolbar = swing.JToolBar()
            toolbar.setPreferredSize(awt.Dimension(300,25))
            self.add(toolbar, awt.BorderLayout.NORTH)
            #Add layer button
            icon = ImageIO.read(File(os.path.join(self.currentPath, 'image/add_layer.png')))
            icon = swing.ImageIcon(icon)
            exitButton = swing.JButton(icon, actionPerformed=self.click_addlayer)
            toolbar.add(exitButton)
            toolbar.addSeparator()
            #Zoom buttons
            icon = ImageIO.read(File(os.path.join(self.currentPath, 'image/zoom_in.png')))
            icon = swing.ImageIcon(icon)
            zoomInButton = swing.JButton(icon, actionPerformed=self.click_zoomIn)
            toolbar.add(zoomInButton)
            icon = ImageIO.read(File(os.path.join(self.currentPath, 'image/zoom_out.png')))
            icon = swing.ImageIcon(icon)
            zoomOutButton = swing.JButton(icon, actionPerformed=self.click_zoomOut)
            toolbar.add(zoomOutButton)
            icon = ImageIO.read(File(os.path.join(self.currentPath, 'image/pan.png')))
            icon = swing.ImageIcon(icon)
            panButton = swing.JButton(icon, actionPerformed=self.click_pan)
            toolbar.add(panButton)
            icon = ImageIO.read(File(os.path.join(self.currentPath, 'image/full_extent.png')))
            icon = swing.ImageIcon(icon)
            fullExtentButton = swing.JButton(icon, actionPerformed=self.click_fullExtent)
            toolbar.add(fullExtentButton)
            toolbar.addSeparator()
            #Identifer
            icon = ImageIO.read(File(os.path.join(self.currentPath, 'image/identifer.png')))
            icon = swing.ImageIcon(icon)
            idenButton = swing.JButton(icon, actionPerformed=self.click_identifer)
            toolbar.add(idenButton)

            #Add figure
            self.fig = Figure()
            self.fig.set_mousemode('pan')
            self.ax = self.fig.add_axes(position=[0,0,1,1], axestype='map', \
                proj='merc', aspect='auto', gridlabel=False, frameon=False)
            self._loadlayers()
            self.ax.axis([80,130,20,50])
            self.add(self.fig)
            
            self.pack()

            #Set main form
            icon = ImageIO.read(File(os.path.join(self.currentPath, 'image/earth_24.png')))
            self.title = 'Map axes'
            self.setIconImage(icon)
            self.defaultCloseOperation = swing.JFrame.DISPOSE_ON_CLOSE   
            self.windowClosing = self.formWindowClosing          

        def _loadlayers(self):
            self.ax.webmap(provider='GoogleSatelliteMap')
            self.ax.geoshow('cn_province', edgecolor='b')        

        def click_addlayer(self, e):
            fc = swing.JFileChooser()
            filter = FileNameExtensionFilter('shape files', ['shp'])
            fc.addChoosableFileFilter(filter)
            result = fc.showOpenDialog( None )
            if result == swing.JFileChooser.APPROVE_OPTION :
                f = fc.getSelectedFile()
                layer = geolib.shaperead(f.getAbsolutePath())
                self.ax.add_layer(layer)
                self.fig.draw()

        def click_zoomIn(self, e):
            self.fig.set_mousemode('zoom_in')

        def click_zoomOut(self, e):
            self.fig.set_mousemode('zoom_out')

        def click_pan(self, e):
            self.fig.set_mousemode('pan')

        def click_fullExtent(self, e):
            self.fig.onUndoZoomClick()

        def click_identifer(self, e):
            self.fig.set_mousemode('identifer')

        def formWindowClosing(self, e):
            self.dispose()

        def onClick_exit(self, e):        
            self.dispose()

    if __name__ == '__main__':
        frm = MainGUI()
        frm.pack()
        frm.size = (1000, 650)
        frm.locationRelativeTo = None
        frm.visible = True
        
.. image:: ../_static/gui_map.png