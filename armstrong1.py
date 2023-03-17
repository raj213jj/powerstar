class display:
    def _init_(self):
        self.n=int(input("enter a given number:"))
        self.num=self.n
        self.x=self.n
    def process(self):
        self.count=0
        self.sum=0
        while self.n!=0:
          self.n=self.n//10
          self.count=self.count+1
        while self.x!=0:
            self.i=self.x%10
            self.sum=self.sum+(self.i**self.count)
            self.x=self.x//10
        print("given number is a {} digit number".format(self.count))
        if(self.sum==self.num):
            print("{} is a amstrong number".format(self.sum))
        else:
            print("{} is not a amstrong number".format(self.sum))
        
d=display()
d.process()
