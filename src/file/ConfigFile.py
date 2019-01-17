import json

class ConfigFile:
	def __init__(self):
		file = open("config.json", "r");
		self.config = json.load(file);


	def getDiscordToken(self):
		return self.config["keys"]["discordBotToken"];


	def getDiscordCopyCommand(self):
		return self.config["commands"]["discordCopy"];


	def getDiscordPasteCommand(self):
		return self.config["commands"]["discordPaste"];
