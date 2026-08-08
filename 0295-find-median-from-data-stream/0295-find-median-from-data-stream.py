class MedianFinder:

    def __init__(self):
        
        self.maxheap=[]
        self.minheap=[]
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap,-num)
        val=-heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap,val)

        if len(self.maxheap)<len(self.minheap):
            val=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-val)

    def findMedian(self) -> float:
        if len(self.maxheap)>len(self.minheap):
            return float(-self.maxheap[0])
        else:
            return (-self.maxheap[0]+self.minheap[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()