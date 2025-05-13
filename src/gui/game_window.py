from tkinter import Tk, Frame, Button, messagebox
import random

class GameWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Card Matching Game")
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.cards = self.create_card_deck()
        self.buttons = self.create_buttons()
        self.first_card = None
        self.second_card = None
        self.lock_board = False
        self.attempts = 0

    def create_card_deck(self):
        card_names = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6'] * 2
        random.shuffle(card_names)
        return card_names

    def create_buttons(self):
        buttons = []
        for i in range(12):
            button = Button(self.frame, text='', width=10, height=5, command=lambda i=i: self.flip_card(i))
            button.grid(row=i // 4, column=i % 4)
            buttons.append(button)
        return buttons

    def flip_card(self, index):
        if self.lock_board or self.buttons[index]['text'] != '':
            return

        self.buttons[index]['text'] = self.cards[index]
        
        if self.first_card is None:
            self.first_card = index
        else:
            self.second_card = index
            self.attempts += 1
            self.check_match()

    def check_match(self):
        if self.cards[self.first_card] == self.cards[self.second_card]:
            self.buttons[self.first_card]['state'] = 'disabled'
            self.buttons[self.second_card]['state'] = 'disabled'
            self.reset_board()
        else:
            self.lock_board = True
            self.master.after(1000, self.unflip_cards)

    def unflip_cards(self):
        self.buttons[self.first_card]['text'] = ''
        self.buttons[self.second_card]['text'] = ''
        self.reset_board()

    def reset_board(self):
        self.first_card = None
        self.second_card = None
        self.lock_board = False

if __name__ == "__main__":
    root = Tk()
    game_window = GameWindow(root)
    root.mainloop()