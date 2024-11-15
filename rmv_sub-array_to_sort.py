class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        n = len(arr)
        # Handle edge cases
        if n <= 1:
            return 0
        
        # Find the longest sorted prefix from left
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
            
        # If the array is already sorted
        if left == n - 1:
            return 0
        
        # Find the longest sorted suffix from right
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
            
        # If we need to remove everything between left and right
        result = min(n - left - 1, right)  # Remove suffix or prefix
        
        # Try to merge prefix and suffix
        i = 0
        j = right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                # Current merge is possible, try to minimize removal length
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
                
        return result
