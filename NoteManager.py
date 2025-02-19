from Note import Note

class NoteManager:
    def __init__(self):
        self.__list = []
        self.__freeID = 1

    def addNote(self, head, text):
        self.__list.append(Note(self.__freeID, head, text))
        self.__freeID += 1