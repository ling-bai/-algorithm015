### Week 04 Summary

#### 1. 深度优先搜索和广度优先搜索

遍历搜索：在树（图/状态集）中寻找特定结点

示例代码

```python
class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left,self.right = None
```

 搜索 - 遍历

* 每个节点都要访问一次
* 每个节点仅仅要访问一次
* 对于节点的访问顺序不限
  - 深度优先：depth first search
  - 广度优先：breadth first search
  - 优先级优先：更加适用于现实中的业务场景（启发式搜索）

示例代码

```python
def dfs(node):
  
  if node in visited:
    # already visited
    return
  
  visited.add(node)
  
  # process current node
  # ... # logic here
  dfs(node.left)
  dfs(node.right)
```

##### 深度优先搜索 （Depth-First-Search）

```python
# DFS 代码 - 递归写法

visited = set()

def dfs(node, visited): # 递归终止条件
  visited.add(node)
  # process current node here.
  ...
  for next_node in node.children():
    if not next_node in visited:
      dfs(next node, visited)
```

```python
# DFS 代码 - 非递归写法（即，手动维护一个栈）

def DFS(self, tree):
  
  if tree.root is None:
    return []
  
  visited, stack = [],[tree.root]
  
  while stack:
    node = stack.pop()
    visited.add(node)
    
    process(node)
    nodes = generate_related_nodes(node)
    stack.push(nodes)
    
   # other processing work
  ...
```

##### 广度优先搜索 （Breath-First-Search）

```python
# BFS 代码（也可用Python connection库里的deque）

def BFS(graph, start, end):
  
  queue = []
  queue.append([start])
  visited.add(start)
  
  while queue:
    node = queue.pop()
    visited.add(node)
    
    process(node)
    nodes = generate_related_nodes(node)
    queue.push(nodes)
  
  # other processing work
  ...
```

#### 例题讲解

102.二叉树的层次遍历

思路：

1. BFS
2. DFS

433.最小基因变化

22.括号生成

200.岛屿数量



#### 2.贪心算法 (Greedy)

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

* 贪心：当下做局部最优判断

* 回溯：能够回退

* 动态规划：最优判断+回退

贪心发可以解决一些最优化问题，如：求图中的最小生成树，求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们所要求的的答案。

一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。

##### 实战题目

coin change

322.零钱兑换

##### 适用贪心算法的场景

问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。

##### 实战题目

455.分发饼干

121.买卖股票的最佳时机

55.跳跃游戏

注意：

* 使用贪心时，要能证明贪心是可以得到全局的最优解的。
* 有些时候，可能是从后往前贪心，或从某个局部切入进行贪心



#### 3.二分查找

##### 二分查找的前提

1. 目标函数单调性（单调递增或者递减）
2. 存在上下界 (bounded)
3. 能够通过索引访问 (index accessible，即可以用下标进行访问)

##### 代码模板

```python
left,right = 0, len(array)-1
while left <= right:
  mid = (left + right)/2
  if array[mid] == target:
    # find the target!
    break or return result
  elif array[mid] < target:
    left = mid + 1
  else:
    right = mid - 1
```

##### 实战题目

69. x的平方根

法1：二分查找

y = x^2, (x >0): 抛物线，在y轴右侧单调递增；上下界

法2：牛顿迭代法

```python
class Solution(object):
  def mySqrt(self,x):
    r = x
    while r*r > x:
      r = (r + x/r) / 2 #迭代的方式
     return r
```

367.有效的完全平方数

33.搜索旋转排序数组

法1：暴力：还原O(logN) -> 升序 -> 二分：O(logN)

法2：正解：二分查找

a. 单调

b. 边界

c. index

74.搜索二维矩阵
