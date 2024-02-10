# Airline Manager 4 Bot
A bot that connects to a PHP Session of Airlines Manager 4 and automate some tasks

> [!IMPORTANT]
> You are required to know the basics of python and docker to be able to use this bot.
> I cannot guarantee that I will maintain the bot. Am just doing it for fun and want to share the fun.

## Features
✔️ Autodepartures.
✔️ Autobuy Fuel when price is low.
✔️ Autobuy CO2 Quotas when price is low.
✔️ Automaintain Aircraft.
✔️ Automaintain Aircraft.
✔️ Autolaunch Eco Marketing Campaign at 8h Everyday

## How To Run
Clone The Repository
Create a `.env` file and add the following line:
```
PHP_SESSION=<PHP_SESSION>
```
How to get PHP Session?
Sign in to AM4 account.
Open your browser's DEV tool. The Standard is the F12 Key on your keyboard.
Go to the Network Tab and hit Ctrl + R

<img src="https://raw.githubusercontent.com/yanickflyer/airlinemanager4bot/master/img/phpsess.png" width="1000px">

Then either use `docker-compose up -d` to spin a docker container and that's it.
Or use install python on your machine and use requirements.txt to install the modules.
Run the bot `python src/main.py`