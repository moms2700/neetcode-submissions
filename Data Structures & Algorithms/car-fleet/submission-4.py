class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        times = [(target - p) / s for p, s in sorted(zip(position, speed), reverse=True)]
        fleets = 0
        max_time = 0.0
        for t in times:
            if t > max_time:
                max_time = t
                fleets += 1
                
        return fleets

        

