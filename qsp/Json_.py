
## json: Java Script Object Notation
## Python has the in built package called as json to work with json data

import json

######################################################################################

## converting(Parsing) json to python: to perform this operation we make use of loads() present in json module

data = '{"name": "abc", "age": 23, "ph_no": 9876544567}'
# print(data)
# print(type(data))

## Parsing json to python

data = json.loads(data)
# print(data)
# print(type(data))

#####################################################################################

## converting(parsing) python to json: to perform this operation we make use of dumps() present in the json module

data1 = {"name": "abc", "age": 23, "ph_no": 9876544567}
# print(type(data1))
# print(data1)

## Paring the python data to json

data1 = json.dumps(data1)
# print(type(data1))
# print(data1)

#################################################################################

## when we convert python to json it converts to equivante type

# Python	        JSON
# dict	        Object/map
# list	        Array
# tuple	        Array
# str	        String
# int	        Number
# float	        Number
# True	        true
# False	        false
# None	        null

x = {
  "name": "steve",
  "age": 40,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))
# print(json.dumps(x, indent = 4))
# print(json.dumps(x, indent = 4, separators = ('.', '=')))
# print(json.dumps(x, indent = 4, separators = ('.', '='), sort_keys = True))

########################################################################################

## writing the python data into the json file: to perform this operation we make use of a dump() present in json module

res = {
  "name": "steve",
  "age": 40,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

with open('Sample.json', 'w') as var:
    json.dump(res, var, indent = 5)


###########################################################################################

## Reading the data from the json file: to perform this operation we make use of load() present in json module

with open('Sample.json', 'r') as a:
  print(json.load(a))







