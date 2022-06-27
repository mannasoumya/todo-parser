# todo-parser
Simple TODO parser written in Python

#### Auto Parsing Coomment Identifier
Supported for the following languges:

**Python, Bash, Java, C, C++, R, Perl, Elixir, Erlang, Javascript, Typescript, PHP, C#, Rust, Golang, Kotlin, Haskell**
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
               (Auto-Comment-Identification Parser will be overridden if this flag is passed)
   -k (str)  : Keyword to be parsed (default: `TODO`)
   -s (bool) : Save TODOs to file
   -p (bool) : Enable/Disable Priority Mode (default: enabled)
   -v (bool) : Enable/Disable Verbose Mode (default: disabled)
   -h (bool) : Print this help and exit

$ python3 todo_parser.py -i todo_parser.py
Line: 29 -> TODOOOOOO: This is a self referencing item; Highest priority
Line: 206 -> TODOOO: Take file name as input and save to that file name
Line: 48 -> TODOO: Another one
Line: 72 -> TODO: another one
Line: 209 -> TODO: Test todo and this is a continuation

# With priority disabled (pass `-p` flag)
$ python3 todo_parser.py -i todo_parser.py -p
Line: 29 -> TODOOOOOO: This is a self referencing item; Highest priority
Line: 48 -> TODOO: Another one
Line: 72 -> TODO: another one
Line: 206 -> TODOOO: Take file name as input and save to that file name
Line: 209 -> TODO: Test todo and this is a continuation

# With verbose mode (pass -v flag)
$ python3 todo_parser.py -i todo_parser.py -k 'FIXME' -v
Auto found comment identifier for file `todo_parser.py` : #
------------------------------------
Keyword            : FIXME
Comment Identifier : #
Priority Mode      : enabled
Save To File       : disabled
------------------------------------
File               : todo_parser.py
Total Lines        : 220
Total Blank Lines  : 31
------------------------------------

Line: 64 -> FIXMEEE : Highest Priority Fix
Line: 199 -> FIXMEE: Second priority fix
Line: 122 -> FIXME: Demo FixMe
```
