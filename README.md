# todo-parser
Simple TODO parser written in Python

## Quick Start

```console
$ python3 todo_parser.py -h

Usage: python todo_parser.py -i <file_path> [OPTIONS]

OPTIONS:
   -i : Input file path
   -c : Comment Identifier (default: `//`)
   -k : Keyword to be parsed (default: `TODO`)
   -s : Save TODOs to file
   -h : Print this help and exit

$ python3 todo_parser.py -i todo_parser.py -c '#'
Line: 6 -> TODO: This is a self referencing TODO
Line: 25 -> TODO: Another one
Line: 90 -> TODO: Take file name as input
```
