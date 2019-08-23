import random

# Deck Of Cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The Deck has : "+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self,card):
        # card passed in
        # from Deck.deal()  ---> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def show_some(player, dealer):
    print("\n--> Dealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\n--> Player's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print('\n'*100)
    print("\n--> Dealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\n--> Player's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


class NewChips:
    def __init__(self):
        self.funds = 100

    def balance(self):
        print(self.funds)

    def deposite(self,bet):     ######## if he wins
        self.funds = self.funds + bet
        print(f"Now you have {self.funds}")
        return self.funds

    def withdraw(self,bet):    ################ if he looses
        if self.funds >= bet:
            self.funds = self.funds - bet
            print(f"Now you have {self.funds}")
            return self.funds
        else:
            print("Not enough funds ")

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s : ")

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn ")
            playing = False

        else:
            print("Sorry, I did not understand that, Please enter h or s only :")
            continue

        break


def overview():
    print("OverView for the game""\n")
    print("# There would be a player and a dealer:")
    print("--> player will start with 100 chips in the account")
    print("--> Two cards each will be given to Player and the Dealer")
    print("--> Only one of the Dealer's cards would be shown, the other remains hidden")
    print("--> If the Player's hand is > 21 or Player's hand < Dealer's hand, Player loose !!!""\n")







act1 = NewChips()


turn = 0
print('\t\t'"Welcome To Black Jack""\n")
overview()
user = input("Would You Lke to Play A Game Of Black Jack [Y/N]:  ").lower()
while True:
    if turn == 0 and user[0] == 'y':



        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())


        try:
            bet = int(input("How much would you like to bet : "))
        except:
            print("Only enter integer's")
            continue

        if bet > act1.funds:
            print(f"You Don't have enough funds you have {act1.funds}")
            continue


        show_some(player_hand,dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function

            if act1.funds <= 1:
                print("Sorry you don't have enough funds to play")
                turn = 1
                break
            else:
                # Prompt for Player to Hit or Stand
                hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                print("You Loose ")
                act1.withdraw(bet)
            break

        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                print("You Win")
                act1.deposite(bet)
            elif dealer_hand.value > player_hand.value:
                print("You Loose")
                act1.withdraw(bet)
            elif dealer_hand.value < player_hand.value:
                print("You Win")
                act1.deposite(bet)
            else:
                print("The game is Tie!!")

        # Inform Player of their chips total
        print(f"\n Player total chips are at : {act1.funds}"'\n')

        if act1.funds <=1:
            print("You don't have enough funds to proceed, Thanks for playing")
            turn = 1
            break
        else:
            new_game = input("Would you like to play another hand [Y/N] :")
            if new_game[0].lower() == 'y':
                print('\n' * 100)
                turn = 0
                user = 'y'
                continue
        if new_game[0] == "n":
            print("Thanks for playing")
            turn = 1
            break

    else:
        print("Thank You")
        break

    break














