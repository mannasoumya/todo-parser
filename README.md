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

$ python3 todo_parser.py -i input_file.py -c '#'
```
