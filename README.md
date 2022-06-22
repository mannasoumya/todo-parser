# todo-parser
Simple TODO parser written in Python
### Priorities in TODOs
The more number of ending characters in the **keyword** will have more priority and will be listed accordingly.

Consider following example sorted accordingly:
- TODOOO: Highest priority 
- TODOO: Less priority
- TODO: Lowest priority

Here, number of '**O**'s determine the priority of each item.
### Quick Start

```console
$ python3 todo_parser.py -h

Usage: python ./todo_parser.py -i <file_path> [OPTIONS]

OPTIONS:
   -i : Input file path
   -c : Comment Identifier (default: `//`)
   -k : Keyword to be parsed (default: `TODO`)
   -s : Save TODOs to file
   -p : Enable/Disable priority mode (default: enabled)
   -v : Verbose mode (default: disabled)
   -h : Print this help and exit

$ python3 todo_parser.py -i todo_parser.py -c '#'
Line: 6 -> TODOOOOOO: This is a self referencing TODO; Highest priority
Line: 132 -> TODOOO: Take file name as input
Line: 25 -> TODOO: Another one
Line: 45 -> TODO: another one

# With priority disabled (pass `-p` flag)
$ python3 todo_parser.py -i todo_parser.py -c '#' -p
Line: 6 -> TODOOOOOO: This is a self referencing TODO; Highest priority
Line: 25 -> TODOO: Another one
Line: 45 -> TODO: another one
Line: 132 -> TODOOO: Take file name as input

# With verbose mode (pass -v flag)
$ python3 todo_parser.py -i todo_parser.py -c '#' -k 'FIXME' -v
-------------------------------
Keyword            : FIXME
Comment Identifier : #
Priority Mode      : enabled
Save To File       : disabled
-------------------------------
Line: 7 -> FIXMEEE : Highest Priority Fix
Line: 151 -> FIXMEE: Second priority fix
Line: 27 -> FIXME: Lowest Priority Fix
```
