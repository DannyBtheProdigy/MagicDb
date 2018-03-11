'''
Created on Dec 19, 2017

@author: DannyB
'''
from PIL import Image
from PIL import ImageTk


class Deck(object):
    '''
    classdocs
    '''


    def __init__(self, CallStack, DeckName, ImageLocation):
        '''
        Constructor
        '''
        CallStack.info("Deck.__init__: Called")
        self._callstack = CallStack
        
        self._name = DeckName
        self._im_file = ImageLocation 
        
        
        self._callstack.info("Deck.__init__: Returned")
        
        
    def LoadImage(self):
        self._callstack.info("Deck.LoadImage: Called")

        self._image = Image.open(self._im_file)
        self._tk_image = ImageTk.PhotoImage(self._image)

        self._callstack.info("Deck.LoadImage: Returned")