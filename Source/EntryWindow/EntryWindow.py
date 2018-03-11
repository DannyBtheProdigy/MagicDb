'''
Created on Dec 19, 2017

@author: DannyB
'''
import Tkinter as tk

class EntryWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, takefocus=1,*args, **kwargs)
        self.title=("Please enter a database location")
        self.message = tk.Message(master=self, text="Stop being a dumbass")
        self.message.pack()

        self.button = tk.Button(master=self, text="I'm Sorry", command=self.destroy)
        self.button.pack()