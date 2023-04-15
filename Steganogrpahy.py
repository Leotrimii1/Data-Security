from PIL import Image
import random

image_path = r'C:\Users\User\Desktop\Python\Picture1.png'
# Mapping of characters to colors
color_map = {
    "a": (255, 0, 0), # red
    "b": (0, 255, 0), # green
    "c": (0, 0, 255), # blue
    "d": (255, 255, 0), # yellow
    "e": (255, 0, 255), # magenta
    "f": (0, 255, 255), # cyan
    "g": (128, 0, 0), # maroon
    "h": (0, 128, 0), # dark green
    "i": (0, 0, 128), # navy
    "j": (128, 128, 0), # olive
    "k": (128, 0, 128), # purple
    "l": (0, 128, 128), # teal
    "m": (128, 0, 64), # crimson
    "n": (0, 128, 64), # forest green
    "o": (64, 0, 128), # indigo
    "p": (64, 128, 0), # olive green
    "q": (128, 64, 0), # brown
    "r": (128, 0, 1), # maroon
    "s": (0, 128, 128), # teal
    "t": (128, 128, 128), # gray
    "u": (255, 128, 0), # orange
    "v": (255, 0, 128), # pink
    "w": (0, 255, 128), # spring green
    "x": (128, 0, 255), # violet
    "y": (0, 255, 0), # lime green
    "z": (128, 128, 0), # olive
    "0": (255, 255, 255), # white
    "1": (0, 0, 0), # black
    "2": (255, 165, 0), # orange
    "3": (255, 192, 203), # pink
    "4": (46, 139, 87), # forest green
    "5": (255, 215, 0), # gold
    "6": (255, 69, 0), # orange red
    "7": (218, 112, 214), # orchid
    "8": (238, 232, 170), # pale goldenrod
    "9": (0, 255, 255), # aqua
    "!": (128, 0, 35), # maroon
    "@": (0, 128, 4), # dark green
    "#": (10, 0, 128), # navy
    "$": (128, 123, 0), # olive
    "%": (128, 5, 128), # purple
    "^": (0, 138, 128), # teal
    "&": (128, 108, 128), # gray
    " ": (123, 128, 118), # space
}


# Generate a random padding color
pad_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Encryption function
def encrypt_text(text):
    # Convert the text to lowercase
    text = text.lower()

    # Determine the dimensions of the image
    width = len(text)
    height = width

    # Count the number of spaces in the text
    num_spaces = text.count(" ")

    # Increase the width and height to account for the spaces
    width += num_spaces
    height += num_spaces

    # Create a new image
    image = Image.new("RGB", (width, height), pad_color)

    # Map each character to a color and set the corresponding pixel
    x = 0
    y = 0
    for char in text:
        if char == " ":
            # Assign a color for spaces
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

# Decryption function
def decrypt_text(image):
    # Determine the dimensions of the image
    width, height = image.size

    # Retrieve the color of each pixel along the diagonal
    colors = [image.getpixel((i, i)) for i in range(width)]

    # Map each color to a character and concatenate the results
    text = ""
    for c in colors:
        if c == (123, 128, 118):
            text += " "  # add a space for white pixels
        else:
            text += next((char for char, color in color_map.items() if color == c), "")


    return text

    return text

# Example usage
plaintext = "Leotrim2    34@@$!lirak"
encrypted_image = encrypt_text(plaintext)
decrypted_text = decrypt_text(encrypted_image)

print("Plaintext: ", plaintext)
print("Encrypted image: ")
encrypted_image.show()
print("Decrypted text: ", decrypted_text)
