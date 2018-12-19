# I/O Practise
## open()
- param:
    + encoding=''
    + errors='ignore'
    + r     read
    + rb    read binary file
    + w     write sth. into the file, if the file is not exit, it will create file automatically

## write()
- Before we use write(), we should set the 'open()'param as 'w'
- After writing finish, we must call 'close()', only then, the data in cache would write into the disk
- We can call write() repeatedly
- If we want write specific encoding content, we should use param 'encoding'

## close()
- Don't forget to close the file once 'open()'



## read()
- read() will load all content in the file, we can repeatedly call read(size) function
- read(size)

## readline()
- Read one line once time

## readlines()
- Transfer all the content into a list, we can use iterator to read every line expediently

## strip()
- wipe off the last's '\n'
