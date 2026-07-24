class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1f = [0] * 26
        for c in s1:
            ind = ord(c) - ord('a')
            s1f[ind] = s1f[ind] + 1
        s1fs = ",".join(map(str,s1f))

        s2f = [0] * 26
        for c in s2[:len(s1)]:
            ind = ord(c) - ord('a')
            s2f[ind] = s2f[ind] + 1
        if s1fs == ",".join(map(str,s2f)):
            return True

        
        for i in range(len(s1), len(s2)):
            inds = ord(s2[i - len(s1)]) - ord('a')
            inde = ord(s2[i]) - ord('a')
            s2f[inds] = s2f[inds] - 1
            s2f[inde] = s2f[inde] + 1
            if s1fs == ",".join(map(str,s2f)):
                return True
        return False


