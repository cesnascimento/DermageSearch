import json
import re

json_string = "jQuery007283177966862353_1673368638960([{'name':'John', 'age':30, 'car':null},{'name':'Mike', 'age':23, 'car':'BMW'}])"

json_string = re.sub("^jQuery[0-9_]+", "", json_string)

json_string = json_string[1:-1]

print(json_string)

json_data = json.loads(json.dumps(json_string))

print(json_data)