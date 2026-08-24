# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:32:16 2026

@author: DEll
"""

import random
words= ["python", "vasim", "akram", "java"]

def get_random_word():
    return random.choice(words)
def display_word_progress(word, guessed_letters): 
    display = [letter if letter in guessed_letters else "_"for letter in word]
    print("word: " + " ".join(display))


def get_user_guess(guessed_letters):
    while True:
        guess= input("guess a letter:").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Please enter a single letter")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
           
            return guess
        



def play_Hangman():
    word= get_random_word()
    guessed_letters=[]
    wrong_guesses=0
    max_wrong_guesses=5
    print("Welcome to hangman!")
    
    while wrong_guesses< max_wrong_guesses:
        display_word_progress(word, guessed_letters)
        guess= get_user_guess(guessed_letters)
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess!'{guess}'is in the word")
        else:
            wrong_guesses+=1
            print(f"wrong guess! you have{max_wrong_guesses- wrong_guesses} attempts left")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations ! You have guessed the word: {word}")
                break
    else:
        print(f"Game over ! The word was:{word}")

play_Hangman()            
