import random


class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.ranks.index(rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def deal(self):
        """Deals a card from the deck."""
        return self.cards.pop() if self.cards else None


class WarGame:

    def __init__(self):
        self.deck = Deck()
        self.user_hand = [self.deck.deal() for _ in range(26)]
        self.computer_hand = [self.deck.deal() for _ in range(26)]

    def play_round(self):
        if not self.user_hand or not self.computer_hand:
            return None  # The game is over

        user_card = self.user_hand.pop(0)
        computer_card = self.computer_hand.pop(0)

        print(f"\nYou play {user_card}")
        print(f"Computer plays {computer_card}")

        if user_card.value > computer_card.value:
            print("You win this round!")
            self.user_hand.extend([user_card, computer_card])
        elif user_card.value < computer_card.value:
            print("Computer wins this round!")
            self.computer_hand.extend([user_card, computer_card])
        else:
            print("It's a tie! Time for war!")
            self.tie([user_card], [computer_card])

    def tie(self, user_pile, computer_pile):
        """Handles the war scenario when there's a tie."""
        if len(self.user_hand) < 4 or len(self.computer_hand) < 4:
            print("Not enough cards for war. The game ends.")
            return

        user_pile.extend([self.user_hand.pop(0) for _ in range(3)])
        computer_pile.extend([self.computer_hand.pop(0) for _ in range(3)])

        print("\nWar cards placed!")
        print(f"You place {', '.join(str(card) for card in user_pile[-3:])}")
        print(f"Computer places {', '.join(str(card) for card in computer_pile[-3:])}")

        if self.user_hand and self.computer_hand:
            user_pile.append(self.user_hand.pop(0))
            computer_pile.append(self.computer_hand.pop(0))

            user_card = user_pile[-1]
            computer_card = computer_pile[-1]

            print(f"\nWar battle cards: You play {user_card}, Computer plays {computer_card}")
            if user_card.value > computer_card.value:
                print("You win the war!")
                self.user_hand.extend(user_pile + computer_pile)
            elif user_card.value < computer_card.value:
                print("Computer wins the war!")
                self.computer_hand.extend(user_pile + computer_pile)
            else:
                print("War again!")
                self.tie(user_pile, computer_pile)

    def check_winner(self):
        """Checks for the winner of the game."""
        if not self.user_hand:
            return "Computer wins the game!"
        elif not self.computer_hand:
            return "You win the game!"
        return None

    def start_game(self):
        """Starts the game and runs rounds until there is a winner."""
        print("Welcome to War! You vs. the Computer!")
        while True:
            result = self.check_winner()
            if result:
                print(result)
                break
            input("\nPress Enter to play the next round...")
            self.play_round()


game = WarGame()
game.start_game()
