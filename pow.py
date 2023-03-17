class demo:
    def __init__(self):
        self.result=1
        self.c=1
    def accept(self):
        self.b=int(input("enter base  value"))
        self.p=int(input("enter power value"))
    def process(self):
        while self.c<=self.p:
            self.result=self.result*self.b
            self.c=self.c+1
        print("{} to the power {}={}".format(self.b,self.p,self.result))
g=demo()
g.accept()
g.process()
