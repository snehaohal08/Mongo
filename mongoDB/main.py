from pymongo import MongoClient

client = MongoClient('localhost',27017)

db=client.mudb
# create collection
todo =db.todo

# todo_1={
#     'name':'sneha',
#     'age':'21',
#     'DOB':'8/12/2003',
#     'done':'False'
# }

# todo.insert_one(todo_1)

# get database in mogodb
# todo_1=todo.find()
# print(list(todo_1))

# update

todo.update_one({"name":"sneha"},{"$set":{"done":"True"}})
todo_1=todo.find()
print(list(todo_1))

# delete

todo.delete_one({"DOB":"8/12/2003"})
todo_1=todo.find()
print(list(todo_1))
