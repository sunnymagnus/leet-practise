class Solution:
    def reverse(self, x: int) -> int:
        res=0
        if x>0 :
            while x>0 :
                res = res * 10 + x%10
                x=x//10
            if res>2**31-1 :
                return 0
            else :
                return res 
        else :
            x = x * -1
            while x>0 :
                res = res * 10 + x%10
                x=x//10

        if res>2**31-1 :
            return 0
        else :
            return -res