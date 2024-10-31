class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #replace the last n elements in nums1 with nums2 elemnts
        nums1[m:] = nums2
        #sort nums1 in order
        nums1.sort()
