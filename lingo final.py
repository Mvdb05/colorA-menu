# word guessing game with TKinter gui in Python

import random
import tkinter as tk
from tkinter import messagebox

# Gebruik de woordenlijst uit het bestand 'words.txt'
words = open('words.txt').read().splitlines()
# Gebruik een random woord uit de woordenlijst
word = random.choice(words)
# Maak een lijst met alle letters in het woord
letters = list(word)
# Maak een lijst het aantal blanks voor het woord
blanks = ['_' for i in range(len(word))]
# maak een lijst met de geraden letters
guessed = [] 
# Maak een lijst met de fout geraden letters
wrong = [] 
# maak een lijst met de goed geraden letters
correct = []
# Maak een lijst met de al geraden letters
already = []
# Maak een TKinter GUI
root = tk.Tk()
root.title('Lingo')
root.geometry('500x500')

# Maak een label voor het woord
label = tk.Label(root, text=' '.join(blanks), font=('Helvetica', 30))
label.pack()
# maak een label voor de letters geraden
label2 = tk.Label(root, text=' '.join(guessed), font=('Helvetica', 20))
label2.pack()
# Maak een label voor de fout geraden letters
label3 = tk.Label(root, text=' '.join(wrong), font=('Helvetica', 20))
label3.pack()
# Maak een label voor de goed geraden letters
label4 = tk.Label(root, text=' '.join(correct), font=('Helvetica', 20))
label4.pack()
# Maak een label voor het aantal gokken dat je nog over hebt.
label6 = tk.Label(root, text='Guesses left: ' + str(10), font=('Helvetica', 20))
label6.pack()

# Maak een input box voor het invoeren van de letter
entry = tk.Entry(root, width=5)
entry.pack()

# maak een confirm button voor het invoeren van de letter
button = tk.Button(root, text='Guess', command=lambda: guess(entry.get()))
button.pack()

# Maak e en reset button voor het resetten van het spel
button2 = tk.Button(root, text='Reset', command=lambda: reset())
button2.pack()

# Maak een button voor het quitten van het spel
button3 = tk.Button(root, text='Quit', command=lambda: quit())
button3.pack()



# Functie voor het raden van de letter
def guess(letter):
    # Als de letter niet in de woord voorkomt
    if letter in already:
        messagebox.showinfo('Error', 'You already guessed that letter!')
    elif letter in letters:
        messagebox.showinfo('Correct', 'Correct!')
        correct.append(letter)
        already.append(letter)
        for i in range(len(letters)):
            if letters[i] == letter:
                blanks[i] = letter
        # Update de label voor het woord
        label['text'] = ' '.join(blanks)
        label2['text'] = ' '.join(guessed)
        label4['text'] = ' '.join(correct)
        # Haal 1 van de aantal gokken over
        label6['text'] = 'Guesses left: ' + str(10 - len(wrong))
        
    # Als de letter niet in de woord voorkomt
    else:
        messagebox.showinfo('Incorrect', 'Incorrect!')
        wrong.append(letter)
        already.append(letter)
        label3['text'] = ' '.join(wrong)
        label6['text'] = 'Guesses left: ' + str(10 - len(wrong))
    entry.delete(0, tk.END)

    if '_' not in blanks:
        messagebox.showinfo('Congratulations', 'You won!')
        reset()
        
        
    elif len(wrong) == 10:
        messagebox.showinfo('Game Over', 'You lost!')
        reset()
    
# Maak een functie voor het resetten van het spel
def reset():
    word = random.choice(words)
    letters = list(word)
    blanks = ['_' for i in range(len(word))]
    guessed = [] 
    wrong = [] 
    correct = []
    already = []
    label['text'] = ' '.join(blanks)
    label2['text'] = ' '.join(guessed)
    label3['text'] = ' '.join(wrong)
    label4['text'] = ' '.join(correct)
    label6['text'] = 'Guesses left: ' + str(10)
    entry.delete(0, tk.END)
    
# Functie om de eerste letter van het woord te laten zien
def show():
    messagebox.showinfo('Hint', 'The first letter of the word is ' + word[0] + '.')
button4 = tk.Button(root, text='Show', command=lambda: show())
button4.pack()


# Start het spel
root.mainloop()
