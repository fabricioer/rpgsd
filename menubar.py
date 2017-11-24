#!/usr/bin/env pytho
import gi
import csv
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import json
class menubar:
	def filemenu(self):
		filemenu = Gtk.Menu()
		filem = Gtk.MenuItem("Arquivo")
		filem.set_submenu(filemenu)
		self.MenuBar.append(filem)

		new = Gtk.MenuItem("Novo")
		new.connect("activate", self.function_new)
		filemenu.append(new)
		
		openfile = Gtk.MenuItem("Abrir")
		openfile.connect("activate", self.function_openfile)
		filemenu.append(openfile)
		
		save = Gtk.MenuItem("Salvar")
		save.connect("activate", self.function_save)
		filemenu.append(save)
		
		saveas = Gtk.MenuItem("Salvar Como")
		saveas.connect("activate", self.function_saveas)
		filemenu.append(saveas)
		
		gexit = Gtk.MenuItem("Sair")
		gexit.connect("activate", self.function_exit)
		filemenu.append(gexit)

	def  edit_menu(self):
		editmenu = Gtk.Menu()
		editm = Gtk.MenuItem("Editar")
		editm.set_submenu(editmenu)
		self.MenuBar.append(editm)

		undo = Gtk.MenuItem("Destazer")
		undo.connect("activate", self.function_undo)
		editmenu.append(undo)

		redo = Gtk.MenuItem("Refazer")
		redo.connect("activate", self.function_redo)
		editmenu.append(redo)

		cut = Gtk.MenuItem("Recortar")
		cut.connect("activate", self.function_cut)
		editmenu.append(cut)

		copy = Gtk.MenuItem("Copiar")
		copy.connect("activate", self.function_copy)
		editmenu.append(copy)

		paste = Gtk.MenuItem("Colar")
		paste.connect("activate", self.function_paste)
		editmenu.append(paste)
		
	def view_menu(self): 
		viewmenu = Gtk.Menu()
		viewm = Gtk.MenuItem("Exibir")
		viewm.set_submenu(viewmenu)
		self.MenuBar.append(viewm)
		
		campos = Gtk.MenuItem("Campos")
		campos.connect("activate", self.function_campos)
		viewmenu.append(campos)


	def function_new(self,a):
		print(self.fields)
		
	def function_openfile (self,a):
		save_dialog = Gtk.FileChooserDialog(title="Save", action=Gtk.FileChooserAction.SAVE,   buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
		
		response = save_dialog.run()
		
		
	def function_save(self,a=None):
		save_dialog = Gtk.FileChooserDialog(title="Save", action=Gtk.FileChooserAction.SAVE,   buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
		
		response = save_dialog.run()
		
		if response == Gtk.ResponseType.OK:
			save_dict = {}
			for i in self.fields.keys():
				if self.fields[i]["type"] == "number":
					save_dict[i] = {}
					save_dict[i]["type"] = "number"
					save_dict[i]["width"] = self.fields[i]["entry"].get_width_chars()
					save_dict[i]["height"] = self.fields[i]["entry"].get_size_request()[1]
					save_dict[i]["position_x"] = self.fields[i]["position_x"]
					save_dict[i]["position_y"] = self.fields[i]["position_y"]
					save_dict[i]["label"] = self.fields[i]["label"].get_text()
					save_dict[i]["loc label"] = self.fields[i]["loc label"]
					save_dict[i]["min"] = self.fields[i]["min"]
					save_dict[i]["max"] = self.fields[i]["max"]
					save_dict[i]["negative"] = self.fields[i]["negative"] 
					save_dict[i]["float"] = self.fields[i]["float"]
					save_dict[i]["font"] = self.fields[i]["font"]
			print()
			print()
			print(save_dict)
			file_save = open(save_dialog.get_filename()+".pym", "w")
			file_save.write(json.dumps(save_dict))
			file_save.close()

			save_dialog.destroy()
		elif response == Gtk.ResponseType.CANCEL:
			save_dialog.destroy()

		
	
	def function_saveas(self,a):
		pass
		
	def function_exit(self, a):
		print(self)
		print(a)
		Gtk.main_quit()
		
	def function_copy(self,a):
		pass
		
	def function_paste(self,a):
		pass		
		
	def function_cut(self,a):
		pass
		
	def function_undo(self,a):
		pass
		
	def function_redo(self,a):
		pass
		
	def function_campos(self,a):
		pass

	
