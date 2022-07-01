# word guessing game with TKinter gui in Python where the user guesses a word depending on how many letters the to be guessed word has and the user can guess 5 words per game

from logging import root
import random
import tkinter as tk
from tkinter import messagebox

# player can guess 5 words per game and the game will end when the player guesses the correct word or when the player runs out of guesses (5 guesses per word) or when the player quits the game in a tkinter gui

root = tk.Tk()
root.title("Lingo")
root.geometry("500x500")
root.configure(background='#f0f0f0')

# use list of words to be guesses from the file words.txt
with open("words.txt", "r") as f:
    words = f.read().splitlines()
    
# chose 5 random words from the list of words to be guessed and store them in a list called word_list 
word_list = []
for i in range(5):
    word_list.append(random.choice(words))

# tkinter label to display the word to be guessed 
word_label = tk.Label(root, text="", font=("Helvetica", 20), bg='#f0f0f0')
word_label.pack()

# tkinter label to display the second word to be guessed
word_label2 = tk.Label(root, text="", font=("Helvetica", 20), bg='#f0f0f0')
word_label2.pack()

# tkinter label to display the third word to be guessed
word_label3 = tk.Label(root, text="", font=("Helvetica", 20), bg='#f0f0f0')
word_label3.pack()

# tkinter label to display the fourth word to be guessed
word_label4 = tk.Label(root, text="", font=("Helvetica", 20), bg='#f0f0f0')
word_label4.pack()

# tkinter label to display the fifth word to be guessed
word_label5 = tk.Label(root, text="", font=("Helvetica", 20), bg='#f0f0f0')
word_label5.pack()

# tkinter label to display the number of guesses left
guesses_left_label = tk.Label(root, text="", font=("Helvetica", 20), bg='#f0f0f0')
guesses_left_label.pack()

# tkinter label to display the words that the player has guessed so far 
guessed_words_label = tk.Label(root, text="", font=("Helvetica", 20), bg='#f0f0f0')
guessed_words_label.pack()

# tkinter entry to take in the word the player guesses 
guess_entry = tk.Entry(root, width=20, font=("Helvetica", 20))
guess_entry.pack()

# tkinter button to submit the word the player guesses
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 20), command=submit_word)

# tkinter button to quit the game
quit_button = tk.Button(root, text="Quit", font=("Helvetica", 20), command=quit_game)

# tkinter button to reset the game
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 20), command=reset_game)

# function to check if the word the player guesses is in the list of words to be guessed and if it is, display the word in the word_label
def submit_word():
    word = guess_entry.get()
    if word in word_list:
        word_label.configure(text=word)
        word_label2.configure(text=word)
        word_label3.configure(text=word)
        word_label4.configure(text=word)
        word_label5.configure(text=word)
        guessed_words_label.configure(text="You guessed the word!")
        root.destroy()
    else:
        guesses_left_label.configure(text="You guessed wrong!")
        guessed_words_label.configure(text="You guessed: " + word)
        guess_entry.delete(0, tk.END)
        root.update()
        root.after(1000)
        guesses_left_label.configure(text="You have " + str(guesses_left) + " guesses left!")
        guessed_words_label.configure(text="You guessed: " + word)
        guess_entry.delete(0, tk.END)
        root.update()
        root.after(1000)
        if guesses_left == 0:
            root.destroy()
            messagebox.showinfo("Game Over", "You ran out of guesses! The word was " + word)
            root.destroy()
            root.quit()

# if the word to be guessed and the word guessed have equal letters in the same position, the word is displayed in the word_label
def display_word():
    word = word_list[0]
    word_label.configure(text=word)
    word_label2.configure(text=word)
    word_label3.configure(text=word)
    