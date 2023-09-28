# Author: Masui Taichi

import os
from git import Repo

def push(filepath : str):
    """
    push file to github

    Parameters
    ----------
    filepath : str
        file path to push

    """ 
    repo = Repo(os.getcwd())
    add_file = [filepath]
    repo.index.add(add_file)
    repo.index.commit("update from python")
    repo.remotes.origin.push()