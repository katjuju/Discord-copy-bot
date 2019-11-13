from model.CategoryModel import *
from model.TextChannelModel import *
from model.VoiceChannelModel import *
from model.GuildModel import *
from model.EmojiModel import *
from model.MemberModel import *
from model.PermissionsModel import *
from model.RoleModel import *
from model.BanModel import *
from model.SystemChannelFlags import *

class GuildModel:

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
		self.categories = None;
		self.text_channels = None;
		self.voice_channels = None;
		self.bans = None;
		self.members = None;
		self.default_message_notifications = None;
		self.explicit_content_filter = None;
		self.system_channel = None;
		self.system_channel_flags = None;


	async def fillFromGuild(self, guild):
		self.id = guild.id;
		self.name = guild.name;
		self.region = guild.region.value;
		self.icon = guild.icon;
		self.icon_url = str(guild.icon_url);
		self.afkTimeout = guild.afk_timeout;
		if guild.afk_channel != None:
			self.afkChannel  = guild.afk_channel.id;
		self.verificationLevel = guild.verification_level.value;
		self.mfaLevel = guild.mfa_level;
		self.default_message_notifications = guild.default_notifications.value;
		self.explicit_content_filter = guild.explicit_content_filter.value;
		if guild.system_channel != None:
			self.system_channel = guild.system_channel.id;

		systemChannelFlags = SystemChannelFlags();
		systemChannelFlags.fillFromSystemChannelFlags(guild.system_channel_flags);
		self.system_channel_flags = systemChannelFlags.__dict__;

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

		self.categories = list();
		for channel in guild.categories:
			channelModel = CategoryModel();
			channelModel.fillFromChannel(channel);

			self.categories.append(channelModel.__dict__);

		self.text_channels = list();
		for channel in guild.text_channels:
			channelModel = TextChannelModel();
			channelModel.fillFromChannel(channel);

			self.text_channels.append(channelModel.__dict__);

		self.voice_channels = list();
		for channel in guild.voice_channels:
			channelModel = VoiceChannelModel();
			channelModel.fillFromChannel(channel);

			self.voice_channels.append(channelModel.__dict__);

		self.members = list();
		for member in guild.members:
			memberModel = MemberModel();
			memberModel.fillFromMember(member);

			self.members.append(memberModel.__dict__);

		self.bans = list();
		for banMember in await guild.bans():
			banModel = BanModel();
			banModel.fillFromBan(banMember);

			self.bans.append(banModel.__dict__);
