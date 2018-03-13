
import unittest
import logging
from Tkinter import *
from CardSet.CardSet import CardSet
from Mocks.DbIf import DbIf


class TestCardSet(unittest.TestCase):
    
    def test_init(self):
        call_handle = logging.FileHandler("test_stack.txt")
        call_stack = logging.getLogger('call_stack')
        
        dummy_dbif = 2
        
        new_cardset = CardSet(call_stack, dummy_dbif)
        self.assertEqual(new_cardset._callstack, call_stack, "Call Stack not set correctly")
        self.assertEqual(new_cardset._dbif, 2, "DbIf not set correctly")
        
    def test_loadcards(self):
        call_handle = logging.FileHandler("test_stack.txt")
        call_stack = logging.getLogger('call_stack')
        
        dummy_dbif = DbIf()
        
        new_cardset = CardSet(call_stack, dummy_dbif)
        
        new_cardset.LoadCards()
        
        
