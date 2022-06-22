# todo-parser
Simple TODO parser written in Python
### Priorities in TODOs
The more number of ending characters in the **keyword**, the more priority.

Consider following example sorted accordingly:
- TODOOO: Highest priority 
- TODOO: Less priority
- TODO: Lowest priority

Here, number of '**O**'s determine the priority of each item.
### Quick Start

```console
$ python3 todo_parser.py -h

Usage: python todo_parser.py -i <file_path> [OPTIONS]

OPTIONS:
   -i (str)  : Input file path
   -c (str)  : Comment Identifier (default: `//`)
   -k (str)  : Keyword to be parsed (default: `TODO`)
   -s (bool) : Save TODOs to file
   -p (bool) : Enable/Disable Priority Mode (default: enabled)
   -v (bool) : Enable/Disable Verbose Mode (default: disabled)
   -h (bool) : Print this help and exit   

$ python3 todo_parser.py -i todo_parser.py -c '#'
Line: 6 -> TODOOOOOO: This is a self referencing item; Highest priority
Line: 162 -> TODOOO: Take file name as input and save to that file name
Line: 25 -> TODOO: Another one
Line: 48 -> TODO: another one
Line: 165 -> TODO: Test todo and this is a continuation

# With priority disabled (pass `-p` flag)
$ python3 todo_parser.py -i todo_parser.py -c '#' -p
Line: 6 -> TODOOOOOO: This is a self referencing item; Highest priority
Line: 25 -> TODOO: Another one
Line: 48 -> TODO: another one
Line: 162 -> TODOOO: Take file name as input and save to that file name
Line: 165 -> TODO: Test todo and this is a continuation

# With verbose mode (pass -v flag)
$ python3 todo_parser.py -i todo_parser.py -c '#' -k 'FIXME' -v
------------------------------------
Keyword            : FIXME
Comment Identifier : #
Priority Mode      : enabled
Save To File       : disabled
------------------------------------
File               : todo_parser.py
Total Lines        : 185
Total Blank Lines  : 27
------------------------------------

Line: 40 -> FIXMEEE : Highest Priority Fix
Line: 165 -> FIXMEE: Second priority fix
Line: 88 -> FIXME: Demo FixMe
```
