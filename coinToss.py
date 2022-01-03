from coinflipper import coinflipper

# Introduction
print('Welcome to coin toss.')

# Ask the user how many coins they'd like to flip
coins = int(input('How many coins would you like to flip: '))

# Return the list values
totalPoints = coinflipper(coins)

# Print the outcome
print(f'Out of {coins} coins')
print(f'{totalPoints[0]} were heads | {totalPoints[0] / coins * 100}%')
print(f'{totalPoints[1]} were tails | {totalPoints[1] / coins * 100}%')





