import random

def main():
  try:
    dice_rolls = int(input("How many dice you want to roll?"))
    dice_size = int(input("How many sides of the dice?"))
  except:
    dice_rolls = 2

  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    ## f-sting functionality.
    print(f'You rolled a {roll}')
  if dice_sum == 1:
    print(f'You have rolled a total of {dice_sum}! Critical Failure.')
  else:
    print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()