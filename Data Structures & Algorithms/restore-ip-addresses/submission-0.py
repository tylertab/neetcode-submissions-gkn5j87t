class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        validint = lambda s: int(s) in range(0, 256) and len(str(int(s))) == len(s)
        buildcurr = lambda b: ".".join(b)
        validbuild = lambda b: len(b) == len(s) + 3
        out = []
        start = 0
        currbuild = []
        def helper(start, end):
            if len(currbuild) == 4:
                build = buildcurr(currbuild)
                if validbuild(build):
                    out.append(build)
                    return

            if end not in range(len(s)):
                return
            if start > end:
                return
            currint = s[start:end + 1]
            if not validint(currint):
                return
            
            
            #op1 addtobuild
            currbuild.append(currint)
            helper(end + 1, end + 1)
            currbuild.pop(-1)

            #op2 add digit
            helper(start, end + 1)
        helper(0,0)
        return out
            
            
            


