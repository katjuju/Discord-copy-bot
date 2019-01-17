from commands.Command import *
from Bot import *

class CopyDiscordCommand(Command):

	def __init__(self, bot):
		Command.__init__(self, bot.config.getDiscordCopyCommand(), bot);


	async def run(self, msg):
		pass;
