import pypyodbc
import logging
from Card.Card import Card
from Deck.Deck import Deck

class DbIf:
    def __init__(self, CallStack):
        CallStack.info("DbIf.__init__: Called")

        self._callstack = CallStack

        module_log = logging.FileHandler("DbIf.txt")
        sql_log = logging.FileHandler("SqlLog.txt")
        self._log = logging.getLogger('DbIf')
        self._log.addHandler(module_log)
        self._sql_log = logging.getLogger('Sql')
        self._sql_log.addHandler(sql_log)
        self._sql_log.setLevel(logging.INFO)

        
        self._conn = pypyodbc.win_connect_mdb("..\..\..\..\MDbTest.mdb")
        self._cur = self._conn.cursor()
        
        self._callstack.info("DbIf.__init__: Returned")

    def GetAllCards(self):
        self._callstack.info("DbIf.GetAllCards: Called")

        next_transaction = "SELECT CardID, CardName, ImageLocation \
                            FROM UniqueCards"

        self._sql_log.info(next_transaction)
        self._cur.execute(next_transaction)

        sql_result = self._cur.fetchall()

        card_list = set()

        for entry in sql_result:
            card_list.add(Card(self._callstack, entry[0], entry[1], entry[2]))


        self._callstack.info("DbIf.GetAllCards: Returned")

        return card_list
    
    def GetAllDecks(self):
        self._callstack.info("DbIf.GetAllDecks: Called")
        
        next_transaction = "SELECT UniqueCards.ImageLocation, Decks.DeckName \
                            FROM UniqueCards \
                            RIGHT JOIN Decks \
                            ON UniqueCards.CardID = Decks.Headliner"
                            
        self._sql_log.info(next_transaction)
        self._cur.execute(next_transaction)
        
        sql_result = self._cur.fetchall()
        
        deck_list = set()
        for entry in sql_result:
            deck_list.add(Deck(self._callstack, entry[1], entry[0]))
        
        self._callstack.info("DbIf.GetAllDecks: Returned")
        
        return deck_list
        
