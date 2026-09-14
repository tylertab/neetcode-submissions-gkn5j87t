class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mp = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9
}

        def stringtoint(s):
            res = 0
            p = 0
            for i in range(len(s) - 1, -1, -1):
                res += (10 ** p) * mp[s[i]]
                p += 1
            return res
        # print(stringtoint(num1))
        # print(stringtoint(num2))
        
        return str(stringtoint(num1) * stringtoint(num2))