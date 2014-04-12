# -*- coding: utf-8 -*-
"""
/***************************************************************************
 vector_selectbypoint
                                 A QGIS plugin
 Select vector features, point and click.
                              -------------------
        begin                : 2014-04-07
        copyright            : (C) 2014 by Brylie Oxley
        email                : brylie@geolibre.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from vector_selectbypointdialog import vector_selectbypointDialog
import os.path


class vector_selectbypoint:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        
        # Reference map canvas
        self.canvas = self.iface.mapCanvas()
        
        # Emit QgsPoint after each click on canvas
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'vector_selectbypoint_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = vector_selectbypointDialog()
        
        # Create the GUI
        self.canvas.setMapTool( self.clickTool )

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/vector_selectbypoint/icon.png"),
            u"Select by point and click.", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Select vector features by point and click.", self.action)
        
        # Signal connections for mouse clicks
        result = QObject.connect(self.clickTool,  SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"),  self.handleMouseDown)
        #QMessageBox.information( self.iface.mainWindow(),  "Info",  "connect = %s" %str(result) )
        
    def handleMouseDown(self,  point,  button):
        #QMessageBox.information( self.iface.mainWindow(),  "Info",  "X,Y = %s, %s" % (str(point.x()), str(point.y())) )
        self.dlg.clearTextBrowser()
        self.dlg.setTextBrowser( str(point.x()) + " , " + str(point.y()) )

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Select vector features by point and click.", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # Activate click tool
        
        
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass

