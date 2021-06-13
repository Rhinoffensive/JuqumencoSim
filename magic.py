suits = ['Clubs',  'Spikes', 'Hearts','Diamonds']
values = [*range(1,14)]

deck = []
for s in suits:
  for v in values:
    deck.append([s,v])
        
for item in deck:
    print(item)


class Table:
    def __init__(self) -> None:
        suits = ['Clubs',  'Spikes', 'Hearts','Diamonds']
        values = [*range(1,14)]

        self.deck = []

        for s in suits:
            for v in values:
                self.deck.append([s,v])
        
        #random.shuffle(self.deck)
        
        
        self.initial = self.deck.copy()

tab = Table()

for item in tab.initial:
    print(item)