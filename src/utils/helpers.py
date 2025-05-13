def shuffle_cards(cards):
    import random
    random.shuffle(cards)
    return cards

def delay(seconds):
    import time
    time.sleep(seconds)

def load_image(image_path):
    from PIL import Image
    return Image.open(image_path)