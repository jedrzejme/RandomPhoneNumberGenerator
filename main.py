from random import randint
from contextlib import redirect_stdout
import requests
import shutil
import os

def download_file(url, destination):
    folder_name = "templates"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        file_path = os.path.join(destination, file_name)

        with open(file_path, 'wb') as file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, file)

def generate_phone_number(template):
    exec(f"""print(f"{template}")""")

def generate_output(template):
    n = int(input("How many phone numbers to generate: "))
    save_to_file = str(input("Save to file? [y/n] "))
    if save_to_file == "y":
        filename = str(input("File name: "))
        if ".txt" in filename:
            with open(f"{filename}", 'w') as file:
                with redirect_stdout(file):
                    for i in range(n):
                        generate_phone_number(template)
        else:
            with open(f"{filename}.txt", 'w') as file:
                with redirect_stdout(file):
                    for i in range(n):
                        generate_phone_number(template)
    else:
        for i in range(n):
            generate_phone_number(template)
    end()

def end():
    input("Press enter to exit")
    exit()

url = f"https://raw.githubusercontent.com/jedrzejme/RandomPhoneNumberGenerator/main/templates/USA.txt"
destination = "templates"
download_file(url, destination)
url = f"https://raw.githubusercontent.com/jedrzejme/RandomPhoneNumberGenerator/main/templates/POL.txt"
destination = "templates"
download_file(url, destination)

country = str(input("Select country [USA/POL/Custom] "))

if os.path.isfile(f"templates/{country}.txt"):
    if country != "Custom":
        file = open(f"templates/{country}.txt", "r")
        generate_output(file.read())

    if country == "Custom":
        filename = str(input("File name with custom template: "))
        if ".txt" in filename:
            file = open(f"templates/{filename}","r")
        else:
            file = open(f"templates/{filename}.txt","r")
        template = file.read()

        generate_output(template)

print("Wrong country")
end()