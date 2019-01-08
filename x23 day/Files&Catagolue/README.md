# OS
Use OS module to operate file and file catalog
# Command
- os.name
- os.uname() #Windows can not use this command
- os.environ
- os.environ.get('XXX')
- os.mkdir()
- os.rmdir()
- os.path.split()

# shutil
shutil module can be seen as the supplement of OS module
- copyfile()

# Tips
- List all the dir
```
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
```

- List all the dir and file
```
>>> [x for x in os.listdir('.')]
```

- List all the .py file
```
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']