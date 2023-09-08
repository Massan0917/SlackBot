import os
from git import Repo

def push(file_name : 'str' ,title : str, member : str):
    repo = Repo(os.getcwd())
    upload_file = 'push_files/'+file_name+'.txt'

    with open(upload_file , 'w') as f:
        f.write('title = "'+ title + '"\n')
        f.write('member = "'+ member + '"\n')
    
    add_file = [upload_file]
    repo.index.add(add_file)
    repo.index.commit("update from python")
    repo.remotes.origin.push()