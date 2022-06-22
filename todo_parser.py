#!/usr/bin/python3
import sys
import os
import uuid

# TODOOOOOO: This is a self referencing TODO; Highest priority
def parse_arguments(arr, argument, bool=False, verbose=False):
    for i, val in enumerate(arr):
        if val.replace("-", "") == argument:
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
    print("   -i : Input file path")
    print("   -c : Comment Identifier (default: `//`)")
    print("   -k : Keyword to be parsed (default: `TODO`)")
    print("   -s : Save TODOs to file")
    print("   -p : Enable/Disable priority mode (default: enabled)")
    print("   -h : Print this help and exit")
    print()
    if exit_code != None:
        sys.exit(exit_code)

file_name          = ""
comment_identifier = "//"
keyword            = "TODO"
save_to_file       = False
priority_mode      = True

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
    file_name = parse_arguments(sys.argv[1:],'i')
except Exception as e:
    print("ERROR: File path is required")
    usage(1)

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

if not os.path.exists(file_name):
    print("Invalid File Path")
    sys.exit(1)

file_content = ""
with open(file_name) as f:
    file_content = f.read()

todos_str = ""
lines = file_content.split("\n")
keyword_content_arr = []

for line_number in range(len(lines)):
    line_content = lines[line_number].strip().strip("\t")
    if line_content == "":
        continue
    if line_content.startswith(comment_identifier):
        keyword_content = line_content.removeprefix(comment_identifier).strip()
        if keyword_content.startswith(keyword):
            keyword_content_arr.append((keyword_content,line_number+1))

def count_priority(last_char,k):
    global keyword
    new_str = k.removeprefix(keyword[:-1])
    count = 0
    for c in new_str:
        if c == last_char:
            count = count + 1
        else:
            break
    return count

def check_priority(keyword_content_arr):
    global keyword
    res = {}
    last_char = keyword[-1]
    for k in keyword_content_arr:
        priority = count_priority(last_char,k[0])
        res[k] = priority
    return res

res        = check_priority(keyword_content_arr)
sorted_res = dict(sorted(res.items(), key=lambda item: item[1],reverse=True))

if not priority_mode:
    sorted_res = res

for tup in sorted_res:
    content     = tup[0]
    line_number = tup[1]
    print(f"Line: {line_number} -> {content}")
    todos_str = todos_str + f"Line: {line_number} -> {content}" + "\n"

# TODOOO: Take file name as input
if save_to_file:
    save_file_name = str(uuid.uuid4())[:7] + ".txt"
    with open(save_file_name,"w") as f:
        f.write(f"File: {file_name}\n")
        f.write(todos_str)
    print(f"\nWritten To `{save_file_name}`")
