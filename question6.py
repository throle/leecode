class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        :type s: str
        :type numRows :int
        :rtype :str
        """
        if (numRows==1):
            return s
        length=len(s)
        result=''
        cyc=2*numRows-2
        for i in range(numRows):
            for j in range(0,(length-i),cyc):
                result=result+s[j+i]
                if (i!=0 and i!=(numRows-1) and (j+cyc-i)<length ):
                    result=result+s[j+cyc-i]

        return result