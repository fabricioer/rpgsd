
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import json




class reader:
	def __init__(self):
		self.main = Gtk.Window()
		self.main.connect("delete-event", Gtk.main_quit)
		self.fixedmain = Gtk.Fixed()
		self.fixedmain.show_all()
		self.fixedmain.set_size_request(800, 800) 	
		self.main.add(self.fixedmain)
		
		self.function_addmonude(self)
		self.main.show_all()
		Gtk.main()

		
		
	def function_addmonude(self,a=None):
		add_dialog = Gtk.FileChooserDialog(title="ADD module", action=Gtk.FileChooserAction.OPEN,   buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		
		response = add_dialog.run()
		if response == Gtk.ResponseType.OK:
			file_open = open(add_dialog.get_filename(), "r")
			open_dict =  json.loads(file_open.read())
			file_open.close()
			campos = {}
			for i in open_dict.keys():
				if open_dict[i]["type"] == "number":
					campos[i] = {}
					campos[i]["label"] = Gtk.Label(open_dict[i]["label"])
					campos[i]["entry"] = Gtk.Entry()
					campos[i]["entry"].set_size_request(-1, open_dict[i]["height"])
					campos[i]["entry"].set_width_chars(open_dict[i]["width"])
					if open_dict[i]["loc label"] == "Direita":
						campos[i]["box"] = Gtk.HBox()
						campos[i]["box"].add(campos[i]["label"])
						campos[i]["box"].add(campos[i]["entry"])
						
					elif open_dict[i]["loc label"] == "Cima":
						campos[i]["box"] = Gtk.VBox()
						campos[i]["box"].add(campos[i]["label"])
						campos[i]["box"].add(campos[i]["entry"])
						campos[i]["box"].show_all()
						
					elif open_dict[i]["loc label"] == "Esquerda":
						campos[i]["box"] = Gtk.HBox()
						campos[i]["box"].add(campos[i]["entry"])
						campos[i]["box"].add(campos[i]["label"])
						campos[i]["box"].show_all()
					else:
						campos[i]["box"] = Gtk.VBox()
						campos[i]["box"].add(campos[i]["entry"])
						campos[i]["box"].add(campos[i]["label"])
						campos[i]["box"].show_all()
					self.fixedmain.put(campos[i]["box"], open_dict[i]["position_x"], open_dict[i]["position_y"])
					
			add_dialog.destroy()
		elif response == Gtk.ResponseType.CANCEL:
			save_dialog.destroy()
					
			
reader()
