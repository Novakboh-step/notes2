from Note import Note

class NoteManager:
    def __init__(self):
        self.__list = []
        self.__freeID = 1
        self.__takeNotes()

    def __takeNotes(self):
        with open("notes.txt") as fileHandler:
            notes = fileHandler.read()
            if len(notes):
                notes = notes.split("\n\n")
                for i in range(len(notes) - 1):
                    note = notes[i].split(") ")
                    note[1] = note[1].split(":\n")
                    self.__freeID = int(note[0])
                    self.addNote(note[1][0], note[1][1])

    def addNote(self, head, text):
        self.__list.append(Note(self.__freeID, head, text))
        self.__freeID += 1

    def __findNote(self, id):
        if id > len(self.__list) or id < 1:
            return None
        for i in range(id - 1, -1, -1):
            if self.__list[i].getID() == id:
                return i
        return None

    def getNote(self, id):
        i = self.__findNote(id)
        if i != None:
            return self.__list[i].ToString()
        return None

    def deleteNote(self, id):
        i = self.__findNote(id)
        if i != None:
            self.__list.pop(i)

    def saveNotes(self):
        with open("notes.txt", "w") as fileHandler:
            for note in self.__list:
                fileHandler.write(f"{note.ToString()}\n\n")