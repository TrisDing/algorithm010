"""
146. LRU Cache <Medium>
https://leetcode.com/problems/lru-cache/
"""
import collections

class LRUCache:
	def __init__(self, capacity):
		self.dic = collections.OrderedDict()
		self.remain = capacity

	def get(self, key):
		if key not in self.dic:
			return -1
		value = self.dic.pop(key)
		self.dic[key] = value # key is now the latest one
		return value

	def put(self, key, value):
		if key in self.dic:
			self.dic.pop(key)
		else:
			if self.remain > 0:
				self.remain -= 1
			else: # self.dic is full
				self.dic.popitem(last=False)
		self.dic[key] = value

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache2:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # if key exists, locate node in cache, then move to head
        node = self.cache[key] # key is now least recently used
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

cache = LRUCache(2)
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))       # returns 1
print(cache.put(3, 3))    # evicts key 2
print(cache.get(2))       # returns -1 (not found)
print(cache.put(4, 4))    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4

cache2 = LRUCache2(2)
print(cache2.put(1, 1))
print(cache2.put(2, 2))
print(cache2.get(1))       # returns 1
print(cache2.put(3, 3))    # evicts key 2
print(cache2.get(2))       # returns -1 (not found)
print(cache2.put(4, 4))    # evicts key 1
print(cache2.get(1))       # returns -1 (not found)
print(cache2.get(3))       # returns 3
print(cache2.get(4))       # returns 4