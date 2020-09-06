学习笔记

### Week 2 Summary

**1. 哈希表、映射、集合的实现与特性**

哈希表（Hash Table），也叫散列表，是根据关键码值（Key value）而直接进行访问的数据结构。
它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。
这个映射函数叫作散列函数（Hash Function），存放记录的数组叫作哈希表（或散列表）  

* 工程实践
1. 电话号码簿
2. 用户信息表
3. 缓存（LRU  Cache）
4. 键值对存储（Redis）

* 哈希表的复杂度分析
Time Complexity
Average:
Access N/a
Search O(1)
Insertion O(1)
Deletion O(1)

Worst:
Access N/a
Search O(n)
Insertion O(n)
Deletion O(n)

Space Complexity
Worst:
O(n)

* 红黑树的复杂度分析
Time Complexity
Average:
Access O(log(n))
Search O(log(n))
Insertion O(log(n))
Deletion O(log(n))

Worst:
Access O(log(n))
Search O(log(n))
Insertion O(log(n))
Deletion O(log(n))

Space Complexity
Worst:
O(n)

* 实战例题：
242. 有效的字母异位词
`解题四件套`
1. clarification
2. possible solutions --> optimal (time & space)
3. code
4. test cases

49. 字母异位词分组

-> 同一题，收藏所有好的解题方法  


**2. 树、二叉树、二叉搜索树**

Linked List 是特殊化的Tree
Tree是特殊化的Graph

* 示例代码模板（默写背诵！！！）
Class TreeNode:
  def__init__(self,val):
  self.val = val
  self.left, self.right = None, None

* 二叉树遍历
1.前序 (Pre-order) : 根-左-右
2.中序 (In-order): 左-根-右
3.后序 (Post-order): 左-右-根

* 示例代码模板（默写背诵！！！）
```
def preorder(self, root):

  if root: 
  self.traverse_path.append(root.val)
  self.preorder(root.left)
  self.preorder(root.right)


def inorder(self, root):

  if root: 
  self.inorder(root.val)
  self. traverse_path.append (root.left)
  self.inorder(root.right)


def postorder(self, root):

  if root: 
  self.postorder(root.val)
  self. postorder(root.left)
  self. traverse_path.append (root.right)
```

二叉搜索树（Binary Search Tree）

也称二叉排序树、有序二叉树（Ordered Binary Tree）、排序二叉树（Sorted Binary Tree），是指一颗空树或者具有下列性质的二叉树：
1.左子树上所有结点的值均小于它的根结点的值；
2.右子树上所有结点的值均大于它的根结点的值；
3.以此类推：左、右子树也分别为二叉查找树。（这就是 重复性！）

中序遍历：升序排列

注意：空树也是二叉搜索树

二叉搜索树常见操作
1.查询
2.插入新结点（创建）
3.删除

二叉搜索树的复杂度分析
Time Complexity（大部分操作都是log(n)的）
Average:
Access O(log(n))
Search O(log(n))
Insertion O(log(n))
Deletion O(log(n))

Worst: （这棵树退化成了一根棍子）
Access O(n)
Search O(n)
Insertion O(n)
Deletion O(n)

Space Complexity
Worst:
O(n)

树的面试题解法一般都是递归

示例代码模板（again）
```
Class TreeNode:
  def__init__(self,val):
  self.val = val
  self.left, self.right = None, None
```

实战例题：
94. 二叉树的中序遍历  


**3. 堆和二叉堆、图**

堆 Heap 
可以迅速找到一堆数中的最大或者最小值的数据结构。

将根节点最大的堆叫做大顶堆或大根堆，根节点最小的堆叫做小顶堆或小根堆。常见的堆有二叉堆、斐波那契堆等。

假设是大顶堆，则常见操作（API）：
find-max: O(1)
delete-max: O(logN)
insert(create): O(logN) or O(1)

二叉堆性质
通过完全二叉树来实现（注意：不是二叉搜索树）；
二叉堆（大顶）满足下列性质：
1.是一棵完全树
2.树中任意节点的值总是>=其子节点的值；

二叉堆实现细节
1. 二叉堆一般都通过“数组”来实现
2.假设“第一个元素”在数组中的索引为0的话，则父节点和子节点的位置关系如下：
a) 索引为i的左孩子的索引是 (2*i + 1)
b) 索引为i的右孩子的索引是 (2*i + 2)
c) 索引为i的父节点的索引是floor((i-1)/2)

insert 插入操作
1. 新元素一律先插入到堆的尾部
2. 依次向上调整整个堆的结构（一直到根即可）
“HeapifyUp”

Delete Max 删除堆顶操作
1. 将堆尾元素替换到顶部（即堆顶被替代删除掉）
2. 依次从根部向下调整整个堆的结构（一直到堆尾即可）
“HeapifyDown”

注意：二叉堆是堆（优先队列priority queue）的一种常见且简单的实现；但是并不是最优的实现

实战例题：
面试题40.最小的k个数
剑指Offer 59-I.滑动窗口的最大值
347.前K个高频元素

图的属性和分类
基于图相关的算法

图的属性
Graph (V, E)

V – vertex: 点
1. 度 – 入度和出度
2. 点与点之间：连通与否

E – edge: 边
1. 有向和无向（单行线）
2. 权重（边长）

图的表示和分类

基于图的常见算法

DFS 代码 – 递归写法
```
visited = set() #和树中的DFS最大区别

def dfs(node, visited):
    if node in visited: # terminator
    # already visited
    return
 
  visited.add(node)

  process current node here.
  …
  for next_node in node.children():
if not next_node in visited:
dfs(next_node, visited)
```

BFS 代码
```
def BFS(graph, start, end):

        queue = []
        queue.append([start])

        visited = set() # 和树中的BFS的最大区别

        while queue:
            node = queue.pop()
            visited.add(node)

            process(node)
            nodes = generate_related_nodes(node)
            queue.push(nodes)
```

实战例题：
200.岛屿数量  

图的高级算法
1.连通图个数
2. 拓扑排序（Topological Sorting）
https://zhuanlan.zhihu.com/p/34871092
3. 最短路径（Shortest Path）
https://www.bilibili.com/video/av25829980?from=search&seid=13391343514095937158
4. 最小生成树（Minimum Spanning Tree）
https://www.bilibili.com/video/av84820276?from=search&seid=17476598104352152051

