class student:
    name=input("Enter the name: ")
    age=input("Enter the age: ")
    marks=int(input("Enter the marks: "))
    
    
    
    print("NAME: ",name)
    print("AGE: ",age)
    print("MARKS: ",marks)
    
    def display(self):
        if self.marks > 90:
            print("A")
        elif self.marks > 70:
            print("B")
        elif self.marks > 40:
            print("c")
        else:
            print("fail....")
        
s=student()
s.display()