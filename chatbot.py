import os
import re
import json
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import testgit

json_open = open('tokens.json', 'r')
tokens = json.load(json_open)

SLACK_BOT_TOKEN = tokens['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = tokens['SLACK_APP_TOKEN']
# print(SLACK_BOT_TOKEN)
# print(SLACK_APP_TOKEN)

app = App(token=SLACK_BOT_TOKEN)

@app.message("hello")  # 送信されたメッセージ内に"hello"が含まれていたときのハンドラ
def ask_who(say):
    say("can I help you?")

@app.event("app_mention")  # chatbotにメンションが付けられたときのハンドラ
def push_to_git(event, say):
    say('pushing to github...')
    message = re.sub(r'^<.*>', '', event['text']) # メンションを削除
    splited_message = message.split('\n')
    print(splited_message)
    testgit.push(splited_message[0] ,splited_message[1], splited_message[2])
    say('done!')
    

@app.event("message") # ロギング
def handle_message_events(body, logger):
    logger.info(body)

SocketModeHandler(app, SLACK_APP_TOKEN).start()