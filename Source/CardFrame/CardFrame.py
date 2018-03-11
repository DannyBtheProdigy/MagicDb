import Tkinter as tk
import logging
from DbIf.DbIf import DbIf
from CardSet.CardSet import CardSet
from PIL import Image
from PIL import ImageTk

class CardFrame(tk.Frame):
    def __init__(self, Width, CallStack, DbIf):
        CallStack.info("CardFrame.__init__: Called")
        self._callstack = CallStack
        
        tk.Frame.__init__(self, width=Width)


        module_log = logging.FileHandler("CardFrame.txt")
        self._log = logging.getLogger('CardFrame')
        self._log.addHandler(module_log)        

        self.canvas = tk.Canvas(width=1000, height=1200)
        
        self._drag_data = {"x": 0, "y": 0, "item": None}

        self._start_data = {"x": 0, "y": 0}

        self._cardset = CardSet(self._callstack, DbIf)

        self._cardset.LoadCards()

        x_coord = 0
        y_coord = 0
        row_count = 2

        for card in self._cardset._cardset:
            item = self.canvas.create_image(x_coord, y_coord, image=card._tk_image, anchor="nw", tags="image")
            x_coord = x_coord + 250
            if x_coord > 900:
                x_coord = 0
                y_coord = y_coord + 350
                row_count = row_count + 1

        
        self.scroll = tk.Scrollbar(orient="vertical")
        self.scroll.config(command=self.canvas.yview)

        self.canvas.config(scrollregion=(0, 0, 10000, (row_count * 350)), yscrollcommand=self.scroll.set)
        
        self.canvas.grid(row=1, column=2, rowspan=10, columnspan=10)
        self.scroll.grid(row=1, column=13, rowspan=5, sticky="n s e")
        
        self.canvas.tag_bind("image", "<ButtonPress-1>", self.OnTokenButtonPress)
        self.canvas.tag_bind("image", "<ButtonRelease-1>", self.OnTokenButtonRelease)
        self.canvas.tag_bind("image", "<B1-Motion>", self.OnTokenMotion)
        
        self.searchBar = tk.Entry()
        self.searchBar.grid(row=0, column=9, columnspan=3, sticky="ew")
        self.searchBar.bind("<Key>", self.Search)
        
        self._callstack.info("CardFrame.__init__: Returned")
        
    def OnTokenButtonPress(self, event):
        self._callstack.info("CardFrame.OnTokenButtonPress: Called")
        '''Begin drag of an object'''
        # find the slider offset to calculate "true" coordinates
        offset_pcnt = self.scroll.get()[0]
        offset = 12000 * offset_pcnt
        adjusted_y = event.y + offset
        
        # record the item and its location
        self._drag_data["item"] = self.canvas.find_closest(event.x, adjusted_y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = adjusted_y
        self._start_data["x"] = event.x
        self._start_data["y"] = adjusted_y
        self._callstack.info("CardFrame.OnTokenButtonPress: Returned")

    def OnTokenButtonRelease(self, event):
        self._callstack.info("CardFrame.OnTokenButtonRelease: Called")
        '''End drag of an object'''
        # find the slider offset to calculate "true" coordinates
        offset_pcnt = self.scroll.get()[0]
        offset = 12000 * offset_pcnt
        adjusted_y = event.y + offset
        
        # reset the drag information
        delta_x = self._start_data["x"] - self._drag_data["x"]
        delta_y = self._start_data["y"] - self._drag_data["y"]
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)

#         if event.x < 0:
#             deckNum = self.deckFrame.deckList.find_closest(event.x, adjusted_y)[0]
#             cardName = ""
# 
#             for card in self._cardSet:
#                 if card[0] == self._drag_data["item"]:
#                     cardName = card[1]
#                     cardID = card[2]
# 
#             for deck in self._deckSet:
#                 if deck[0]== deckNum:
#                     if "Main" == self._view:
#                         self._cur.execute("INSERT INTO Collection \
#                                           (CardID, Deck) \
#                                           VALUES (?, ?)", \
#                                           (cardName, deck[1]))
#                         self._conn.commit()
#                     if "Collection" == self._view:
#                         self._cur.execute("UPDATE Collection \
#                                           SET Deck=? \
#                                           WHERE ID=?", \
#                                           (deck[1], cardID))
#                         self._conn.commit()
#                     if "Deck" == self._view:
#                         self._cur.execute("UPDATE Collection \
#                                           SET Deck=? \
#                                           WHERE ID=?", \
#                                           (deck[1], cardID))
#                         self._conn.commit()
#                         self.SwitchToDeckView()
            
        
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0
        self._callstack.info("CardFrame.OnTokenButtonRelease: Returned")
        

    def OnTokenMotion(self, event):
        self._callstack.info("CardFrame.OnTokenMotion: Called")
        '''Handle dragging of an object'''
        # find the slider offset for to calculate "true" coordinates
        offset_pcnt = self.scroll.get()[0]
        offset = 12000 * offset_pcnt
        adjusted_y = event.y + offset

        
        # compute how much this object has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = adjusted_y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = adjusted_y
        
        self._callstack.info("CardFrame.OnTokenMotion: Returned")
        
    def Search(self, event):
        self._callstack.info("CardFrame.Search: Called")
        
        self.canvas.delete("all")
        self._tkim.clear()
        self._cardSet.clear()

        self.scroll.set(self._scroll_base[0], self._scroll_base[1])
        self.canvas.yview_moveto(0.0)

        if 'A' < event.char:        
            search_string = self.searchBar.get() + event.char
            
        else:
            search_string = self.searchBar.get()
            
#         if "Main" == self._view:
        self._cur.execute("SELECT ImageLocation, CardID \
                              FROM UniqueCards \
                              WHERE CardName BETWEEN ? AND ?", \
                              (search_string, (search_string + 'z')))
        fileStrings = self._cur.fetchall()

        for image_file in fileStrings:
            im = Image.open(image_file[0])
            self._tkim.add((ImageTk.PhotoImage(im), image_file[1]))

        x_coord = 0
        y_coord = 0

        for new_image in self._tkim:
            card = self.frame.canvas.create_image(x_coord, y_coord, image=new_image[0], anchor="nw", tags="image")
            self._cardSet.add((card, new_image[1], 0))
            x_coord = x_coord + 250
            if x_coord > 900:
                x_coord = 0
                y_coord = y_coord + 350

#         if "Collection" == self._view:
#             self._cur.execute("SELECT UniqueCards.ImageLocation, UniqueCards.CardID, Collection.ID \
#                   FROM UniqueCards \
#                   RIGHT JOIN Collection \
#                   ON UniqueCards.CardID = Collection.CardId \
#                   WHERE CardName BETWEEN ? AND ?", \
#                   (search_string, (search_string + 'z')))
# 
# 
#             fileStrings = self._cur.fetchall()
# 
#             for image_file in fileStrings:
#                 im = Image.open(image_file[0])
#                 self._tkim.add((ImageTk.PhotoImage(im), image_file[1], image_file[2]))
# 
#             x_coord = 0
#             y_coord = 0
# 
#             for new_image in self._tkim:
#                 card = self.frame.canvas.create_image(x_coord, y_coord, image=new_image[0], anchor="nw", tags="image")
#                 self._cardSet.add((card, new_image[1], new_image[2]))
#                 x_coord = x_coord + 250
#                 if x_coord > 900:
#                     x_coord = 0
#                     y_coord = y_coord + 350
# 
#         if "Deck" == self._view:
#             self._cur.execute("SELECT UniqueCards.ImageLocation, UniqueCards.CardID, Collection.ID \
#                   FROM UniqueCards \
#                   RIGHT JOIN Collection \
#                   ON UniqueCards.CardID = Collection.CardId \
#                   WHERE Collection.Deck=? \
#                   AND UniqueCards.CardName BETWEEN ? AND ?", \
#                   (self._selectedDeck, search_string, (search_string + 'z')))
# 
# 
#             fileStrings = self._cur.fetchall()
# 
#             for image_file in fileStrings:
#                 im = Image.open(image_file[0])
#                 self._tkim.add((ImageTk.PhotoImage(im), image_file[1], image_file[2]))
# 
#             x_coord = 0
#             y_coord = 0
# 
#             for new_image in self._tkim:
#                 card = self.frame.canvas.create_image(x_coord, y_coord, image=new_image[0], anchor="nw", tags="image")
#                 self._cardSet.add((card, new_image[1], new_image[2]))
#                 x_coord = x_coord + 250
#                 if x_coord > 900:
#                     x_coord = 0
#                     y_coord = y_coord + 350
        
        self._callstack.info("CardFrame.Search: Returned")
        
