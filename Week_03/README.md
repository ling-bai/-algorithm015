### Week 03 Summary

#### 1. 分治 (Divide & Conquer)

分治本质上就是递归

递归状态树：将问题一步步split为 子问题，conquer解决所有子问题 (sub-problem)，再将这些解法 (sub-solution) merge为问题的solution。最后本质上就是找重复性以及分解问题。

**分治代码模板**

```python
def divide_conquer (problem, param1, param2, ...):
  # recursion terminator (递归终结者)
  if problem is None:
    print_result
    return
  # prepare data (处理当前层逻辑)
  data = prepare_data(problem)
  subproblems = split_probem(problem, data)
  # conquer subproblems (下探到下一层)
  subresult1 = self.divide_conquer(subproblems[0], p1, ...)
  subresult2 = self.divide_conquer(subproblems[1], p1, ...)
  subresult3 = self.divide_conquer(subproblems[2], p1, ...)
  ...
  # process and generate the final result
  result = process_result(subresult1, subresult2, subresult3)
```

分治的代码模板与递归的很类似，比递归多了一步

**递归代码模板**

```python
def recursion(level, param1, param2, ...):
  # recursion terminator
  if level > MAX_LEVEL:
    process_result
    return
  
  # process logic in current level
  process(level, data...)
  
  # drill down
  self.recursion(level+1, p1, ...)
  
  # reverse the current level status if needed
```

#### 2. 回溯 (Backtracking)

回溯法采用试错的思想，通常用最简单的递归方法来实现，最后可能出现两种情况：

1) 找到一个可能存在的正确答案

2) 尝试了所有可能分步方法后，没有答案

在最坏情况下，回溯会导致复杂度为指数时间的计算

**例题讲解**

22.括号生成

50.Pow (x,n)

```python
# 1.暴力 O(n)时间复杂度
# result = 1
# for i: 0 -> n {
#  result *= x
# }

# 2.分治
# template:
# 1.terminator
# 2.process(split your big problem)
# 3.drill down (sub-problems), merge(sub-solution)
# 4.reverse states

# x^n ---> 2^10: 2^5 ---> (2^2)*2
# pow(x, n):
# 		subproblem: subresult = pow(x, n/2)

# merge: 
#			if n % 2 == 1 {
# odd
# 				result = subresult * subresult * x;
# 		} else {
# even
# 				result = subresult * subresult
# 		}

class Solution(object):
  def subsets(self, nums):
    result = [[]]
    
    for num in nums:
      	newsets = []
        for subset in result:
          new_subset = subset + [num]
          newsets.append(new_subset)
          
        result.extend(newsets)
        
     return result
 
# 优秀题解
# 思路：迭代
class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    res = [[]]
    for i in nums:
      	res = res + [[i] + num for num in res]
    return res
  
# 思路：递归（回溯）
class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    
    def helper(i, tmp):
      res.append(tmp)
      for j in range(i, n): # 往后面选元素，加入这里
        helper(j + 1, tmp + [nums[j]])
    helper(0, [])
    return res
```

17.电话号码的字母组合

51.N皇后

```python
class Solution(object):
  
  def solveNQueens(self, n):
    if n < 1: return []
    
    self.result = []
    self.cols = set();
    self.pie = set();
    self.na = set();
    self.DFS(n, 0, [])
    return self._generate_result(n)
  
  def DFS(self, n, row, cur_state):
    # recursion terminator
    if row >= n:
      	self.result.append(cur_state)
        return
      
    # current level
    for col in range(n):
      if col in self.cols or row + col in self.pie or row - col in self.na:
        # go die!
        continue
        
      # update the flags
      self.cols.add(col)
      self.pie.add(row + col)
      self.na.add(row - col)
      
      self.DFS(n, row + 1, cur_state + [col])
      # reverse states
      self.cols.remove(col)
      self.pie.remove(row + col)
      self.na.remove(row - col)
      
      # 生成满足要求的输出数组形式(输出棋盘)
  def _generate_result(self, n):
      board = []
      for res in self.result:
        for i in res:
          board.append("." * i + "Q" + "." * (n - i -1))
          
      return [board[i: i + n] for i in range(0, len(board), n)]    
```

