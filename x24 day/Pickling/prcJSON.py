import json


d = dict(name="Toky", age=30, love="TY")
with open("./jsonFile.txt", "w+") as f:
    # json.dumps() return one string which exactly is the json
    print("Use function dumps(): {0}".format(json.dumps(d)))
    # json.dump() write json into file directly
    json.dump(d, f)

with open("./jsonFile.txt", "r+") as f1:
    # json.loads() read strings from file, and deserialization
    print("Read from file: {0}".format(json.load(f1)))

