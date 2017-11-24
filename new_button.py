#!/usr/bin/env pytho
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class new_button:		
	def dialog_button(self):
		dropmenu_dialog = Gtk.Window()
		nome_var = Gtk.Entry()
		name_fiel = Gtk.Entry()


