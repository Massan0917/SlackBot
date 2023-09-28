# Author: Masui Taichi

import json
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import push_to_git as ptg

json_open = open('tokens.json', 'r')
tokens = json.load(json_open)

SLACK_BOT_TOKEN = tokens['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = tokens['SLACK_APP_TOKEN']

app = App(token=SLACK_BOT_TOKEN)

# when app is mentioned
@app.event("app_mention") 
def file_share(event, say):
    """
    download file from slack and push to github

    Parameters
    ----------
    event : dict
        event data from slack
    say : function
        function to say

    """
    say(event['files'][0]['filetype'])
    say(event['files'][0]['name'])

    # get filename
    filename = event['files'][0]['name']
    # check filetype and set path
    if event["files"][0]["filetype"] in["png", "jpg"]:
        path='img/'
    elif event["files"][0]["filetype"] == "markdown":
        path='news/'
    else:
        path=''

    # download file from slack
    download_from_slack(
        download_url = event["files"][0]["url_private_download"], 
        auth = SLACK_BOT_TOKEN,
        path = path,
        filename = filename
    )

    # push to github
    push_to_git(filepath=path + filename , say=say)

def download_from_slack(download_url: str, auth: str, path:str, filename:str):
    """
    download file from slack

    Parameters
    ----------
        download_url : str
            URL to download
        auth : str
            Slack Bot Token
        path : str
            path to save
        filename : str
            filename to save
    """

    # download file
    img_data = requests.get(
        download_url,
        allow_redirects=True,
        headers={"Authorization": f"Bearer {auth}"},
        stream=True,
    ).content

    # save file
    filename = path + filename
    with open(filename, "wb") as f:
        f.write(img_data)

def push_to_git(filepath:str, say):
    """
    push file to github

    Parameters
    ----------
        filepath : str
            path to file
        say : function
            function to say
    """

    # this link is just say to user
    # repository to push depends on running environment
    link_to_github = "https://github.com/NAIST-SE/naist-se.github.io/"
    say('pushing to github...')
    ptg.push(filepath=filepath)
    say('done!')
    say(f'pushed at {link_to_github}')


@app.event("message") # logging
def handle_message_events(body, logger):
    logger.info(body)

SocketModeHandler(app, SLACK_APP_TOKEN).start()