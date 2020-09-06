# 347. 前 K 个高频元素
## 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # #解1
        # temp = list(set(nums))        #求得不重复的元素
        # dit = []                      #用于存储出现频率

        # for i in range(len(temp)):     #统计这些不重复元素的出现频率
        #     c = nums.count(temp[i])    #注意，python中的count函数时间复杂度为O(N),当存在M个不重复元素时，时间复杂度为M*O(N)
        #     dit.append(c)

        # temp = sorted(zip(dit,temp))[::-1]  #将元素和其出现频率组合在一起形成一个新的元祖列表，并对该列表排序
        # return [temp[i][1] for i in range(k)]  #使用列表推导式求前k个高频元素

        #解法2
        dit={}                   #{元素值：出现频率}                
        for i in nums:           #使用字典的特性（相同元素后面值的会覆盖前面的值）统计元素的频率，时间复杂度为O(N)
            if i not in dit:     #如果不存在，则将其存入字典中，此时该值的出现频率为1
                dit[i] = 1
            else:                #如果已经存在，则其出现频率加1
                dit[i] =  dit[i]+1

        temp = []                     #由于字典无法排序，因此需要先将字典转换为列表，列表中的每一个元素为 键-值 构成的元祖
        for item in dit.items():      #使用字典的items函数,获取 键-值对元祖列表
            temp.append(item[::-1])   #这里需要对出现频率进行排序，因此将每一个元祖元素进行转置
        
        # temp = list(map(lambda x:(x[1],x[0]),dit.items()))  #上面的for循环也可以这样实现

        temp.sort(reverse=True)       #对列表进行排序，对于每一个元素都是元祖的列表来说，其排序是按照元祖的第一个元素进行的
        return [temp[i][1] for i in range(k)]  #使用列表推导式求前k个高频元素