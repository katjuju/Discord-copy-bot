from model.GuildChannelModel import *

class CategoryModel(GuildChannelModel):

	def __init__(self):
		GuildChannelModel.__init__(self);


	def fillFromChannel(self, channel):
		super(CategoryModel, self).fillFromChannel(channel)
