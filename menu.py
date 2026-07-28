from validators import string_validator, integer_validator, float_validator
from game import blackjack
from chips import Chips
def intro():
    print()
    print("GAME RULES")
    print("-" * 10)
    print("• Your goal is to get as close to 21 as possible")
    print("  without going over 21.")
    print("• Number cards are worth their face value.")
    print("• Jacks, Queens, and Kings are worth 10.")
    print("• An Ace is worth either 11 or 1,")
    print("  whichever gives the best hand.")
    print("• A Blackjack is an Ace and any 10-value")
    print("  card dealt as your first two cards.")
    print()
    print("BETTING RULES")
    print("-" * 13)
    print("• You begin the game with 10,000 chips.")
    print("• Before each round, place a bet.")
    print("• Your bet cannot be greater than")
    print("  your current chip balance.")
    print("• If you win, you receive double")
    print("  your bet.")
    print("• If you lose, your bet is deducted")
    print("  from your chips.")
    print("• If the round is a push (tie),")
    print("  your bet is returned.")
    print()
    print("GAMEPLAY")
    print("-" * 8)
    print("• You and the dealer each receive")
    print("  two cards.")
    print("• One of the dealer's cards remains hidden.")
    print("• Type 'hit' to receive another card.")
    print("• Type 'stand' to keep your current hand.")
    print("• If you go over 21, you bust and lose.")
    print("• The dealer must draw until")
    print("  reaching at least 17.")
    print()
    print("=" * 40)
def view_wallet(chips):
    print('=' * 25)
    print('      VIEW WALLET')
    print('=' * 25)
    print(f'You have {chips.total:,} chips')
    print()
    return
    if chips.total == 0:
        print(f'You have {chips.total:,} chips!')
        print('=' * 20)
        return
def reset_wallet(chips):
    print('=' * 25)
    print('      RESET WALLET')
    print('=' * 25)
    print()
    print(f'Current balance: {chips.total:,} chips')
    print('1. Reset Wallet')
    print()
    print('Reset your wallet back to 1000 chips')
    print()
    reset = string_validator('Select yes or no: ')
    if reset == 'yes':
        chips.total = 1000
        chips.bet = 0
        print('Wallet successfully reset to 1000 chips')
        print('=' * 20)
        return
    elif reset == 'no':
        print('Wallet reset cancelled')
        return
def menu(chips):
    while True:
        print()
        print("=" * 40)
        print("      WELCOME TO BLACKJACK CASINO ")
        print("=" * 40)
        print('1. Play Blackjack')
        print('2. View Wallet')
        print('3. Help / Rules')
        print('4. Reset Wallet')
        print('5. Exit Game')
        print('=' * 20)
        print()
        choice = integer_validator('Choose an option: ',1, 5)
        if choice == 1:
            blackjack(chips)
        elif choice == 2:
            view_wallet(chips)
        elif choice == 3:
            intro()
        elif choice == 4:
            reset_wallet(chips)
        elif choice == 5:
            print('Goodbye')
            break 