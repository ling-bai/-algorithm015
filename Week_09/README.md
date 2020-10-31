

### Week 09 Summary

#### 第十九课 高级动态规划

**小结提纲**

1.动态规划复习；附带 递归、分治

2.多种情况的动态规划的状态转移方程串讲

3.进阶版动态规划的习题



**递归：函数自己调用自己**

**分治代码模板**

```python
def divide_conquer(problem, param1, param2, ...):
  # recursion terminator
  if problem is None:
    print_result
    return
  
  # prepare data (准备数据和拆分问题)
  data = prepare_data(problem)
  subproblems = split_problem(problem, data)
  
  # conquer subproblems (调分治函数递归求解)
  subresult1 = self.divide_conquer(subproblems[0], p1, ...)
  subresult2 = self.divide_conquer(subproblems[1], p1, ...)
  subresult3 = self.divide_conquer(subproblems[2], p1, ...)
  ...
  
  # process and generate the final result (合并结果)
  result = process_result(subresult1, subresult2, subresult3)
  
  # revert the current level states
```

**感触**

1.人肉递归低效、很累

2.找到最近最简方法，将其拆解成可重复解决问题

3.数学归纳法思维

**本质：寻找重复性--->计算机指令集**



**动态规划 Dynamic Programming**

1."Simplifying a complicated problem by breaking it down into simpler sub-problems" (in a recursive manner)

2.Divide & Conquer + Optimal substructure (分治+最优子结构)

3.顺推形式：动态递推



**DP顺推模板**

```python
function DP():
  dp = [][] #二维情况
  
  for i = 0..M{
    for j = 0..N{
      dp[i][j] = _Function(dp[i'][j']...)
    }
  }
  
  return dp[M][N]
```

**关键点：**

动态规划 和 递归或者分治 没有根本上的区别（关键看有无最优的子结构）

拥有共性：找到重复子问题

差异性：最优子结构、中途可以淘汰次优解



#### 常见的DP题目和状态方程

![IMG_3830](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3830.PNG)

![IMG_3831](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3831.PNG)

![IMG_3832](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3832.PNG)

![IMG_3833](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3833.PNG)

**实战例题**

121.买卖股票的最佳时机

![IMG_3835](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3835.PNG)

![IMG_3836](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3836.PNG)

![IMG_3837](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3837.PNG)

#### 高阶的DP问题

**复杂度来源**

1.状态拥有更多维度（二维、三维、或者更多维）

2.状态方程更加复杂

**本质：内功、逻辑思维、数学**

**爬楼梯问题改进**

* 1、2、3
* x1, x2, ..., xm步
* 前后不能走相同的步伐

70.爬楼梯

```python
class Solution{
  public int climbStairs(int n){
    if(n <= 1)
    return n;
    
    int[] a = new int[n];
    
    a[0] = 1;
    a[1] = 2;
    
    for (int i = 2; i < n; ++i)
    		 a[i] = a[i-1] + a[i-2];
    
    return a[n-1];
  }
}
```

746.使用最小花费爬楼梯

72.编辑距离

```python
def minDistance(self, word1: str, word2: str) -> int:
  n1 = len(word1)
  n2 = len(word2)
  dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
  # 第一行
  for j in range(1, n2 + 1):
    dp[0][j] = dp[0][j-1] + 1
  # 第一列
  for i in range(1, n1 + 1):
    dp[i][0] = dp[i-1][0] + 1
  for i in range(1, n1 + 1):
    dp[i][0] = dp[i-1][0] + 1
  for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
      if word1[i-1] == word2[j-1]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
  # print(dp)
  return dp[-1][-1]
```

![IMG_3862](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3862.PNG)

85.最大矩形



#### 第二十课 字符串

字符串基础知识

遍历字符串

```python
for ch in "abbc":
  print(ch)
```

387.字符串中的第一个唯一字符

法1：brute-force:

i 枚举所有字符，j 枚举i 后面的所有字符 //找重复

O(n^2)

法2：map (hashmap O(1), treemap O(logN))

O(N) or O(NlogN)

法3：hash table

8.字符串转换整数（atoi）

```python
class Solution(object):
  
  def myAtoi(self, s):
    
    if len(s) == 0: return 0
    ls = list(s.strip())
    
    sign = -1 if ls[0] == '-' else 1
    
    if ls[0] in ['-','+']: del ls[0]
    
    ret, i = 0, 0
    
    while i < len(ls) and ls[i].isdigit():
      ret = ret*10 + ord(ls[i]) - ord('0')
      i += 1
      
    return max(-2**31, min(sign * ret, 2**31-1))
```

14.最长公共前缀

法1.纯暴力

法2.

flower

flow

flight

法3.Trie

344.反转字符串

1.split, reverse, join

2.reverse 整个string, 然后再单独reverse每个单词

eg:

the sky is blue

eulb si yks eht

blue is sky the

**anagram 异位词问题**

438.找到字符串中所有字母异位词

**Palindrome回文串问题**

5.最长回文子串



#### 高级字符串算法

![IMG_3897](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3897.PNG)

72.编辑距离

1143.最长公共子序列

```python
class Solution(object):
  def longestCommenSubsequence(self, text1, text2):
    if not text1 or not text2:
      return 0
    m = len(text1)
    n = len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
      for j in range(1, n+1):
        if text1[i-1] == text2[j-1]:
          dp[i][j] = 1 + dp[i-1][j-1]
        else:
          dp[i][j] = max(dp[i-1][j], dp[j][j-1])
    return dp[m][n]
```

![IMG_3903](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3903.PNG)

5.最长回文子串

法1：嵌套循环，枚举i, j （起点和终点），判断该子串是否回文

法2：中间向两边扩张法

法3：DP [i] [j]

![IMG_3907](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3907.PNG)

115.不同的子序列

#### 字符串匹配算法

![IMG_3910](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3910.PNG)

![IMG_3912](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3912.PNG)

![IMG_3913](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3913.PNG)

![IMG_3914](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3914.PNG)

![IMG_3915](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 9/IMG_3915.PNG)

