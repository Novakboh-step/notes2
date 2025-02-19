class Note:
    def __init__(self, id, head, text):
        self.__id = id
        self.__head = head
        self.__text = text

    def getID(self):
        return self.__id

    def setHead(self, head):
        self.__head = head

    def setText(self, text):
        self.__text = text