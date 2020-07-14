def caesar_cipher(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = []
    for letter in text:
        if letter.islower():
            cipher.append(alphabet[(alphabet.index(letter)+3)%26])
        elif letter.isupper():
            cipher.append(alphabet.upper()[(alphabet.upper().index(letter)+3)%26])
        else :
            cipher.append(letter)
    return ''.join(cipher)