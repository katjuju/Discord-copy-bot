import json

class ConfigFile:

	def __init__(self, bot):
		self.bot = bot;
		self.configError = False;

		try:
			file = open("config.json", "r");

			self.config = json.load(file);
		except:
			self.bot.log.error("The \"config.json\" file is missing or corrupted. You can create a new one from the \"config-default.json\" file.");
			self.configError = True;

	def getDiscordToken(self):
		return self.config["keys"]["discordBotToken"];


	def getDiscordCopyCommand(self):
		return self.config["commands"]["discordCopy"];


	def getDiscordPasteCommand(self):
		return self.config["commands"]["discordPaste"];

	def getConfigError(self):
		return self.configError;
