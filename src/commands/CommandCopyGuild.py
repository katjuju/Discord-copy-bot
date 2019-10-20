from Bot import *

from commands.Command import *

from file.GuildFile import *

from model.GuildModel import *

class CommandCopyGuild(Command):

    def __init__(self, bot):
        Command.__init__(self, bot.config.getDiscordCopyCommand(), bot);


    async def run(self, msg):
        if not msg.author.guild_permissions.manage_guild:
            await msg.channel.send("Only user with the \"Manage Guild\" permission can execute this command.");
            return

        guild = msg.guild;

        guildModel = GuildModel();
        await guildModel.fillFromGuild(self.bot, guild);

        file = GuildFile(self.bot)
        await file.saveGuild(guildModel, msg.channel);

        self.bot.log.info("Discord saved");
