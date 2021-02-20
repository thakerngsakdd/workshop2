import json

python_dict = {"name": "Jim & Por", "age": 26, "city": "Bangkok"}

json_string = json.dumps(python_dict)

print(json_string)