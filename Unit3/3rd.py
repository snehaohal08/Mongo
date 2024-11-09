class my_complex:
    def __init__(self,f,s):
        self.first=f
        self.second=s
        print("Addition: ",self.first+self.second)
        
first=complex(input("Enter the 1st no "))
second=complex(input("enter the second no "))

c=my_complex(first,second)
