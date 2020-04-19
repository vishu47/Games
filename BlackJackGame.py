#1st of all create the deck

import random
suits = ('hearts', 'diamonds', 'spades','clubs')
ranks = ('two', 'three','four','five','six','seven','eight','nine','ten','jack','king','queen','ace')
values = {'two':2, 'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'king':10,'queen':10,'ace':11}

playing = True

#create the card class
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit

# test_card = Card('spade','two')
# print(test_card)

#create the deck class
class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ' '
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "this deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# test_hand = Deck()
# p = test_hand.deal()
# print(p)

class Hand():   #creating the player hand

    def __init__(self):
        self.cards = []   #start with the empty list
        self.value = 0    #value of the hand start with Zero
        self.aces = 0     #adjustment of the aces

    def add_card(self,card):     #card object from Deck.deal()-->single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
    #track the aces
        if card.rank == 'ace':
            self.aces += 1
    def adjust_for_ace(self):
        while self.value>21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

#creating the chips class
class Chips():
    def __init__(self):    #if you define total like self,total=100 it means user can chenge the chips value
        self.total = 100   #but in this case user can not change the chips value
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

#write the function for taking bets
def take_bet(chips):
    while True:      #we use while here to continually prompt the user input untill we recieved an integer
        try:
            chips.bet = int(input("how many chips would like to bet? "))
        except:
            print("Sorry! Please provide the integer ")
        else:
            if chips.bet > chips.total:
                print("oops! you didn't have enough chips.You have only: {} ".format(chips.total))
            else:
                break

#write a function for taking hits
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

#write function promptint the player hit or stand
def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("Hit or Stand? please provide h or s: ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stands and Dealer's turn")
            playing = False
        else:
            print("Sorry! i didn't understand that, Please enter h or s only: ")
            continue
        break

#write funcion to handle the end of the game scenarios
def show_some(player,dealer):
    print('\n dealers_hand')
    print("<card hidden>")
    print('',dealer.cards[1])
    print("\n players_hand: ", *player.cards, sep = '\n')

def show_all(player,dealer):

    print("\ndealers_hand: ", *dealer.cards, sep = '\n')
    print("\ndealers_hand= ",dealer.value)
    print("\nplayers_hand: ", *player.cards, sep = '\n')
    print("\nplayers_hand: ", player.value)

    #remeber pass player's hand dealer's hand and chips itself
def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("PLAYER WIN!")
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print("PLAYER WIN! DEALER BUSTED")
    chips.lose_bet()
def dealer_wins(player,dealer,chips):
    print("DEALER WIN!")
    chips.win_bet()
def push(player,dealer):
    print("Dealer and Player TIE! PUSH")


#Now on the game logic

while True:
    #print opening statement
    print("WELCOME TO THA BLACK JACK GAME!!!")
    #create and shuffle the deck,deal two cards to each player
    deck = Deck()
    deck.shuffle()

    players_hand = Hand()
    players_hand.add_card(deck.deal())
    players_hand.add_card(deck.deal())

    dealers_hand = Hand()
    dealers_hand.add_card(deck.deal())
    dealers_hand.add_card(deck.deal())

    #set up players chips
    players_chips = Chips()
    #prompt the player to the bet
    take_bet(players_chips)

    # Show cards(but keep one dealer card hidden)
    show_some(players_hand, dealers_hand)

    while playing:   #recall thos variable from our hit and stand function

        #prompt for player hit or stand
        hit_or_stand(deck,players_hand)

        # Show cards(but keep one dealer card hidden)
        show_some(players_hand, dealers_hand)

        #if players cards exceed 21,run player busts() and break out of the loop
        if players_hand.value > 21:
            player_busts(players_hand ,dealers_hand,players_chips)
            break
    #if player han not busted,play dealers hand until dealer reaches < players and
    if players_hand.value <= 21:
        while dealers_hand.value < players_hand.value:
            hit(deck,dealers_hand)
        #show all cards
        show_all(players_hand,dealers_hand)
            #run differnt winning scenarios
        if dealers_hand.value > 21:
            dealer_busts(players_hand,dealers_hand,players_chips)
        elif dealers_hand.value > players_hand.value:
            dealer_wins(players_hand,dealers_hand,players_chips)
        elif dealers_hand.value < players_hand.value:
            player_wins(players_hand,dealers_hand,players_chips)
        else:
            push(players_hand,dealers_hand)

        #inform player to their chips total
    print("\n player total chips are {}".format(players_chips.total))

        #ask t play again
    new_game = input("Want to play another hand? y or n: ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for the Game!!!!")
        break



# test_hand = Hand()
# p = test_hand.add_card('clubs')
# print(p)

# test_deck = Deck()
# test_deck.shuffle()
# test_player = Hand()
# pulled_card = test_deck.deal()
# print(pulled_card)
# test_player.add_card(pulled_card)
# print(test_player.value)

