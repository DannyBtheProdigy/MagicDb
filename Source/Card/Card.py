from PIL import Image
from PIL import ImageTk  

class Card:
    def __init__(self, CallStack, CardId, CardName, ImageLocation):
        CallStack.info("Card.__init__: Called")
        self._callstack = CallStack

        self._id = CardId
        self._name = CardName
        self._im_file = ImageLocation        

        self._callstack.info("Card.__init__: Returned")


    def LoadImage(self):
        self._callstack.info("Card.LoadImage: Called")

        self._image = Image.open(self._im_file)
        self._tk_image = ImageTk.PhotoImage(self._image)

        self._callstack.info("Card.LoadImage: Returned")


    def RemoveImage(self):
        self._callstack.info("Card.RemoveImage: Called")

        del self._tk_image
        del self._image

        self._callstack.info("Card.RemoveImage: Returned")
        