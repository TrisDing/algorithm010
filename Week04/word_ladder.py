"""
127. Word Ladder <Medium>
https://leetcode.com/problems/word-ladder/description/
"""
from typing import List
import collections
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        step = 1
        queue = collections.deque([beginWord])
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c == word[i]:
                            continue
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordList:
                            queue.append(new_word)
                            wordList.remove(new_word)
            step += 1
        return 0


solution = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(solution.ladderLength(beginWord, endWord, wordList)) # 5

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(solution.ladderLength(beginWord, endWord, wordList)) # 0
