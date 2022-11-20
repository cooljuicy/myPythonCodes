'''
60. 排列序列
困难
726
相关企业
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

 

示例 1：

输入：n = 3, k = 3
输出："213"
示例 2：

输入：n = 4, k = 9
输出："2314"
示例 3：

输入：n = 3, k = 1
输出："123"
 

提示：

1 <= n <= 9
1 <= k <= n!
通过次数
119K
提交次数
223K
通过率
53.4%
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a=1
        for i in range(2,n+1):a*=i
        an=''
        res=[i for i in range(n+1)]
        j=n
        while j:
            a/=j 
            kshang=int(k//a)
            k=k%a
            if k==0:k=a
            else:kshang+=1
            an+=str(res[kshang])
            res.pop(kshang)
            j-=1
        return an
aa=Solution()
print(aa.getPermutation(3,3))