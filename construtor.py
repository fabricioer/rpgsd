#!/usr/bin/env pytho
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from new_number import new_number
from new_button import new_button
from new_text import new_text
from new_label import new_label
from new_function import new_function
from new_table import new_table
from new_dropmenu import new_dropmenu
from menubar import menubar


class construtor(new_number, new_button, new_text, new_label, new_function, new_table, new_dropmenu, menubar):
	def __init__(self):
		self.fields = {}
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
		#self.dialog_function()

		
		self.main.show_all()
		Gtk.main()
		

	def tool_box(self):
		hpaned = Gtk.HPaned()
		self.vboxmain.add(hpaned)
		
		toolbox = Gtk.VBox(False)
		vpaned = Gtk.VPaned()
		hpaned.add1(vpaned)
		vpaned.add1(toolbox)
		
		
		self.fixe_size_x = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=800, lower=0, upper=5000, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		self.fixe_size_x.connect("value-changed", self.redraw_fixe_size)
		toolbox.add(self.fixe_size_x)
		self.fixe_size_y = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=800, lower=0, upper=5000, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		self.fixe_size_y.connect("value-changed", self.redraw_fixe_size)
		toolbox.add(self.fixe_size_y)
		
		bnum = Gtk.Button("Numero")
		bnum.connect("clicked", self.number_dialog)
		bnum.set_size_request(20, 20)
		toolbox.add(bnum)
		btext = Gtk.Button("texto")
		btext.set_size_request(20, 20)
		toolbox.add(btext)
		blabel = Gtk.Button("label")
		blabel.set_size_request(20, 20)
		toolbox.add(blabel)	
		bfunc = Gtk.Button("função")
		bfunc.connect("clicked", self.function_dialog)
		bfunc.set_size_request(20, 20)
		toolbox.add(bfunc)
		btable = Gtk.Button("tabela")
		btable.set_size_request(20, 20)
		toolbox.add(btable)
		bmenudrop = Gtk.Button("Menu drop")	
		bmenudrop.set_size_request(20, 20)
		toolbox.add(bmenudrop)
		
		
		
		
		self.current_tree_filter = None
		self.list_store = Gtk.ListStore(str, str)
		tree_filter = self.list_store.filter_new()
		tree_filter.set_visible_func(self.tree_filter_func)
		treeview = Gtk.TreeView.new_with_model(tree_filter)
		vpaned.add2(treeview)
		for i, column_title in enumerate(["Nome", "Tipo"]):
			renderer = Gtk.CellRendererText()
			column = Gtk.TreeViewColumn(column_title, renderer, text=i)
			treeview.append_column(column)
		
		
		
		treeview.show()

#==== 	fixed
		self.fixedmain = Gtk.Fixed()
		self.fixedmain.show_all()
		self.fixedmain.set_size_request(800, 800) 	
		hpaned.add2(self.fixedmain)
		
	def tree_filter_func(self, model, iter, data):
		if self.current_tree_filter is None or self.current_tree_filter == "None":
			return True
		else:
			return model[iter][2] == self.tree_filter


	def redraw_fixe_size(self, a):
		self.fixed.set_size_request(self.fixe_size_x.get_value(), self.fixe_size_y.get_value())
		
construtor()
