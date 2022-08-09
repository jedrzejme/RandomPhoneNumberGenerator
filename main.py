from random import randint
from contextlib import redirect_stdout

def generate_phone_number():
    print(f"+1 ({randint(0,9)}{randint(0,9)}{randint(0,9)}){randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}")

n = int(input("How many phone numbers to generate: "))
save_to_file = str(input("Save to file? [y/n] "))
if save_to_file == "y":
    filename = str(input("File name: "))
    with open(f"{filename}.txt", 'w') as file:
        with redirect_stdout(file):
            for i in range(n):
                generate_phone_number()
else:
    for i in range(n):
        generate_phone_number()

input()