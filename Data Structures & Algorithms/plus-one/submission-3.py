class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        addone = digits[-1] + 1
        carry = addone // 10
        digits[-1] = addone % 10
        for i in range(len(digits) - 2, -1, -1):
            currdigit = digits[i]
            if carry != 0:
                addcarry = digits[i] + carry
                carry = addcarry // 10
                digits[i] = addcarry % 10
            else:
                break
        if carry:
            digits = [1] + digits
        return digits

