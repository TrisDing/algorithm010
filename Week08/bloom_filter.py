"""
Bloom Filter
"""
from bitarray import bitarray
import mmh3

class BloomFilter:
	def __init__(self, size, hashes):
		self.size = size
		self.hashes = hashes
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)

	def add(self, s):
		for seed in range(self.hashes):
			result = mmh3.hash(s, seed) % self.size
			self.bit_array[result] = 1

	def lookup(self, s):
		for seed in range(self.hashes):
			result = mmh3.hash(s, seed) % self.size
			if self.bit_array[result] == 0:
				return 'Nope'
		return 'Probably'

bf = BloomFilter(500000, 7)
bf.add("bloom")
print(bf.lookup("bloom"))
print(bf.lookup("filter"))