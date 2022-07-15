# todo-parser
Simple TODO parser written in Python.
Report **TODOS** as **ISSUES** in Github.
### Priorities in TODOs
The more number of ending characters in the **keyword**, the more priority.

Consider following example sorted accordingly:
- TODOOO: Highest priority 
- TODOO: Less priority
- TODO: Lowest priority

Here, number of '**O**'s determine the priority of each item.

### Auto Parsing Comment Identifier
Supported for the following languages:

**Python, Bash, Java, C, C++, R, Perl, Elixir, Erlang, Javascript, Typescript, PHP, C#, Rust, Golang, Kotlin, Haskell**

### Github Issue Reporting

Pass the **-gh** flag in the program to enable ***Github Issue Reporting***. The github credentials are picked up from ```creds.json``` in the current working directory. The file looks like following:
```json
{
   "user"       : <github-username>,
   "repo"       : <github-repository>,
   "auth_token" : <github-access-token>
}
```
```pip -r requirements.txt``` will install **requests** library of Python which is needed to send request to github API.
Guide on creating your own **Access Token**: [link](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

### Quick Start

```console
$ python3 todo_parser.py -h

Usage: python ./todo_parser.py -i <file_path> [OPTIONS]

OPTIONS:
   -i  (str)  : Input file path
   -c  (str)  : Comment Identifier (default: `//`)
                (Auto-Comment-Identification Parser will be overridden if this flag is passed)
   -k  (str)  : Keyword to be parsed (default: `TODO`)
   -s  (bool) : Save TODOs to file
   -p  (bool) : Enable/Disable Priority Mode (default: enabled)
   -v  (bool) : Enable/Disable Verbose Mode (default: disabled)
   -gh (bool) : Report issues to Github (default: disabled)
   -h  (bool) : Print this help and exit

$ python3 todo_parser.py -i todo_parser.py
Line: 31 -> TODOOOOOO: This is a self referencing item; Highest priority
Line: 234 -> TODOOO: Take file name as input and save to that file name
Line: 50 -> TODOO: Another one
Line: 76 -> TODO: another one
Line: 237 -> TODO: Test todo and this is a continuation
```

### With priority disabled (pass `-p` flag)
```console
$ python3 todo_parser.py -i todo_parser.py -p
Line: 31 -> TODOOOOOO: This is a self referencing item; Highest priority
Line: 50 -> TODOO: Another one
Line: 76 -> TODO: another one
Line: 234 -> TODOOO: Take file name as input and save to that file name
Line: 237 -> TODO: Test todo and this is a continuation
```
### With verbose mode (pass -v flag)
```console
$ python3 todo_parser.py -i todo_parser.py -k 'FIXME' -v
Auto found comment identifier for file `todo_parser.py` : #
--------------------------------------
Keyword                 : FIXME
Comment Identifier      : #
Priority Mode           : enabled
Save To File            : disabled
Report Issues to Github : disabled
--------------------------------------
File               : todo_parser.py
Total Lines        : 278
Total Blank Lines  : 36
--------------------------------------

Line: 67 -> FIXMEEE : Highest Priority Fix
Line: 218 -> FIXMEE: Second priority fix
Line: 132 -> FIXME: Demo FixMe
```
### Github Issue Reporting (pass -gh flag)
```console
$ python3 todo_parser.py -i ./todo_parser.py -v -gh
Auto found comment identifier for file `./todo_parser.py` : #
----------------------------------------
Keyword                 : TODO
Comment Identifier      : #
Priority Mode           : enabled
Save To File            : disabled
Report Issues to Github : enabled
----------------------------------------
File               : ./todo_parser.py
Total Lines        : 278
Total Blank Lines  : 36
----------------------------------------

Line: 31 -> TODOOOOOO: This is a self referencing item; Highest priority
Line: 234 -> TODOOO: Take file name as input and save to that file name
Line: 50 -> TODOO: Another one
Line: 76 -> TODO: another one
Line: 237 -> TODO: Test todo and this is a continuation

-----------------------------------------
Github User : mannasoumya
Github Repo : test-gh-api
-----------------------------------------
----------------------------
Title : `This is a self referencing item; Highest priority`
Body  :  
----------------------------
Do you want to report this todo ? (y/n/q)  n
Not reporting this issue....

----------------------------
Title : `Another one`
Body  :  
----------------------------
Do you want to report this todo ? (y/n/q)  n
Not reporting this issue....

----------------------------
Title : `another one`
Body  :  
----------------------------
Do you want to report this todo ? (y/n/q)  n
Not reporting this issue....

----------------------------
Title : `Take file name as input`
Body  :  and save to that file name 
----------------------------
Do you want to report this todo ? (y/n/q)  y
Issue 9: `Take file name as input` created successfully

----------------------------
Title : `Test todo`
Body  :  and this  is a continuation
----------------------------
Do you want to report this todo ? (y/n/q)  y
Issue 10: `Test todo` created successfully

```
