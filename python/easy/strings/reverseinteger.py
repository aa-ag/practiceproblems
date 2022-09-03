class Solution:    
    def reverse(self, x: int) -> int:
        high = -(pow(2, 31))
        low = pow(2, 31) -1
        if x < 0:
            y = -1 * int(str(x).replace('-', '')[::-1])
            if y <= high:
                return 0
            return y
        else:
            y = int(str(x)[::-1])
            if y >= low:
                return 0
            return y