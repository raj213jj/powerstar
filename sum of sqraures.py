class Sum:
    def _init_(self):
        self.sum=0
    def acpt(self):
        self.n=int(input("enter the n value:"))
    def process(self):
        while self.n>0:
            r=self.n%10
            self.sum=self.sum+r*r
            self.n=self.n//10
        print(self.sum)
d=Sum()
d.acpt()
d.process()
