class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        l=0
        r=len(s)-1
        while l < len(s):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
