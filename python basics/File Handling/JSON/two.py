import json
emp={
    'id':101,
    'name':'rahul',
    'avail':True,
    'discount':None
}

#converting into python to json file
emp_json=json.dumps(emp)
print(type(emp_json))
print(emp_json)