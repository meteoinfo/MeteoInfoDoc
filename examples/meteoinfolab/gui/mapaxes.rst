.. _examples-meteoinfolab-map-mapaxes:

*******************
Map axes
*******************

Create a JFrame and add menu, toolbar and a figure which contains a MapAxes object. A web map layer was
loaded, and some buttons for map zooming and feature identifing was added.

::

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
    
.. image:: ../../../_static/gui_map.png