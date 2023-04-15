from PIL import Image
import random


color_map = {
    "a": (255, 0, 0),
    "b": (0, 255, 0),
    "c": (0, 0, 255),
    "d": (255, 255, 0),
    "e": (255, 0, 255),
    "f": (0, 255, 255),
    "g": (128, 0, 0),
    "h": (0, 128, 0),
    "i": (0, 0, 128),
    "j": (128, 128, 0),
    "k": (128, 0, 128),
    "l": (5, 128, 128),
    "m": (128, 0, 64),
    "n": (0, 128, 64),
    "o": (64, 0, 128),
    "p": (64, 128, 0),
    "q": (128, 64, 0),
    "r": (128, 0, 1),
    "s": (0, 128, 128),
    "t": (128, 128, 128),
    "u": (255, 128, 0),
    "v": (255, 0, 128),
    "w": (0, 255, 128),
    "x": (128, 0, 255),
    "y": (0, 255, 1),
    "z": (156, 132, 12),
    "0": (255, 255, 255),
    "1": (0, 0, 0),
    "2": (255, 165, 0),
    "3": (255, 192, 203),
    "4": (46, 139, 87),
    "5": (255, 215, 0),
    "6": (255, 69, 0),
    "7": (218, 112, 214),
    "8": (238, 232, 170),
    "9": (23, 135, 128),
    "!": (128, 0, 35),
    "@": (0, 128, 4),
    "#": (10, 0, 128),
    "$": (128, 123, 0),
    "%": (128, 5, 128),
    "^": (0, 138, 128),
    "&": (128, 108, 128),
    "-": (127, 108, 128),
    " ": (123, 128, 118)
}



pad_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def encrypt_text(text):

    text = text.lower()


    width = len(text)
    height = width


    num_spaces = text.count(" ")


    width += num_spaces
    height += num_spaces


    image = Image.new("RGB", (width, height), pad_color)


    x = 0
    y = 0
    for char in text:
        if char == " ":

            color = color_map.get(" ", pad_color)
            image.putpixel((x, y), color)
            x += 1
            y += 1
        else:
            color = color_map.get(char, pad_color)
            image.putpixel((x, y), color)
            x += 1
            y += 1

    return image


def decrypt_text(image):

    width, height = image.size


    colors = [image.getpixel((i, i)) for i in range(width)]


    text = ""
    for c in colors:
        if c == (123, 128, 118):
            text += " "
        else:
            text += next((char for char, color in color_map.items() if color == c), "")


    return text



plaintext = "Data Security - Group 26"
encrypted_image = encrypt_text(plaintext)
decrypted_text = decrypt_text(encrypted_image)

print("Plaintext: ", plaintext)
print("Encrypted image: ")
encrypted_image.show()
print("Decrypted text: ", decrypted_text)
