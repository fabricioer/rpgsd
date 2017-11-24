#!/usr/bin/env pytho
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import re

#exec()
#eval()
class new_function:
	def function_dialog(self, a=None):
		function_table = Gtk.Table(12,4)
		fixed = Gtk.Fixed()
		fixed.put(function_table, 0, 0)
		label_var = Gtk.Label("Nome da variavel")
		self.entry_func_var = Gtk.Entry()
		function_table.attach(label_var, 0, 1, 0, 1)
		function_table.attach(self.entry_func_var, 1, 2, 0, 1)
		function_table.set_row_spacing(0,5)
		function_table.set_row_spacing(1,5)
		function_table.attach(Gtk.HSeparator(), 0, 2, 1, 2)
		
		
		
		label_function = Gtk.Label("Função")
		sw = Gtk.ScrolledWindow()
		self.entry_function= Gtk.TextView()
		
		self.function_buffer = self.entry_function.get_buffer()
		
		self.function_buffer.set_text('output = "Função"')
		sw.add(self.entry_function)
		sw.set_size_request(-1, 200)
		function_table.attach(label_function,  0, 1, 2, 3)
		function_table.attach(sw, 1, 2, 2, 3)
		function_table.set_row_spacing(6,5)
		function_table.set_row_spacing(7,5)
		function_table.attach(Gtk.HSeparator(), 0, 2, 6, 7)
		self.font_func = Gtk.FontSelection()
		
		function_table.set_row_spacing(8,5)
		function_table.attach(self.font_func, 1, 2, 10, 12)
		
		#self.function_view = Gtk.ScrolledWindow()
		self.function_view = Gtk.Fixed()
		self.function_view.set_size_request(100, 350)

		label_position_x = Gtk.Label("Posição x")
		self.entry_position_x = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=0, lower=0, upper=5000, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		#self.entry_position_x.connect("value-changed", self.redraw_function_position)
		label_position_y = Gtk.Label("Posição y")
		self.entry_position_y = Gtk.SpinButton(adjustment=Gtk.Adjustment(value=0, lower=0, upper=5000, step_incr=1, page_incr=0, page_size=0), climb_rate=1 ,digits=0)
		#self.entry_position_y.connect("value-changed", self.redraw_function_position)
		button_close = Gtk.Button("Fechar")
		button_ok = Gtk.Button("Ok")
		button_ok.connect("clicked", self.keep_func)
		button_test = Gtk.Button("Testar")
		button_test.connect("clicked", self.redraw_function)
		
		function_table2 = Gtk.Table(12,2)
		fixed.put(function_table2, 700, 0)
		
		function_table2.attach(self.function_view, 0, 2, 0, 7)
		function_table2.attach(button_test, 0, 1, 8, 9)
		function_table2.attach(label_position_x, 0, 1, 9, 10)
		function_table2.attach(self.entry_position_x, 1, 2, 9, 10)
		function_table2.attach(label_position_y, 0, 1, 10, 11)
		function_table2.attach(self.entry_position_y, 1, 2, 10, 11)
		function_table2.attach(button_close, 0, 1, 11, 12)
		function_table2.attach(button_ok, 1, 2, 11, 12)
		
		self.temp_view_func ={}
		self.temp_view_func["function"] = ""
		self.temp_view_func["label"] = Gtk.Label("Função")
		self.function_view.put(self.temp_view_func["label"], 0, 150)
		
		self.temp_func ={}
		self.temp_func["type"] = "Função"
		self.temp_func["label"] = Gtk.Label("Função")
		self.temp_func["font"] = {"family": self.font_func.get_family(), "face":self.font_func.get_face(), "size":self.font_func.get_size()}
		self.fixedmain.put(self.temp_func["label"], 0, 0)
		self.temp_func["label"].show()
		
		
		
		self.func_dialog = Gtk.Window()
		self.func_dialog.add(fixed)
		self.func_dialog.show_all()

	def redraw_function(self, a = None):
		ban_list = ["open(", "exec(", "import ", "compile(" , "input(", "print("]
		temp_code = str(self.function_buffer.get_text(self.function_buffer.get_start_iter(), self.function_buffer.get_end_iter(), 1))
		for i in ban_list:
			if temp_code.find(i) != -1:
				self.temp_func["label"].set_text("termo invalido: " + i)
				return -1
		print(temp_code)
		vars_list = re.findall(r"@\w*", temp_code)
		print(vars_list)
		

		for i in vars_list:
			try:
				if self.fields[i[1:]]["type"] == "Num":
					print(self.fields[i[1:]])
					temp_code = temp_code.replace(i, "self.fields['"+i[1:]+"']['value']")
					print("\n "+temp_code)
			except KeyError:
				self.temp_func["label"].set_text("Variavel não encontrada: "+ i)
				self.temp_view_func["label"].set_text("Variavel não encontrada: "+ i)
				return -3
		#try:
		temp_code = temp_code.replace('output', 'self.temp_func["output"]')
		exec(temp_code)
		self.temp_func["label"].set_text(self.temp_func["output"])
		self.temp_view_func["label"].set_text(self.temp_func["output"])
		return 0
		"""except TypeError:
			self.temp_func["label"].set_text("O output precisa ser str")
			self.temp_view_func["label"].set_text("O output precisa ser str")
			return -1 
		except:
			self.temp_func["label"].set_text("codigo invatido")
			self.temp_view_func["label"].set_text("codigo invatido")
			return -2"""
		
		

	def keep_func(self, a=None):
		if self.redraw_function(self) == 0:
			self.fields[self.entry_func_var.get_text()] = self.temp_func
			self.temp_func["position_x"] = self.entry_position_x.get_value()
			self.temp_func["position_y"] = self.entry_position_y.get_value()
			self.list_store.append([self.entry_func_var.get_text(), self.temp_func["type"]])
			del self.temp_func
			self.func_dialog.destroy()
