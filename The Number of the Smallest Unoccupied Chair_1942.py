class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        indexes = [i for i in range(len(times))]
        indexes.sort(key=lambda i: times[i][0])

        used_chairs = []  # (leave_time, chair_number) min heap
        available_chairs = [i for i in range(len(times))]  # min-heap of available chairs
        
        heapq.heapify(available_chairs)  

        for i in indexes:
            av, leave = times[i]
            
            while used_chairs and used_chairs[0][0] <= av:
                leave_time, chair = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, chair) 
         
            chair = heapq.heappop(available_chairs)
            heapq.heappush(used_chairs, (leave, chair))
            
            # If this is the target friend, return the chair number
            if i == targetFriend:
                return chair
            
