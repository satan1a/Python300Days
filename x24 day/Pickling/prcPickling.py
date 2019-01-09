import pickle

d = dict(name="Toky", age="30", love="TY")
#  Function dumps() serialize any object into bytes, then we can write these bytes into file
print(pickle.dumps(d))
with open("./byteFile.txt", "wb") as f:
    # Function dump() serialize a object and write it into a file-like object directly
    pickle.dump(d, f)

with open("./byteFile.txt", "rb") as f1:
    # print("These are reading from the file:\n{0}".format(f1.read()))
    d = pickle.load(f1)
    print(d)

