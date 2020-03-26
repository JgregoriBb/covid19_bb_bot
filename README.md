# COVID-19 INFO BOT

A simple bot with chatterbot and Flask to provide users with information about COVID-19
This bot is trained with information from the WHO Coronavirus FAQ that can be found here: https://www.who.int/news-room/q-a-detail/q-a-coronaviruses. The script in scrapper.py connects to the WHO FAQ about COVID-19 and uses Beautiful Soup to scrap the information, formatting it to a YAML file that is then used to train the bot.

Given the need from accurate medical information from a reliable source, this bot will not learn from user responses.It also does not collect any personal information from the user.

This bot is a proof of concept, it is not meant to be used in production. Whatever you do with it, it´s at your own risk.

I used a number of tutorials and resources online:
---> Chatterbot documentation: https://chatterbot.readthedocs.io/en/stable/
---> Webscraping tutorial with Beautiful Soup: https://realpython.com/beautiful-soup-web-scraper-python/
---> How to create a bot with Flask and Chatterbot: https://github.com/chamkank/flask-chatterbot/blob/master/app.py
---> Creando un chatbot with Python en muy pocos minutos: https://www.youtube.com/watch?v=Yd0e4uven-g&t=256s

# Deployment:

After some trial and error, I adapted this app to be deployed on Heroku via their CLI tool, that explains having the NTLK packages in a separate txt file and Gunicorn in the requirements file. Also the usage of mongo db. If you want to deploy the app as I did you will need to update your Mongo DB database and URI in the app.py file. 

It is also easy to change the database adapter in chatterbot to use other databases such as SQL or postgress.

Finally, before deployment, do not forget to run the scrapper.py script to generate the training file.
