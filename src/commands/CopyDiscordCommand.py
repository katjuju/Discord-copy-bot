from Bot import *

from commands.Command import *

from file.GuildFile import *

from model.GuildModel import *
from model.RoleModel import *
from model.PermissionsModel import *

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
            roleModel.color = role.color.value;
            roleModel.hoist = role.hoist;
            roleModel.position = role.position;
            roleModel.mentionable = role.mentionable;
            roleModel.is_everyone = role.is_everyone;
            roleModel.managed = role.managed;
            roleModel.permissions = self.getPermissionsModel(role.permissions).__dict__;

            roles.append(roleModel.__dict__);

        guildModel.roles = roles;

        file = GuildFile()
        file.saveGuild(guildModel);

        self.bot.log.info("File saved");


    def getPermissionsModel(self, permissions):
        permissionsModel = PermissionsModel();

        permissionsModel.value = permissions.value;
        permissionsModel.create_instant_invite = permissions.create_instant_invite;
        permissionsModel.kick_members = permissions.kick_members;
        permissionsModel.ban_members = permissions.ban_members;
        permissionsModel.administrator = permissions.administrator;
        permissionsModel.manage_channels = permissions.manage_channels;
        permissionsModel.manage_server = permissions.manage_server;
        permissionsModel.add_reactions = permissions.add_reactions;
        permissionsModel.view_audit_logs = permissions.view_audit_logs;
        permissionsModel.read_messages = permissions.read_messages;
        permissionsModel.send_messages = permissions.send_messages;
        permissionsModel.send_tts_messages = permissions.send_tts_messages;
        permissionsModel.manage_messages = permissions.manage_messages;
        permissionsModel.embed_links = permissions.embed_links;
        permissionsModel.attach_files = permissions.attach_files;
        permissionsModel.read_message_history = permissions.read_message_history;
        permissionsModel.mention_everyone = permissions.mention_everyone;
        permissionsModel.external_emojis = permissions.external_emojis;
        permissionsModel.connect = permissions.connect;
        permissionsModel.speak = permissions.speak;
        permissionsModel.mute_members = permissions.mute_members;
        permissionsModel.deafen_members = permissions.deafen_members;
        permissionsModel.move_members = permissions.move_members;
        permissionsModel.use_voice_activation = permissions.use_voice_activation;
        permissionsModel.change_nickname = permissions.change_nickname;
        permissionsModel.manage_nicknames = permissions.manage_nicknames;
        permissionsModel.manage_roles = permissions.manage_roles;
        permissionsModel.manage_webhooks = permissions.manage_webhooks;
        permissionsModel.manage_emojis = permissions.manage_emojis;

        return permissionsModel;
