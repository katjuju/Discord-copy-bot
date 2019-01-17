from commands.Command import *
from Bot import *
from model.GuildModel import *
from file.GuildFile import *

class CopyDiscordCommand(Command):
    def __init__(self, bot):
        Command.__init__(self, bot.config.getDiscordCopyCommand(), bot);


    async def run(self, msg):
        guild = msg.server;

        guildModel = GuildModel();
        guildModel.id = guild.id;
        guildModel.name = guild.name;
        guildModel.region = guild.region.value;
        guildModel.icon = guild.icon;
        guildModel.afkTimeout = guild.afk_timeout;
        guildModel.afkChannel  = guild.afk_channel.id;
        guildModel.verificationLevel = guild.verification_level.value;
        guildModel.mfaLevel = guild.mfa_level;

        file = GuildFile()
        file.saveGuild(guildModel);
