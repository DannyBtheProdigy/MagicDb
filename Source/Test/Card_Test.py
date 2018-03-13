import unittest
import logging
from Tkinter import *
from Card.Card import Card


class TestCard(unittest.TestCase):
    
    def test_init(self):
        call_handle = logging.FileHandler("test_stack.txt")
        call_stack = logging.getLogger('call_stack')
        
        new_card = Card(call_stack, 0, "Frank", "C:\Users\DannyB\Pictures\Card_Images\DDP_AffaGuardHound.jpg")
        self.assertEqual(new_card._callstack, call_stack, "Call Stack not set correctly")
        self.assertEqual(new_card._id, 0, "Id not set correctly")
        self.assertEqual(new_card._name, "Frank", "Name not set correctly")
        self.assertEqual(new_card._im_file, "C:\Users\DannyB\Pictures\Card_Images\DDP_AffaGuardHound.jpg", "File Location not set correctly")
        
    def test_load_image(self):
        call_handle = logging.FileHandler("test_stack.txt")
        call_stack = logging.getLogger('call_stack')
        new_card = Card(call_stack, 0, "Frank", "C:\Users\DannyB\Pictures\Card_Images\DDP_AffaGuardHound.jpg")
        root = Tk()
        
        new_card.LoadImage()
        
        self.assertIsNotNone(new_card._image, "Image not Set")
        self.assertIsNotNone(new_card._tk_image, "Tk Image not Set")
        
        
    def test_remove_image(self):
        call_handle = logging.FileHandler("test_stack.txt")
        call_stack = logging.getLogger('call_stack')
        new_card = Card(call_stack, 0, "Frank", "C:\Users\DannyB\Pictures\Card_Images\DDP_AffaGuardHound.jpg")
        root = Tk()
        
        new_card.LoadImage()        
        new_card.RemoveImage()
        
        self.assertEqual(hasattr(new_card, '_image'), False, "Image not Deleted")
        self.assertEqual(hasattr(new_card, '_tk_image'), False, "Tk Image not Deleted")
        