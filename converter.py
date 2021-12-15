class converter:

    def dectobin(self, number: int) -> str:
        ans = ""
        while(number > 0):
            ans += str(number % 2)
            number //= 2
        while len(ans) < 8:
            ans += "0"
        return ans[::-1]

    def bintodec(self, number: str) -> int:
        ans = 0
        for i in number:
            ans *= 2
            ans += int(i)
        return ans
