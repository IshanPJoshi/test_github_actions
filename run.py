import os
import json

food = os.environ.get('FAVORITE_FOOD')
if(food == "Pizza"):
        print("My favorite food is Pizza")
        f = open('data.json')
        print(json.load(f))
else:
        print("I guess I don't know")
