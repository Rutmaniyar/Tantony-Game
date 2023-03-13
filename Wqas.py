import random


class Player:
    def __init__(self, name, hand, trick_won=None, Runt_Face=None):
        self.name = name
        self.hand = hand
        self.trick_won = []
        self.Runt_Face = []

    def __repr__(self):
        return f"{self.name}: {self.hand}"


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"'{self.rank} of {self.suit}'"


class trick:
    def __init__(self, playerId, RuntValue, TrickCards):
        self.TrickAssignedTo = playerId
        self.RuntValue = RuntValue
        self.TrickCards = TrickCards

    def keeping_trick(player, TrickCards, runt_value):
        # Keeping the Trick
        #player_tricks = player#(player.name, player.hand)

        if (len(player.trick_won) <= 3):
            player.trick_won.append(TrickCards)
            player.Runt_Face.append(runt_value)
            print(f"The trick won are {player.trick_won}")
            print(f"The Runt faces are {player.Runt_Face}")
            return player
        else:
            print("You already have three tricks Please give it to any other player")
            trick.assign_trick(TrickCards, runt_value)

    def assign_trick(TrickCards, runt_value):
        # player.trick_won.append[TrickCards]
        assigned_to = str(
            input("Enter the name of the player you want to assign the trick:"))
        if (assigned_to == player1.name):
            if (len(player1.trick_won) <= 3):
                player1.trick_won.append(TrickCards)
                player1.Runt_Face.append(runt_value)
                print(player1.trick_won)
                return player1
            else:
                print(
                    "The Player already has three tricks you have to give to other player")
        if (assigned_to == player2.name):
            if (len(player2.trick_won) <= 3):
                player2.trick_won.append(TrickCards)
                player2.Runt_Face.append(runt_value)
                print(player2.trick_won)
                trick.playingtrick(player2)
                return player2
            else:
                print(
                    "The Player already has three tricks you have to give to other player")
        if (assigned_to == player3.name):
            if (len(player3.trick_won) <= 3):
                player3.trick_won.append(TrickCards)
                player3.Runt_Face.append(runt_value)
                print(player3.trick_won)
                trick.playingtrick(player3)
                return player3
            else:
                print(
                    "The Player already has three tricks you have to give to other player")
        if (assigned_to == player4.name):
            if (len(player4.trick_won) <= 3):
                player4.trick_won.append(TrickCards)
                player4.Runt_Face.append(runt_value)
                print(player4.trick_won)
                trick.playingtrick(player4)
                return player4
            else:
                print(
                    "The Player already has three tricks you have to give to other player")

        # player_value = [players for players in player if player.name == assigned_to]
        # print(player_value)

        # if(len(player.trick_won) <= 3):
        #     player.trick_won.append(TrickCards)
        #     player.Runt_Face.append(runt_value)
        #     #Trick = trick('123',trick_cards,player.name)
        #     print('Tricks In Hand',player.trick_won)
        #     # print('Players Turn',Trick.PlayerTurn)
        # else:
        #     print("The Player already has three tricks in his hand Can't be assigned to this player")

    def playingtrick(player):
        # Turn issue can not differentiate between the turn in parameter and other data because of conflict
        #i = 0
        #while i <= num_cards:
         #   i = i + 1
        for i in range(num_cards):
            sel=[]
            print("-----------------------------------------------------------------------------------------------")
            #print("Hand:", i)
            if (player.name == player1.name):
                print(
                    "-----------------------------------------------------------------------------------------------")
                print(player1.name, "Turn")
                print("Cards in Hand for ", player1.name, ":", player1.hand)
                selected_card1_index = int(
                    input("Enter the position of the card you want to select: "))
                selected_card1 = player1.hand.select_card(
                    selected_card1_index-1)
                sel.append(selected_card1)
                print(f"The selected card is :{selected_card1}")
                print(
                    "-----------------------------------------------------------------------------------------------")
                print(player2.name, "Turn")
                print("Cards in Hand for ", player2.name, ":", player2.hand)
                selected_card2_index = int(
                    input("Enter the position of the card you want to select: "))
                selected_card2 = player2.hand.select_card(
                    selected_card2_index-1)
                print(f"The selected card is :{selected_card2}")
                sel.append(selected_card2)
                print(
                    "-----------------------------------------------------------------------------------------------")
                print(player3.name, "Turn")
                print("Cards in Hand for ", player3.name, ":", player3.hand)
                selected_card3_index = int(
                    input("Enter the position of the card you want to select: "))
                selected_card3 = player3.hand.select_card(
                    selected_card3_index-1)
                print(f"The selected card is :{selected_card3}")
                sel.append(selected_card3)
                print(
                    "-----------------------------------------------------------------------------------------------")
                if game_type == 4:
                    print(player4.name, "Turn")
                    print("Cards in Hand for ", player4.name, ":", player4.hand)
                    selected_card4_index = int(
                        input("Enter the position of the card you want to select: "))
                    selected_card4 = player4.hand.select_card(
                        selected_card4_index-1)
                    print(f"The selected card is :{selected_card4}")
                    sel.append(selected_card4)
                    print(
                        "-----------------------------------------------------------------------------------------------")
            if (player.name == player2.name):
                print(
                    "-----------------------------------------------------------------------------------------------")
                print(player2.name, "Turn")
                print("Cards in Hand for ", player2.name, ":", player2.hand)
                selected_card2_index = int(
                    input("Enter the position of the card you want to select: "))
                selected_card2 = player2.hand.select_card(
                    selected_card2_index-1)
                print(f"The selected card is :{selected_card2}")
                sel.append(selected_card2)
                print(
                    "-----------------------------------------------------------------------------------------------")
                print(player3.name, "Turn")
                print("Cards in Hand for ", player3.name, ":", player3.hand)
                selected_card3_index = int(
                    input("Enter the position of the card you want to select: "))
                selected_card3 = player3.hand.select_card(
                    selected_card3_index-1)
                print(f"The selected card is :{selected_card3}")
                sel.append(selected_card3)
                print(
                    "-----------------------------------------------------------------------------------------------")
                
                if game_type == 4:
                    print(player4.name, "Turn")
                    print("Cards in Hand for ", player4.name, ":", player4.hand)
                    selected_card4_index = int(
                        input("Enter the position of the card you want to select: "))
                    selected_card4 = player4.hand.select_card(
                        selected_card4_index-1)
                    print(f"The selected card is :{selected_card4}")
                    sel.append(selected_card4)
                    print(
                        "-----------------------------------------------------------------------------------------------")
                print(player1.name, "Turn")
                print("Cards in Hand for ", player1.name, ":", player1.hand)
                selected_card1_index = int(
                    input("Enter the position of the card you want to select: "))
                selected_card1 = player1.hand.select_card(
                    selected_card1_index-1)
                print(f"The selected card is :{selected_card1}")
                sel.append(selected_card1)
                print(
                    "-----------------------------------------------------------------------------------------------")
            if (player.name == player3.name):
                print(
                    "-----------------------------------------------------------------------------------------------")
                print(player3.name, "Turn")
                print("Cards in Hand for ", player3.name, ":", player3.hand)
                selected_card3_index = int(
                    input("Enter the position of the card you want to select: "))
                selected_card3 = player3.hand.select_card(
                    selected_card3_index-1)
                print(f"The selected card is :{selected_card3}")
                sel.append(selected_card3)
                
                if game_type == 4:
                    print(player4.name, "Turn")
                    print("Cards in Hand for ", player4.name, ":", player4.hand)
                    selected_card4_index = int(
                        input("Enter the position of the card you want to select: "))
                    selected_card4 = player4.hand.select_card(
                        selected_card4_index-1)
                    print(f"The selected card is :{selected_card4}")
                    sel.append(selected_card4)
                    print(
                        "-----------------------------------------------------------------------------------------------")
                    print(
                    "-----------------------------------------------------------------------------------------------")
                print(player1.name, "Turn")
                print("Cards in Hand for ", player1.name, ":", player1.hand)
                selected_card1_index = int(
                    input("Enter the position of the card you want to select: "))
                selected_card1 = player1.hand.select_card(
                    selected_card1_index-1)
                print(f"The selected card is :{selected_card1}")
                sel.append(selected_card1)
                print(
                    "-----------------------------------------------------------------------------------------------")
                print(player2.name, "Turn")
                print("Cards in Hand for ", player2.name, ":", player2.hand)
                selected_card2_index = int(
                    input("Enter the position of the card you want to select: "))
                selected_card2 = player2.hand.select_card(
                    selected_card2_index-1)
                print(f"The selected card is :{selected_card2}")
                sel.append(selected_card2)
                print(
                    "-----------------------------------------------------------------------------------------------")
            if game_type == 4:
                if (player.name == player4.name):
                    print(
                        "-----------------------------------------------------------------------------------------------")
                    print(player4.name, "Turn")
                    print("Cards in Hand for ", player4.name, ":", player4.hand)
                    selected_card4_index = int(
                        input("Enter the position of the card you want to select: "))
                    selected_card4 = player4.hand.select_card(
                        selected_card4_index-1)
                    print(f"The selected card is :{selected_card4}")
                    sel.append(selected_card4)
                    print(
                        "-----------------------------------------------------------------------------------------------")
                    print(player1.name, "Turn")
                    print("Cards in Hand for ", player1.name, ":", player1.hand)
                    selected_card1_index = int(
                        input("Enter the position of the card you want to select: "))
                    selected_card1 = player1.hand.select_card(
                        selected_card1_index-1)
                    print(f"The selected card is :{selected_card1}")
                    sel.append(selected_card1)
                    print(
                        "-----------------------------------------------------------------------------------------------")
                    print(player2.name, "Turn")
                    print("Cards in Hand for ", player2.name, ":", player2.hand)
                    selected_card2_index = int(
                        input("Enter the position of the card you want to select: "))
                    selected_card2 = player2.hand.select_card(
                        selected_card2_index-1)
                    print(f"The selected card is :{selected_card2}")
                    sel.append(selected_card2)
                    print(
                        "-----------------------------------------------------------------------------------------------")
                    print(player3.name, "Turn")
                    print("Cards in Hand for ", player3.name, ":", player3.hand)
                    selected_card3_index = int(
                        input("Enter the position of the card you want to select: "))
                    selected_card3 = player3.hand.select_card(
                        selected_card3_index-1)
                    print(f"The selected card is :{selected_card3}")
                    sel.append(selected_card3)
                    print(
                        "-----------------------------------------------------------------------------------------------")
           
            trick_values = get_winning_card(sel)
            Trick_cards = trick_values[0]
            Runt_value = trick_values[3]
            print("Trick Cards:", Trick_cards)
            win_player =None
            if(sel[trick_values[2]] == selected_card1):
                print("Trick Winner:", player1.name)
                win_player=player1
            if(sel[trick_values[2]] == selected_card2):
                print("Trick Winner:", player2.name)
                win_player=player2
            if(sel[trick_values[2]] == selected_card3):
                print("Trick Winner:", player3.name)
                win_player=player3
            if game_type == 4: 
                if(sel[trick_values[2]] == selected_card4):
                    print("Trick Winner:", player4.name)
                    win_player=player4

            Trick_assign = str(
                input("Do you want to keep the trick or give it to someone? (Keep/Give):"))
            if (Trick_assign == "Keep"):
                player = trick.keeping_trick(
                    win_player, Trick_cards, Runt_value)
            if (Trick_assign == "Give"):
                player = trick.assign_trick(Trick_cards, Runt_value)


class Deck:
    def __init__(self):
        suits = ["\u2764\ufe0f", "\u2666", "\U00002660", "\u2663"]
        if(game_type == 4):
            ranks = ["Ace", "2", "3", "4", "5", "6", "7",
                    "8", "9", "10", "Jack", "Queen", "King"]
        else:
            ranks = ["Ace", "2", "3", "4", "5", "6", "Jack", "Queen", "King"]
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()


def get_points(card):
    #print(card)
    if num_cards == 13:
        rank_points = {"Ace": 30, "King": 25, "Queen": 20, "Jack": 15, "10": 10,
                       "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    else:
        rank_points = {"Ace": 25, "King": 20, "Queen": 15, "Jack": 10, "6": 6,
                       "5": 5, "4": 4, "3": 3, "2": 2}
    return rank_points[card.rank]


def get_winning_card(cards):
    print(cards)
    suit = cards[0].suit
    trick =cards #[card1, card2, card3]
    #cards = [card for card in [card1, card2, card3] if card.suit == suit]
    #if card4:
    #    cards.append(card4)
    #    trick.append(card4)
    car = [card for card in cards if card.suit == suit]
    if len(cards) == 0:
        print("No winning card as no cards have the same suit as the first card.")
        return
    points = [get_points(card) for card in car]
    max_point = max(points)
    winning_card = car[points.index(max_point)]
    print(f"Winning card: {winning_card}")

    min_point = min(points)
    runt_card = car[points.index(min_point)]
    print(f"Runt card: {runt_card} and the points are {min_point}")
    return [trick, min_point, trick.index(winning_card), runt_card]


class Hand:
    def __init__(self, deck, cards_per_hand):
        self.hand = [deck.draw() for _ in range(cards_per_hand)]

    def select_card(self, index):
        selected_card = self.hand.pop(index)
        return selected_card

    def __repr__(self):
        return str(self.hand)

print("-------------------------------------------------------------------------------------------------")
game_type = int(input(
    "Enter the Type of the Game: \n 4 for Partnership \n 3 for Three Player \n"))
print("-------------------------------------------------------------------------------------------------")
if game_type == 4:
    num_cards = 13
else:
    num_cards = 12


print("-------------------------------------------------------------------------------------------------")
name1 = input("Enter the Player 1 name: ")
name2 = input("Enter the Player 2 name: ")
name3 = input("Enter the Player 3 name: ")
if num_cards == 13:
    name4 = input("Enter the Player 4 name: ")
print("-------------------------------------------------------------------------------------------------")


def cutting_for_dealer(game_type, Listplayer):
    Leader_cards = []
    print("----------------------------- Assigning Leader ----------------------------------------------")
    for i in range(game_type):
        deck = Deck()
        deck.shuffle()
        Leader_cards.append(deck.draw())
        print(f"The Card is {Leader_cards[i]} for '{Listplayer[i].name}'")
    return Leader_cards

def get_current_player(players, current_turn):
    return players[current_turn % len(players)]

def assigning_dealer(New_card1, New_card2, New_card3, New_card4=None):
    # Error for Three player version
    newcards = [new_card for new_card in [New_card1, New_card2, New_card3]]
    if New_card4:
        newcards.append(New_card4)
    newcards = [new_card for new_card in newcards]
    print(newcards)
    points = [get_points(new_card) for new_card in newcards]
    print("points",points)
    min_point = min(points)
    winning_card = newcards[points.index(min_point)]
    if (winning_card == New_card1):
        winning_player = player1
    if (winning_card == New_card2):
        winning_player = player2
    if (winning_card == New_card3):
        winning_player = player3
    if (winning_card == New_card4):
        winning_player = player4
    print("---------------------------------------------------------------------------------------------------")
    
    print(f"Highest Card: {winning_card} & the dealer is {winning_player.name}")

    print("---------------------------------------------------------------------------------------------------")
    return winning_player


print("-------------------------------------------------------------------------------------------------")

deck = Deck()
deck.shuffle()
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

List_player = [player1, player2, player3]
if num_cards == 13:
    player4 = Player(name4, hand4)
    List_player.append(player4)

Leading_player = cutting_for_dealer(game_type, Listplayer=List_player)
if (game_type == 4):
    assigned_leader = assigning_dealer(
        Leading_player[0], Leading_player[1], Leading_player[2], Leading_player[3])
if (game_type == 3):
    assigned_leader = assigning_dealer(
        Leading_player[0], Leading_player[1], Leading_player[2])
lime_pos = (List_player.index(assigned_leader) + 1) % int(game_type)
Dealer_left = List_player[lime_pos]

print(player1)
print(player2)
print(player3)
if num_cards == 13:
    print(player4)


trick.playingtrick(Dealer_left)
