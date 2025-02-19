from NoteManager import NoteManager

notes = NoteManager()
notes.addNote("Note 1", "This is a test note")
notes.addNote("Note 2", "This is also a test note")
print(notes.getNote(1))
notes.deleteNote(1)
print(notes.getNote(1))