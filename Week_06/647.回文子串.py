class Solution:
        def countSubstrings(self, s: str) -> int:
            n = len(s)
            self.res = 0
            def helper(i,j):
                while i >= 0 and j < n and s[i] == s[j]:
                    i -= 1
                    j += 1
                    self.res += 1
            for i in range(n):
                helper(i,i)
                helper(i,i+1)
            return self.res