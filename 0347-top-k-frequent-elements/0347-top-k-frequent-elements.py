class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        minheap=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1

        for num,freq in freq.items():
            heapq.heappush(minheap,(freq,num))
            if len(minheap)>k:
                heapq.heappop(minheap)
        
        ans=[]
        while minheap:
            count,num=heapq.heappop(minheap)
            ans.append(num)
        return ans