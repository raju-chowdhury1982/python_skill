import itertools

shapes = ['spade', 'heart', 'club', 'daimond']
cards = ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", 'J', 'Q', 'K']

# deck = dict(itertools.product(shapes, cards))

# deck = [{shape:card} for shape in shapes for card in cards]
deck = dict([{shape:card} for shape in shapes for card in cards])

print(deck)
