class Solution:    
    def reverse(self, x: int) -> int:
        final = int(str(x).replace("-","")[::-1])
        high = 2147483648
        low = -2147483648
        if x < 0:
            negative = final * -1
            if negative < low or negative > high:
                return 0
            else:
                return negative
        else:
            if final < low or final > high:
                return 0
            else:
                return final