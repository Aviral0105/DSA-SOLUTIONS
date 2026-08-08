class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq={}
        for num in range(len(tasks)):
            freq[tasks[num]]=freq.get(tasks[num],0)+1
        
        maxheap=[]
        
        maxheap=[-cnt for cnt in freq.values()]
        heapq.heapify(maxheap)

        c_q=deque()
        t=0

        while maxheap or c_q:
            t+=1
            if maxheap:
                cnt=1+heapq.heappop(maxheap)
                if cnt<0:
                    c_q.append((cnt,t+n))
                
            if c_q and c_q[0][1]==t:
                cnt,readytime=c_q.popleft()
                heapq.heappush(maxheap,cnt)
        return t