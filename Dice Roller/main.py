import tkinter as tk
import random

root = tk.Tk()
root.title("🎲Dice Roller")
root.geometry("1599x820")
root.resizable(True,True)

dice_label = tk.Label(root, text= "Roll The Dice!🎲", font=("Helvetica", 50))
dice_label.pack(pady= 40)

def roll_dice():
    dice_number = random.randint(1 , 100000)
    dice_label.config(text= f'{dice_number}')

roll_button = tk.Button(root, text= "Roll The Dice",font= ("Comic Sans",100), command= roll_dice)
roll_button.pack()

root.mainloop()