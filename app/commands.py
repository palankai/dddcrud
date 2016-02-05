from .messaging import cmd


CreateContact = cmd('create_contact', 'name', 'phone')
ReadContact = cmd('read_contact', 'name')
UpdateContact = cmd('update_contact', 'name', 'phone')
DeleteContact = cmd('delete_contact', 'name')
