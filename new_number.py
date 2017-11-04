#!/usr/bin/env pytho
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class number_entry:
	def __init__(self):
		pass
	def number_dialog(self, a):
		number_table = Gtk.Table(12,4)
		fixed = Gtk.Fixed()
		fixed.put(number_table, 0, 0)
		label_var = Gtk.Label("Nome da variavel")
		self.entry_var = Gtk.Entry()
		number_table.attach(label_var, 0, 1, 0, 1)
		number_table.attach(self.entry_var, 1, 2, 0, 1)
		number_table.set_row_spacing(0,5)
		number_table.set_row_spacing(1,5)
		number_table.attach(Gtk.HSeparator(), 0, 2, 1, 2)
		
		
		
		label_max = Gtk.Label("Valor maximo")
		self.entry_max = Gtk.Entry()
		label_min = Gtk.Label("Valor minimo")
		self.entry_min = Gtk.Entry()
		self.float_number = Gtk.CheckButton("Permitir numeros racionais")
		self.negative_number = Gtk.CheckButton("Permitir numeros negativos")
		number_table.attach(label_max,  0, 1, 2, 3)
		number_table.attach(self.entry_max, 1, 2, 2, 3)
		number_table.attach(label_min,  0, 1, 3, 4)
		number_table.attach(self.entry_min, 1, 2, 3, 4)
		number_table.attach(self.float_number,  0, 2, 4, 5 )
		number_table.attach(self.negative_number, 0, 2, 5,6)
		number_table.set_row_spacing(6,5)
		number_table.set_row_spacing(7,5)
		number_table.attach(Gtk.HSeparator(), 0, 2, 6, 7)


		
		
		label_field = Gtk.Label("Rotulo da variavel")
		self.entry_number_field = Gtk.Entry()
		self.font = Gtk.FontSelection()
		label_loc_field = Gtk.Label("Localização do rótulo")
		self.number_combo_loc_field = Gtk.ComboBoxText()
		self.number_combo_loc_field.append_text("Direita")
		self.number_combo_loc_field.append_text("Cima")
		self.number_combo_loc_field.append_text("Esquerda")
		self.number_combo_loc_field.append_text("Baixo")
		
		number_table.set_row_spacing(8,5)
		number_table.attach(label_field, 0, 1, 8, 9)
		number_table.attach(self.entry_number_field, 1, 2, 8, 9)
		number_table.attach(label_loc_field, 0, 1, 9, 10)
		number_table.set_row_spacing(8,5)
		number_table.attach(self.number_combo_loc_field, 1, 2, 9, 10)
		number_table.attach(self.font, 1, 2, 10, 12)
		
		#self.number_view = Gtk.ScrolledWindow()
		self.number_view = Gtk.Fixed()
		self.number_view.set_size_request(100, 350)
		#self.number_view.set_policy(Gtk.POLICY_AUTOMATIC, Gtk.POLICY_AUTOMATIC)
		
		label_width = Gtk.Label("Largura")
		self.entry_width = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=50, lower=10, upper=500, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		label_height = Gtk.Label("Altura")
		self.entry_height = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=10, lower=10, upper=500, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		label_position_x = Gtk.Label("Posição x")
		self.entry_position_x = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=0, lower=0, upper=10000, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		label_position_y = Gtk.Label("Posição y")
		self.entry_position_y = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=0, lower=0, upper=10000, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		button_close = Gtk.Button("Fechar")
		button_ok = Gtk.Button("Ok")
		button_ok.connect("clicked", self.draw_number)
		
		number_table2 = Gtk.Table(12,2)
		fixed.put(number_table2, 750, 0)
		
		number_table2.attach(self.number_view, 0, 2, 0, 7)
		number_table2.attach(label_width, 0, 1, 7, 8)
		number_table2.attach(self.entry_width, 1, 2, 7, 8)
		number_table2.attach(label_height, 0, 1, 8, 9)
		number_table2.attach(self.entry_height, 1, 2, 8, 9)
		number_table2.attach(label_position_x, 0, 1, 9, 10)
		number_table2.attach(self.entry_position_x, 1, 2, 9, 10)
		number_table2.attach(label_position_y, 0, 1, 10, 11)
		number_table2.attach(self.entry_position_y, 1, 2, 10, 11)
		number_table2.attach(button_close, 0, 1, 11, 12)
		number_table2.attach(button_ok, 1, 2, 11, 12)
		
		
		
		num_dialog = Gtk.Window()
		num_dialog.add(fixed)
		num_dialog.show_all()
		
	def draw_number(self, a):
		hbox = Gtk.HBox()
		num_label = Gtk.Label(self.entry_number_field.get_text())
		hbox.add(num_label)
		entry = Gtk.Entry()
		entry.set_size_request(self.entry_width.get_value(), self.entry_width.get_value())
		hbox.add(entry)
		hbox.show_all()
		self.number_view.put(hbox, 0, 150)
		
	
