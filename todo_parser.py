import sys
import os

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

def usage(exit_code):
    print(f"\nUsage: python {sys.argv[0]} -i <file_path> [OPTIONS]")
    print("\nOPTIONS:")
    print("   -i : Input file path")
    print("   -c : Comment Identifier (default: `//`)")
    print("   -k : Keyword to be parsed (default: `TODO`)")
    print("   -h : Print this help and exit")
    print()
    if exit_code != None:
        sys.exit(exit_code)

file_name = ""
comment_identifier = "//"
keyword = "TODO"

try:
    if parse_arguments(sys.argv, 'h', True):
        usage(0)
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

if not os.path.exists(file_name):
    print("Invalid File Path")
    sys.exit(1)

file_content = ""
with open(file_name) as f:
    file_content = f.read()

lines = file_content.split("\n")
for line_number in range(len(lines)):
    line_content = lines[line_number].strip().strip("\t")
    if line_content == "":
        continue
    if line_content.startswith(comment_identifier):
        keyword_content = line_content.removeprefix(comment_identifier).strip()
        if keyword_content.startswith(keyword):
            print(f"Line: {line_number+1} -> {keyword_content}")