import random

stages = ["you lose 5 life ========", "you lose 4 life ========", "you lose 3 life ========",
          "you lose 2 life ========", "you lose 1 life========"]
list_1 = ["camel", "dog", "cat", "duck"]
rand_word = random.choice(list_1)
print(f"The word is : {rand_word}")

display_word = []
lives = 4
game_over = False

for x in range(len(rand_word)):
    display_word += "_"

while not game_over:
    user_word = input("Enter a letter : ").lower()
    for x in range(len(rand_word)):
        y = rand_word[x]
        if y == user_word:
            display_word[x] = y
    print(display_word)

    if user_word not in rand_word:
        lives -= 1
        if lives == 0:
            game_over = True

    if "_" not in display_word:
        game_over = True
        print("you win")
    print(stages[lives])
