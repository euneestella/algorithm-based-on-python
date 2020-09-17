def palindrome(sentence):
    ans = []
    for char in sentence:
        if char.isalnum():
            ans.append(char.lower())
    return ans == ans[::-1]