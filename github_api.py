import requests
import json
import os
import sys 

def parse_creds(path):
    if not os.path.exists(path):
        print(f"ERROR: path `{path}` not found")
        sys.exit(1)

    with open(path,"r") as f:
        json_content = json.load(f)
    
    return json_content

def validate_creds_existence(cred_file_path,creds_dct):
    try:
        assert "user" in creds_dct           , "ERROR: " + f"`user` key must be present in `{cred_file_path}`"
        assert creds_dct["user"] != ""       , "ERROR: " + "`user` value cannot be ''"
        assert "repo" in creds_dct           , "ERROR: " + f"`repo` key must be present in `{cred_file_path}`"
        assert creds_dct["repo"] != ""       , "ERROR: " + "`repo` value cannot be ''"
        assert "auth_token" in creds_dct     , "ERROR: " + f"`auth_token` key must be present in `{cred_file_path}`"
        assert creds_dct["auth_token"] != "" , "ERROR: " + "`auth_token` value cannot be ''"
    except Exception as e:
        print(e)
        sys.exit(1)

def create_gh_issue(creds_dct,todo):
    user       = creds_dct["user"]
    repo       = creds_dct["repo"]
    auth_token = creds_dct["auth_token"]
    title      = todo["title"]
    body       = todo["body"] if "body" in todo else ""
    typ        = todo["type"] if "type" in todo else "todo"
    header_con = {"Authorization" : f"token {auth_token.strip()}"}
    data       = {
        "owner": user,
        "repo": repo,
        "title": title,
        "body": body,
        "labels": [typ]
    }

    url = f"https://api.github.com/repos/{user}/{repo}/issues"

    try:
        r = requests.post(url,headers=header_con,data=json.dumps(data))
        res_dct = json.loads(r.text)
        
        if r.status_code != 201:
            print()
            print(f"ERROR: {res_dct['message']}")
            print(res_dct)
            if "errors" in res_dct:
                print(res_dct["errors"])
            print()
        else:
            print(f"Issue {res_dct['number']}: `{title}` created successfully")
    
    except Exception as e:
        print(e)
        print(e.args)


def gh_main_runner(cred_file_path="creds.json",todo={}):
    creds_dct = parse_creds(cred_file_path)
    validate_creds_existence(cred_file_path=cred_file_path,creds_dct=creds_dct)
    assert todo["title"] != "" , "Todo title cannot be blank"
    create_gh_issue(creds_dct=creds_dct,todo=todo)
