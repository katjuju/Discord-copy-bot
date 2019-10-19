from commands.CopyDiscordCommand import *
from commands.PasteDiscordCommand import *

from file.ConfigFile import *

from Logger import *

import discord

import sys

class Bot(discord.Client):
	def __init__(self):
		discord.Client.__init__(self);
		self.log = Logger();
		self.config = ConfigFile(self);

		if(not self.config.read()):
			sys.exit();

		self.commands = [CopyDiscordCommand(self), PasteDiscordCommand(self)];


	async def on_ready(self):
		await self.user.edit(username="Discord Copy");
		self.log.info("Bot online!");


	async def on_message(self, msg):
		for command in self.commands:
			if(await command.processMessage(msg)):
				break;


	def runBot(self):
		self.run(self.config.getDiscordToken());
