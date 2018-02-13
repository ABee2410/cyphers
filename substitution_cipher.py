alphabet = "abcdefghijklmnopqrstuvwxyz !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`{|}~"
key = "qwyuiop1@2#37*8(9)0_-+=sazxlkjhe$4%5^6&rtgfd]|YUIcvbnm ~`!{[}OPLKJH\\:;\"'?/>.<,QWERTGFDSAZXCVBNM"

def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]
        
    return result

def decrypt(message):
    result = ""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]
        
    return result

unencrypted_message = "GUARD: I don't want to talk to you no more, you empty headed animal food trough whopper! I fart in your general direction! You mother was a hamster and your father smelt of elderberries!"
encrypted_message = encrypt(unencrypted_message)

print(unencrypted_message)
print(encrypted_message)
print(decrypt(encrypted_message))
