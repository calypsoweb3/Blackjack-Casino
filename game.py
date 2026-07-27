from validators import string_validator, integer_validator, float_validator
from display import show_some, show_all, player_busts, dealer_busts, player_wins, dealer_wins, push
from cards import Deck, Hand
from chips import Chips
def take_bets(chips):
    chips.place_bet()
def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)
def hit_or_stand(deck, hand):
    while True:
        print()
        d = string_validator('Hit or Stand: ').lower()
        if d == 'hit':
            hit(deck, hand)
            return True
        elif d == 'stand':
            print()
            return False
        else:
            print('Invalid input')
def blackjack(chips):
    print("=" * 20)
    print('   BLACKJACK')
    print('=' * 20)            
    playing = True
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    take_bets(chips)
    for num in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
    show_some(dealer_hand, player_hand)
    if (player_hand.value == 21 and len(player_hand.cards) == 2 and dealer_hand.value == 21 and len(dealer_hand.cards) == 2):
        show_all(dealer_hand, player_hand)
        print()
        print('DOUBLE BLACKJACK')
        push(chips)
        return
    elif player_hand.value == 21 and len(player_hand.cards) == 2:
        show_all(dealer_hand, player_hand)
        print()
        print('BLACKJACK')
        player_wins(chips)
        return
    elif dealer_hand.value == 21 and len(dealer_hand.cards) == 2:
        show_all(dealer_hand, player_hand)
        print()
        print('BLACKJACK')
        dealer_wins(chips)
        return
    while playing:
        if hit_or_stand(deck, player_hand):
            show_some(dealer_hand, player_hand)
        if player_hand.value < 17:
            hit_or_stand(deck, player_hand)
            show_some(dealer_hand, player_hand)
        if player_hand.value > 21:
            show_all(dealer_hand, player_hand)
            player_busts(chips)
            return
        else:
            playing = False
    while dealer_hand.value < 17:
            hit(deck, dealer_hand)
    show_all(dealer_hand, player_hand) 
    if dealer_hand.value > 21:
        dealer_busts(chips)
        return
    elif dealer_hand.value > player_hand.value:
        dealer_wins(chips)
        return
    elif dealer_hand.value < player_hand.value and player_hand.value <= 21:
        player_wins(chips)
        return
    else:
        push(chips)
        return