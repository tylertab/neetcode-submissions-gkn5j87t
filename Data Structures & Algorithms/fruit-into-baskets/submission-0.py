class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        end = 0
        freq = {}
        n = len(fruits)
        
        while end < n:
            fruittype = fruits[end]
            freq[fruittype] = freq.get(fruittype, 0) + 1
            if len(freq) > 2:
                freq[fruits[start]] = freq.get(fruits[start]) - 1
                if freq[fruits[start]] == 0:
                    del freq[fruits[start]]
                start += 1
            end += 1

        return end - start

        