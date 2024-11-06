class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_set_bits(n: int) -> int:
            return bin(n).count('1')
        
        # If array is already sorted, return True
        if nums == sorted(nums):
            return True
        
        n = len(nums)
        # Group numbers by their set bit count
        groups = []
        current_group = [nums[0]]
        current_bits = count_set_bits(nums[0])
        
        for i in range(1, n):
            bits = count_set_bits(nums[i])
            if bits == current_bits:
                current_group.append(nums[i])
            else:
                groups.append(current_group.copy())
                current_group = [nums[i]]
                current_bits = bits
        groups.append(current_group)
        
        # Check if each group can be sorted properly
        result = []
        for group in groups:
            sorted_group = sorted(group)
            result.extend(sorted_group)
        
        # Check if the final result would be sorted
        return result == sorted(result)
