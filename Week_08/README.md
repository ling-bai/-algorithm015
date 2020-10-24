### Week 08 Summary

#### 第十六课 位运算

* 位运算符
* 算数移位与逻辑移位
* 位运算的应用



**为什么需要位运算**

机器里的数字表示方式和存储格式就是二进制

十进制与二进制的转换：余数短除法除以二

**位运算符**

含义        运算符                    示例

左移            <<                 0011 => 0110

右移            >>                 0110 => 0011

按位或         |                   0011

​                                              ------ => 1011

​                                         1011

按位与         &                  0011

​                                              ------ => 0011

​                                         1011

按位取反      ~                      0011 => 1100

按位异或      ^                   0011

​                                              ------ => 1000

​                                         1011

（相同为零不同为一）   



* XOR - 异或

异或：相同为0，不同为1.也可用“不进位加法”来理解。

异或操作的一些特点：

x ^ 0 = x   x异或全0 = x

x ^ 1s = ~x  //注意1s = ~0 （1s指的是全1，异或全1 就把x里面的所有的位0变1）

x ^ (~x) = 1s

x ^ x = 0

c = a ^ b => a ^ c =b, b ^ c = a  // 交换两个数

a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c  // associative



**指定位置的位运算** 

1. 将x最右边的n位清零：x & (~0 << n)

2. 获取x的第n位值（0或者1）：(x >> n) & 1

3. 获取 x的第n位的幂值：x & (1<< n)

4. 仅将第n位置为1：x | (1<<n)

5. 仅将第n位置为0：x & (~(1<<n))

6. 将x最高位至第n位（含）清零：x & ((1<<n)-1)

    

**实战位运算要点**

* 判断奇偶：

  x%2 == 1 ---> (x&1) == 1

  x%2 == 0 ---> (x&1) ==0

* x>>1 ---> x/2

  即：x=x/2; ---> x =x>>1;

  ​       mid=(left+right)/2; ---> mid=(left+right) >>1;

* X = X&(X-1)清零最低位的1
* X&-X =>得到最低位的1
* X &~X =>0



**实战题目**

**191.位1的个数**

法1：for loop: 0 -->32

法2：%2, /2

法3：&1，x = x >>1; (32)

法4：while (x>0) {count ++; x=x & (x-1); }

```python
class Solution(object):
  def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while n:
      count += n&1
      n >>= 1
    return count
```

**231.2的幂**

n与上n-1表示把n的最低位的1打掉了之后，这时候n就必须等于0

```python
class Solution(object):
  def isPowerOfTwo(self, n):
    return n !=0 and (n & (n-1)) == 0
```

**reversebits**

法1：int转换为一个0101的这种String

int -->"010101" string --> reverse --> int

法2：int -->位运算 -->

**n皇后问题**

```python
def solveQueens(self,n):
  def DFS(queens,xy_dif,xy_sum):
    p = len(queens)
    if p ==n:
      result.append(queens)
      return None
    for q in range(n):
      if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
        DFS(queens+[q],xy_dif+[p-q],xy_sum+[p+q])
  result = []
  DFS([],[],[])
  return[["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
```

```python
# N皇后的位运算解法
def totalQueens(self,n):
  if n < 1: return []
  self.count = 0 #入口，设定最后的结果=0
  self.DFS(n, 0, 0, 0, 0) # 然后调 DFS（n0000）
  return self.count # self.count 存结果

def DFS(self, n, row, cols, pie, na): # 这里的n表示要求的n皇后问题，即递归共有n层；row表示当前我们正在审查哪一层。cols,pie,na这三个现在是一个数
  # rescursion terminator
  if row >= n:
    self.count += 1
    return
  
  bits = (~(cols | pie | na)) & ((1 << n)-1) #得到当前所有的空位，就是8个二进制的1放在这里
  
  while bits:
    p = bits & -bits # 取到最低位的1
    bits = bits & (bits - 1) #表示在p位置上放入皇后
    self.DFS(n, row +1, cols | p) << 1, (na | p) >>1)
    # 不需要revert cols, pie, na的状态
```

**338.比特位计数**

思路：位运算+DP



#### 第十七课：布隆过滤器(Bloom Filter)、LRU Cache

**Bloom Filter vs Hash Table**

一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索一个元素是否在一个集合中。

优点：空间效率和查询时间都远远超过一般的算法；

缺点：有一定的误识别率和删除困难

布隆过滤器在工程实践中，放在最外边当缓存，即当一个很快速的判断使用。在初步判断某个数存在之后，再去DB中搜索，确定这个数是否真正存在。（挡在一台机器前面快速查询的缓存）

案例：

1.比特币网络

2.分布式系统（Map-Reduce） --- Hadoop, search engine

3.Redis缓存

4.垃圾邮件、评论等的过滤

```python
from bitarray import bitarray
import mmh3

class BloomFilter:
  def __init__(self, size, hash_num):
    self.size - size
    self.hash_num = hash_num
    self.bit.array = bitarray(size)
    self.bit_array.setall(0)
  
  def add(self,s):
    for seed in range(self.hash_num):
      result = mmh3.hash(s,seed) % self.size
      if self.bit_array[result] == 0:
        return "Nope"
    return "Probably"

bf = BloomFilter(500000, 7)
bf.add("dantezhao")
print(bf.lookup("dantezhao"))
print(bf.lookup("yyj"))
```

#### LRU Cache（Least recently Used）

两个要素：大小、替换策略

Hash Table + Double LinkedList

O(1) 查询

O(1)修改、更新

替换策略

LFU-least frequently used

LRU-least recently used

**实战例题**

LRU实现（LRUCache）

```python
class LRUCache(object):
  def __init__(self, capacity):
    self.dic = collections.OrderedDict()
    self.remain = capacity
  
  def get(self, key):
    if key not in self.dic:
      return -1
    v = self.dic.pop(key)
    self. dic[key] = v # key as the newset one
    return v
  
  def put(self, key, value):
    if key in self.dic:
      self.dic.pop(key)
    else: 
      if self.remain >0:
        self.remain -= 1
        else:   # self.dic is full
          self.dic.popitem(last=False)
    self.dic[key] = value
```

#### 第十八课：排序

排序算法共分为两大类：

1.比较类排序：

通过比较来决定元素间的相对次序，由于时间复杂度不能突破O(nlogn), 因此也称为非线性时间比较类排序。

（cmp函数，可以是任何结构体或者是类的对象）

2.非比较类排序：

不通过比较来决定元素间的相对次序，它可以突破基于比较类排序的时间下界，以线性时间运行，因此也称为线性时间非比较类排序。

![IMG_3553](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 8/IMG_3553.PNG)

![IMG_3556](/Users/lingbai/Documents/极客时间/算法训练营/作业/Week 8/IMG_3556.PNG)

**初级排序-O(n^2)**

1.选择排序（Selection Sort）

每次找最小值，然后放到待排序数组的起始位置。

2.插入排序（Insertion Sort）

从前到后逐步构建有序序列；对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

3.冒泡排序（Bubble Sort）

嵌套循环，每次查看相邻的元素如果逆序，则交换。

每一次冒泡最大的元素都会被挪到最后。

**高级排序-O(N * LogN)**

1.快速排序（Quick Sort）

数组取标杆pivot, 将小元素放pivot左边，大元素放右侧，然后依次对右边的右边的子数组继续快排，以达到整个序列有序。

【注意】正常情况下数组的prepend操作的时间复杂度是O(n),但是可以进行特殊优化到O(1)。采用的方式是申请稍大一些的内存空间，然后在数组最开始预留一部分空间，然后prepend的操作则是把头下标前移一个位置即可。

2.归并排序（Merge Sort）--- 分治

1）把长度为n的输入序列分成两个长度为n/2的子序列；

2）对这两个子序列分别采用归并排序；

3）将两个排序好的子序列合并成一个最终的排序序列

归并可以理解为快排的逆向操作。两者具有相似性，但步骤顺序相反。

归并：先排序左右子数组，然后合并两个有序子数组

快排：先调配出左右子数组，然后对于左右子数组进行排序

3.堆排序（Heap Sort）---堆插入O(logN)，取最大/小值O(1)

1）数组元素依次建立小顶堆

2）依次取堆顶元素，并删除

**特殊排序 - O(n)**

1.计数排序（Counting Sort）

计数排序要求输入的数据必须是有确定范围的整数。将输入的数据值转化为键存储在额外开辟的数组空间中；然后依次把计数大于1的填充回原数组

2.桶排序（Bucket Sort）

工作原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）

3.基数排序（Radix Sort）

是按照低位先排序，然后收集；再按照高位排序，然后再收集，依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。

**实战例题**

242.有效的字母异位词

56.合并区间

493.反转对

法1：暴力法：两个嵌套循环：O(n^2)

法2：merge-sort O(nlogn)

法3：树状数组 O(nlogn)
