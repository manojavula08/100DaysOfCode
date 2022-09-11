import random
from turtle import clear
import hangman_words
import hangman_art
#choosing the rondom word
chosen_word = random.choice(hangman_words.word_list)
# finding lenght of chosen word
word_length = len(chosen_word)
# number of lives for a wrong answer
lives = (len(hangman_art.stages))-1
#below is optional for devloper understanding 
print(chosen_word)
print("\n"+ hangman_art.logo+"\n")
# Generating the number of blanks
unfilled_word=[]
for letters in chosen_word:
    unfilled_word +='_'
# while loop
end_game = True
while end_game:
    # .lower() is using because the word_list all are in lower case for a better match.
    user_input_letter = input("guess a letter from the word ").lower()
# checking user input is in word
    if user_input_letter in unfilled_word:
        print("You already guessed this letter.")
    for index in range(word_length):
        letter = chosen_word[index]
        if letter == user_input_letter:
            unfilled_word[index] = user_input_letter
    
# if user input is not in word then user lost a life
    if user_input_letter not in chosen_word:
        print(hangman_art.stages[lives])
        print(f"The letter you guessed '{user_input_letter}' not in the word, you lost a life")
        lives-=1
# printing the output
    print(" ".join(unfilled_word).upper())
    
# user ran out of lives exit the game
    if lives < 0:
        end_game = False
        print("You ran out of lives, Try again")
    
    if '_' not in unfilled_word:
        end_game = False
    
    