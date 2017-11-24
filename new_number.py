#!/usr/bin/env pytho
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class new_number:
	def number_dialog(self, a):
		number_table = Gtk.Table(12,4)
		fixed = Gtk.Fixed()
		fixed.put(number_table, 0, 0)
		label_var = Gtk.Label("Nome da variavel")
		self.entry_num_var = Gtk.Entry()
		number_table.attach(label_var, 0, 1, 0, 1)
		number_table.attach(self.entry_num_var, 1, 2, 0, 1)
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
		self.entry_number_field.set_text("Rotulo")
		self.entry_number_field.connect("changed", self.redraw_number_label)
		self.font_num = Gtk.FontSelection()
		label_loc_field = Gtk.Label("Localização do rótulo")
		self.number_combo_loc_field = Gtk.ComboBoxText()
		self.number_combo_loc_field.append_text("Direita")
		self.number_combo_loc_field.append_text("Cima")
		self.number_combo_loc_field.append_text("Esquerda")
		self.number_combo_loc_field.append_text("Baixo")
		self.number_combo_loc_field.connect("changed", self.redraw_number_loc_field)
		self.number_combo_loc_field.set_active(0)
		
		number_table.set_row_spacing(8,5)
		number_table.attach(label_field, 0, 1, 8, 9)
		number_table.attach(self.entry_number_field, 1, 2, 8, 9)
		number_table.attach(label_loc_field, 0, 1, 9, 10)
		number_table.set_row_spacing(8,5)
		number_table.attach(self.number_combo_loc_field, 1, 2, 9, 10)
		number_table.attach(self.font_num, 1, 2, 10, 12)
		
		#self.number_view = Gtk.ScrolledWindow()
		self.number_view = Gtk.Fixed()
		self.number_view.set_size_request(100, 350)

		
		label_width = Gtk.Label("Largura")
		self.entry_width = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=1, lower=1, upper=500, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		self.entry_width.connect("value-changed", self.redraw_number_size)
		label_height = Gtk.Label("Altura")
		self.entry_height = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=30, lower=30, upper=500, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		self.entry_height.connect("value-changed", self.redraw_number_size )
		label_position_x = Gtk.Label("Posição x")
		self.entry_position_x = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=0, lower=0, upper=5000, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		self.entry_position_x.connect("value-changed", self.redraw_number_position)
		label_position_y = Gtk.Label("Posição y")
		self.entry_position_y = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=0, lower=0, upper=5000, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		self.entry_position_y.connect("value-changed", self.redraw_number_position)
		button_close = Gtk.Button("Fechar")
		button_ok = Gtk.Button("Ok")
		button_ok.connect("clicked", self.keep_num)
		
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
		
		#===temp
		self.temp_view_num ={}
		self.temp_view_num["box"] = Gtk.HBox()
		self.temp_view_num["label"] = Gtk.Label(self.entry_number_field.get_text())
		self.temp_view_num["box"].add(self.temp_view_num["label"])
		self.temp_view_num["entry"] = Gtk.Entry()
		self.temp_view_num["entry"].set_size_request(self.entry_width.get_value(), self.entry_height.get_value())
		self.temp_view_num["box"].add(self.temp_view_num["entry"])
		self.temp_view_num["box"].show_all()
		self.number_view.put(self.temp_view_num["box"], 0, 150)
		self.temp_view_num["entry"].set_width_chars(1)
		
		self.temp_num ={}
		self.temp_num["type"] = "Num"
		self.temp_num["value"] = 0
		self.temp_num["loc label"] = "Direita"
		self.temp_num["min"] = 0
		self.temp_num["max"] = 1
		self.temp_num["negative"] = 0
		self.temp_num["float"] = 0
		self.temp_num["box"] = Gtk.HBox()
		self.temp_num["label"] = Gtk.Label(self.entry_number_field.get_text())
		self.temp_num["font"] = {"family": self.font_num.get_family(), "face":self.font_num.get_face(), "size":self.font_num.get_size()}
		self.temp_num["box"].add(self.temp_num["label"])
		self.temp_num["entry"] = Gtk.Entry()
		self.temp_num["entry"].set_size_request(-1, self.entry_height.get_value())
		self.temp_num["entry"].set_width_chars(1)
		self.temp_num["box"].add(self.temp_num["entry"])
		self.temp_num["box"].show_all()
		self.fixedmain.put(self.temp_num["box"], 0, 0)
		
		
		
		self.num_dialog = Gtk.Window()
		self.num_dialog.add(fixed)
		self.num_dialog.show_all()
		
	def redraw_number_label(self, a):
		self.temp_view_num["label"].set_text(self.entry_number_field.get_text())
		self.temp_num["label"].set_text(self.entry_number_field.get_text())
		
	def redraw_number_loc_field(self, a):
		self.temp_num["loc label"] = self.number_combo_loc_field.get_active_text()
		if self.temp_num["loc label"] == "Direita":
			self.temp_view_num["box"].remove(self.temp_view_num["label"])
			self.temp_view_num["box"].remove(self.temp_view_num["entry"])
			del self.temp_view_num["box"]
			self.temp_view_num["box"] = Gtk.HBox()
			self.temp_view_num["box"].add(self.temp_view_num["label"])
			self.temp_view_num["box"].add(self.temp_view_num["entry"])
			self.temp_view_num["box"].show_all()
			self.number_view.put(self.temp_view_num["box"], 0, 150)
			
			self.temp_num["box"].remove(self.temp_num["label"])
			self.temp_num["box"].remove(self.temp_num["entry"])
			del self.temp_num["box"]
			self.temp_num["box"] = Gtk.HBox()
			self.temp_num["box"].add(self.temp_num["label"])
			self.temp_num["box"].add(self.temp_num["entry"])
			self.temp_num["box"].show_all()
			self.fixedmain.put(self.temp_num["box"], 0, 0)
			
		elif self.temp_num["loc label"] == "Cima":
			self.temp_view_num["box"].remove(self.temp_view_num["label"])
			self.temp_view_num["box"].remove(self.temp_view_num["entry"])
			del self.temp_view_num["box"]
			self.temp_view_num["box"] = Gtk.VBox()
			self.temp_view_num["box"].add(self.temp_view_num["label"])
			self.temp_view_num["box"].add(self.temp_view_num["entry"])
			self.temp_view_num["box"].show_all()
			self.number_view.put(self.temp_view_num["box"], 0, 150)
			
			self.temp_num["box"].remove(self.temp_num["label"])
			self.temp_num["box"].remove(self.temp_num["entry"])
			del self.temp_num["box"]
			self.temp_num["box"] = Gtk.VBox()
			self.temp_num["box"].add(self.temp_num["label"])
			self.temp_num["box"].add(self.temp_num["entry"])
			self.temp_num["box"].show_all()
			self.fixedmain.put(self.temp_num["box"], 0, 0)
			
		elif self.temp_num["loc label"] == "Esquerda":
			self.temp_view_num["box"].remove(self.temp_view_num["label"])
			self.temp_view_num["box"].remove(self.temp_view_num["entry"])
			del self.temp_view_num["box"]
			self.temp_view_num["box"] = Gtk.HBox()
			self.temp_view_num["box"].add(self.temp_view_num["entry"])
			self.temp_view_num["box"].add(self.temp_view_num["label"])
			self.temp_view_num["box"].show_all()
			self.number_view.put(self.temp_view_num["box"], 0, 150)
			
			self.temp_num["box"].remove(self.temp_num["label"])
			self.temp_num["box"].remove(self.temp_num["entry"])
			del self.temp_num["box"]
			self.temp_num["box"] = Gtk.HBox()
			self.temp_num["box"].add(self.temp_num["entry"])
			self.temp_num["box"].add(self.temp_num["label"])
			self.temp_num["box"].show_all()
			self.fixedmain.put(self.temp_num["box"], 0, 0)
			
		else:
			self.temp_view_num["box"].remove(self.temp_view_num["label"])
			self.temp_view_num["box"].remove(self.temp_view_num["entry"])
			del self.temp_view_num["box"]
			self.temp_view_num["box"] = Gtk.VBox()
			self.temp_view_num["box"].add(self.temp_view_num["entry"])
			self.temp_view_num["box"].add(self.temp_view_num["label"])
			self.temp_view_num["box"].show_all()
			self.number_view.put(self.temp_view_num["box"], 0, 150)
			
			self.temp_num["box"].remove(self.temp_num["label"])
			self.temp_num["box"].remove(self.temp_num["entry"])
			del self.temp_num["box"]
			self.temp_num["box"] = Gtk.VBox()
			self.temp_num["box"].add(self.temp_num["entry"])
			self.temp_num["box"].add(self.temp_num["label"])
			self.temp_num["box"].show_all()
			self.fixedmain.put(self.temp_num["box"], 0, 0)
			
	def redraw_number_size(self, a):
		self.temp_num["entry"].set_size_request(-1, self.entry_height.get_value())
		self.temp_num["entry"].set_width_chars(self.entry_width.get_value())
		self.temp_view_num["entry"].set_size_request(-1, self.entry_height.get_value())
		self.temp_view_num["entry"].set_width_chars(self.entry_width.get_value())
		
	def redraw_number_position(self, a):
		self.fixedmain.move(self.temp_num["box"], self.entry_position_x.get_value(), self.entry_position_y.get_value())
		
		
	def keep_num(self, a=None):
		self.temp_num["position_x"] = self.entry_position_x.get_value()
		self.temp_num["position_y"] = self.entry_position_y.get_value()
		self.list_store.append([self.entry_num_var.get_text(), self.temp_num["type"]])
		self.fields[self.entry_num_var.get_text()] = self.temp_num
		del self.temp_num
		#self.num_dialog.destroy()
