
# COVID-19 INFO BOT
# A simple bot with chatterbot and Flask to provide users with information about COVID-19
# This bot is trained with information from the WHO Coronavirus FAQ that can be found here: https://www.who.int/news-room/q-a-detail/q-a-coronaviruses
# Given the need from accurate medical information from a reliable source, this bot will not learn from user responses.
# This bot is a proof of concept, it is not meant to be used in production. Whatever you do with it, it´s at your own risk.
# I used a number of tutorials and resources online:
# ---> Chatterbot documentation: https://chatterbot.readthedocs.io/en/stable/
# ---> Webscraping tutorial with Beautiful Soup: https://realpython.com/beautiful-soup-web-scraper-python/
# ---> How to create a bot with Flask and Chatterbot:

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

bot = ChatBot(
    'COVID-19 INFO BOT',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, by design I can only provide COVID-19 answers from the WHO faq, please ask in a different way.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    read_only=True,
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('./data/covidfaq.yaml')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()
    