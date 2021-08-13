class Solution:
    def reverse(x: int) -> int:
        """
        :type x: int
        : rtype : int
        """
        length=0
        result=[]
        if x==0 :
            return 0
        if x>0:
            strnum=str(x)
            length=len(str(x))
            for i in range(length):
                result.append(strnum[length-i-1])
            number="".join(result)
            return int(number)
        if x<0:
            strnum=str(abs(x))
            length=len(strnum)
            for i in range(length):
                result.append(strnum[length-i-1])
            number="".join(result)
            return (0-int(number))

rr=Solution.reverse(-1250)
print(rr)
