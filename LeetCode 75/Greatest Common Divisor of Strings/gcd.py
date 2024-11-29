class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 + str2 == str2 + str1, ensuring a common divisor exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Define a custom GCD function
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        # Compute the GCD of the lengths of the two strings
        gcd_length = gcd(len(str1), len(str2))
        
        # The GCD string is the prefix of str1 with the GCD length
        return str1[:gcd_length]

