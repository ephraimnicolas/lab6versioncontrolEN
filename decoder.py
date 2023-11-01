
#Sneha Nair COP3502C

def decode(encoded_password):
    decode_password = ""
    for eachchar in encoded_password:
        newchar = str(int(eachchar) - 3)
        decode_password += newchar
    return decode_password

