def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encoder(password):
    new_password = ""
    for element in password:
        nums = str(int(element) + 3)
        new_password += nums
    return new_password

if __name__ == '__main__':
    while True:
        print_menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            requested_password = input("Please enter your password to 
encode: ")
            encoded_password = encoder(requested_password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            print(f"The encoded password is {encoded_password}, and the 
original password is {requested_password}.")
        elif choice == 3:
            exit()

