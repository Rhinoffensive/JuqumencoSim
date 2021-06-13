import numpy as np
import random

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.isOpen = False
        self.isSelectable = False
        self.isDestroyed = False
    
    def update(self,table,top_card_val):
        if self.isDestroyed:
            self.isSelectable = False
            self.isOpen = False
            self.left = None
            self.right = None
            return
        if self.left is None or self.right is None:
            self.isOpen = True
        
        if self.left and self.right and table[self.left].isDestroyed and table[self.right].isDestroyed:
            self.isOpen = True

        if self.isOpen:
            absVal = abs(self.value[1] - top_card_val)

            self.isSelectable = absVal == 1 or absVal == 12 

    def __repr__(self) -> str:
        #return repr(str(self.isDestroyed))

        if self.isDestroyed:
            return repr(" ")
        elif self.isOpen and self.isSelectable:
            return repr("|"+str(self.value[1]+"|"))
        elif self.isOpen:
            return repr(str(self.value[1]))
        elif not self.isOpen:
            return repr("X")

class Table:
    def __init__(self) -> None:
        suits = ['Clubs', 'Diamonds', 'Spikes', 'Hearts']
        values = np.arange(1,14).tolist()

        deck = []

        for s in suits:
            for v in values:
                deck.append([s,v])
        
        random.shuffle(deck)
        
        self.deck = deck

    def generateTable(self):
        self.table = dict()
        for j in range(1,8):
            for i in range(1,j+1):
                n = Node(self.deck.pop())
                if j != 7:
                    n.left = (j+1) * 10 + i
                    n.right = (j+1) * 10 + (i+1)
                else:
                    pass
                    #n.isOpen = True
                self.table[j*10 + i] = n
        self.updateTable()
    
    def updateTable(self):
        for k in self.table.keys():
            self.table[k].update(self.table, self.deck[-1][1])

    def succes(self):
        for c in self.table.keys():
            if self.table[c].isDestroyed == False:
                return False
        print('Solved!!')
        return True

    def getSelectable(self):
        selectableList = []
        for k in self.table:
            if self.table[k].isSelectable:
                selectableList.append(k)
        return selectableList
        

