'''
Created on May 26, 2018

@author: DannyB
'''
from Card.Card import Card


class CardRequester(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        
    def GetAllCards(self):
        self._callstack.info("CardRequester.GetAllCards: Called")

        next_transaction = "SELECT CardID, CardName, ImageLocation \
                            FROM UniqueCards"

        self._sql_log.info(next_transaction)
        self._cur.execute(next_transaction)

        sql_result = self._cur.fetchall()

        card_list = set()

        for entry in sql_result:
            card_list.add(Card(self._callstack, entry[0], entry[1], entry[2]))


        self._callstack.info("CardRequester.GetAllCards: Returned")

        return card_list