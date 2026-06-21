# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if pairs == []:
            return []
        sortedind = 0
        ans = []
        while (sortedind < len(pairs) - 1):
            ans.append(pairs.copy())
            targetind = sortedind + 1
            while targetind > 0:
                if pairs[targetind].key < pairs[targetind - 1].key:
                    pairs = self.swap(targetind,targetind - 1,pairs)
                targetind = targetind - 1

            sortedind = sortedind + 1
            
        ans.append(pairs.copy())
        return ans



    def swap(self, ind1, ind2, pairs):
        temp = pairs[ind1]
        pairs[ind1] = pairs[ind2]
        pairs[ind2] = temp
        return pairs

    
