class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isboth(str1,str2):
            if len(str2) < len(str1): 
                return False
            
            return str1 == str2[:len(str1)] and str1 == str2[-len(str1):]
        count = 0
        for i in range(len(words)):
            j = i + 1
            while j < len(words):
                if isboth(words[i],words[j]):
                    count += 1
                j += 1
        return count
