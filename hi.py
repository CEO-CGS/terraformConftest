#!/usr/bin/python

from github import Github
import sys
import os
import datetime
  
Current_Date_Formatted = datetime.datetime.today().strftime ('%d-%m-%Y')

# authenticate to github
g = Github(os.environ['ACCESS_TOKEN'])
# get the authenticated user
user = g.get_user()
    
repo = g.get_repo("CEO-CGS/test")
contents = repo.get_contents("/errors/README.md")

#adds new content
newContent = contents.decoded_content.decode() + "|" + str(Current_Date_Formatted) + " | " + "".join(sys.argv) + "|\n" 

print(newContent)

repo.update_file(contents.path, "more tests",str.encode(newContent), contents.sha)
