from model.GuildChannelModel import *

class TextChannelModel(GuildChannelModel):

	def __init__(self):
		GuildChannelModel.__init__(self);

		self.nsfw = None;
		self.topic = None;
		self.slowmode_delay = None;


	def fillFromChannel(self, channel):
		super(TextChannelModel, self).fillFromChannel(channel)

		self.nsfw = channel.nsfw;
		self.topic = channel.topic;
		self.slowmode_delay = channel.slowmode_delay;
