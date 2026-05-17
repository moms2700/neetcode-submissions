class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            temps = (target - pos) / spd 
            
            if not stack or temps > stack[-1]:
                stack.append(temps)
        
        return len(stack)