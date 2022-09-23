class calculator:
    x = int(input("Enter number 1\n"))
    y = int(input("Enter number 2\n"))

    def sum(self):
        self.z = self.x + self.y
        print("The sum of the entered numbers is ",self.z)
    def prod(self):
        self.z = self.x * self.y
        print("The product of the entered numbers is ",self.z) 
    def div(self):
        self.z = self.x / self.y
        print("The division of the entered numbers give ",self.z)   
    def diff(self):
        self.z = self.x - self.y
        print("The difference of the entered numbers is ",self.z)  
    def ssqr(self):
        self.z = (self.x*self.x) + (self.y*self.y)
        print("The sum square of the entered numbers is ",self.z)             

bb = calculator()

bb.sum()
bb.diff()
bb.prod()
bb.div()
bb.ssqr()





