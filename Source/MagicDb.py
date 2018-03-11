import Tkinter as tk
import logging

from DbIf.DbIf import DbIf
from DeckFrame.DeckFrame import DeckFrame
from CardFrame.CardFrame import CardFrame
from EntryWindow.EntryWindow import EntryWindow

global gCallStack

call_handle = logging.FileHandler("callstack.txt")
gCallStack = logging.getLogger('call_stack')
gCallStack.addHandler(call_handle)
gCallStack.setLevel(logging.INFO)


class MagicDb(tk.Tk):
    def __init__(self, *args, **kwargs):
        gCallStack.info("MagicDb.__init__: Called")
        

        module_log = logging.FileHandler("MagicDb.txt")
        self._log = logging.getLogger('MagicDb')
        self._log.addHandler(module_log)

        self._dbif = DbIf(gCallStack)

        tk.Tk.__init__(self, *args, **kwargs)
        #Set window dimensions
        self.geometry("1340x630+0+0")
        self.menubar = tk.Menu(self, title="Menu")

        self.menubar.add_command(label="Create Deck", command=self.createDeckWizard)

        self.config(men=self.menubar)

        self._deck_frame = DeckFrame(Width=300, CallStack=gCallStack, DbIf=self._dbif)
        self._card_frame = CardFrame(Width=1000, CallStack=gCallStack, DbIf=self._dbif)
        
        self._scroll_base = self._card_frame.scroll.get()
        self._deck_scroll_base = self._deck_frame.scroll.get()
        
        gCallStack.info("MagicDb.__init__: Returned")

    def createDeckWizard(self):
        print("Placeholder")



        

myapp = MagicDb()

myapp.mainloop()
