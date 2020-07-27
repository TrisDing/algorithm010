"""
Trie Data Structure
"""
import collections

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for letter in word:
            root = root.setdefault(letter, {})
        root['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for letter in word:
            root = root.get(letter)
            if root is None:
                return False
        return '#' in root

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for letter in prefix:
            root = root.get(letter)
            if root is None:
                return False
        return True

    def __str__(self):
        root = self.root
        return str(root)

trie = Trie()
trie.insert('apple')
print(trie)
print(trie.search('apple')) # True
print(trie.search('app')) # False
print(trie.startsWith('app')) # True
trie.insert("app")
print(trie.search("app")) # True