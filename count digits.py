class sum:
    def __init__(self):
        self.count=0
    def accept(self):
        self.n=int(input("enter a number"))
    def process(self):
        while self.n>0:
            self.count=self.count+1
            self.n=self.n//10
        print("no. of  digits=",self.count)
g=sum()
g.accept()
g.process()
