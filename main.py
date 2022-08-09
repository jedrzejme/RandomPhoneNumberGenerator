from random import randint
from contextlib import redirect_stdout

country = str(input("Select country [USA/Poland/Custom] "))

if country == "USA":
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

    input("Press enter to exit")
    exit()

if country == "Poland":
    def generate_phone_number():
        print(f"+48 {randint(1,9)}{randint(0,9)}{randint(0,9)} {randint(0,9)}{randint(0,9)}{randint(0,9)} {randint(0,9)}{randint(0,9)}{randint(0,9)}")

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

    input("Press enter to exit")
    exit()

if country == "Custom":
    def generate_phone_number():
        exec(f"""print(f"{template}")""")
    
    filename = str(input("File name with custom template: "))
    file = open(f"{filename}.txt","r")
    template = file.read()

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

    input("Press enter to exit")
    exit()

print("Wrong country")
input("Press enter to exit")
exit()