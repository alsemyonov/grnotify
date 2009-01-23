#!/usr/bin/env python
import sys
import os

##################
#installs the pixmaps and config files into your system
#

# Check for Python < 2.2
if sys.version < '2.2':
	sys.exit('Error: Python-2.2 or newer is required. Current version:\n %s'
			% sys.version)

try:
	import gtk
	import gtk.glade
	import egg.trayicon
except:
	sys.exit('Error: gtk and gtk.glade are required')

try:
	import pygtk
	pygtk.require("2.0")
except:
	sys.exit('Error: pygtk 2.0 is required')


if not os.path.exists('/usr/share/pixmaps/grnotify/'):
	os.system('sudo mkdir /usr/share/pixmaps/grnotify/')
	
if not os.path.exists('/usr/share/grnotify/'):
	os.system('sudo mkdir /usr/share/grnotify/')


os.system('sudo cp pixmaps/*.gif /usr/share/pixmaps/grnotify')
os.system('sudo cp share/*.glade /usr/share/grnotify/')
os.system('sudo cp grnotify /usr/bin/')
os.system('sudo cp share/grnotify.desktop /usr/share/applications')
os.system('sudo cp pixmaps/grnotify.xpm /usr/share/pixmaps')
os.system('sudo chmod 777 /usr/bin/grnotify')
os.system('sudo chmod 777 /usr/share/grnotify/config.glade')
