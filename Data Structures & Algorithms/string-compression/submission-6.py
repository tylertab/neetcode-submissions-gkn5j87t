class Solution:
    def compress(self, chars: List[str]) -> int:
        start = 0
        end = 0
        k = 0
        while end < len(chars):
            while end < len(chars) and chars[end] == chars[start]:
                end += 1
            count = end - start
            chars[k] = chars[end - 1]
            k += 1
            if count > 1:
                for c in str(count):
                    chars[k] = c
                    k += 1
            
            start = end
    
            
            
                
            
        return k