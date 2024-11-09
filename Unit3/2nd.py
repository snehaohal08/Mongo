class shape:
    def area(self,s):
        a=s*s
        print("Area: ",a)
class rect(shape):
    def area(self,len,bre):
        a=len*bre
        print("Area: ",a)

r=rect()
r.area(10,20)