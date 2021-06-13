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