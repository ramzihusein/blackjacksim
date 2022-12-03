import random
import matplotlib.pyplot as plt

#add class for deck of cards

class Deck:
    def __init__(self):
        self.suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
        self.face = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A": 11}
        self.deck = []
# creates a deck
    def create_deck(self):
        for suit in self.suits:
            for card in self.face:
                self.deck.append(Card(card, self.values[card], suit))
        return self.deck
# prints deck for testing purposes
    def print_deck(self):
        for card in self.deck:
            print(card.value,card.suit)
#shuffles deck
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        deal = random.choice(self.deck)
        self.deck.remove(deal)
        return deal

# resets deck
    def reset_deck(self):
        self.deck = []
        self.create_deck()
        self.shuffle()





#add class for each card

class Card:
    def __init__(self, face, value, suit):
        self.value = value
        self.face = face
        self.suit = suit
    def print_card(self):
        print(self.face, self.value, self.suit)

#function for game flow
def blackjack(deck):
    cards_dealer = []
    cards_player = []
    score_dealer = 0
    score_player = 0
    dealer_i = 0
    player_i = 0
    done_flag = 0
    bet = 10
    while len(cards_player) < 2:

         #draw = deck.deal_card()
        cards_player.append(deck.deal_card())
          #print(len(gamedeck.deck))
        score_player += cards_player[player_i].value

           #draw = deck.deal_card()
        cards_dealer.append(deck.deal_card())
        #print(len(gamedeck.deck))
        score_dealer += cards_dealer[dealer_i].value

        player_i += 1
        dealer_i += 1
    #account for aces
    if score_player==22: score_player = 12
    if score_dealer==22: score_dealer = 12

    #account for naturals
    if score_player==21: return bet

    if strategy=='basic':

    #implement basic strategy

    #double down if necessary
        if score_player == 11 or (score_player == 10 and 10<=score_dealer<=11) or (score_player == 9 and 2<=score_dealer<=6):
            bet = bet*2
        if 7<=cards_dealer[0].value<=11:
            while score_player < 17:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player==21: return bet
                if score_player>=22: return bet*-1
            #    done_flag = 1

        if 4<=cards_dealer[0].value<=6:
            while score_player < 12:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player==21: return bet
                if score_player>=22: return bet*-1
        if 1<=cards_dealer[0].value<=3:
            while score_player < 13:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet*-1

    #stand on 16 if dealer has 10 upcard and player has multi-card 16
    if strategy=='multistand':
        #double down if necessary
        if score_player == 11 or (score_player == 10 and 10<=score_dealer<=11) or (score_player == 9 and 2<=score_dealer<=6):
            bet = bet*2

        if 7<=cards_dealer[0].value<=11:

            if cards_dealer[0].value==10:
                if (cards_player[0] != cards_player[1]) and score_player == 16:
                    while score_dealer < 17:
                        cards_dealer.append(deck.deal_card())
                        score_dealer += cards_dealer[dealer_i].value
                        dealer_i += 1
                        if score_dealer>=22: return bet
                    if score_player >= score_dealer: return bet
                    else: return bet*-1
            while score_player < 17:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player==21: return bet
                if score_player>=22: return bet*-1
            #    done_flag = 1

        if 4<=cards_dealer[0].value<=6:
            while score_player < 12:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player==21: return bet
                if score_player>=22: return bet*-1
        if 1<=cards_dealer[0].value<=3:
            while score_player < 13:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet*-1

    #when player has score of 8, and dealer has a 5 or 6 upcard, double down
    if strategy=='double8':
        # double down if necessary
        if score_player == 8 and 5<=cards_dealer[0].value<=6:
            bet = bet * 2

        if 7 <= cards_dealer[0].value <= 11:

            while score_player < 17:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet * -1
            #    done_flag = 1

        if 4 <= cards_dealer[0].value <= 6:
            while score_player < 12:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet * -1
        if 1 <= cards_dealer[0].value <= 3:
            while score_player < 13:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet * -1

        # when player has score of 10, and dealer's upcard is 9 or less, double down
    if strategy == 'double10':
        # double down if necessary
        if score_player == 10 and cards_dealer[0].value <= 9:
            bet = bet * 2

        if 7 <= cards_dealer[0].value <= 11:

            while score_player < 17:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet * -1
            #    done_flag = 1

        if 4 <= cards_dealer[0].value <= 6:
            while score_player < 12:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet * -1
        if 1 <= cards_dealer[0].value <= 3:
            while score_player < 13:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet * -1

    #double down on hard 11
    if strategy == 'double11':
        # double down if necessary
        if score_player == 11:
            bet = bet * 2

        if 7 <= cards_dealer[0].value <= 11:

            while score_player < 17:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet * -1
            #    done_flag = 1

        if 4 <= cards_dealer[0].value <= 6:
            while score_player < 12:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet * -1
        if 1 <= cards_dealer[0].value <= 3:
            while score_player < 13:
                cards_player.append(deck.deal_card())
                score_player += cards_player[player_i].value
                player_i += 1
                if score_player == 21: return bet
                if score_player >= 22: return bet * -1

    while score_dealer<17:
        cards_dealer.append(deck.deal_card())
        score_dealer += cards_dealer[dealer_i].value
        dealer_i += 1
        if score_dealer>=22: return bet
    #print("player score = ", score_player)
    #print("dealer score = ", score_dealer)
    if score_player >= score_dealer: return bet
    else: return bet*-1

gamedeck = Deck()
gamedeck.create_deck()
gamedeck.shuffle()
strategy='basic'
basic_profit = 0
for runs in range(10000):
    basic_profit += blackjack(gamedeck)
    gamedeck.reset_deck()
print(basic_profit)

#simulate multistand
strategy='multistand'
ms_profit = 0
for runs in range(10000):
    ms_profit += blackjack(gamedeck)
    gamedeck.reset_deck()
print(ms_profit)


#simulate double8
strategy='double8'
d8_profit = 0
for runs in range(10000):
    d8_profit += blackjack(gamedeck)
    gamedeck.reset_deck()
print(d8_profit)

#simulate double10
strategy='double10'
d10_profit = 0
for runs in range(10000):
    d10_profit += blackjack(gamedeck)
    gamedeck.reset_deck()
print(d10_profit)

#simulate double11
strategy='double11'
d11_profit = 0
for runs in range(10000):
    d11_profit += blackjack(gamedeck)
    gamedeck.reset_deck()
print(d11_profit)
#gamedeck.print_deck()


#plot results

graph = plt.figure()
#axes = graph.add_axes([0,0,1,1])
ax = graph.add_subplot(111)
ax.set_title('Expected Winnings for Various Blackjack Strategies')
strategies = ['Basic', 'Stand on Multi 16', 'Double down 8', 'Double down 10', 'Double down 11']
profits = [basic_profit, ms_profit, d8_profit, d10_profit, d11_profit]
bars = ax.bar(strategies, profits)
#graph, ax = plt.subplots()
#bars = ax.barh(strategies, profits)
ax.bar_label(bars)
plt.show()