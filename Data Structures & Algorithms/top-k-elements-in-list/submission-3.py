class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        # B. Using Hashmap
        dic = {}

        for i,num in enumerate(nums):
            dic[num] = dic.get(num, 0) + 1
        # print(dic)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        # print(buckets)

        for num, f in dic.items():
            buckets[f].append(num)
        # print(buckets)

        # 3) Collect from highest frequency down
        res = []
        for f in range(len(nums), 0, -1):
            if buckets[f]:
                print(buckets[f])
                for num in buckets[f]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res  # in case k == 0

        
        
        
        