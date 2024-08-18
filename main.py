# Random Phone Number Generator
# Author: Jędrzej Bakalarski
# Github: https://github.com/jedrzejme/RandomPhoneNumberGenerator

from random import randint
from contextlib import redirect_stdout
import requests
import shutil
import os

directoryOfRandomPhoneNumberGenerator = "RandomPhoneNumberGenerator"
directoryOfTemplates = f"{directoryOfRandomPhoneNumberGenerator}/templates"
directoryOfGenerated = f"{directoryOfRandomPhoneNumberGenerator}/generated"

def download_file(url, destination):
    folder_name = directoryOfTemplates
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        file_path = os.path.join(destination, file_name)

        with open(file_path, 'wb') as file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, file)

urlUSA = f"https://raw.githubusercontent.com/jedrzejme/RandomPhoneNumberGenerator/main/templates/USA.txt"
urlPOL = f"https://raw.githubusercontent.com/jedrzejme/RandomPhoneNumberGenerator/main/templates/POL.txt"
destination = directoryOfTemplates
print("Downloading templates...")
download_file(urlUSA, destination)
download_file(urlPOL, destination)

def generate_phone_number(template):
    exec(f"""print(f"{template}")""")

def generate_output(template):
    n = int(input("How many phone numbers to generate: "))
    save_to_file = str(input("Save to file? [y/n] "))
    if save_to_file == "y":
        filename = str(input("File name: "))
        folder_name = directoryOfGenerated
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        if ".txt" in filename:
            print("Generating phone numbers...")
            with open(f"{directoryOfGenerated}/{filename}", 'w') as file:
                with redirect_stdout(file):
                    for i in range(n):
                        generate_phone_number(template)
            print("Done!")
        else:
            print("Generating phone numbers...")
            with open(f"{directoryOfGenerated}/{filename}.txt", 'w') as file:
                with redirect_stdout(file):
                    for i in range(n):
                        generate_phone_number(template)
            print("Done!")
    else:
        print("Generating phone numbers...")
        for i in range(n):
            generate_phone_number(template)
        print("Done!")
    end()

def end():
    input("Press enter to exit")
    exit()

country = str(input("Select country [USA/POL/Custom] "))

if os.path.isfile(f"{directoryOfTemplates}/{country}.txt"):
    if country != "Custom":
        file = open(f"{directoryOfTemplates}/{country}.txt", "r")
        generate_output(file.read())

    if country == "Custom":
        filename = str(input("File name with custom template: "))
        if ".txt" in filename:
            file = open(f"{directoryOfTemplates}/{filename}","r")
        else:
            file = open(f"{directoryOfTemplates}/{filename}.txt","r")
        template = file.read()

        generate_output(template)

print("Wrong country")
end()