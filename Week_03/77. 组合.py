class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def recall(n, k, start, result, subset):
            if len(subset) == k:
                result.append(subset[:])
                return
            for i in range(start, n+1):
                if k-len(subset) > n-i+1:
                    break
                subset.append(i)
                recall(n, k, i+1, result, subset)
                subset.pop()
        recall(n, k, 1, result, [])
        return result