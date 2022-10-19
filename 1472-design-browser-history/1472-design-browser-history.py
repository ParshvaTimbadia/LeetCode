class BrowserHistory:

    def __init__(self, homepage: str):
        self.backHist = [homepage]
        self.forwardHist = []
        

    def visit(self, url: str) -> None:
        self.backHist.append(url)
        self.forwardHist = []
    
    def back(self, steps: int) -> str:
        while self.backHist and len(self.backHist) !=1 and steps!=0:
            self.forwardHist.append(self.backHist.pop())
            steps -= 1
        
        return self.backHist[-1]
        

    def forward(self, steps: int) -> str:
        while self.forwardHist and steps!=0:
            steps -= 1
            self.backHist.append(self.forwardHist.pop())
        
        return self.backHist[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)