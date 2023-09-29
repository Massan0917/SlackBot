# Author: Masui Taichi

import os
from git import Repo

def push(filepath : str, repository_path : str):
    """
    push file to github

    Parameters
    ----------
    filepath : str
        file path to push
    repository_path : str
        repository path to push

    """ 

    print(filepath, repository_path)
    # content/news/2023-08-12-poster.md interns-hugo-playground/
    repo = Repo(repository_path)
    add_file = [filepath]

    # show added file
    print(repo.git.status())

    repo.index.add(add_file)
    repo.index.commit("update from slakbot")
    repo.remote("origin").push(refspec="slackbot:slackbot")
    # repo.remotes.origin.push()