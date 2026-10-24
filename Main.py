import GameRunner

class MAI:
    CURRENT_HAND=[]

    def _init_(self, deck):
        temp = [int(x) for x in deck.split(",")]
        if(temp.length != 13):
            return False
        self.CURRENT_HAND = temp

GR = GameRunner.GameManager()
GR.get()
P1
P2
P3
P4

##Game Start
#TODO Give random deck to player

#TODO Enter Current deck
currentDeck = input("Whats your current deck?")
MAI = MAI(currentDeck)
#TODO Find quickest path to shanten
