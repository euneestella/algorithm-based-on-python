def alphabet_position(text):
    # Use ASCII Code to incode alphabet into a digit
    pass
    letter_order = []
    for letter in text:
        if letter.islower():
            letter_order.append(ord(letter)-(97-1)) # lowercase starts from 97
        elif letter.isupper():
            letter_order.append(ord(letter)-(65-1)) # uppercase starts from 65
        else:
            pass
    for letter in range(len(letter_order)):
        letter_order[letter] = str(letter_order[letter])
    return ' '.join(letter_order)