class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        for pointer in range(len(s) - 1, -1, -1):
            if s[pointer] == " ":
                return len(s) - pointer - 1


        return  len(s)
            