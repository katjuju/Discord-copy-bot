class Command:
	def __init__(self, commandLabel, bot):
		self.commandLabel = commandLabel;
		self.bot = bot;

	async def processMessage(self, msg):
		if(msg.author.bot):
			return;
	
		if(msg.content.startswith(self.commandLabel)):
			await self.run(msg);

	async def run(self, msg):
		pass;
