"""
127. Word Ladder <Medium>
https://leetcode.com/problems/word-ladder/description/
"""
from typing import List
import collections
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Bidirectional BFS
        """
        wordList = set(wordList)
        if not wordList or endWord not in wordList:
            return 0

        beginQueue = collections.deque([beginWord])
        endQueue = collections.deque([endWord])
        visited = set([beginWord])
        step = 0

        while beginQueue and endQueue:
            step += 1
            if len(beginQueue) > len(endQueue):
                beginQueue, endQueue = endQueue, beginQueue
            for _ in range(len(beginQueue)):
                word = beginQueue.popleft()
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c == word[i]:
                            continue
                        newword = word[:i] + c + word[i+1:]
                        if newword in endQueue:
                            return step + 1
                        if not newword in visited and newword in wordList:
                            beginQueue.append(newword)
                            visited.add(newword)
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
