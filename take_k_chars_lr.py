# take_k_chars_lr.py

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Count total occurrences of each character
        total_a = s.count('a')
        total_b = s.count('b')
        total_c = s.count('c')
        
        # Check if possible to get k of each character
        if total_a < k or total_b < k or total_c < k:
            return -1
        
        # Track current window counts
        curr_a = curr_b = curr_c = 0
        max_window = 0
        left = 0
        
        # Try all possible window sizes from the middle
        # The goal is to find the largest window of characters we can leave in the middle
        # after taking k of each character from the left and right combined
        for right in range(len(s)):
            # Add current character to window
            if s[right] == 'a':
                curr_a += 1
            elif s[right] == 'b':
                curr_b += 1
            else:
                curr_c += 1
            
            # Shrink window if we exceed the maximum allowed characters
            # We need to ensure we leave at least k of each character outside the window
            while curr_a > total_a - k or curr_b > total_b - k or curr_c > total_c - k:
                if s[left] == 'a':
                    curr_a -= 1
                elif s[left] == 'b':
                    curr_b -= 1
                else:
                    curr_c -= 1
                left += 1
            
            # Update max window size
            max_window = max(max_window, right - left + 1)
        
        # The answer is the total length minus the maximum window size
        # This gives us the minimum characters we need to take from left and right
        return len(s) - max_window

# Example usage
def test_solution():
    solution = Solution()
    
    # Test Case 1
    assert solution.takeCharacters("aabaaaacaabc", 2) == 8
    
    # Test Case 2
    assert solution.takeCharacters("a", 1) == -1
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
