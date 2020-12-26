![](https://img.shields.io/badge/Language-Python3-brightgreen?style=flat-square)

# Most Common Word

출처 : https://leetcode.com/problems/most-common-word/



## ❓ Problem

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words. It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation. Words in the paragraph are not case sensitive. The answer is in lowercase.

### Example

```
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
```





## ❗ Submit

```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^\w]',' ', paragraph)
                 .lower().split()
                 if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
```

- Runtime : 36ms
- Memory : 14.6MB



### Commentary

- 문자열 정규식 활용 방법

  - ```\w``` : 단어 문자
  - ```^``` : not

  ```paragraph```에서 단어 문자가 아닌 모든 문자열을 공백으로 치환하는 것을 의미한다.

- 리스트 컴프리헨션을 활용하면 간결하고 직관적으로 코드를 작성할 수 있다. 
- ```collections.Counter```는 Python에 내장된 모듈을 이용한 것으로, 원소들의 개수를 딕셔너리 형태로 출력한다. 



### References

- 박상길,  ｢파이썬 알고리즘 인터뷰｣, 책만(2020)

- https://docs.python.org/3/library/collections.html#collections.Counter