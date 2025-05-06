import random
import string


# print("Welcome to the password generator")


def generator():
    def input_length():
        try:
            length = int(input("Enter password length : "))
            if 0 < length < 600:
                return length
            else:
                print("The password length must be between 0 and 600")
        except:
            print("Your input not is int")
            print("Try again")
        input_length()

    def amount_of_string_usage():
        characters = string.ascii_letters
        upper_lower_case = input("Enter None or Low or Medium or High or Very High : ")
        match upper_lower_case.title():
            case "None":
                return characters * 0
            case "Low":
                return characters * 1
            case "Medium":
                return characters * 2
            case "High":
                return characters * 3
            case "Very High":
                return characters * 4
            case _:
                print("This input in not valid\nTry again")
                amount_of_string_usage()

    def confirm_use_item(show_input_text, try_again_text, item):
        while True:
            input_request = input(show_input_text)
            match input_request.title():
                case "Yes":
                    return item
                case "No":
                    return ""
                case _:
                    print(try_again_text)

    def password_generator():
        def random_characters():
            result = random.choice(characters)
            yield result

        password_length = input_length()
        print("How much uppercase and lowercase letters are used ? ")
        characters = amount_of_string_usage()
        characters = characters + confirm_use_item(
            "Should a numbers be used ? ", "Enter Yes or No", string.digits
        )
        characters = characters + confirm_use_item(
            "Should a Spaces be used ? ", "Enter Yes or No", " "
        )
        characters = characters + confirm_use_item(
            "Should a Symbols be used ? ", "Enter Yes or No", string.punctuation
        )
        password = ""
        while password_length > 0:
            password += next(random_characters())
            password_length -= 1
        return password

    password = password_generator()
    print("Password created")
    print(f"Password : '{password}'")
    return password


def run_task_password_generator():
    password_list = []
    while True:
        run_request = input(
            "Do you want to create a password (Type 'show' to see all passwords) ? "
        )
        match run_request.title():
            case "Yes":
                password = generator()
                password_list.append(password)
            case "No":
                print("\nThe password generator task has been closed\n")
                break
            case "Show" | "List" | "Show List" | "Passwords" | "Password List":
                if len(password_list) > 0:
                    run = 1
                    for i in password_list:
                        print(f"password {run} : {i}")
                        run += 1
                    while True:
                        save_request = input(
                            "Do you want to save these passwords in a file ? "
                        )
                        match save_request.title():
                            case "Yes":
                                file_name = input("Enter file name : ")
                                with open(file_name, "w") as file:
                                    for i in password_list:
                                        file.write(f"{i}\n")
                                        print(
                                            f"The Password have been saved if file {file_name}"
                                        )
                                break
                            case "No":
                                break
                            case _:
                                print("Enter Yes or No")
                else:
                    print("You didn't generate any passwords")
            case _:
                print("Enter Yes or No")


if __name__ == "__main__":
    run_task_password_generator()
