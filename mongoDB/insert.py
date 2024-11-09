from pymongo import MongoClient

Client = MongoClient('localhost',27017)

db=Client.student_info
def insert():
    try:
        empID=input("Enter emp id: ")
        empname=input("Enter emp name: ")
        empsal=input("Enter emp Salary: ")
        db.Employee.insert_one({
            
            "id":empID,
            "ename":empname,
            "salary":empsal,
           
        })
        print("data inserted succefully.............")
        
    except Exception:
        print(str(e))

def update():
    try:
        empsal=input("Enter emp salary")
        db.Employee.update_one({"ename":"ajayx"},{"$set":{"salary":" "}})
        print("updated successfully.......")
    except Exception :
        print(str(e))
        
    
        
def delete():

     try:
        
         db.Employee.delete_one({"id":"111"})
         print("deleted successfully..........")
     except Exception:
         print(str(e))
        
    

#insert()
update()
#delete()