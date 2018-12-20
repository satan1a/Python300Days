# Input and output in the RAM, not in the file
## StringIO
- IO strings in the RAM
- First we should instantiate a 'StringIO()' object
- What we can operate will only be strings in StringIO
- write()       # write only the strings
- getvalue()    # get the value of the StringIO instantiation

## ByteIO()
- IO bytes in the RAM
- Operate bytes
- If we want write the UTF-8 character, we should encode the strings while *write*
- Else are similar with the former