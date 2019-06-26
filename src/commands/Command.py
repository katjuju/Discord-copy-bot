class Command:
	def __init__(self, commandLabel, bot):
		self.commandLabel = commandLabel;
		self.bot = bot;

	async def processMessage(self, msg):
		if(msg.author.bot):
			return;

		if(	msg.content.startswith("<@"+str(self.bot.user.id)+"> " + self.commandLabel) or
			msg.content.startswith("<@!"+str(self.bot.user.id)+"> " + self.commandLabel)):
			await self.run(msg);
			return True;

		return False;

	async def run(self, msg):
		pass;
