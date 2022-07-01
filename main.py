import random

wordlist = ["Python", "Java", "HTML", "CSS"]
word = random.choice(wordlist)

def lingo():

    while True:
        print("Je woord heeft ", len(word), "letters")
        guessword = input("Guess the word:")
        if len(guessword) != len(word): print("typ een woord met", len(word),"letters")

        elif guessword == word: break

        elif guessword != word:

            for position, letter in enumerate(guessword):
                if letter == word[position]:
                    print(letter, end="")
                elif letter not in word:
                    print("-", end="")
                else:
                    print("?", end="")
            print("")
lingo()

print("Gefeliciteerd, goed gegokt!")

class Lingo:
    def __init__(self):
        self.wordlist = ["Python", "Java", "HTML", "CSS"]
        self.word = random.choice(self.wordlist)
        self.guessword = ""
        self.guess = ""
        self.guesslist = []
        self.guesscount = 0
        self.guesslimit = 3
        self.guessword = ""
        self.guesswordlist = []
        
        
    # def guess_word(self):
    #     while True:
    #         self.guessword = input("Guess the word:")
    #         if len(self.guessword) != len(self.word): print("typ een woord met", len(self.word),"letters")
    #         elif self.guessword == self.word: break
    #         else:
    #             for position, letter in enumerate(self.guessword):
    #                 if letter == self.word[position]:
    #                     print(letter, end="")
    #                 elif letter not in self.word:
    #                     print("-", end="")
    #                 else:
    #                     print("?", end="")
    #             print("")
                
    def guess_letter(self):
        while True:
            self.guess = input("Guess a letter:")
            if len(self.guess) != 1: print("typ een letter")
            elif self.guess in self.guesslist: print("je hebt al geprobeerd met deze letter")
            elif self.guess not in self.word:
                self.guesscount += 1
                print("fout")
                self.guesslist.append(self.guess)
                if self.guesscount == self.guesslimit:
                    print("je hebt verloren")
                    break
            else:
                self.guesscount += 1
                print("goed")
                self.guesslist.append(self.guess)
                if self.guesscount == self.guesslimit:
                    print("je hebt verloren")
                    break
            if self.guesscount == self.guesslimit:
                break
            for position, letter in enumerate(self.word):
                if letter == self.guess:
                    print(letter, end="")
                elif letter not in self.guesslist:
                    print("-", end="")
                else:
                    print("?", end="")
            print("")
            
# play game
lingo = Lingo()
lingo.guess_letter()
