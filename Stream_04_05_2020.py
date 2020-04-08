import time
import sys
import random
from random import randrange
import os

dir = os.path.dirname(__file__)
FILE_LOCATION_INSULTS = os.path.join(dir, "Compliments.txt")

def import_file():

    with open(FILE_LOCATION_INSULTS, "r") as fp:
        words = [line.strip().lower() for line in fp.readlines()]

    return words

def make_hangman(hangman):
    hangman_pieces = ['O\n', "_\n", '|\n', "^\n"]
    hangman.append(hangman_pieces[len(hangman)])
    return hangman

def win_check(hangman, word_string, word):
    game_continue_yn = True
    continue_counter = 0
    for i in range(len(word_string)):
        if word_string[i] == "_" or word_string[i] == " ":
            continue_counter += 1
    if continue_counter == 0:
        game_continue_yn = False
        
    
    if len(hangman) == 4:
        print("The correct word was: {}!".format(word))
        #print_string(hangman)
        game_continue_yn = False
    
    return game_continue_yn

def change_string(word_letters, letter, position, word_string):
    new_list = []
    for i in range(len(word_letters)):
        if word_letters[i] != letter:
            if word_string[i] == "_ ":
                new_list.append("_ ")
            else:
                new_list.append(word_string[i])
        else:
            new_list.append("{} ".format(letter))

    return(new_list)
    

    


def letters_in_word(word, guess, word_string):
    word_letters = []
    letter_in_word_yn = False
    for i in range(len(word)):
        word_letters.append(word[i])
    for k in range(len(word_letters)):
        if guess == word_letters[k]:
            word_string = change_string(word_letters, guess, k, word_string)
            letter_in_word_yn = True
        else:
            pass
    return(word_string, letter_in_word_yn)

def print_string(word_string):
    print_string = ""
    for i in range(len(word_string)):
        print_string += word_string[i]
    print(print_string)

def main():

    all_the_words = import_file()
    max_num = int(len(all_the_words)) - 1
    word = all_the_words[random.randint(0, max_num)]
    word_len = len(word)
    word_string = ""
    for i in range(word_len):
        word_string += "_ "
    print(word_string)
    #print(word)
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-']
    game_continue = True
    hangman = []
    while game_continue:
        correct_guess = False
        guess = input("Enter a letter to guess: ").lower().strip()
        while guess not in all_letters:
            print("That's not an option.")
            guess = input("Enter a letter to guess: ").lower().strip()
        all_letters.remove(guess)
        word_string, correct_guess = letters_in_word(word, guess, word_string)
        if correct_guess:
            game_continue = win_check(hangman, word_string, word)
        else:
            hangman = make_hangman(hangman)
            game_continue = win_check(hangman, word_string, word)
            #print_string(hangman)
        print_string(hangman)
        print_string(word_string)
    print("Game Over!")

    input("Press ENTER to exit: ")

if __name__ == "__main__":
    main()

