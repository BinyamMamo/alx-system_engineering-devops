#!usr/bin/python3
import json
ls = {'2': [
        {
            'name': 'Binyam',
            'age': 20
        }, 
        {
            'name': 'Abere', 
            'age': 35
        }, 
        {
            'name': 'Kebede',
            'age': 45
        }
        ]
    }
with open("data.json", 'w') as js:
    json.dump(ls)
