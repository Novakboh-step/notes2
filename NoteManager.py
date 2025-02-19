from Note import Note

class NoteManager:
    def __init__(self):
        self.__list = []
        self.__freeID = 1

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