from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter
import google.generativeai as genai

genai.configure(api_key="AIzaSyAtcumU5XB1iJhXrWUr1WU4dyCdamfLXu4"),
#root and models being used 
model = genai.GenerativeModel("gemini-1.5-flash")
root = tk.Tk()

character = tk.StringVar()
race = tk.StringVar()
colorCombo = tk.StringVar()
playStyle = tk.StringVar()
#height = tk.StringVar()
#startingWeight= tk.StringVar()
#goalWeight = tk.StringVar()

#def response(e1, e2, e3):
    #outputWindow = Toplevel(root)

    #outputWindow.title('Response')
    #response = model.generate_content( 'I am '+ e1 + ' and ' + e2 + ' pounds and want to reach ' + e3 + 'pounds how what should I start eating in order to reach this weight. List both the important macro nutrients and what foods to try and eat to reach my goal')
    #print(response.text)
    #output = Label(outputWindow, text = response.text, wraplength= 1000)
    #output.grid()
def charOutput(character, race):
    output = Toplevel(root)

    response = model.generate_content('Create a Dungeons and Dragons character that is of this class ' + character + 'and of this race ' + race + '. Also state what attributes I should focus on and a sample character sheet for this character.')

    response = Label(output, text = response.text, wraplength = 1000)
    response.grid()

def deckOutput(format, color, play):
    output = Toplevel(root)

    response = model.generate_content('Create a Magic: The Gathering deck for ' + str(format) + '. It must be this color combination ' + color + 'and this play style ' + play + '. Provide the deck or a similar deck and how to achieve best results.')

    response = Label(output, text = response.text, wraplength = 1000)
    response.grid()

def modern(): 
    modern = Toplevel(root)
    
    modern.geometry('600x600')
    modern.title('Modern Deck Builder')

    colorPrompt = Label(modern, text = "What color would you like to play: ", font = ('Times New Roman', 12)).grid(row = 0, column = 0)
    playPrompt = Label(modern, text = "What play style do you prefer: ", font = ('Times New Roman', 12)).grid(row = 1, column = 0)
    colorInput = ttk.Entry(modern, textvariable = colorCombo).grid(row = 0, column = 1)
    playInput = ttk.Entry(modern, textvariable = playStyle).grid(row = 1, column = 1)

    response = tk.Button(modern, text = "Enter", command = lambda: deckOutput("modern", colorCombo.get(), playStyle.get())).grid(row = 2, column=1)

def commander():
    commander = Toplevel(root)
    
    commander.geometry('600x600')
    commander.title('Commander Deck Builder')

    colorPrompt = Label(commander, text = "What color would you like to play: ", font = ('Times New Roman', 12)).grid(row = 0, column = 0)
    playPrompt = Label(commander, text = "What play style do you prefer: ", font = ('Times New Roman', 12)).grid(row = 1, column = 0)
    colorInput = ttk.Entry(commander, textvariable = colorCombo).grid(row = 0, column = 1)
    playInput = ttk.Entry(commander, textvariable = playStyle).grid(row = 1, column = 1)

    response = tk.Button(commander, text = "Enter", command = lambda: deckOutput("commander", colorCombo.get(), playStyle.get())).grid(row = 2, column=1)

def legacy():
    legacy = Toplevel(root)
    
    legacy.geometry('600x600')
    legacy.title('Commander Deck Builder')

    colorPrompt = Label(legacy, text = "What color would you like to play: ", font = ('Times New Roman', 12)).grid(row = 0, column = 0)
    playPrompt = Label(legacy, text = "What play style do you prefer: ", font = ('Times New Roman', 12)).grid(row = 1, column = 0)
    colorInput = ttk.Entry(legacy, textvariable = colorCombo).grid(row = 0, column = 1)
    playInput = ttk.Entry(legacy, textvariable = playStyle).grid(row = 1, column = 1)

    response = tk.Button(commander, text = "Enter", command = lambda: deckOutput("legacy", colorCombo.get(), playStyle.get())).grid(row = 2, column=1)

def standard():
    standard = Toplevel(root)
    
    standard.geometry('600x600')
    standard.title('Commander Deck Builder')

    colorPrompt = Label(standard, text = "What color would you like to play: ", font = ('Times New Roman', 12)).grid(row = 0, column = 0)
    playPrompt = Label(standard, text = "What play style do you prefer: ", font = ('Times New Roman', 12)).grid(row = 1, column = 0)
    colorInput = ttk.Entry(standard, textvariable = colorCombo).grid(row = 0, column = 1)
    playInput = ttk.Entry(standard, textvariable = playStyle).grid(row = 1, column = 1)

    response = tk.Button(standard, text = "Enter", command = lambda: deckOutput("standard", colorCombo.get(), playStyle.get())).grid(row = 2, column=1)

def formatScrn():
    scrn = Toplevel(root)

    scrn.geometry('600x600')

    modernScrn = tk.Button(scrn, text = 'Modern', command = modern)
    modernScrn.config(font = ('Times New Roman', 20))
    modernScrn.place(x = 300, y = 0, height = 300, width = 300)
    commanderScrn = tk.Button(scrn, text = 'Commander', command = commander)
    commanderScrn.config(font = ('Times New Roman', 20))
    commanderScrn.place(x = 0, y = 0, height = 300, width = 300)
    legacyScrn = tk.Button(scrn, text = 'Legacy', command = legacy)
    legacyScrn.config(font = ('Times New Roman', 20))
    legacyScrn.place(x = 0, y = 300, height = 300, width = 300)
    standardScrn = tk.Button(scrn, text = 'Standard', command = standard)
    standardScrn.config(font = ('Times New Roman', 20))
    standardScrn.place(x = 300, y = 300, height = 300, width = 300)

def characterCreator():
    charWindow = Toplevel(root)
    
    charWindow.geometry('600x600')
    charWindow.title('Character Creator')

    classPrompt = Label(charWindow, text = "What class would you like to play: ", font = ('Times New Roman', 12)).grid(row = 0, column = 0)
    racePrompt = Label(charWindow, text = "What race would you like to pick: ", font = ('Times New Roman', 12)).grid(row = 1, column = 0)
    classInput = ttk.Entry(charWindow, textvariable = character).grid(row = 0, column = 1)
    raceInput = ttk.Entry(charWindow, textvariable = race).grid(row = 1, column = 1)

    response = tk.Button(charWindow, text = "Enter", command = lambda: charOutput(character.get(), race.get())).grid(row = 2, column=1)

root.title("Wizards AI")

root.geometry('600x600')
#title = Label(root, text = 'Enter Height:').grid(row = 0, column = 0)
#title = Label(root, text = 'Enter Current Weight: ').grid(row = 1, column = 0)
#title = Label(root, text = 'Enter Your Ideal Weight: ').grid(row = 2, column = 0)
#e1 = str(ttk.Entry(root, textvariable=height).grid(row = 0, column = 1))
#e2 = str(ttk.Entry(root, textvariable= startingWeight).grid(row = 1, column = 1))
#e3 = str(ttk.Entry(root, textvariable= goalWeight).grid(row = 2, column = 1))

DBbutton = tk.Button(root, text = 'Deck Builder', command = formatScrn)
DBbutton.config(font = ('Times New Roman', 20))
DBbutton.place(x = 0,y=0, height = 300, width = 300)
CBbutton = tk.Button(root, text = "Character builder", command = characterCreator) 
CBbutton.config(font = ('Times New Roman', 20))
CBbutton.place(x = 300, y = 300, height = 300, width = 300)


# Execute Tkinter
root.mainloop()