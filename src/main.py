from tkinter import Tk
from gui.game_window import GameWindow

def main():
    root = Tk()
    root.title("Memory Card Matching Game")
    game_window = GameWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()