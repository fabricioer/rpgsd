#!/usr/bin/env pytho
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from number_entry import number_entry
class construtor(number_entry):
	def __init__(self):
		self.campos = {}
		self.main = Gtk.Window()
		self.main.connect("delete-event", Gtk.main_quit)
		self.vboxmain = Gtk.VBox()
		self.main.add(self.vboxmain)
		self.MenuBar = Gtk.MenuBar()
		self.vboxmain.add(self.MenuBar)
		
		self.filemenu()
		self.edit_menu()
		self.view_menu()
		self.tool_box()
		self.number_dialog(self)
		
		self.main.show_all()
		Gtk.main()
		

	def tool_box(self):
		hbox = Gtk.HBox()
		self.vboxmain.add(hbox)
		
		toolbox = Gtk.VBox()
		hbox.add(toolbox)
		
		bnum = Gtk.Button("Numero")
		bnum.connect("clicked", self.number_dialog)
		toolbox.add(bnum)
		btext = Gtk.Button("texto")
		toolbox.add(btext)
		blabel = Gtk.Button("label")
		toolbox.add(blabel)
		bfuncao = Gtk.Button("função")
		toolbox.add(bfuncao)
		btable = Gtk.Button("tabela")	
		toolbox.add(btable)
		bmenudrop = Gtk.Button("Menu drop")	
		toolbox.add(bmenudrop)

#==== 	fixed
		self.fixed = Gtk.Fixed()
		hbox.add(self.fixed)
		

