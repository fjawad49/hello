from PyMultiDictionary import MultiDictionary
from english_dictionary.scripts.read_pickle import get_dict
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# English_dict is a Python dictionary of English
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def increment_score(self, points):
        self.score += points
    def __str__(self):
        return f"{self.name} has score: {self.score}"

console = input("What is the name of Player 1?: ")
player1 = Player(console)

console = input("What is the name of Player 2?: ")
player2 = Player(console)

playerTurn = 1
dictionary = MultiDictionary()

def process_option(console, word):
    if console == "1":
        print(dictionary.meaning('en', word))
        return "Meaning"
    elif console == "2":
        print(dictionary.synonym('en', word))
        return "Synonym"
    elif console == "3":
        print(dictionary.antonym('en', word))
        return "Antonym"
    elif console == "4":
        return "Give Up"
    else:
        return word

while(True):
    word = input("%s (%d points) please enter a word: " % (player1.name if playerTurn == 1 else player2.name, player1.score if playerTurn == 1 else player2.score))
    english_dict = get_dict()

    valid_word = False
    while(valid_word == False):
        try:
            print(english_dict[word])
        except:
            console = input("Invalid word. %s, please enter a word: " % (player1.name if playerTurn == 1 else player2.name))
            continue
        valid_word = True

    clear()
    points = 4

    while(True):
        console = input("%s (%d points), your word is %d letters. You can earn %d points. Enter your word or as for a hint:\n(1) for definition\n(2) for synonym\n(3) for antonym\n(4) Give up\n " % (player1.name if playerTurn == 2 else player2.name, player1.score if playerTurn == 2 else player2.score, len(word), points))
        option = process_option(console, word)
        if option == word:
            if playerTurn == 1:
                player2.increment_score(points)
            else:
                player1.increment_score(points)
            print("You got it! Points: %d" % (player1.score if playerTurn == 2 else player2.score))
            break
        elif option == "Give Up":
            print("Skipping Turn. Word was %s" % (word))
            break
        elif (option == "Meaning") or (option == "Synonym") or (option == "Antonym"):
            points -= 1

    if(player1.score >= 10 or player2.score >=10):
        print("Game Over")
        break

    playerTurn = 2 if playerTurn == 1 else 1