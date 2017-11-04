#!/usr/bin/env pytho
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
		

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
		print(self.campos)
		
	def function_openfile (self,a):
		pass
		
	def function_save(self,a):
		pass
		
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

	
