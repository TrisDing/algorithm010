"""
433. Minimum Genetic Mutation <Medium>
https://leetcode.com/problems/minimum-genetic-mutation/
"""
from typing import List
from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        step = 0
        queue = deque([start])
        while queue:
            n = len(queue)
            for _ in range(n):
                gene = queue.popleft()
                if gene == end:
                    return step
                mutations = self.mutate(gene)
                for mutation in mutations:
                    if mutation in bank:
                        queue.append(mutation)
                        bank.remove(mutation)
            step += 1

        return -1

    def mutate(self, gene: str) -> List[str]:
        mutation_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }
        res = []
        for i, s in enumerate(gene):
            for c in mutation_map[s]:
                mutation = gene[:i] + c + gene[i+1:]
                res.append(mutation)
        return res

solution = Solution()
print(solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])) # 1
print(solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])) # 2
print(solution.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"])) # 3