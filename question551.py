class Solution:
    def checkRecord(s: str) :
        """
        :type s: str
        :rtype : true or false
        """
        length=len(s)
        absent=0
        for i in range(length):
            if s[i]=='A':
                absent=absent+1

            if i<(length-2) and s[i]=='L':
                if s[i+1]=='L' and s[i+2]=='L':
                    return False
        if absent>=2:
            return False
        return True
rr=Solution.checkRecord('PPALLPPLL')
print(rr)