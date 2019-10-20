from executor.ExecutorPasteGuild import *
from executor.ExecutorListener import *

from commands.Command import *

from file.GuildFile import *

import discord

class PasteDiscordCommand(Command, ExecutorListener):
    def __init__(self, bot):
        Command.__init__(self, bot.config.getDiscordPasteCommand(), bot);
        ExecutorListener.__init__(self);


    async def run(self, msg):
        if not msg.author.guild_permissions.manage_guild:
            await msg.channel.send("Only user with the \"Manage Guild\" permission can execute this command.");
            return

        guild = msg.guild;
        args = msg.content.split(" ");
        if len(args) <= 2:
            await msg.channel.send("Please, tell me the guild to paste...");
            return;

        guildIdToRestore = args[2];

        guildFile = GuildFile(self.bot);
        try:
            guildModel = guildFile.loadGuild(guildIdToRestore);
        except IOError:
            errorMsg = "The \"guild.json\" file can't be found. Did you already saved this server?";
            self.bot.log.error(errorMsg);
            await msg.channel.send(errorMsg);
            return;

        self.embedStatus = EmbedStatus("Pasting Discord");
        self.embedStatus.addField("General Settings");
        self.embedStatus.addField("Roles");
        self.embedStatus.addField("Emojis");
        self.embedStatus.addField("Channels");
        self.embedStatus.addField("Bans");
        self.embedStatus.addField("Post channels settings");
        await self.embedStatus.post(msg.channel);

        executor = ExecutorPasteGuild(self.bot, guild, guildModel, guildIdToRestore, self);
        await executor.pasteGuild();


    async def taskFinished(self, details=""):
        await self.embedStatus.setStatus(CONST_STATUS_OK, details);


    async def taskError(self, details):
        await self.embedStatus.setStatus(CONST_STATUS_FAIL, details);
