from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server



class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse', 'Name','GID')
    self.label_direktor.text = anvil.server.call('get_direktor',"Name",self.gefaengnisse_drop_down.selected_value) 
    self.label_freie_zellen.text = anvil.server.call('get_zellen',"AnzahlFreieZellen",self.gefaengnisse_drop_down.selected_value)
    self.repeating_zellen.items = [{'zellennummer': 'TODO', 'anzahl_häftlinge': anvil.server.call('get_zellen',"AnzahlBelegteZellen",self.gefaengnisse_drop_down.selected_value)}, 
                                   {'zellennummer': 'TODO', 'anzahl_häftlinge': anvil.server.call('get_zellen',"AnzahlBelegteZellen",self.gefaengnisse_drop_down.selected_value)}]

  def gefaengnisse_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    self.label_direktor.text = anvil.server.call('get_direktor',"Name",self.gefaengnisse_drop_down.selected_value) 
    self.label_freie_zellen.text = anvil.server.call('get_zellen',"AnzahlFreieZellen",self.gefaengnisse_drop_down.selected_value)
    self.repeating_zellen.items = [{'zellennummer': 'TODO', 'anzahl_häftlinge': anvil.server.call('get_zellen',"AnzahlBelegteZellen",self.gefaengnisse_drop_down.selected_value)}, 
                                   {'zellennummer': 'TODO', 'anzahl_häftlinge': anvil.server.call('get_zellen',"AnzahlBelegteZellen",self.gefaengnisse_drop_down.selected_value)}]
 



  
 
