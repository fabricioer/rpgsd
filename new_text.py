#!/usr/bin/env pytho
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class new_text:
	def dialog_text(self):
		text_dialog = Gtk.Window()
		nome_var = Gtk.Entry()
		name_fiel = Gtk.Entry()
