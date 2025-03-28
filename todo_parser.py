#!/usr/bin/python3
import sys
import os
import uuid
from types import MappingProxyType

common_languages_comments = MappingProxyType({
    ".py"    : "#",
    ".r"     : "#",
    ".pl"    : "#",
    ".ex"    : "#",
    ".exs"   : "#",
    ".sh"    : "#",
    ".erl"   : "%",
    ".java"  : "//",
    ".c"     : "//",
    ".cpp"   : "//",
    ".js"    : "//",
    ".ts"    : "//",
    ".rs"    : "//",
    ".php"   : "//",
    ".cs"    : "//",
    ".go"    : "//",
    ".swift" : "//",
    ".kt"    : "//",
    ".kts"   : "//",
    ".hs"    : "--",
    ".asm"   : ";"
})

# TODOOOOOO: This is a self referencing item; Highest priority
def parse_arguments(arr, argument, bool=False, verbose=False):
    for i, val in enumerate(arr):
        if val.startswith('-') or val.startswith('--'):
            if (val.removeprefix("-") == argument) or (val.removeprefix("--") == argument):
                if bool:
                    if verbose:
                        print(f"{argument} : True")
                    return True
                if i+1 == len(arr):
                    if verbose:
                        print(f":ERROR: No Value Passed for Argument: `{argument}`")
                    raise Exception("NoValueForArgument")
                if verbose:
                    print(f"{argument} : {arr[i+1]}")
                return arr[i+1]
    if verbose:
        print(f"ERROR: Argument '{argument}' not found")
    raise Exception("ArgumentNotFound")

# TODOO: Another one
def usage(exit_code):
    print(f"\nUsage: python {sys.argv[0]} -i <file_path> [OPTIONS]")
    print("\nOPTIONS:")
    print("   -i        (str)  : Input file path")
    print("   -c        (str)  : Comment Identifier (default: `//`)")
    print("                      (Auto-Comment-Identification Parser will be overridden if this flag is passed)")
    print("   -k        (str)  : Keyword to be parsed (default: `TODO`)")
    print("   -s        (bool) : Save TODOs to file (default: disabled)")
    print("   -p        (bool) : Enable/Disable Priority Mode (default: enabled)")
    print("   -v        (bool) : Enable/Disable Verbose Mode (default: disabled)")
    print("   -gh       (bool) : Report issues to Github (default: disabled)")
    print("   -e        (bool) : Suppress Error Reporting (default: disabled)")
    print("   -newlines (bool) : New Lines in TODOs (default: disabled)")
    print("   -h        (bool) : Print this help and exit")
    print()
    if exit_code != None:
        sys.exit(exit_code)

# FIXMEEE : Highest Priority Fix
file_name                = ""
comment_identifier       = "//"
keyword                  = "TODO"
save_to_file             = False
priority_mode            = True
verbose_mode             = False
report_to_github         = False
suppress_error_reporting = False
new_lines_in_todo        = False

# TODO: another one
try:
    if parse_arguments(sys.argv, 'h', True):
        usage(0)
except Exception as e:
    pass

try:
    if parse_arguments(sys.argv, 'p', True):
        priority_mode = False
except Exception as e:
    pass

try:
    if parse_arguments(sys.argv, 'v', True):
        verbose_mode = True
except Exception as e:
    pass

try:
    if parse_arguments(sys.argv, 'gh', True):
        report_to_github = True
except Exception as e:
    pass

try:
    file_name = parse_arguments(sys.argv[1:],'i')
except Exception as e:
    print("ERROR: File path is required")
    usage(1)

comment_identifier_found = False
for ext in common_languages_comments:
    if file_name.endswith(ext):
        comment_identifier       = common_languages_comments[ext]
        comment_identifier_found = True

if verbose_mode:
    if comment_identifier_found:
        comment_identifier_message = f"Auto found comment identifier for file `{file_name}` : {comment_identifier}"
        print(comment_identifier_message)

try:
    comment_identifier = parse_arguments(sys.argv[1:],'c')
except Exception as e:
    pass

try:
    keyword = parse_arguments(sys.argv[1:],'k')
except Exception as e:
    pass

try:
    save_to_file = parse_arguments(sys.argv[1:],'s',True)
except Exception as e:
    pass

try:
    suppress_error_reporting = parse_arguments(sys.argv[1:],'e',True)
except Exception as e:
    pass

try:
    new_lines_in_todo = parse_arguments(sys.argv[1:],'newlines',True)
except Exception as e:
    pass

# FIXME: Demo FixMe

if not os.path.exists(file_name):
    print("Invalid File Path")
    sys.exit(1)

dash_counter = len(comment_identifier_message) + 1 if verbose_mode else 23 + len(file_name) + 1
if verbose_mode:
    print("-" * dash_counter)
    print(f"Keyword                  : {keyword}")
    print(f"Comment Identifier       : {comment_identifier}")
    print(f"Priority Mode            : {'enabled' if priority_mode else 'disabled'}")
    print(f"Save To File             : {'enabled' if save_to_file else 'disabled'}")
    print(f"Report Issues to Github  : {'enabled' if report_to_github else 'disabled'}")
    print(f"Suppress Error Reporting : {'enabled' if suppress_error_reporting else 'disabled'}")
    print(f"New Lines in TODOs       : {'enabled' if new_lines_in_todo else 'disabled'}")
    print("-" * dash_counter)

file_content = ""
with open(file_name) as f:
    try:
        file_content = f.read()
    except Exception as e:
        if not suppress_error_reporting:
            print(f"File: {file_name}\nERROR: {str(e)}\n")
        sys.exit(1)


todos_str           = ""
lines               = file_content.split("\n")
non_blank_lines     = [line for line in lines if line.strip("\t").strip() != ""]
keyword_content_arr = []
todos_content       = []
todos_line_break    = "\n" if new_lines_in_todo else " "

commented_out_lines_count = 0
for line_number in range(len(lines)):
    line_content = lines[line_number].strip().strip("\t")
    if line_content == "":
        continue
    if line_content.startswith(comment_identifier):
        keyword_content = line_content.removeprefix(comment_identifier).strip()
        if len(keyword_content) == 0:
            continue
        commented_out_lines_count = commented_out_lines_count + 1
        todo_content_dct = {"title": keyword_content}
        if keyword_content.startswith(keyword):
            for i in range(line_number+1,len(lines)):
                nxt_line = lines[i].strip().strip("\t")
                if nxt_line == "":
                    continue
                if nxt_line.startswith(comment_identifier):
                    if nxt_line.removeprefix(comment_identifier).strip().startswith(keyword):
                        break
                    nxt_line_content = nxt_line.removeprefix(comment_identifier).strip()
                    keyword_content = keyword_content + todos_line_break + nxt_line_content
                    if "body" not in todo_content_dct:
                        todo_content_dct["body"] = nxt_line_content + todos_line_break
                    else:
                        todo_content_dct["body"] = todo_content_dct["body"] + todos_line_break + nxt_line_content
                else:
                    break
            todos_content.append(todo_content_dct)
            keyword_content_arr.append((keyword_content,line_number+1))

if verbose_mode:
    print(f"File                : {file_name}")
    print(f"Total Lines         : {len(lines)}")
    print(f"Total Blank Lines   : {len(lines) - len(non_blank_lines)}")
    print(f"Total TODOs         : {len(todos_content)}")
    print(f"Commented Out Lines : {commented_out_lines_count} (non-blank)")
    print("-" * dash_counter)
    print()

def count_priority(last_char,k):
    global keyword
    new_str = k.removeprefix(keyword[:-1])
    count   = 0
    for c in new_str:
        if c == last_char:
            count = count + 1
        else:
            break
    return count

def check_priority(keyword_content_arr):
    global keyword
    res       = {}
    last_char = keyword[-1]
    for k in keyword_content_arr:
        priority = count_priority(last_char,k[0])
        res[k]   = priority
    return res

res        = check_priority(keyword_content_arr)
sorted_res = dict(sorted(res.items(), key=lambda item: item[1],reverse=True))

if not priority_mode:
    sorted_res = res

# FIXMEE: Second priority fix

if len(sorted_res) > 0:
    file_name_message = f"File: {file_name}"
    if new_lines_in_todo:
        file_name_message = file_name_message + "\n" + "-" * len(file_name_message)
        print(file_name_message)
    else:
        print(file_name_message)

for tup in sorted_res:
    content             = tup[0]
    line_number         = tup[1]
    line_number_message = f"Line: {line_number}"
    line_number_dashes  = "-" * len(line_number_message)
    if new_lines_in_todo:
        line_print_msg = f"{line_number_dashes}\n{line_number_message}\n{line_number_dashes}\n{content}\n"
    else:
        line_print_msg = f"{line_number_message} -> {content}"
    print(line_print_msg)
    todos_str = todos_str + line_print_msg + "\n"
if len(sorted_res) > 0:
    print()

def chop_keyword(line):
    global keyword
    chopped_str = line.lstrip(keyword)
    for i in range(len(chopped_str)):
        if chopped_str[i].isalnum():
            break
    return chopped_str[i:].strip()

# TODOOO: Take file name as input
# and save to that file name

# TODO: Test todo

# and this
# is a continuation

if save_to_file:
    save_file_name = str(uuid.uuid4())[:7] + ".txt"
    with open(save_file_name,"w") as f:
        f.write(f"File: {file_name}\n")
        f.write(todos_str)
    print(f"\nWritten To `{save_file_name}`")

if report_to_github:
    from github_api import gh_main_runner,parse_creds,validate_creds_existence
    print()
    print("--------------------")
    print("REPORTING TO GITHUB")
    print("--------------------")
    if verbose_mode:
        cred_dct = parse_creds("creds.json")
        validate_creds_existence("creds.json",cred_dct)
        dashes = len(cred_dct["auth_token"])
        print("-"*(dashes+1))
        print(f"Github User : {cred_dct['user']}")
        print(f"Github Repo : {cred_dct['repo']}")
        print("-"*(dashes+1))

    for todo in todos_content:
        title = chop_keyword(todo["title"])
        body  = todo["body"] if "body" in todo else ""
        print("----------------------------")
        print(f"Title : `{title}`")
        print(f"Body  :  {body}")
        print("----------------------------")
        print("Do you want to report this todo ? (y/n/q)  ",end="")
        answer = input()
        if answer.strip().lower() == "y" or answer.strip().lower() == "yes":
            gh_main_runner(todo={"title":title,"body":body})
            print()
        elif answer.strip().lower() == "q" or answer.strip().lower() == "quit":
            print("Exited by user")
            sys.exit(0)
        else:
            print("Not reporting this issue....")
            print()
