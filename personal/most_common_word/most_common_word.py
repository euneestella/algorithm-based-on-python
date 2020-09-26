import re
from collections import Counter

paragraph = "Bob hit a bAll, the hit BALL flew far after it was hit."
banned = ["hit"]

def common_word(paragraph):
    word = [word for word in re.sub('[,.]','',paragraph).lower().split()
            if word not in banned]
    return Counter(word).most_common(1)[0][0]