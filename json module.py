#json module
import json
name=input("enter your name")
age=int(input("enter your age"))
data={"name":name,"age":age}
stringify_json=json.dumps(data)
print("seralized data of json",stringify_json)