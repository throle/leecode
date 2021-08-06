class solution:
    def twoNumbersSum(nums,target):

        """
        :type nums=list[int]
        :type target=int
        :rtype  list[int]
        """
   
        sorted_id=sorted(range(len(nums)),key=lambda k:nums[k])
        head=0
        tail=len(nums)-1
        sum_result=nums[sorted_id[head]]+nums[sorted_id[tail]]
        while sum_result != target:
            if sum_result>target:
                tail=tail-1
            elif sum_result<target:
                head=head+1
            sum_result=nums[sorted_id[head]]+nums[sorted_id[tail]]
        return [sorted_id[head],sorted_id[tail]]

    result=twoNumbersSum([1,2,4,8,15],10)
    print(result)


