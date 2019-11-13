import json

from file.update.GuildFileUpdater import *

from model.GuildModel import *

from utils.const import *;
from utils.EmbedStatus import *
from utils.Logger import *

class GuildFile:
	def __init__(self):
		pass;


	@staticmethod
	def load(guildId):
		guildModel = None;

		try:
			file = open("guilds/"+guildId+"/guild.json", "r");
			guildModel = json.load(file);
		except IOError:
			return None;

		updater = GuildFileUpdater();
		return updater.updateToLatestVersion(guildModel);


	@staticmethod
	async def createFromGuild(guild):
		guildModel = GuildModel();
		await guildModel.fillFromGuild(guild);

		return guildModel;
