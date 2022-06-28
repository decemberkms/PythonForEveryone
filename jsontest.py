import json

data = '''{
"name" : "Chuck",
"phone" : {
    "type" : "intl",
    "number" : "+1 734 434 34432"
    },
"email" : {
    "hide" : "yes"
    }
}
'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print('Phone:', info["phone"]["number"])
