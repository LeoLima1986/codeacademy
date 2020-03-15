import random

money = 100

#Write your game of chance functions here
def coin_flip(guess,bet):
  #Starts the game and flips the coin
  print("------------------")
  print("Let's flip a coin! You guessed " + guess)
  num = random.randint(1, 2)
  if num == 1:
    print("Heads")
  elif num == 2:
    print("Tails")
  if (num == 1 and guess == "Heads") or (num == 2 and guess == "Tails"):
    print("You won " + str(bet)+" dollars!")
    print("------------------")    
    return bet
  else:
    print("You lost " + str(bet)+" dollars!")
    print("------------------")    
    return -bet
    
def cho_han(guess,bet):
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  print("------------------")
  print("Let's flip Cho Han! Dice values are: " + str(die1) + " and " + str(die2))
  sum = die1 + die2
  if sum % 2 == 0 and guess == "Even":
    print("You won " + str(bet)+" dollars!")
    print("------------------")
    return bet
  elif sum % 2 == 1 and guess == "Odd":
    print("You won " + str(bet)+" dollars!")
    print("------------------")
    return bet
  else:
    print("You lost " + str(bet)+" dollars!")
    print("------------------")
    return -bet
  
def higher_card(bet):
  mine = random.randint(1, 10)
  house = random.randint(1, 10)
  if mine > house:
    print("You won " + str(bet)+" dollars!")
    print("------------------")
    return bet
  elif mine < house:
    print("You lost " + str(bet)+" dollars!")
    print("------------------")
    return -bet
  return 0

def roulette(guess,bet):
  result = random.randint(0, 37)
  if result == 37:
    print("The wheel landed on 00")
  else:
    print("The wheel landed on " + str(result))
    
  if guess == "Even" and result % 2 == 0 and result != 0:
    print("You won " + str(bet)+" dollars!")
    print("------------------")
    return bet
  elif guess == "Odd" and result % 2 == 1 and result != 37:
    print("You won " + str(bet)+" dollars!")
    print("------------------")
    return bet
  elif guess == result:
    print("You won " + str(bet*35)+" dollars!")
    print("------------------")
    return bet*35
  else:
    print("You lost " + str(bet)+" dollars!")
    print("------------------")
    return -bet
print("""
  1. Coin Flip
  2. Cho Han
  3. Higher Hard
  4. Roullete
  5. Exit""")
print("Enter game number to play.")
game = int(input())

if game == 1:
  guess = str(print("Enter Heads or Tails"))
  print("Wager")
  bet = int(input())
  money += coin_flip(guess,bet)
elif game == 2:
  guess = str(print("Enter Even or Odd"))
  print("Wager")
  bet = int(input())
  money += cho_han(guess,bet)
elif game == 3:
  print("Wager")
  bet = int(input())
  money += higher_card(bet)
elif game == 4:
  print("Guess a number (0-36)")
  guess = int(input())
  print("Wager")
  bet = int(input())
  money += roulette(guess,bet)
elif game == 5:
  exit

print("Your total amount of money is " + str(money))
