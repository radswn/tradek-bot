from flask import Flask, request
from exchange import *
import telegram
from os import environ

app = Flask(__name__)
global bot
global TOKEN
TOKEN = environ.get('BOT_TOKEN')
bot = telegram.Bot(token=TOKEN)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    # for debugging purposes only
    print("got text message :", text)
    if text == '/balance':
        bot.sendMessage(chat_id=chat_id, text=f'Current BTC balance = {wallet_balance()}', reply_to_message_id=msg_id)
    # elif text == '/status':
    # bot.sendMessage(chat_id=chat_id, text=text, reply_to_message_id=msg_id)
    #     try:
    #
    #     except Exception:
    #         # if things went wrong
    #         bot.sendMessage(chat_id=chat_id,
    #                         text="There was a problem in the name you used, please enter different name",
    #                         reply_to_message_id=msg_id)

    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL="https://tradek-bot.ew.r.appspot.com/", HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return str(wallet_balance())


if __name__ == '__main__':
    app.run(threaded=True)
