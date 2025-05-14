import random
from collections import defaultdict, deque

# Constants
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RANK_VALUES = {str(i): i for i in range(2, 11)}
RANK_VALUES.update({'J': 15, 'Q': 20, 'K': 25, 'A': 30})

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def value(self):
        return RANK_VALUES[self.rank]

class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in SUITS for r in RANKS]
        random.shuffle(self.cards)

    def deal(self, num_players, cards_each):
        return [[self.cards.pop() for _ in range(cards_each)] for _ in range(num_players)]

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.tricks = []
        self.trick_count = 0

    def play_card(self):
        print(f"{self.name}'s hand: {[str(card) for card in self.hand]}")
        while True:
            choice = input(f"{self.name}, choose a card to play (e.g., 2 of Hearts): ")
            for card in self.hand:
                if str(card).lower() == choice.lower():
                    self.hand.remove(card)
                    return card
            print("Invalid choice. Try again.")

    def receive_trick(self, trick, runt_value):
        self.tricks.append((trick, runt_value))
        self.trick_count += 1

class TantonyGame:
    def __init__(self):
        self.players = [Player(f"Player {i+1}") for i in range(4)]
        self.current_leader = 0

    def play_game(self):
        for hand_num in range(4):
            print(f"\n=== HAND {hand_num + 1} ===")
            self.play_hand()

    def play_hand(self):
        deck = Deck()
        hands = deck.deal(4, 13)
        for i, player in enumerate(self.players):
            player.hand = hands[i]
            player.tricks.clear()
            player.trick_count = 0

        for trick_num in range(13):
            print(f"\n--- Trick {trick_num + 1} ---")
            trick, lead_suit = [], None
            player_order = deque(self.players)
            player_order.rotate(-self.current_leader)

            for player in player_order:
                card = player.play_card()
                if lead_suit is None:
                    lead_suit = card.suit
                trick.append((player, card))

            valid_trick = [c for p, c in trick if c.suit == lead_suit]
            winner = max(valid_trick, key=lambda c: RANKS.index(c.rank))
            winner_player = next(p for p, c in trick if c == winner)
            runt = min(valid_trick, key=lambda c: RANKS.index(c.rank))
            runt_value = runt.value()

            print(f"Trick won by {winner_player.name} with {winner}. Runt is {runt}, worth {runt_value} points.")

            # Full version: choose who gets the trick
            eligible_players = [p for p in self.players if p.trick_count < 3]
            print("Eligible players to receive the trick:")
            for idx, p in enumerate(eligible_players):
                print(f"{idx + 1}: {p.name} (has {p.trick_count} tricks)")

            while True:
                try:
                    choice = int(input(f"{winner_player.name}, choose a player to receive the trick (1-{len(eligible_players)}): "))
                    if 1 <= choice <= len(eligible_players):
                        chosen_player = eligible_players[choice - 1]
                        break
                except ValueError:
                    pass
                print("Invalid choice. Try again.")

            chosen_player.receive_trick(trick, runt_value)
            self.current_leader = self.players.index(chosen_player)

        self.score_hand()

    def score_hand(self):
        print("\n--- Scoring ---")
        team1_score = sum(trick[1] for player in self.players[::2] for trick in player.tricks)
        team2_score = sum(trick[1] for player in self.players[1::2] for trick in player.tricks)
        print(f"Team 1 (Player 1 & 3): {team1_score} points")
        print(f"Team 2 (Player 2 & 4): {team2_score} points")

if __name__ == "__main__":
    game = TantonyGame()
    game.play_game()
