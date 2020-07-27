def alphabet_position(text):
    pass
    letter_order = []
    for letter in text:
        if letter.islower():
            letter_order.append(ord(letter)-96)
        elif letter.isupper():
            letter_order.append(ord(letter)-64)
        else:
            pass
    for letter in range(len(letter_order)):
        letter_order[letter] = str(letter_order[letter])
    return ' '.join(letter_order)