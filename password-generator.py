import string
import random


class PasswordGenerator:
    password_list = []

    def start_generate(self, length):
        password = ""
        all_characters = string.printable + string.digits + string.ascii_letters
        while length > 0:
            characters = random.choice(all_characters)
            if "\n" in characters or "\t" in characters or " " in characters:
                continue
            password += characters
            length -= 1
        self.password_list.append(password)
        return password, f"password length is {len(password)}"


while True:
    request = input("Run password generator (Enter Yes or No) ? ")
    match request.title():
        case "Yes":
            obj = PasswordGenerator()
            length = int(input("Enter password length : "))
            result = obj.start_generate(length)
            print(f"Password generated. {result[1]}\n{result[0]}")
        case "No":
            print("Password generator task finished")
            break
        case "Show" | "List" | "All" | "List Password" | "All Password":
            count_run = 0
            for i in obj.password_list:
                count_run += 1
                print(f"password {count_run} : {i}")
        case _:
            print("Enter Yes or No")
