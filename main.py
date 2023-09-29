import os

def valid_input(input_prompt, validate_func, value_error_msg):
    valid = False  
    while not valid:
        try:
            user_input = input(input_prompt)
            user_input = validate_func(user_input)
        except ValueError:
            os.system("clear")
            print(value_error_msg)
        else:
            valid = True
    return user_input

def valid_num_guesses_input(user_input):
    guesses = int(user_input)
    if guesses < 1:
        raise ValueError    
    return guesses

def valid_num_players_input(user_input):            
    num_players = int(user_input)
    if num_players < 2:
        raise ValueError
    return num_players

def valid_word_to_guess_input(user_input):
    word_to_guess = user_input.lower()
    if not word_to_guess.isalpha():
        raise ValueError  
    return word_to_guess

def valid_guess_letter_input(*args):
    guess_letter, guessed_letters = args
    guess_letter = guess_letter.lower()
    if (
        not guess_letter.isalpha()
        or not (len(guess_letter) == 1)
        or guess_letter in guessed_letters
    ):
        raise ValueError
    return guess_letter

def valid_play_again_response_input(user_input):
    play_again_response = user_input.lower()
    if (
        not play_again_response.isalpha()
        or not ((len(play_again_response)) == 1)
        or not (play_again_response == "n" or play_again_response == "y")
    ):
        raise ValueError
    return play_again_response

def main():
    os.system("clear")
    play_again = True

    # input the number of guesses - valid input (integer > 0) stored in var guesses
    num_guesses = valid_input("Enter number of guesses allowed: ", valid_num_guesses_input, 
                              "Invalid input. Please enter a valid integer at least great than 0")
    # input the number of players - valid input (integer > 1) stored in num_players
    num_players = valid_input("How many players: ", valid_num_players_input, 
                              "Invalid input. Please enter a valid integer at least greater than 1")

    guessed_letters = "abcdefghijklmnop"
    
    # input the word_to_guess - valid input string with size greater than 1 with out any non-alpha chars that has been lowered()
    word_to_guess = valid_input("Please enter the word to guess: ", valid_word_to_guess_input,
                                "Please enter a word at least 1 letter long with out any non-alpha characters")

    # input a letter from the guessing_player, validate it is an alpha character that has been lowered() and stored in guess_letter
    '''guess_letter = valid_input("Trevor please guess a letter:", valid_guess_letter_input("z", guessed_letters),
                               f"Please enter a valid character (a-z) that hasn't been guessed yet.\nGuessed  Letters: guessed_letters\nRevealed Letters: revealed_letters\nGuesses left: guesses_left")'''
    
    # see if players want to play again with a prompt
    play_again_response = valid_input("\nPlay again (y/n): ", valid_play_again_response_input, "Please enter a valid entry (y/n)")
            
    if play_again_response == "n":
        play_again = False

    os.system("clear")
    print(f"Number of guesses: {num_guesses}")
    print(f"Number of players: {num_players}")
    print(f"Word to guess: {word_to_guess}")
    ##print(f"Guessed letter: {guess_letter}")
    print(f"Play again response: {play_again_response} {play_again}")

main()