from mahjong.tile import TilesConverter
import random

class GameManager:
    CURRENT_DECK=[]
    WANPAI=[]

    def __init__(self):
        for i in range(0,136):
            self.CURRENT_DECK.append(i)
        random.shuffle(self.CURRENT_DECK)
        for i in range (0,14):
            self.WANPAI.append(self.CURRENT_DECK[122+i])

    def get(self):
        print(self.CURRENT_DECK)
        print(self.WANPAI)
            





    ##@staticmethod
    ##def start():


        

