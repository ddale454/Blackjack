import pygame, random

pygame.init()
screen = pygame.display.set_mode([1800, 900])
screen.fill([255,255,255])
x = 100
y = 500


_RANK_STRINGS = (
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
)

_SUITS = ["hearts", "diamonds", "spades", "clubs"]

_CARD_WIDTH = 150
_CARD_HEIGHT = 300
_CARD_SPACING = 10

class Card:
    rank: int
    suit: str

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return _RANK_STRINGS[self.rank - 1] + ' of ' + self.suit

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(x, y, _CARD_WIDTH, _CARD_HEIGHT), 1)
        name_font = pygame.font.Font(None, 25)
        name_render = name_font.render(str(self), 1, (0, 0, 0))
        name_pos = [x + 10, y + 10]
        screen.blit(name_render, name_pos);

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def value(self):
        return 0

    def draw(self, screen, x, y):
        for card in self.cards:
            card.draw(screen, x, y)
            x += _CARD_WIDTH + _CARD_SPACING

deck = []
for card in range(1, 14):
    for suit in _SUITS:
        deck.append(Card(card, suit))
        
random.shuffle(deck)
hand = Hand()
for deal in range(2):
    hand.add_card(deck.pop(0))

hand.draw(screen, x, y)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                hand.add_card(deck.pop(0))
                screen.fill((255, 255, 255))
                hand.draw(screen, x, y)
                pygame.display.flip()

pygame.quit
