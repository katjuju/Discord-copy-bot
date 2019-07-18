# What is that bot for?

It allows you to copy and paste a Discord Server. You may want to save it so you can use it as a template or, maybe, because you may want to recreate a Guild you are about to delete in the future. If so, then this bot can help you!

# Limitations...

The bot can't do the following things :

- Retore MFA
- Restore Webhooks settings
- Restore Widget settings
- Restore Integrations settings

_NB : A message will be send to remind you to enable mfa if it was previously enabled._

# Setting up the bot

_This is a self hosted bot using at least python 3.5.3, meaning it is up to you to register it on [Discord Developer Portal](https://discordapp.com/developers/applications/) and to make it run when you want to save or paste a server (it can be stopped then)._

Once you've configure your bot on [Discord Developer Portal](https://discordapp.com/developers/applications/) you need to go to the bot folder and make a copy of the "config-default.json" file renamed "config.json". Then you need to open the pasted file and edit the "discordBotToken" value using the bot token provided by Discord.

Then, you can make the bot run using the following commands :

For Windows

```sh
py -3 pip install -r requirements.txt
py -3 src/index.py
```

For Linux

```sh
sudo pip3 install -r requirements.txt
python3 src/index.py
```

You should end up with a message in the console telling you that the bot is currently running.

# Commands

Commands works by mentionning the bot and then giving a keyword ("copy" or "paste" by default).

## Save a Discord

You only need to mention the bot and use the "copy" keyword (by default). When you do so, a message appear giving you the states of that tasks. When it is complete a folder will be created in the "guilds" folder. That folder and all his files are very important to keep. It's the copy of your Discord Server. It will be required when you want to paste the server.  

## Paste a Discord

To paste a server you need to mention the bot and use the "paste" keyword (by default) following by the name of the folder containing the previous save in the "guilds" folder.

For exemple if you have a folder in "guilds" named "900718620735686367_My_Super_Server" the command will be :

```sh
@Discord Copy paste 900718620735686367_My_Super_Server
```

You will end up with a message giving you the states of the tasks. When it's done, enjoy your fresh old server again!

# Contributors

This project is made by :

AnonDax ([@anondax](https://www.github.com/anondax))
