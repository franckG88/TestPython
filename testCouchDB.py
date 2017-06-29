#!/usr/bin/env python32
# -*- coding: utf-8 -*-

import couchdb

couch = couchdb.Server("http://127.0.0.1:5984/")
db = couch['albums']
# create a dictionary to hold vehicle documents
abum_data = {}

# set flag variable
flag = True

# loop for data input
while (flag):
   test1 = input("Do you want to enter a new record [Y/N]: ")
   if test1 == "N":
        break
   album_artist = input("Enter Album artist: ")
   album_title = input("Enter Album title: ")

   # place values in dictionary
   album_data = {'artist':album_artist,'title':album_title}

   # insert the record
   db.save(album_data)

   # Prompt if user wants to continue?
   flag = input('Enter another record? ')
   if (flag[0].upper() == 'N'):
        flag = False

print("Nous avons trouvé {} objets :\n===========================\n".format(len(db)))
count = 0
libId = {}
for docid in db:
    doc = db.get(docid)
    if 'artist' in doc:
        count += 1
        print("[{}] {} - {}, ID: {}".format(count, doc['artist'], doc['title'], doc['_id']))
        libId[str(count)] =  doc['_id']
    else:
        print("Cet objet n'est pas un album correctement renseigné")
   
print(libId)
idToDelete = 0
while idToDelete not in libId.keys():
    idToDelete = input("Do you want to delete a record (Give me the number): ")

try:
    doc = db.get(libId[idToDelete])
    db.delete(doc)
except:
    print("impossible de supprimer l'album ID : {}".format(libId[idToDelete]))