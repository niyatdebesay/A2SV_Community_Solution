class Solution(object):
    def applyOperations(self, nums):
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i],nums[i+1] = 2*nums[i],0
            continue
        j = 0
        for i in range(len(nums)):
            if nums[i]!= 0:
                nums[j] = nums[i]
                j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1
        return nums
        