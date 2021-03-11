import json
from collections import defaultdict
thisdict = '{"brand": {"hi":[]},"model": "Mustang","year": 1964}'
print(json.loads(thisdict))
'''
json.loads(newdict)=defaultdict(thisdict)
print(newdict)
'''
newdict=json.loads(thisdict)
newdict.setdefault("brand")["hi"].append(1)
print(newdict)

