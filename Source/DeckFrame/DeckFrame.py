import Tkinter as tk
import logging
from DbIf.DbIf import DbIf
from DeckSet.DeckSet import DeckSet
from Tkinter import Label
from tkFont import Font

class DeckFrame(tk.Frame):
    def __init__(self, Width, CallStack, DbIf):
        CallStack.info("DeckFrame.__init__: Called")
        self._callstack = CallStack

        tk.Frame.__init__(self, width=Width)
        
        module_log = logging.FileHandler("DeckFrame.txt")
        self._log = logging.getLogger('DeckFrame')
        self._log.addHandler(module_log)

        self.canvas= tk.Canvas(width=300, height=1200)
        self.canvas.grid(row=1, column=0, rowspan=10)

        self._deckset = DeckSet(self._callstack, DbIf)
        self._deckset.LoadDecks()
        
        x_coord = 0
        y_coord = 0
        row_count = 2

        for deck in self._deckset._deckset:
            item = self.canvas.create_image(x_coord, y_coord, image=deck._tk_image, anchor="nw", tags="deck")
            self.canvas.create_text((110, (y_coord + 325)), text=deck._name, font=Font(size=15, weight="bold"))
            y_coord = y_coord + 370
            row_count = row_count + 1


        self.scroll = tk.Scrollbar(orient="vertical")
        self.scroll.config(command=self.canvas.yview)

        self.canvas.config(scrollregion=(0, 0, 10000, (row_count * 450)), yscrollcommand=self.scroll.set)
        
        self.scroll.grid(row=1, column=1, rowspan=5, sticky="n s e")

        CallStack.info("DeckFrame.__init__: Returned")

        
        
