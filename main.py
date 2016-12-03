from collections import OrderedDict
from peewee import *
import datetime
import sys
import os

db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
  
    class Meta:
      database = db

def initialize():
  db.connect()
  db.create_tables([Entry], safe=True)
  
def clear():
  os.system('cls' if os.name =='nt' else 'clear')
    
def menu_loop():
  """Show the menu"""
  choice = None
  
  while choice != 'q':
    clear()
    print("Enter 'q' to quit.")
    for key, value in menu.items():
      print('{} {}'.format(key, value.__doc__)) # Returns doc string
    choice = input('Action: ').lower().strip()
    
    if choice in menu:
      clear()
      menu[choice]()
  
def add_entry():
  """Add an entry."""
  print("Enter your entry. Press Ctrl+D when finished.")
  data = sys.stdin.read().strip()
  
  if data:
    if input('Save entry? [Y/n] ').lower() != 'n':
      Entry.create(content=data)
      print('Saved successfully!')
  
def view_entries():
  """View previous entries."""
  entries = Entry.select().order_by(Entry.timestamp.desc())
  if search_query:
    entries = entries.where(Entry.content.contains(search_query))
    
  for entry in entires:
    timestamp = entry.timestamp.strftime('%A %B %d, %Y %I: %M%p')
    clear()
    print(timestamp)
    print('='*len(timestamp))
    print(entry.content)
    print('\n\n' + '='*len(timestamp))
    print('n) next entry')
    print('q) return to main menu')
    
    next_actuion = input('Action: [Nq] ').lower().strip()
    if next_action == 'q':
      break
  
def delete_entry(entry):
  """Delete an entry."""
  if input('Are you sure? [Y/N] ').lower() == 'y':
       entry.delete_instance()

menu = OrderedDict([
    ('a',add_entry),
    ('v',view_entries)
  ])
  
if __name__ == '__main__':
  menu_loop()
