class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res=0
        check=x
        while x!=0 :
            res = res + x%10
            x=x//10
        if check%res==0 :
            return res
        else :
            return -1