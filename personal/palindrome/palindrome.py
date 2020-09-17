def palindrome(sentence):
    ans = []
    for letter in sentence:
        if letter.isalnum():
            ans.append(letter.lower())
    if ans == ans[::-1]:
        return True
    else:
        return False