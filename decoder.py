
#Sneha Nair COP3502C

def decode(encoded_password):
    decoded_password = ""
    for eachchar in encoded_password:
        newchar = str(int(eachchar) - 3)
        decoded_password += newchar
    return decoded_password

