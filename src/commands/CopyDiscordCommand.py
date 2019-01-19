from commands.Command import *
from Bot import *
from model.GuildModel import *
from model.RoleModel import *
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

        roles = list();
        for role in guild.roles:
            roleModel = RoleModel();
            roleModel.id = role.id;
            roleModel.name = role.name;
            #roleModel.permissions = role.permissions;
            roleModel.color = role.color.value;
            roleModel.hoist = role.hoist;
            roleModel.position = role.position;
            roleModel.mentionable = role.mentionable;
            roleModel.is_everyone = role.is_everyone;
            roleModel.managed = role.managed;

            roles.append(roleModel.__dict__);

        guildModel.roles = roles;

        file = GuildFile()
        file.saveGuild(guildModel);

        self.bot.log.info("File saved");
