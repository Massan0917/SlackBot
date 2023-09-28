# Slackbot for appload lab news

## Description
This is a slackbot for appload lab news.  
When the bot is mentioned with file(markdown or image), the bot will post the file to the appload github repository.

## Environment
Confirmed to work with python 3.10.12

| Package            | Version  |
|--------------------|----------|
| certifi            | 2023.7.22|
| charset-normalizer | 3.2.0    |
| gitdb              | 4.0.10   |
| GitPython          | 3.1.34   |
| idna               | 3.4      |
| pip                | 22.0.2   |
| requests           | 2.31.0   |
| setuptools         | 59.6.0   |
| slack-bolt         | 1.18.0   |
| slack-sdk          | 3.21.3   |
| smmap              | 5.0.0    |
| urllib3            | 2.0.5    |
| wheel              | 0.37.1   |

## How to use
1. IN TERMINAL, run `python3 chatbot.py` to start the bot
2. IN SLACK, mention the bot with file(markdown or image) to post the news and images.
3. the bot will post the file to the appload github repository.
4. the bot response with the link to the news or images.

## Remarks
- The bot will post the file to the appload github repository.
  - to check where repository the bot push, check `git remote -v` in the terminal.
- tokens of slack is hidden in the code.
  - to use the bot, you need to get the tokens and put them in the json file : `tokens.json`.