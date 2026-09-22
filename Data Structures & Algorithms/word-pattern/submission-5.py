class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        mp = {}
        wordset = set()
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in mp:
                if words[i] not in wordset:
                    wordset.add(words[i])
                    mp[pattern[i]] = words[i]
                else:
                    return False
            else:
                if mp[pattern[i]] != words[i]:

                    return False
        return True