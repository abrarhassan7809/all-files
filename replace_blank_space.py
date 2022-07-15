import random

list_1 = ['cat', 'camel', 'dog']
rand_word = random.choice(list_1)
print(f"the word is {rand_word}")

display = []
for num in range(len(rand_word)):
    display += "_"
print(display)

chosen_word = input("enter any character : ").lower()

for letter in range(len(rand_word)):
    final_word = rand_word[letter]
    if final_word == chosen_word:
        display[letter] = final_word

print(display)