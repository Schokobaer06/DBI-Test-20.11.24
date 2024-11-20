import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

conn = sqlite3.connect(data_files['prison.db'])
@anvil.server.callable
def get_gefaengnisse(rows, id):
  #return [('TODO 1', 1), ('TODO 2', 2)]
  #conn = sqlite3.connect(data_files['prison.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT {rows},{id} FROM Gefängnis"))
  return res
@anvil.server.callable
def get_direktor(DirektorName, GefängnisID):
  cursor = conn.cursor()
  res = cursor.execute(f"SELECT Direktor.{DirektorName} from Gefängnis JOIN Verwaltung ON Gefängnis.VID = Verwaltung.VID JOIN Direktor ON Verwaltung.VID = Direktor.VID WHERE Gefängnis.VID = {GefängnisID}")
  results = res.fetchall()
  for row in results:
    direktor_name = str(row[0])
    return direktor_name
@anvil.server.callable
def get_zellen(row,GefängnisID):
  cursor = conn.cursor()
  res = cursor.execute(f"SELECT Verwaltung.{row} FROM Gefängnis Join Verwaltung ON Gefängnis.VID = Verwaltung.VID WHERE Gefängnis.VID = {GefängnisID}")
  results = res.fetchall()
  for row in results:
    zelle = str(row[0])
    return zelle