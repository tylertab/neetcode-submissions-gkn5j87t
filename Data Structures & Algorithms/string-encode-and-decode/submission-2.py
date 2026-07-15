class Solution:

    def encode(self, strs: List[str]) -> str:
        es = ""
        for w in strs:
            lw = str(len(w))
            es += lw + "," + w
        return es
    def decode(self, s: str) -> List[str]:
        i = 0
        msg = []
        print(s)
        while 0 < len(s):
            snum = s[:s.index(',')] #string of "#"
            nchar = int(snum) # int of #
            clength = len(snum) + 1 #length of "#,"
            wstarti = clength #start of word
            wendi = wstarti + nchar #word start index + length
            
            print(snum, nchar, clength, wstarti,wendi)

            msg.append(s[wstarti:wendi])
            s = s[wendi:]

        return msg

