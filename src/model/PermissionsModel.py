import discord

class PermissionsModel:
	def __init__(self):
		self.value = None;
		self.create_instant_invite = None;
		self.kick_members = None;
		self.ban_members = None;
		self.administrator = None;
		self.manage_channels = None;
		self.manage_guild = None;
		self.add_reactions = None;
		self.view_audit_logs = None;
		self.priority_speaker = None;
		self.stream = None;
		self.read_messages = None;
		self.send_messages = None;
		self.send_tts_messages = None;
		self.manage_messages = None;
		self.embed_links = None;
		self.attach_files = None;
		self.read_message_history = None;
		self.mention_everyone = None;
		self.external_emojis = None;
		self.connect = None;
		self.speak = None;
		self.mute_members = None;
		self.deafen_members = None;
		self.move_members = None;
		self.use_voice_activation = None;
		self.change_nickname = None;
		self.manage_nicknames = None;
		self.manage_roles = None;
		self.manage_webhooks = None;
		self.manage_emojis = None;


	def fillFromPermissions(self, permissions):
		if not isinstance(permissions, discord.PermissionOverwrite):
			self.value = permissions.value;
		self.create_instant_invite = permissions.create_instant_invite;
		self.kick_members = permissions.kick_members;
		self.ban_members = permissions.ban_members;
		self.administrator = permissions.administrator;
		self.manage_channels = permissions.manage_channels;
		self.manage_guild = permissions.manage_guild;
		self.add_reactions = permissions.add_reactions;
		self.view_audit_logs = permissions.view_audit_log;
		self.priority_speaker = permissions.priority_speaker;
		self.stream = permissions.stream;
		self.read_messages = permissions.read_messages;
		self.send_messages = permissions.send_messages;
		self.send_tts_messages = permissions.send_tts_messages;
		self.manage_messages = permissions.manage_messages;
		self.embed_links = permissions.embed_links;
		self.attach_files = permissions.attach_files;
		self.read_message_history = permissions.read_message_history;
		self.mention_everyone = permissions.mention_everyone;
		self.external_emojis = permissions.external_emojis;
		self.connect = permissions.connect;
		self.speak = permissions.speak;
		self.mute_members = permissions.mute_members;
		self.deafen_members = permissions.deafen_members;
		self.move_members = permissions.move_members;
		self.use_voice_activation = permissions.use_voice_activation;
		self.change_nickname = permissions.change_nickname;
		self.manage_nicknames = permissions.manage_nicknames;
		self.manage_roles = permissions.manage_roles;
		self.manage_webhooks = permissions.manage_webhooks;
		self.manage_emojis = permissions.manage_emojis;
