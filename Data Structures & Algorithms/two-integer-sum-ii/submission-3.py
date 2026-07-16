class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cim = {} #complement to index mapping
        for i in range(len(numbers)):
            n = numbers[i]
            complement = target - n
            if complement in cim:
                return [cim[complement] + 1, i + 1]
            else:
                cim[n] = i
        