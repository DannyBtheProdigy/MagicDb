import logging


class CardSet:
    def __init__(self, CallStack, DbIf):
        CallStack.info("CardSet.__init__: Called")
        self._callstack = CallStack

        self._dbif = DbIf

        self._callstack.info("CardSet.__init__: Returned")


    def LoadCards(self):
        self._callstack.info("CardSet.LoadCards: Called")
        
        self._cardset = self._dbif.GetAllCards()

        for card in self._cardset:
            card.LoadImage()

        self._callstack.info("CardSet.LoadCards: Returned")
