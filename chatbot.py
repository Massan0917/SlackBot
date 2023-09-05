import os
import re
import json
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


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
def respond_to_mention(event, say):
    message = re.sub(r'^<.*>', '', event['text'])
    say(message[::-1]) # 文字列を逆順

@app.event("message") # ロギング
def handle_message_events(body, logger):
    logger.info(body)

SocketModeHandler(app, SLACK_APP_TOKEN).start()