from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

# Card images credit: https://opengameart.org/content/playing-cards-1

class Menu(object):
    
    def __init__(self):
        self.master = Tk()
        
        self.master.title("Menu")
        
        self.master.geometry("600x600")
        
        # Create a frame for game title
        self.title_frame = Frame(self.master)
        self.board_frame = Frame(self.master)
        self.choices_frame=Frame(self.master)
        
        # Title frame widgets
        self.title_label = Label(self.title_frame, text="Four Corners", font='Arial 20')
        self.title_label.pack(side="top")
        
        
        # Board frame widgets
        self.demo_img = ImageTk.PhotoImage(Image.open("demo_cards.png"))
        self.demo = Label(self.board_frame, image=self.demo_img)
        self.demo.pack()
        
        
        # Choices frame widgets
        self.new_game_button = ttk.Button(self.board_frame, text="New game")
        self.rules_button =  ttk.Button(self.board_frame, text="Rules")
        
        self.new_game_button.pack(side="left")
        self.rules_button.pack(side="right")
        
        # Pack frames      
        self.title_frame.pack(side="top")
        self.board_frame.pack()
        self.choices_frame.pack(side="bottom")
        
        
        # Generate the window
        self.master.mainloop()
        
menu=Menu()