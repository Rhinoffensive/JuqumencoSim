import numpy as np
import random
import multiprocessing
import copy

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
        return repr(str(self.value[1]))

        if self.isDestroyed:
            return repr(" ")
        elif self.isOpen and self.isSelectable:
            return repr("|"+str(self.value[1])+"|")
        elif self.isOpen:
            return repr(str(self.value[1]))
        elif not self.isOpen:
            return repr("X")

class Table:
    def __init__(self) -> None:
        suits = ['Clubs',  'Spikes', 'Hearts','Diamonds']
        values = [1,2,3,4,5,6,7,8,9,10,11,12,13 ]
        

        self.deck = []

        for s in suits:
            for v in values:
                self.deck.append([s,v])
        
        random.shuffle(self.deck)
        
        
        self.initial = copy.deepcopy(self.deck)
        

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

    def getSelectables(self):
        selectableList = []
        for k in self.table:
            if self.table[k].isSelectable:
                selectableList.append(k)
        return selectableList

    def Select(self, i):
        if self.getSelectables():
            selected_index = self.getSelectables()[i]
            #print('I select '+ str(self.table[selected_index].value))
        else:
            return
        self.deck[-1][1] = self.table[selected_index].value[1]

        self.table[selected_index].isDestroyed = True
        self.updateTable()
        #DrawTable(self.table)

        #print('Top Card is ' + str(self.deck[-1][1]))

        return self

    def Draw(self):
        if len(self.deck)>0:
            #print(str(len(self.deck) - 1) + " cards remain in deck")
            self.updateTable()
            return self.deck.pop()
            
        else:
            return


def DrawTable(table):
    keys = table.keys()
    row_num = max(keys) // 10
    print_text = ""
    row = -1

    for k in keys:
        if row == k//10:
            print_text += " " + str(table[k]) + " "
        else:
            row = k // 10
            print_text  += "\n"
            print_text += " " * (row_num - row) + str(table[k])
    print(print_text)


def Solve(table, index):
    tab = table
    selectable = tab.getSelectables()
    for i in range(len(selectable)):
        p = multiprocessing.Process(target= tab.Select(i))

if __name__ == '__main__':
    for i in range(100000):
        
        tab = Table()
      
   
        tab.generateTable()

      
        #DrawTable(tab.table)

        while tab.deck:
            if tab.succes():
                print('Iteration num : ',i)
                for item in tab.initial:
                    print(item)
                
                print(tab.table)
                break
            
            if len(tab.getSelectables()) == 0:
                tab.Draw()
            else:
                tab.Select(0)

        

