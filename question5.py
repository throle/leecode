class Solution:
    def longestPalindrome(s:str) :
        """
        :type s:  str
        :rtype ： str
        """
        k=0
        kmax=0
        kmax2=0
        pointmax,pointmax2=0,0
        length=len(s)
        for point in range(length):
            k=0
            while (point-k)>=0 and (point+k)<length:
                if s[point-k]==s[point+k]:
                    
                    if k>kmax:
                        pointmax=point
                        kmax=k
                    k=k+1
                else:
                    break
            
        for point in range(length):
            k=0 
            while (point-k)>=0 and (point+k+1)<length:
                if s[point-k]==s[point+k+1]:
                    if kmax2==0:
                        pointmax2=point
                    if k>kmax2:
                        pointmax2=point
                        kmax2=k
                    k=k+1
                else :
                    break

        if pointmax==0 and pointmax2==0:
            if length>=2 and s[0]==s[1]:
                return s[0:2]
            else :
                return s[0]

        if (2*kmax+1)>(2*kmax2+2):
            return s[(pointmax-kmax):(pointmax+kmax+1)]
        else :
            return s[(pointmax2-kmax2):(pointmax2+kmax2+2)]

rr=Solution.longestPalindrome('babad')
print(rr)
print("结束了")