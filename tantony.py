import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class trick:
    def __init__(self,playerId, RuntValue, TrickCards):
        self.TrickAssignedTo=playerId
        self.RuntValue = RuntValue
        self.TrickCards = TrickCards

    def assign_trick(self,player,TrickCards):
        #player.trick_won.append[TrickCards]
        if(len(player.trick_won) <= 3):
            player.trick_won.append(TrickCards)
            #Trick = trick('123',trick_cards,player.name)
            print(f"Tricks In Hand {player.trick_won} and assined to {player.name}")
            # print('Players Turn',Trick.PlayerTurn)
        else:
            print("The Player already has three tricks in his hand Can't be assigned to this player")

    def keeping_trick(player,TrickCards):
        player = Player(player1.name,player1.hand,TrickCards)
        if(len(player.TricksinHand) <= 3):
            player.TricksinHand.append(TrickCards)
            Trick = trick('123',trick_cards,player.name)
            print('Tricks In Hand',player.TricksinHand)
            print('Players Turn',Trick.PlayerTurn)
        else:
            print("The Player already has three tricks in his hand Can't be assigned to this player")


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)
        
    def draw(self):
        return self.deck.pop()


def get_points(card):
    if num_cards == 13:
        rank_points = {"Ace": 30, "King": 25, "Queen": 20, "Jack": 15, "10": 10,
                   "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    else:
        rank_points = {"Ace": 25, "King": 20, "Queen": 15, "Jack": 10,"6": 6, 
                       "5": 5, "4": 4, "3": 3, "2": 2}
    return rank_points[card.rank]

def get_winning_card(card1, card2, card3, card4=None):
    suit = card1.suit
    trick = [card1,card2,card3]
    cards = [card for card in [card1, card2, card3] if card.suit == suit]
    if card4:
        cards.append(card4)
        trick.append(card4)
    cards = [card for card in cards if card.suit == suit]
    if len(cards) == 0:
        print("No winning card as no cards have the same suit as the first card.")
        return
    points = [get_points(card) for card in cards]
    max_point = max(points)
    winning_card = cards[points.index(max_point)]
    print(f"Winning card: {winning_card}")
    
    min_point = min(points)
    runt_card = cards[points.index(min_point)]
    print(f"Runt card: {runt_card} and the points is {min_point}")
    return [trick, min_point, trick.index(winning_card)]


class Hand:
    def __init__(self, deck, cards_per_hand):
        self.hand = [deck.draw() for _ in range(cards_per_hand)]
    
    def select_card(self,index):
        selected_card = self.hand.pop(index)
        return selected_card

    def __repr__(self):
        return str(self.hand)

class Player:
    def __init__(self, name, hand, trick_won=None):
        self.name = name
        self.hand = hand
        self.trick_won=[]
        
    def __repr__(self):
        return f"{self.name}: {self.hand}"

deck = Deck()
deck.shuffle()

print("-------------------------------------------------------------------------------------------------")
game_type = int(input("Enter the Type of the Game: \n 4 for Partnership \n 3 for Three Player \n"))
print("-------------------------------------------------------------------------------------------------")
if game_type == 4:
    num_cards = 13
else:
    num_cards = 12


print("-------------------------------------------------------------------------------------------------")
name1=input("Enter the Player 1 name: ")
name2=input("Enter the Player 2 name: ")
name3=input("Enter the Player 3 name: ")
if num_cards == 13:
    name4=input("Enter the Player 4 name: ")
print("-------------------------------------------------------------------------------------------------")


def cutting(game_type):
    for i in range (game_type):
        deck = Deck()
        deck.shuffle()
        print(f"The Card is {deck.draw()} for player ")


print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")

if num_cards == 12:
    for card in deck.deck:
        if card.rank in {"7", "8", "9", "10"}:
            deck.deck.remove(card)
    hand1 = Hand(deck, num_cards)
    hand2 = Hand(deck, num_cards)
    hand3 = Hand(deck, num_cards)
else:
    hand1 = Hand(deck, num_cards)
    hand2 = Hand(deck, num_cards)
    hand3 = Hand(deck, num_cards)
    hand4 = Hand(deck, num_cards)
player1 = Player(name1, hand1)
player2 = Player(name2, hand2)
player3 = Player(name3, hand3)
if num_cards == 13:
    player4 = Player(name4, hand4)

player1 = Player(name1, hand1)
player2 = Player(name2, hand2)
player3 = Player(name3, hand3)

List_player=[player1, player2, player3]
if num_cards == 13:
    player4 = Player(name4, hand4)
    List_player.append(player4)

print(player1)
print(player2)
print(player3)
if num_cards == 13:
    print(player4)


print("-----------------------------------------------------------------------------------------------")
selected_card1_index=int(input("Enter the position of the card you want to select: "))
selected_card1 = player1.hand.select_card(selected_card1_index-1)
print(f"The selected card is :{selected_card1}")

selected_card2_index=int(input("Enter the position of the card you want to select: "))
selected_card2 = player2.hand.select_card(selected_card2_index-1)
print(f"The selected card is :{selected_card2}")

selected_card3_index=int(input("Enter the position of the card you want to select: "))
selected_card3 = player3.hand.select_card(selected_card3_index-1)
print(f"The selected card is :{selected_card3}")
if num_cards == 13:
    selected_card4_index=int(input("Enter the position of the card you want to select: "))
    selected_card4 = player4.hand.select_card(selected_card4_index-1)
    print(f"The selected card is :{selected_card4}")

print("-----------------------------------------------------------------------------------------------")

tr = get_winning_card(selected_card1, selected_card2, selected_card3, selected_card4)

print("-----------------------------------------------------------------------------------------------")
win_player=List_player[tr[2]]
print(f"The cards are {tr[0]} the runt value is {tr[1]} and assigned to {win_player.name}")

print("-----------------------------------------------------------------------------------------------")
trick1=trick(tr[2],tr[1],tr[0])
trick1.assign_trick(win_player,tr[0])
print("-----------------------------------------------------------------------------------------------")