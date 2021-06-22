import json
dicts = [
{ "name": "Tom", "age": 10 },
{ "name": "Mark", "age": 5 },
{ "name": "Pam", "age": 7 },
{ "name": "Dick", "age": 12 },
{ "name": "Pam", "age": 21 }
]

print(next(item for item in dicts if item["name"] == "Pam"))
print(next(item for item in dicts if item["name"] == "Pam"))
'''
print(json.loads(thisdict))

json.loads(newdict)=defaultdict(thisdict)
print(newdict)

newdict=json.loads(thisdict)
newdict.setdefault("brand")["hi"].append(1)
print(newdict)

if newdict.get("hi",-1)==-1:
	print("true")
else:
    print("false")
'''

