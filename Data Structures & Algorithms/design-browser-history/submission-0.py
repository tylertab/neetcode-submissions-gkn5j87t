class BrowserHistory:
    class DLL:
        def __init__(self, nex, prev, url):
            self.nex = nex
            self.prev = prev
            self.url = url
    def __init__(self, homepage: str):
        self.currpage = self.DLL(None, None, homepage)

    def visit(self, url: str) -> None:
        node = self.DLL(None, self.currpage, url)
        self.currpage = node
        self.currpage.prev.nex = self.currpage
        

    def back(self, steps: int) -> str:
        while self.currpage.prev and steps != 0:
            self.currpage = self.currpage.prev
            steps -= 1
        return self.currpage.url

    def forward(self, steps: int) -> str:
        while self.currpage.nex and steps != 0:
            self.currpage = self.currpage.nex
            steps -= 1
        return self.currpage.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)