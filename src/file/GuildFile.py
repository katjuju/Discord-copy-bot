import json

class GuildFile:
	def __init__(self):
		pass;


	def saveGuild(self, guildModel):
		file = open("guilds/"+guildModel.id+"_"+guildModel.name+".json", "w");
		file.write(json.dumps(guildModel.__dict__, indent=4));
