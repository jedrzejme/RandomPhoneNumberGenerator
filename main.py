from random import randint
from contextlib import redirect_stdout

def generate_phone_number(template):
    exec(f"""print(f"{template}")""")

def generate_output(template):
    n = int(input("How many phone numbers to generate: "))
    save_to_file = str(input("Save to file? [y/n] "))
    if save_to_file == "y":
        filename = str(input("File name: "))
        with open(f"{filename}.txt", 'w') as file:
            with redirect_stdout(file):
                for i in range(n):
                    generate_phone_number(template)
    else:
        for i in range(n):
            generate_phone_number(template)

def end():
    input("Press enter to exit")
    exit()

country = str(input("Select country [USA/Poland/Custom] "))

if country == "USA":
    generate_output("+1 ({randint(0,9)}{randint(0,9)}{randint(0,9)}){randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}")
    end()

if country == "Poland":
    generate_output("+48 {randint(1,9)}{randint(0,9)}{randint(0,9)} {randint(0,9)}{randint(0,9)}{randint(0,9)} {randint(0,9)}{randint(0,9)}{randint(0,9)}")
    end()

if country == "Custom":
    filename = str(input("File name with custom template: "))
    file = open(f"{filename}.txt","r")
    template = file.read()

    generate_output(template)

    end()

print("Wrong country")
end()