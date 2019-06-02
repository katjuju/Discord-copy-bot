from model.PermissionsModel import *

class GuildChannelModel:

    def __init__(self):
        self.id = None;
        self.name = None;
        self.position = None;
        self.overwrites = None;
        self.parentId = None;

    def fillFromChannel(self, channel):
        self.id = channel.id;
        self.name = channel.name;
        self.position = channel.position;
        if channel.category != None:
            self.parentId = channel.category.id;

        self.overwrites = dict();
        for roleOrMember, perms in channel.overwrites.items():
            permissionsModel = PermissionsModel();
            permissionsModel.fillFromPermissions(perms);

            self.overwrites[roleOrMember.id] = permissionsModel.__dict__;
