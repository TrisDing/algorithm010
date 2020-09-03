Learning Notes Week 09
======================

String
------

String Operations
```py
s.strip([chars])     # return a copy of the string with the leading and trailing characters removed.
s.startswith(prefix) # return True if string starts with the prefix, False otherwise.
s.endswith(prefix)   # return True if string starts with the prefix, False otherwise.
s.slipt(delimiter)   # return a list of the words of the string s.
s.lower()            # return a copy of the string with all the lowercase characters
s.upper()            # return a copy of the string with all the uppercase characters
ord(c)               # the unicode code representation of the char
ord(c) - ord('a')    # the position of the char in 26 letters
chr(i)               # string representation of the char unicode code
```

String Constants
```py
import string

string.digits          # the string '0123456789'
string.hexdigits       # the string '0123456789abcdefABCDEF'
string.octdigits       # the string '01234567'
string.ascii_lowercase # the uppercase letters 'abcdefghijklmnopqrstuvwxyz'
string.ascii_letters   # The lowercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.letters         # The concatenation of the ascii_lowercase and ascii_uppercase
```

Sliding Window Template
```py
from collections import Counter

def slidingWindow(s, t):
    window = Counter()
    target = Counter(t)

    valid = 0
    left = right = 0
    while right < len(s):
        # c is the element to be inserted into the window
        c = s[right]
        # if we insert it, is the window still valid?
        if c in target:
            window[c] += 1
            if window[c] == target[c]:
                valid += 1
        # expand the current window
        right += 1

        print(s[left: right])

        # when we found a valid window
        while right - left >= len(t):
            # check the answer or update the result
            if valid == len(target):
                ...

            # d is the element to be removed from the window
            d = s[left]
            # if we remove it, is the window still valid?
            if d in target:
                if window[d] == target[d]:
                    valid -= 1
                window[d] -= 1
            # shrink the current window
            left += 1
```

String Basics
- [709. To Lower Case](https://leetcode-cn.com/problems/to-lower-case/)
- [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
- [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)
- [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)
- [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

String Operations
- [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- [344. Reverse String](https://leetcode.com/problems/reverse-string/)
- [541. Reverse String II](https://leetcode.com/problems/reverse-string-ii/)
- [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
- [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)
- [917. Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)

Palindrome
- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

Anagram
- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

Sliding Window
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

Advanced String Problems
- [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
- [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
- [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

String-searching algorithms
-----------

| algorithm   | Preprocessing Time | Matching Time | Space |
| ----------  | :----------------: | :-----------: | :---: |
| Naive       | None               | O(mn)         | None  |
| Rabin-Karp  | O(m)               | O(n+m)        | O(1)  |
| KMP         | O(m)               | O(n)          | O(m)  |
| Boyer-Moore | O(m+k)             | O(mn)         | O(k)  |