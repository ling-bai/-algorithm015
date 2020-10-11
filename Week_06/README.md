### Week 06 Summary

#### 动态规划

本质：寻找重复性

分治+最优子结构

关键点：

动态规划 和 递归或者分治 没有根本上的区别（关键看有无最优的子结构）

**共性：找到重复子问题**

差异性：最优子结构、中途可以**淘汰**次优解



##### 实战例题1：斐波那契数列

fib(n) = fib(n-1) + fib(n-2)                "Bottom Up"

fib(0) = 0

fib(1) =1

```python
int fib (int n){
  if (n <= 0){
    return 0;
  } else if (n == 1){
    return 1;
  } else {
    return fib (n-1) + fib (n-2);
  }
}
```

```python
int fib (int n, int[] memo){
  if (n <= 1){
    return n;
  }
  
  if (memo[n] == 0) {   # memo数组，将复杂度从O(2^n)降到O(n)
    memo[n] = fib(n-1) + fib(n-2);
  }
  return memo[n];
}
```



##### 实战例题2：路径计数

状态转移方程（DP方程）

opt[i, j] = opt[i+1, j] + opt[i, j+1]

完整逻辑：

if a[i, j] = “空地”：

opt[i, j] = opt[i+1, j] + opt[i, j+1]

else:

opt[i, j] = 0

**动态规划关键点**

1.最优子结构 opt[n] = best_of(opt[n-1], opt[n-2], ...)

2.储存中间状态：opt[i]

3.递推公式（美其名曰：状态转移方程或者DP方程）

Fib: opt[i] = opt[n-1] + opt[n-2]

二维路径：opt[i,j] = opt[i+1] [j] + opt[i] [j+1] （且判断a[i,j]是否空地）



##### 实战例题3：1143.最长公共子序列

当进行DP的时候，会把它扩展成为一个二维的数组来定义状态

```python
class Solution(object):
  def longestCommonSubsequence(self, text1, text2):
    if not text1 or not text2:
      return 0
    m = len(text1)
    n = len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
      for j in range(1,n+1):
        if text1[i-1] == text2[j-1]:
          dp[i][j] = 1+dp[i-1][j-1]
        else:
          dp[i][j] = max(dp[i-1][j],dp[i][]j-1)
    return dp[m][n]
```

本题思维的关键是，能够把两个字符串求它的距离的问题，求它的类似于你可以认为是编辑距离的问题，转换成一个二维数组递推的问题，也就是我们前面讲的第二步。

就是如何把一个动态规划的问题，然后就得到text1的length。记为m和n是方便后面好写。一开始初始化全部为0，它就会把DP的二维数组搞成m*n，(m+1) * (n+1)的长维度。且里面的每一个值都是0，写两个嵌套的循环，那就是，有时候定义n+1，以及初始化要初始化好，同时它的下标的位置要别越界，以及最后结果是在m和n这个位置。

**字符串问题**

1.S1 = “”

   S2 = 任意字符串

2.S1 =“A”

   S2 = 任意

3.S1 =“……A”

   S2 = "....A"

假设最后一个字符都相同的话，就直接用-1表示最后一个字符

**子问题**

S1 = “ABAZDC”

S2 = "BACBAD"

if S1[-1] != S2[-1]:LCS[s1, s2] = Max(LCS[s1-1, s2], LCS[s1,s2-1])

LCS[s1,s2] = Max(LCS[s1-1, s2], LCS[s1, s2-1], LCS[s1-1, s2-1])

if S1[-1] == S2[-1]:LCS[s1, s2] = LCS[s1-1, s2-1] +1

LCS[s1, s2] = Max(LCS[s1-1, s2], LCS[s1, s2-1], LCS[s1-1, s2-1], LCS[s1-1] [s2-1] + 1)

**DP方程**

if s1[-1] != s2[-1]: LCS[s1, s2] = Max(LCS[s1-1, s2], LCS[s1, s2-1])

if s1[-1] == s2[-1]: LCS[s1, s2] = LCS[s1-1, s2-1] +1

DP方程最后简化下来，就是如果最后一个字符不相同的话，那么，要么第一个字符串减去一个，要么第二个字符串减去一个。求它们的最长公共子序列较大值。

或者，如果是最后一个字符相同的话，我们就+1，然后取把相同的字符丢掉之后，它前面的两个子串之间的最长公共子序列。

**动态规划小结**

1.打破自己的思维惯性，形成机器思维

2.理解复杂逻辑的关键

3.也是职业进阶的要点要领



##### 实战题目

* 70.爬楼梯

DP方程：f(n) = f(n-1) + f(n-2)

1. 1, 2, 3 (easy)

2. 相邻两步的步伐不能相同 (medium)

* 120.三角形最小路径和

1. brute-force, 递归，n层：left or right: 2^n
2. DP

a) 重复性（分治）

b) 定义状态数组

c) DP方程：f[i, j] = min(f[i+1, j], f[i+1, j+1]) + a[i, j]

```python
class Solution(object):
  def minimumTotal(triangle):
    """
    dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
    """
    mini, M = triangle[-1], len(triangle)
    for i in range(M-2, -1, -1):
      for j in range(len(triangle[i])):
        mini[j] = triangle[i][j] + min(mini[j], mini[j+1])
      return mini[0]
```

```python
class Solution(object):
  def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp = triangle #此二维数组可减少在访问triangle[i][j]来累加，把triangle的所有值都初始化到dp里面去了。
    for i in range(len(triangle)-2, -1, -1):
      for j in range(len(triangle[i])):
        dp[i][j] += min(dp[i+1][j],dp[i+1][j+1])
      print(triangle[0][0])
      return dp[0][0]
```

```python
# 另一种解法，从上到下的循环
# O(n*n/2) space, top-down
def minimumTotal(self, triangle):
  if not triangle:
    return
  res = [[0 for i in xrange(len(row))] for row in triangle]
  res[0][0] = triangle[0][0]
  for i in xrange(1, len(triangle)):
    for j in xrange(len(triangle[i])):
      if j == 0:
        res [i][j] = res[i-1][j] + triangle[i][j]
      elif j == len(triangle[i]-1):
        else:
          res[i][j] = min(res[i-1][j-1], res[i-1][j] + triangle[i][j])
   return min(res[-1])

# Modify the original triangle, top-down
def minimumTotal2(self, triangle):
  if not triangle:
    return
  for i in xrange(len(triangle)-2, -1, -1):
    for j in xrange(len(triangle[i])):
      triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

# bottom-up, O(n) space
def minimumTotal(self, triangle):
  if not triangle:
    return
  res = triangle[-1]
  for i in xrange(len(triangle)-2, -1, -1):
    for j in xrange(len(triangle[i])):
      res[j] = min(res[j], res[j+1] + triangle[i][j])
  return res[0]
```

* 53.最大子序和

给定一个整数数组，找到一个具有最大和的连续子数组

思路：定义子问题如下：

1.暴力：n^2

2.DP:

a) 分治（子问题）max_sum(i) = Max(max_sum(i-1), 0)  + a[i]

b) 状态数组定义: f[i]

c) DP方程: f[i] = Max(f[i-1], 0) + a[i]

```python
class Solution(object):
  def maxSubArray(self, nums):
    """
    1.dp问题。公式为：dp[i] = max(nums[i], nums[i] + dp[i-1])
    2.最大子序和 = 当前元素自身最大，或者包含之前后最大
    """
	for i in range(1,len(nums)):
    # nums[i-1]代表dp[i-1]
    nums[i] = max(0, nums[i-1]) + nums[i]
   
  return max(nums)
```

* 152.乘积最大子序列

思路同上，但需要额外考虑负负得正的情况。只要把最正的记下来

```python
class Solution:
  def maxProduct(self, nums:List[int]) -> int:
    mi = ma = res = nums[0]
    for i in range(1, len(nums)):
      if nums[i] < 0: mi, ma = ma, mi
      ma = max(ma * nums[i], nums[i])
      mi = min(mi * nums[i], nums[i])
      res = max(res, ma)
     return res
```

* 322.凑硬币（coin change）

1.暴力：递归：指数

2.BFS

3.DP

a) subproblems

b) DP array: f(n) = min{f(n-k), for k in [1, 2, 5]}) +1

c) DP 方程

* 198.打家劫舍

* 213.打家劫舍II





