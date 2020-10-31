# range第三个参数是一个步进，结合flag，实现第奇数个k步长翻转，偶数个k步长不翻转。range最后一段不够k长度的就是实际剩余长度。

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res, flag = "", True
        for i in range(0, len(s), k):
            res += s[i:i + k][::-1] if flag else s[i:i+k]
            flag = not flag
        return res