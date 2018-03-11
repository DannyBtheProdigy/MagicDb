import logging

class DeckSet:
    def __init__(self, CallStack, DbIf):
        CallStack.info("DeckSet.__init__: Called")
        self._callstack = CallStack

        self._dbif = DbIf

        self._callstack.info("DeckSet.__init__: Called")


    def LoadDecks(self):
        self._callstack.info("DeckSet.LoadDecks: Called")

        self._deckset = self._dbif.GetAllDecks()

        for deck in self._deckset:
            deck.LoadImage()

        self._callstack.info("DeckSet.LoadDecks: Returned")
