import json
name=input("enter your name")
age=int(input("enter your age"))
user={"name":name,"age":age}
with open("user.json",'w')as f:
    json.dump(user,f)
print("data written to json folder")
with open("user.json",'r')as f:
    loaded=json.load(f)
    print("read from file",loaded)