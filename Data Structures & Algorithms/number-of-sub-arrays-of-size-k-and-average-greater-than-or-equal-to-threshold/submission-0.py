class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        avg = lambda tot: tot / k
        tot = 0
        count = 0
        for i in range(k - 1):
            tot += arr[i]
        start = 0
        # sliding window aproach. WindowSize will stay k: keep track of total sum of window
        for end in range(k - 1, len(arr)):
            tot += arr[end]
            if avg(tot) >= threshold:
                count += 1
            tot -= arr[start]
            start += 1

        return count
