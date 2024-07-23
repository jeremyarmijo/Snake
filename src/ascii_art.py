import pyfiglet
from pyfiglet import Figlet

def check_font(figlet, text, my_font):
    try:
        text = pyfiglet.figlet_format(text, font=my_font)
    except:
        print("Invalid usage")
        exit(-1)
    return text

def print_ascii_art(my_input, my_font):
    text = str(my_input)
    figlet = Figlet()
    ascii_art = check_font(figlet, text, my_font)
    print(ascii_art)

if __name__ == "__main__":
    print_ascii_art("hello world", "slant")