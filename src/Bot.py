import libs.discord_py as discord

from commands.CopyDiscordCommand import *
from commands.PasteDiscordCommand import *

from file.ConfigFile import *

from Logger import *

class Bot(discord.Client):
	def __init__(self):
		discord.Client.__init__(self);
		self.log = Logger();
		self.config = ConfigFile();

		self.commands = [CopyDiscordCommand(self), PasteDiscordCommand(self)];


	async def on_ready(self):
		await self.edit_profile(username="Discord Copy");
		await self.change_presence(game=discord.Game(name=self.config.getDiscordCopyCommand()));
		self.log.info("Bot online!");


	async def on_message(self, msg):
		for command in self.commands:
			await command.processMessage(msg);


	def runBot(self):
		self.run(self.config.getDiscordToken());
