import random

# Hangman stages
stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', 
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
]

words = ['python', 'apple', 'banana', 'hangman', 'orange']
word = random.choice(words)
guessed = ['_'] * len(word)
used = []
tries = 0

print("🎮 Welcome to Hangman!")

while tries < len(stages) - 1 and '_' in guessed:
    print(stages[tries])
    print("\nWord:", ' '.join(guessed))
    print("Used letters:", ', '.join(used))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.")
        continue
    if guess in used:
        print("❌ You already guessed that.")
        continue

    used.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("✅ Correct guess!")
    else:
        tries += 1
        print("❌ Wrong guess!")

if '_' not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print(stages[tries])
    print("\n💀 Game over! The word was:", word)
