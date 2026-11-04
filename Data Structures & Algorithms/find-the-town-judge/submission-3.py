class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedby = {}
        notseentrusting = set(range(1, n + 1))

        for trustee, trusted in trust:
            if trustee in notseentrusting: notseentrusting.remove(trustee)

            trustedby[trusted] = trustedby.get(trusted, []) + [trustee]
        
        res = -1

        for notrust in notseentrusting:
            if notrust in trustedby:
                if len(set(trustedby[notrust])) == n - 1:
                    res = notrust
        return res

 
        
