# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers( l1, l2) :
        length1=len(l1)
        length2=len(l2)
        length3=1
        k1=1
        k2=1
        number1=0
        number2=0
        number3=0
        result1=[]
        for k1 in range(1,length1+1):
            number1=number1+l1[k1-1]*10**(k1-1)

        for k2 in range(k2,length2+1):
            number2=number2+l2[k2-1]*10**(k2-1)
        
        number3=number1+number2
        number4=number3
        while number3/10>1:
            length3+=1
            number3=number3/10

        while length3>0:
            a=number4%10
            result1.append(a)
            number4=int(number4/10)
            length3=length3-1
        return result1

    result2=addTwoNumbers([2,5,3],[5,3])
    print(result2)
    