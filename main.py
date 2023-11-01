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

#Sneha Nair COP3502C

def decode(encoded_password):
    decoded_password = ""
    for eachchar in encoded_password:
        newchar = str(int(eachchar) - 3)
        decoded_password += newchar
    return decoded_password


if __name__ == '__main__':
    while True:
        print_menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            requested_password = input("Please enter your password to encode: ")
            encoded_password = encoder(requested_password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
        elif choice == 3:
            exit()

