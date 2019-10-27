from executor.ExecutorCopyGuild import *
from executor.ExecutorListener import *

from commands.Command import *

from file.GuildFile import *

from model.GuildModel import *

from utils.Logger import *

class CommandCopyGuild(Command, ExecutorListener):

    def __init__(self, bot):
        Command.__init__(self, bot.config.getDiscordCopyCommand(), bot);
        ExecutorListener.__init__(self);


    async def run(self, msg):
        if not msg.author.guild_permissions.manage_guild:
            await msg.channel.send("Only user with the \"Manage Guild\" permission can execute this command.");
            return

        self.embedStatus = EmbedStatus("Copying Discord");
        self.embedStatus.addField("Set up save folder");
        self.embedStatus.addField("Guild informations");
        self.embedStatus.addField("Guild's Icon");
        self.embedStatus.addField("Guild's emojis");
        await self.embedStatus.post(msg.channel);

        executor = ExecutorCopyGuild(msg.guild, self);
        await executor.run();


    async def taskFinished(self, details=""):
        await self.embedStatus.setStatus(CONST_STATUS_OK, details);


    async def taskChanged(self, newTaskName):
        Logger.info(newTaskName);


    async def taskError(self, details):
        await self.embedStatus.setStatus(CONST_STATUS_FAIL, details);
        Logger.error(details);


    async def completed(self):
    	Logger.info("Discord saved");
