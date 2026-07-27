from validators import string_validator, integer_validator, float_validator
class Chips():
    def __init__(self,total):
        self.total = total
        self.bet = 0
    def place_bet(self):
        while True:
            self.bet = float_validator('Enter amount to place a bet: ',1, 1000000)
            if self.total >= self.bet:
                self.total -= self.bet
                print(f'Current balance: {self.total:,} chips')
                break
            else:
                print() 
                print('Insufficient balance')
                print(f'Your current balance: {self.total:,} chips')
                print()
    def add_winnings(self):
        self.total += self.bet * 2
        print(f'Congratulations you won {self.bet:,} chips')
        print()
        print(f'Current balance: {self.total:,} chips')
    def return_bet(self):
        self.total += self.bet
        print(f'Your bet of {self.bet:,} chips has been refunded')
        print(f'Current balance: {self.total:,} chips')
    def lose_bet(self):
        print(f'You lost {self.bet:,} chips')
        print(f'Current balance: {self.total:,} chips')
        print('BETTER LUCK NEXT TIME!!!')