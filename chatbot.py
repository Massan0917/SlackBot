import os
import re
import json
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import datetime

import push_to_git as ptg

json_open = open('tokens.json', 'r')
tokens = json.load(json_open)

SLACK_BOT_TOKEN = tokens['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = tokens['SLACK_APP_TOKEN']
# print(SLACK_BOT_TOKEN)
# print(SLACK_APP_TOKEN)

app = App(token=SLACK_BOT_TOKEN)

@app.message("hello")  # 送信されたメッセージ内に"hello"が含まれていたときのハンドラ
def ask_who(event,say):
    say("can I help you?")
    say(event['text'])

@app.event("app_mention")  # chatbotにメンションが付けられたときのハンドラ
def push_to_git(event, say):
    say('pushing to github...')
    message = re.sub(r'^<.*>', '', event['text']) # メンションを削除
    splited_message = message.split('\n')
    print(splited_message)
    ptg.push(splited_message[0] ,splited_message[1])
    say('done!')
    say('pushed at https://github.com/Massan0917/SlackBot')

@app.event({"type": "message", "subtype": "file_share"})
def file_share(event, say):
    say(event['files'][0]['filetype'])
    say(event['files'][0]['name'])

    if event["files"][0]["filetype"] in["png", "jpg"]:
        path='img/'
    elif event["files"][0]["filetype"] == "markdown":
        path='news/'
    else:
        path=''

    # スレッドからファイルをダウンロード
    download_from_slack(
        download_url = event["files"][0]["url_private_download"], 
        auth = SLACK_BOT_TOKEN,
        path = path,
        filename = event['files'][0]['name']
    )

def download_from_slack(download_url: str, auth: str, path:str, filename:str):
    """Slackから画像をダウンロードして保存し、保存したパスを返す。

    Args:
        download_url (str): 画像のURL
        auth (str): 画像の閲覧に必要なSlackの認証キー

    Returns:
        str: 画像が保存されているパス
    """
    img_data = requests.get(
        download_url,
        allow_redirects=True,
        headers={"Authorization": f"Bearer {auth}"},
        stream=True,
    ).content

    filename = path + filename
    with open(filename, "wb") as f:
        f.write(img_data)


@app.event("message") # ロギング
def handle_message_events(body, logger):
    logger.info(body)

SocketModeHandler(app, SLACK_APP_TOKEN).start()