class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #initialize k to first index
        k = 0
        #iterate through the array nums
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                #increment k
                k += 1
        return k
              
