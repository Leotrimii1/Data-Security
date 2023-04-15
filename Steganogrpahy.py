from PIL import Image
import random


color_map = {
    "a": (255, 0, 0),"A":(123, 2, 124),
    "b": (0, 255, 0),"B":(123, 2, 125),
    "c": (0, 0, 255),"C":(123, 2, 126),
    "d": (255, 255, 0), "D":(222, 12, 33),
    "e": (255, 0, 255),"E":(123, 2, 127),
    "f": (0, 255, 255),"F":(123, 2, 128),
    "g": (128, 0, 0), "G":(123, 2, 129),
    "h": (0, 128, 0),"H":(123, 2, 120),
    "i": (0, 0, 128),"I":(123, 2, 131),
    "j": (128, 128, 0),"J":(123, 2, 132),
    "k": (128, 0, 128),"K":(123, 2, 133),
    "l": (5, 128, 128),"L":(123, 2, 134),
    "m": (128, 0, 64),"M":(123, 2, 135),
    "n": (0, 128, 64),"N":(123, 2, 136),
    "o": (64, 0, 128),"O":(123, 2, 137),
    "p": (64, 128, 0),"P":(123, 2, 138),
    "q": (128, 64, 0),"Q":(123, 2, 139),
    "r": (128, 0, 1),"R":(123, 2, 140),
    "s": (0, 128, 128), "S":(133, 3, 113),
    "t": (128, 128, 128),"T":(123, 4, 123),
    "u": (255, 128, 0),"U":(123, 5, 123),
    "v": (255, 0, 128),"V":(123, 6, 123),
    "w": (0, 255, 128),"W":(123, 7, 123),
    "x": (128, 0, 255),"X":(123, 8, 123),
    "y": (0, 255, 1),"Y":(123, 9, 123),
    "z": (156, 132, 12),"Z":(123, 10, 123),

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

    text = text


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
