class GameLogic:
    def __init__(self, cards):
        self.cards = cards
        self.first_card = None
        self.second_card = None
        self.has_flipped_card = False
        self.lock_board = False
        self.attempts = 0

    def flip_card(self, card):
        if self.lock_board:
            return
        if card == self.first_card:
            return

        if not self.has_flipped_card:
            self.has_flipped_card = True
            self.first_card = card
            return

        self.second_card = card
        self.attempts += 1
        return self.check_match()

    def check_match(self):
        is_match = self.first_card.name == self.second_card.name
        if is_match:
            self.disable_cards()
        else:
            self.unflip_cards()
        return is_match

    def disable_cards(self):
        self.first_card = None
        self.second_card = None
        self.reset_board()

    def unflip_cards(self):
        self.lock_board = True
        # Logic to unflip cards after a delay would go here
        self.first_card = None
        self.second_card = None
        self.reset_board()

    def reset_board(self):
        self.has_flipped_card = False
        self.lock_board = False

    def shuffle_cards(self):
        import random
        random.shuffle(self.cards)