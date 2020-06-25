import random

def main():
  dice_rolls = 2
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    ## f-sting functionality.
    print(f'You rolled a {roll}')
  if dice_sum == 1:
    print(f'You have rolled a total of {dice_sum}! Critical Failure.')
  else:
    print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()