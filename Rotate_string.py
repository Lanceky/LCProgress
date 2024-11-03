class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if not s and not goal:
            return True
        return goal in s + s
        
