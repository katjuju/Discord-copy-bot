from model.GuildChannelModel import *

class VoiceChannelModel(GuildChannelModel):

    def __init__(self):
        GuildChannelModel.__init__(self);

        self.bitrate = None;
        self.user_limit = None;


    def fillFromChannel(self, channel):
        super(VoiceChannelModel, self).fillFromChannel(channel)

        self.bitrate = channel.bitrate;
        self.user_limit = channel.user_limit;
