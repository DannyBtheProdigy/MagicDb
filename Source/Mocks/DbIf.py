import pypyodbc
import logging

class DbIf:
    def __init__(self):
        self.__intialized = True

    def GetAllCards(self):
        card_set = set()
        return card_set
    
    def GetAllDecks(self):
        return True
        