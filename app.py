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
    
