from model.ChannelModel import *
from model.GuildModel import *
from model.EmojiModel import *
from model.MemberModel import *
from model.PermissionsModel import *
from model.RoleModel import *

class GuildModel:

    #Missing in Discord.py
    #Integration
    #Webhooks
    #Permissions -> Priority speaker
    def __init__(self):
        self.id = None;
        self.name = None;
        self.region = None;
        self.icon = None;
        self.icon_url = None;
        self.afkTimeout = None;
        self.afkChannel  = None;
        self.verificationLevel = None;
        self.mfaLevel = None;
        self.roles = None;
        self.emojis = None;
        self.channels = None;
        self.bans = None;
        self.members = None;
        self.default_message_notifications = None;
        self.explicit_content_filter = None;
        self.widget_enabled = False;
        self.widget_channel_id = None;
        self.system_channel_id = None;


    async def fillFromGuild(self, bot, guild):
        self.id = guild.id;
        self.name = guild.name;
        self.region = guild.region.value;
        self.icon = guild.icon;
        self.icon_url = guild.icon_url;
        self.afkTimeout = guild.afk_timeout;
        if guild.afk_channel != None:
            self.afkChannel  = guild.afk_channel.id;
        self.verificationLevel = guild.verification_level.value;
        self.mfaLevel = guild.mfa_level;
        self.default_message_notifications = guild.default_message_notifications;
        self.explicit_content_filter = guild.explicit_content_filter;
        self.widget_enabled = guild.widget_enabled;
        self.widget_channel_id = guild.widget_channel_id;
        self.system_channel_id = guild.system_channel_id;

        self.roles = list();
        for role in guild.roles:
            roleModel = RoleModel();
            roleModel.fillFromRole(role);

            self.roles.append(roleModel.__dict__);

        self.emojis = list();
        for emoji in guild.emojis:
            emojiModel = EmojiModel();
            emojiModel.fillFromEmoji(emoji);

            self.emojis.append(emojiModel.__dict__);

        self.channels = list();
        for channel in guild.channels:
            channelModel = ChannelModel();
            channelModel.fillFromChannel(channel);

            self.channels.append(channelModel.__dict__);

        self.members = list();
        for member in guild.members:
            memberModel = MemberModel();
            memberModel.fillFromMember(member);

            self.members.append(memberModel.__dict__);

        self.bans = list();
        for banMember in await bot.get_bans(guild):
            self.bans.append(banMember.id);
