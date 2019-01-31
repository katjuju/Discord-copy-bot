from model.PermissionsModel import *

class ChannelModel:
    def __init__(self):
        self.id = None;
        self.name = None;
        self.topic = None;
        self.position = None;
        self.type = None;
        self.bitrate = None;
        self.user_limit = None;
        self.overwrites = None;
        self.parentId = None;
        self.nsfw = None;
        self.rateLimitPerUser = None;

    def fillFromChannel(self, channel):
        self.id = channel.id;
        self.name = channel.name;
        self.topic = channel.topic;
        self.position = channel.position;
        #type not defined in the enum
        if(str(channel.type).isdigit()):
            self.type = channel.type
        else:
            self.type = channel.type.value;
        self.bitrate = channel.bitrate;
        self.user_limit = channel.user_limit;
        self.parentId = channel.parentId;
        self.nsfw = channel.nsfw;
        self.rateLimitPerUser = channel.rate_limit_per_user;

        self.overwrites = dict();
        for overwrite in channel.overwrites:
            permissionsModel = PermissionsModel();
            permissionsModel.fillFromPermissions(overwrite[1]);

            self.overwrites[overwrite[0].id] = permissionsModel.__dict__;
