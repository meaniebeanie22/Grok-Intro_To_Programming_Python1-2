guesses = set()

guess = input("Guess: ")
while guess:
  if not(guess in guesses):
    guesses.add(guess)
    print('Hit', guess)
  else:
    print("You've chosen that square already")
  guess = input('Guess: ')
