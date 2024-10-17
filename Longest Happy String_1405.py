import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        maxheap = []
        
        if a > 0: heapq.heappush(maxheap, (-a, 'a'))
        if b > 0: heapq.heappush(maxheap, (-b, 'b'))
        if c > 0: heapq.heappush(maxheap, (-c, 'c'))
        while maxheap:
            count, char = heapq.heappop(maxheap)
            n = len(res) 
            if n >= 2 and res[-1] == char and res[-2] == char:
                if not maxheap:
                    break
                nextCount, nextChar = heapq.heappop(maxheap)
                res.append(nextChar)
                nextCount += 1
                if nextCount < 0:
                    heapq.heappush(maxheap, (nextCount, nextChar))
            else:
                res.append(char)
                count += 1
            if count < 0:
                heapq.heappush(maxheap, (count, char))
        return ''.join(res)
