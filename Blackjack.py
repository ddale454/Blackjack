import pygame, random

pygame.init()
screen = pygame.display.set_mode([1200, 600])
screen.fill([255,255,255])
x = 100
y = 100


_RANK_STRINGS = (
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
)

_SUITS = ["hearts", "diamonds", "spades", "clubs"]

class Card:
    rank: int
    suit: str

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return _RANK_STRINGS[self.rank - 1] + ' of ' + self.suit

deck = []
for card in range(1, 14):
    for suit in _SUITS:
        deck.append(Card(card, suit))
        
random.shuffle(deck)
hand = []
for deal in range(2):
    hand.append(deck.pop(0))

   

for card in hand:
    pygame.draw.rect(screen, [0,0,0], pygame.Rect(x, y, 300, 500), 1)
    name_font = pygame.font.Font(None, 25)
    name_render = name_font.render(str(card), 1, (0,0,0))
    name_pos = [x + 10, y + 10]
    screen.blit(name_render, name_pos);
    x += 310
pygame.display.flip()

running = True
while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                hand.append(deck.pop(0))

pygame.quit
