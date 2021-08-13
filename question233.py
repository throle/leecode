class Solution:
    def countDigitOne(n: int) -> int:
        """
        :type n: int
        :rtype : int 
        """
        x=0
        sum=0
        length=0
        for x in range(n+1):
            strnum=str(x)
            length=len(strnum)
            for i in range(length):
                if strnum[i]=='1':
                    sum=sum+1
                    
        return sum
rr=Solution.countDigitOne(11)
print(rr)
            