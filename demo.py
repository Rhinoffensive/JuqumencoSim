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