#!/usr/bin/env pytho
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class new_label:		
	def dialog_label(self):
		label_dialog = Gtk.Window()
		nome_var = Gtk.Entry()
		name_fiel = Gtk.Entry()
		
