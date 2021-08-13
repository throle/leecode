from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        start=0
        end=0
        length=0
        result=0
        sSize=len(s)
        while (end<sSize):
            for k in range(start,end):
                if(s[end]==s[k]):
                    start=k+1
                    length=end-start
                    break
            end +=1
            length +=1
            result=max(result,length)
        return result


rr=Solution.lengthOfLongestSubstring('abaaaa')
print(rr)