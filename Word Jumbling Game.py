import random
words = ("burger","fries","french","hello","equilibrium","potato","nice","truck")
word = random.choice(words)
jumble =""
correct = word
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position]+ word[(position + 1):]

print("""
                Welcome to Word Jumble
        Unscramble the letter to make a word!
""")

print("\nThe jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, thats not it.")
    guess = input("\nYour guess: ")

if guess == correct:
    print("You're right!")