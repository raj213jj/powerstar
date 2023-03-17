class Armstrongnum:
    def __init__(self):
        self.count=0
        self.sum=0
    def accept(self):
        self.n=int(input("enter a number"))
    def findDigitCount(self):
        while self.n>0:
            self.count=+1
            self.n=self.n//10
        print("power=",self.count)
        return self.count
    def power(self,b,p): 
        result=1
        c=1
        while c<=p:
            result=result*b
            c=c+1
        return result
    def process(self):
        num=self.n
        p=self.findDigitCount()
        while num>0:
            r=num%10
            self.sum=self.sum+self.power(r,p)
            num=num//10
        if self.n==self.sum:
            print("number is armstrong")
        else:
            print("not an armstrong")
g=Armstrongnum()
g.accept()
g.process()
        
    
