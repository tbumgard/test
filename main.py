'''import os

def valid_input(input_prompt, validate_func, value_error_msg):
    valid = False  
    while not valid:
        try:
            user_input = input(input_prompt)
            user_input, valid_input = validate_func(user_input)
            if valid_input == False:
                raise ValueError             
        except ValueError:
            ##os.system("clear")
            print(value_error_msg)
        else:
            valid = True
    return user_input

def is_num(user_input):
    i = int(user_input)
    if i: 
        return i, True
    raise ValueError

def is_positive(user_input):
    i = int(user_input)
    if i > 0:
        return i, True
    raise ValueError

def is_gt(user_input, value):
    i = int(user_input)
    if i > value:
        return i, True
    raise ValueError

def is_word(user_input):
    word_to_guess = user_input.lower()
    if not word_to_guess.isalpha():
        raise ValueError  
    return word_to_guess, True

def is_char(user_input):
    guess_letter = user_input    
    guess_letter = guess_letter.lower()
    if (
        not guess_letter.isalpha()
        or not (len(guess_letter) == 1)
    ):
        raise ValueError
    return guess_letter, True

def valid_option(user_input, option_list = []):
    i = user_input[0]
    if i in option_list:
        return i, True
    return i, False

def not_valid_option(user_input, option_list = []):
    i = user_input[0]
    if i not in option_list:
        return i, True
    return i, False

OLD CODE
def valid_num_guesses_input(user_input):
    guesses = int(user_input)
    print(guesses==None)
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

def valid_guess_letter_input(user_input):
    guess_letter = user_input
        
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
    num_guesses = valid_input("Enter number of guesses allowed: ", lambda x: is_num(x) and is_positive(x), 
                              "Invalid input. Please enter a valid integer at least great than 0")
    
    # input the number of players - valid input (integer > 1) stored in num_players
    num_players = valid_input("How many players: ", lambda x: is_num(x) and is_gt(x, 1), 
                              "Invalid input. Please enter a valid integer at least greater than 1")

    guessed_letters = "abcdefghijklmnop"
    
    # input the word_to_guess - valid input string with size greater than 1 with out any non-alpha chars that has been lowered()
    word_to_guess = valid_input("Please enter the word to guess: ", lambda x: is_word(x),
                                "Please enter a word at least 1 letter long with out any non-alpha characters")

    # input a letter from the guessing_player, validate it is an alpha character that has been lowered() and stored in guess_letter
    guess_letter = valid_input("Trevor please guess a letter:", lambda x: not_valid_option(is_char(x), guessed_letters),
                               f"Please enter a valid character (a-z) that hasn't been guessed yet.\nGuessed  Letters: guessed_letters\nRevealed Letters: revealed_letters\nGuesses left: guesses_left")
    
    # see if players want to play again with a prompt
    play_again_response = valid_input("\nPlay again (y/n): ", lambda x: valid_option(is_char(x),["y", "n"]), "Please enter a valid entry (y/n)")
            
    if play_again_response == "n":
        play_again = False
    
    os.system("clear")
    print(f"Number of guesses: {num_guesses}")
    print(f"Number of players: {num_players}")
    print(f"Word to guess: {word_to_guess}")
    print(f"Guessed letter: {guess_letter}")
    print(f"Play again response: {play_again_response} {play_again}")    

main()

class Graph:          
    def bfs_path(self, start, end):
        path_to_end = self.breadth_first_search(start)
        shortest_path = []
        
        if end not in path_to_end:
            return None
        
        path_index = path_to_end.index(end)
        previous_index = path_index - 1
        while path_index != 0:
            if path_to_end[path_index] in self.graph[path_to_end[previous_index]]:
                shortest_path.append(path_to_end[path_index])
                path_index = previous_index

            previous_index -= 1
        
        shortest_path.append(path_to_end[path_index])
      
        return shortest_path[::-1]
  
    # don't touch below this line

    def breadth_first_search(self, v):
        visited = []
        to_visit = []
        to_visit.append(v)
        while to_visit:
            s = to_visit.pop(0)
            visited.append(s)
            sorted_neighbours = sorted(self.graph[s])
            for neighbour in sorted_neighbours:
                if neighbour not in visited and neighbour not in to_visit:
                    to_visit.append(neighbour)
        return visited

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result


def test(edges_to_add, from_vertex, to_vertex):
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    path = graph.bfs_path(from_vertex, to_vertex)
    print("-------------------------------------")
    print(f"Path from {from_vertex} to {to_vertex}: {path}")
    print("=====================================")


def main():
    test(
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("London", "Dubai"),
            ("Cairo", "Kyiv"),
            ("Cairo", "Madrid"),
            ("London", "Madrid"),
            ("Buenos Aires", "New York"),
            ("Tokyo", "Buenos Aires"),
            ("Kyiv", "San Francisco"),
        ],
        "Cairo",
        "San Francisco",
    )
    test(
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("London", "Dubai"),
            ("Cairo", "Kyiv"),
            ("Cairo", "Madrid"),
            ("London", "Madrid"),
            ("Buenos Aires", "New York"),
            ("Tokyo", "Buenos Aires"),
            ("Kyiv", "San Francisco"),
        ],
        "New York",
        "Dubai",
    )


main()'''

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
    