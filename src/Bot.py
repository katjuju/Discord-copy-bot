from commands.CopyDiscordCommand import *
from commands.PasteDiscordCommand import *

from file.ConfigFile import *

from utils.Logger import *

import discord

import sys

class Bot(discord.Client):

	def __init__(self):
		discord.Client.__init__(self);

		self.log = Logger();
		self.config = ConfigFile(self);

		# If we can't have a valid config.json file we can't have a valid api key for the bot. So we stop
		if(not self.config.read()):
			sys.exit();

		self.commands = [CopyDiscordCommand(self), PasteDiscordCommand(self)];


	async def on_ready(self):
		await self.user.edit(username="Discord Copy");
		self.log.info("Bot online!");


	# Check if the message is a command
	async def on_message(self, msg):
		for command in self.commands:
			if(await command.processMessage(msg)):
				break;


	def runBot(self):
		self.run(self.config.getDiscordToken());
