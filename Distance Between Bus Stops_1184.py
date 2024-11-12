class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        return min(partial := sum([distance[i] 
        for i in range(min(start,destination),max(start,destination))]), 
        sum(distance) - partial)
